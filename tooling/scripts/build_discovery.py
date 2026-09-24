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
    must_have = json.loads((ROOT / 'content/data/must-have-skills.json').read_text(encoding='utf-8'))
    for section in must_have['sections']:
        for pick in section['items']:
            item = dict(catalog[(pick['source'], pick['name'])])
            item.update(pick)
            repo = sources[item['source']]
            item['stars'] = repo['stars']
            item['stars_checked'] = repo['checked_at']
            item['archived'] = repo['archived']
            item['install'] = item.get('install', f"npx skills add {item['source']} --skill {item['name']} -a pi -a opencode --copy")
            ref = item['commit'] if item['pinning_status'] == 'verified' else 'main'
            item['source_url'] = f"https://github.com/{item['source']}/blob/{ref}/{item['path']}"
            pick.clear()
            pick.update(item)
    data['must_have'] = must_have
    return data


def esc(value):
    return html.escape(str(value), quote=True)


def render(data, page, group=None):
    prefix = '../' * (len(Path(page).parts) - 1)
    title = group['title'] if group else '你今天想用 Agent 完成什么？'
    subtitle = group['subtitle'] if group else '先选工作需求，再看适合你的 Skill。每个场景给出首选和备选，直接找到下一步。'
    threshold = f"编辑评分 ≥ {data['score_min']} · 来源仓库 ≥ {data['stars_min']:,} Star"
    tiles = []
    for g in data['groups']:
        tasks = ''.join(f'<a class="shortcut" href="{prefix}{g["page"]}?task={t["id"]}#results">{esc(t["title"])} <span>查看首选 →</span></a>' for t in g['tasks'])
        count = len({(p['source'], p['name']) for t in g['tasks'] for p in t['picks'] if p['qualified']})
        badge = f'{count} 个高分高热度推荐' if count else '查看专用候选'
        tiles.append(f'<article class="group-card"><div class="group-top"><span class="number">{g["icon"]}</span><span class="group-count">{badge}</span></div><h2><a href="{prefix}{g["page"]}">{esc(g["title"])}</a></h2><p>{esc(g["subtitle"])}</p><div class="shortcuts">{tasks}</div><a class="group-all" href="{prefix}{g["page"]}">浏览本栏目与全部候选 →</a></article>')
    if group:
        choices = ''.join(f'<a class="task-choice" data-task="{t["id"]}" href="?task={t["id"]}#results"><strong>{esc(t["title"])}</strong><span>{esc(t["description"])}</span></a>' for t in group['tasks'])
        content = f'''<section id="results" class="focus-results" aria-labelledby="task-title"><div class="focus-heading"><div><span class="step">01 / 你的需求</span><p class="focus-path">{esc(group["title"])}</p><h2 id="task-title"></h2><p id="task-description"></p></div><a class="change-group" href="{prefix}index.html#groups">换需求组 →</a></div>
        <div class="quality-callout"><div><strong>默认只看高分高热度</strong><span>{threshold} · 来源路径已核验 · 仓库未归档</span></div><a href="{REPO}/blob/main/SCORING.md">评分规则 ↗</a></div>
        <div class="filters"><div class="segmented" aria-label="推荐范围"><button type="button" data-mode="quality" aria-pressed="true">高分高热度</button><button type="button" data-mode="all" aria-pressed="false">全部适配候选</button></div><label>排序 <select id="sort"><option value="match">按需求匹配</option><option value="score">评分优先</option><option value="stars">Star 优先</option></select></label></div>
        <p class="result-meta" id="result-meta" aria-live="polite"></p><div id="recommendations"></div></section>
        <details class="scenario-switcher"><summary><span><strong>需求不对？切换本栏目里的其他场景</strong><small>共 {len(group["tasks"])} 个场景</small></span><span aria-hidden="true">展开选择 ↓</span></summary><div class="task-grid">{choices}</div></details>'''
        hero_extra = ''
    else:
        must_count = len(data['must_have']['sections'][0]['items'])
        must_banner = f'''<a class="must-banner" href="must-have-skills/"><span class="must-banner-kicker">新栏目 · 社交榜单发现 + 源码复核</span><strong>不知道先装什么？看“必装 Skill”</strong><small>通用必装 {must_count} 个，另有按工作内容加装与热门暂缓清单</small><b>打开栏目 →</b></a>'''
        content = must_banner + f'<section id="groups"><div class="section-heading"><div><span class="step">01 / 先选需求组</span><h2>找到你的问题，直接查看首选 Skill</h2></div><span class="muted">每个具体问题都是一键直达，不用再翻目录</span></div><div class="group-grid">{"".join(tiles)}</div></section>'
        hero_extra = '<div class="quick-queries"><span>试试：</span><button data-search="修 Bug">修 Bug</button><button data-search="RAG">RAG 评测</button><button data-search="报告">生成报告</button><button data-search="上下文">整理上下文</button></div>'
    model = dict(data, current_group=group['id'] if group else None, prefix=prefix)
    encoded = json.dumps(model, ensure_ascii=False).replace('<', '\\u003c')
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{esc(subtitle)}"><title>{esc(title)} · Useful Agent Skills</title><link rel="stylesheet" href="{prefix}assets/discovery.css"></head>
<body><header class="topbar"><div class="shell top-inner"><a class="brand" href="{prefix}index.html"><span class="brand-icon">S</span> Useful Agent Skills</a><nav aria-label="主导航"><a href="{prefix}index.html">按需求找 Skill</a><a href="{prefix}must-have-skills/">必装 Skill</a><a href="{prefix}prompts.html">Prompt 库</a><a href="{REPO}">GitHub ↗</a></nav></div></header>
<main class="shell"><section class="hero {'group-hero' if group else ''}">{f'<div class="breadcrumb"><a href="{prefix}index.html#groups">全部需求</a><span>›</span><strong>{esc(group["title"])}</strong></div>' if group else '<div class="eyebrow">面向 Pi · OpenCode 的实用 Skill 导航</div>'}<h1>{esc(title)}</h1><p class="subtitle">{esc(subtitle)}</p>{'' if group else '<label class="search-label" for="need-search">描述需求，搜索对应场景</label><div class="search-box"><span aria-hidden="true">⌕</span><input id="need-search" type="search" placeholder="例如：修 Bug、RAG 回答不好、生成 HTML 报告" autocomplete="off"><kbd>按需求找</kbd></div>'}{hero_extra}<div id="search-results" aria-live="polite" hidden></div></section>
{content}
<details class="trust-strip"><summary>为什么这些 Skill 值得优先看？</summary><p>先匹配你的任务，再筛选 {threshold}、来源已核验且未归档的推荐项。试用或需适配条目保留在“全部适配候选”。</p><p>评分是本仓库的编辑选型分；Star 是<strong>来源仓库</strong>热度，采集于 {esc(data['sources_checked'][:10])}，不等于单个 Skill 效果。Pi / OpenCode 实机状态单独展示。</p><a href="{REPO}/blob/main/SCORING.md">查看评分维度与采用边界 ↗</a></details>
<footer><a href="{prefix}index.html">返回需求导航</a><a href="{REPO}/blob/main/content/catalog/watchlist.md">观察清单</a><a href="{REPO}/blob/main/CONTRIBUTING.md">提交使用反馈</a><span>{data['unique_skills']} 个去重候选 · 6 个需求组</span></footer></main>
<noscript><p>请启用 JavaScript 查看按需求筛选的推荐，或访问 <a href="{REPO}/tree/main/content/catalog">GitHub 分类清单</a>。</p></noscript><script type="application/json" id="discovery-data">{encoded}</script><script src="{prefix}assets/discovery.js" defer></script></body></html>'''


def render_must_have(data):
    must = data['must_have']
    def card(item, index):
        risk = {'low': '低', 'medium': '中', 'high': '高'}[item['risk']]
        compatibility = item.get('compatibility', '标准 Skill；安装前检查命令依赖、联网行为和项目权限。')
        return f'''<article class="must-card" id="skill-{esc(item['name'])}"><div class="must-rank">{index:02d}</div><div class="must-body"><div class="must-label">解决：{esc(item['need'])}</div><h3>{esc(item['name'])}</h3><p>{esc(item['reason'])}</p><div class="metrics"><a class="metric" href="{REPO}/blob/main/SCORING.md">编辑评分 <strong>{item['score']}</strong>/100</a><a class="metric" title="来源仓库 Star，采集于 {esc(item['stars_checked'])}" href="https://github.com/{esc(item['source'])}/stargazers">仓库 ★ <strong>{item['stars']:,}</strong></a><span class="runtime">{risk}风险 · Pi / OpenCode 均未实机验证</span></div><div class="actions"><a class="source-action" href="{esc(item['source_url'])}">查看已核验源码 ↗</a><button class="copy quick-copy" data-static-copy="{esc(item['install'])}">复制安装命令</button><span class="copy-status" role="status"></span></div><details class="install"><summary class="install-toggle">适配说明与完整命令</summary><p>{esc(compatibility)}</p><pre><code>{esc(item['install'])}</code></pre></details></div></article>'''
    sections = []
    counter = 1
    for section in must['sections']:
        cards = []
        for item in section['items']:
            cards.append(card(item, counter))
            counter += 1
        sections.append(f'''<section class="must-section" id="{esc(section['id'])}"><div class="section-heading"><div><span class="step">{esc(section['id']).upper()}</span><h2>{esc(section['title'])}</h2><p>{esc(section['description'])}</p></div></div><div class="must-list">{''.join(cards)}</div></section>''')
    signals = ''.join(f'''<article class="signal-card"><span>榜单热门</span><h3>{esc(x['name'])}</h3><strong>{esc(x['metric'])}</strong><p>{esc(x['note'])}</p><a href="{esc(x['url'])}">查看来源 ↗</a></article>''' for x in must['market_signals'])
    sources = ''.join(f'''<a class="source-card" href="{esc(x['url'])}"><span>{esc(x['type'])}</span><strong>{esc(x['name'])}</strong><small>{esc(x['note'])}</small></a>''' for x in must['sources'])
    model = dict(data, current_group=None, prefix='../')
    encoded = json.dumps(model, ensure_ascii=False).replace('<', '\\u003c')
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{esc(must['subtitle'])}"><title>必装 Skill · Useful Agent Skills</title><link rel="stylesheet" href="../assets/discovery.css"></head>
<body><header class="topbar"><div class="shell top-inner"><a class="brand" href="../index.html"><span class="brand-icon">S</span> Useful Agent Skills</a><nav aria-label="主导航"><a href="../index.html">按需求找 Skill</a><a href="./" aria-current="page">必装 Skill</a><a href="../prompts.html">Prompt 库</a><a href="{REPO}">GitHub ↗</a></nav></div></header>
<main class="shell"><section class="must-hero"><div class="eyebrow">SOCIAL SIGNALS → SOURCE REVIEW → SHORTLIST</div><h1>必装 Skill：少装几个，先解决高频问题</h1><p>{esc(must['subtitle'])}</p><div class="must-actions"><a class="primary-cta" href="#core">看通用必装 5 个</a><a href="#role">按工作内容加装</a><a href="#signals">看平台热门但暂缓项</a></div><div class="method-note"><strong>入选门槛</strong><span>编辑评分 ≥ 85</span><span>来源仓库 ≥ 1,000 Star</span><span>具体 SKILL.md 已核验</span><span>仓库未归档</span></div></section>
<section class="why-box"><strong>“必装”不是照搬网红榜单</strong><p>抖音、小红书和排行榜负责发现候选；本页的推荐结论来自源码、许可证、维护、风险和适配复核。安装量与收藏量代表热度，不代表效果或安全。</p><span>数据复核：{esc(must['last_verified'])} · Pi/OpenCode 实机状态仍以卡片为准</span></section>
{''.join(sections)}
<section class="must-section" id="signals"><div class="section-heading"><div><span class="step">WATCH</span><h2>榜单很热，但现在不建议盲装</h2><p>这些项目值得关注；功能边界、兼容性或安全成本还不适合写成“人人必装”。</p></div></div><div class="signal-grid">{signals}</div></section>
<section class="must-section" id="sources"><div class="section-heading"><div><span class="step">SOURCES</span><h2>榜单与内容平台来源</h2><p>社交平台用于发现，数据榜与原始仓库用于复核。</p></div></div><div class="source-grid">{sources}</div></section>
<details class="trust-strip"><summary>这个栏目怎么更新？</summary><p>每日任务检查抖音、小红书公开内容、skills.sh、Skillselion、SkillSignal 和 Skill Leaderboard。只有来源、评分或采用结论发生有意义变化时才更新页面。</p><a href="{REPO}/blob/main/content/catalog/discovery-sources.md">查看完整发现源与判断方法 ↗</a></details>
<footer><a href="../index.html">按需求找 Skill</a><a href="{REPO}/blob/main/SCORING.md">评分规则</a><a href="{REPO}/blob/main/content/catalog/watchlist.md">观察清单</a><span>最后核验 {esc(must['last_verified'])}</span></footer></main>
<script type="application/json" id="discovery-data">{encoded}</script><script src="../assets/discovery.js" defer></script></body></html>'''


def outputs(index, payloads):
    data = assemble(index, payloads)
    yield ROOT / 'site/index.html', render(data, 'index.html')
    yield ROOT / 'site/tools/index.html', render(data, 'tools/index.html')
    yield ROOT / 'site/must-have-skills/index.html', render_must_have(data)
    for group in data['groups']:
        yield ROOT / 'site' / group['page'], render(data, group['page'], group)
