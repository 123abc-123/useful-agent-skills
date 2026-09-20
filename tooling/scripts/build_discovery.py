"""Render the task-first navigation using existing catalog facts and GitHub snapshots."""
import copy
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPO = 'https://github.com/123abc-123/useful-agent-skills'


def assemble(index, payloads):
    recommended = json.loads((ROOT / 'content/data/recommended-skills.json').read_text(encoding='utf-8'))
    sources = json.loads((ROOT / 'content/data/tools/sources.json').read_text(encoding='utf-8'))['repositories']
    catalog = {}
    risk_rank = {'low': 0, 'medium': 1, 'high': 2}
    for payload in payloads.values():
        for item in payload['items']:
            key = (item['source'], item['name'])
            if key in catalog:
                # Preserve the most cautious reviewed description for duplicate listings.
                if risk_rank[item['risk']] < risk_rank[catalog[key]['risk']]:
                    continue
            catalog[key] = dict(item)
    for item in recommended['skills']:
        key = (item['source'], item['name'])
        if key not in catalog:
            catalog[key] = dict(item, status='recommended' if item['score'] >= 85 else 'trial')
        else:
            # Editorial scores for shared recommendations have one canonical source.
            catalog[key]['score'] = item['score']
    data = copy.deepcopy(index['navigation'])
    data['sources_checked'] = min(x['checked_at'] for x in sources.values())
    data['unique_skills'] = len(catalog)
    seen_groups = set()
    for group in data['groups']:
        assert group['id'] not in seen_groups, 'duplicate navigation group'
        seen_groups.add(group['id'])
        assert not Path(group['page']).is_absolute() and '..' not in Path(group['page']).parts
        seen_tasks = set()
        for task in group['tasks']:
            assert task['id'] not in seen_tasks, 'duplicate task'
            seen_tasks.add(task['id'])
            assert task['picks'], 'empty task'
            for pick in task['picks']:
                item = dict(catalog[(pick['source'], pick['name'])])
                item.update(pick)
                repo = sources[item['source']]
                assert isinstance(repo['stars'], int) and repo['stars'] >= 0
                item['stars'] = repo['stars']
                item['stars_checked'] = repo['checked_at']
                item['archived'] = repo['archived']
                item['qualified'] = (item['score'] >= data['score_min'] and item['stars'] >= data['stars_min']
                                     and item['status'] == 'recommended' and not item['archived']
                                     and item['source_path'] == 'verified')
                item['install'] = item.get('install', f"npx skills add {item['source']} --skill {item['name']} -a pi -a opencode --copy")
                ref = item['commit'] if item['pinning_status'] == 'verified' else 'main'
                item['source_url'] = f"https://github.com/{item['source']}/blob/{ref}/{item['path']}"
                pick.clear()
                pick.update(item)
    return data


def esc(value):
    return html.escape(str(value), quote=True)


def render(data, page, group=None):
    prefix = '../' * (len(Path(page).parts) - 1)
    title = group['title'] if group else '你今天想用 Agent 完成什么？'
    subtitle = group['subtitle'] if group else '先选工作需求，再看适合你的 Skill。每个场景给出首选和备选，直接找到下一步。'
    nav = ''.join(f'<a class="group-link {"active" if group and g["id"] == group["id"] else ""}" href="{prefix}{g["page"]}">{esc(g["title"])}</a>' for g in data['groups'])
    threshold = f"编辑评分 ≥ {data['score_min']} · 来源仓库 ≥ {data['stars_min']:,} Star"
    tiles = []
    for g in data['groups']:
        tasks = ''.join(f'<a class="shortcut" href="{prefix}{g["page"]}?task={t["id"]}#results">{esc(t["title"])} <span>↗</span></a>' for t in g['tasks'][:3])
        count = len({(p['source'], p['name']) for t in g['tasks'] for p in t['picks'] if p['qualified']})
        badge = f'{count} 个高分高热度推荐' if count else '查看专用候选'
        tiles.append(f'<article class="group-card"><div class="group-top"><span class="number">{g["icon"]}</span><span class="group-count">{badge}</span></div><h2><a href="{prefix}{g["page"]}">{esc(g["title"])}</a></h2><p>{esc(g["subtitle"])}</p><div class="shortcuts">{tasks}</div><a class="group-all" href="{prefix}{g["page"]}">查看全部 {len(g["tasks"])} 个需求场景 →</a></article>')
    if group:
        choices = ''.join(f'<a class="task-choice" data-task="{t["id"]}" href="?task={t["id"]}#results"><strong>{esc(t["title"])}</strong><span>{esc(t["description"])}</span></a>' for t in group['tasks'])
        content = f'''<section aria-labelledby="choose"><div class="section-heading"><div><span class="step">01 / 选择具体需求</span><h2 id="choose">你遇到的是哪种情况？</h2></div><a href="{prefix}index.html">换一个需求组 →</a></div><div class="task-grid">{choices}</div></section>
        <section id="results" aria-labelledby="task-title"><div class="section-heading"><div><span class="step">02 / 看推荐，再决定安装</span><h2 id="task-title"></h2><p id="task-description"></p></div></div>
        <div class="filters"><div class="segmented" aria-label="推荐范围"><button type="button" data-mode="quality" aria-pressed="true">高分高热度</button><button type="button" data-mode="all" aria-pressed="false">全部适配候选</button></div><label>排序 <select id="sort"><option value="match">按需求匹配</option><option value="score">评分优先</option><option value="stars">Star 优先</option></select></label></div>
        <p class="result-meta" id="result-meta" aria-live="polite"></p><div id="recommendations"></div></section>'''
        hero_extra = f'<p class="hero-note">{len(group["tasks"])} 个具体场景 · 每次先看最多 3 项推荐</p>'
    else:
        content = f'<section id="groups"><div class="section-heading"><div><span class="step">01 / 从需求进入</span><h2>六个入口，对应你手上的工作</h2></div><span class="muted">直接点具体问题，也可以进入栏目继续选</span></div><div class="group-grid">{"".join(tiles)}</div></section>'
        hero_extra = '<div class="quick-queries"><span>试试：</span><button data-search="修 Bug">修 Bug</button><button data-search="RAG">RAG 评测</button><button data-search="报告">生成报告</button><button data-search="上下文">整理上下文</button></div>'
    model = dict(data, current_group=group['id'] if group else None, prefix=prefix)
    encoded = json.dumps(model, ensure_ascii=False).replace('<', '\\u003c')
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{esc(subtitle)}"><title>{esc(title)} · Useful Agent Skills</title><link rel="stylesheet" href="{prefix}assets/discovery.css"></head>
<body><header class="topbar"><div class="shell top-inner"><a class="brand" href="{prefix}index.html"><span class="brand-icon">S</span> Useful Agent Skills</a><nav aria-label="主导航"><a href="{prefix}index.html">按需求找 Skill</a><a href="{prefix}prompts.html">Prompt 库</a><a href="{REPO}">GitHub ↗</a></nav></div></header>
<main class="shell"><section class="hero"><div class="eyebrow">面向 Pi · OpenCode 的实用 Skill 导航</div><h1>{esc(title)}</h1><p class="subtitle">{esc(subtitle)}</p><label class="search-label" for="need-search">描述需求，搜索对应场景</label><div class="search-box"><span aria-hidden="true">⌕</span><input id="need-search" type="search" placeholder="例如：修 Bug、RAG 回答不好、生成 HTML 报告" autocomplete="off"><kbd>按需求找</kbd></div>{hero_extra}<div id="search-results" aria-live="polite" hidden></div></section>
{'<nav class="group-nav" aria-label="需求分组">' + nav + '</nav>' if group else ''}
{content}
<aside class="trust-strip"><strong>推荐是怎么选的？</strong><p>先匹配你的任务，再筛选 {threshold}、来源已核验且未归档的推荐项。试用或需适配条目保留在“全部适配候选”。</p><p>评分是本仓库的编辑选型分；Star 是<strong>来源仓库</strong>热度，采集于 {esc(data['sources_checked'][:10])}，不等于单个 Skill 效果。Pi / OpenCode 实机状态单独展示。</p><a href="{REPO}/blob/main/SCORING.md">查看评分维度与采用边界 ↗</a></aside>
<footer><a href="{prefix}index.html">返回需求导航</a><a href="{REPO}/blob/main/content/catalog/watchlist.md">观察清单</a><a href="{REPO}/blob/main/CONTRIBUTING.md">提交使用反馈</a><span>{data['unique_skills']} 个去重候选 · 6 个需求组</span></footer></main>
<noscript><p>请启用 JavaScript 查看按需求筛选的推荐，或访问 <a href="{REPO}/tree/main/content/catalog">GitHub 分类清单</a>。</p></noscript><script type="application/json" id="discovery-data">{encoded}</script><script src="{prefix}assets/discovery.js" defer></script></body></html>'''


def outputs(index, payloads):
    data = assemble(index, payloads)
    yield ROOT / 'site/index.html', render(data, 'index.html')
    yield ROOT / 'site/tools/index.html', render(data, 'tools/index.html')
    for group in data['groups']:
        yield ROOT / 'site' / group['page'], render(data, group['page'], group)
