"""Generate Tools catalog Markdown and GitHub Pages from content/data/tools/*.json."""

from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "content" / "data" / "tools"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def source_url(item: dict) -> str:
    ref = item["commit"] if item.get("pinning_status") == "verified" else "main"
    return f"https://github.com/{item['source']}/blob/{ref}/{item['path']}"


def markdown_escape(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def write_or_check(path: Path, content: str, check: bool, stale: list[str]) -> None:
    content = content.rstrip() + "\n"
    if check:
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            stale.append(path.relative_to(ROOT).as_posix())
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def render_catalog_index(index: dict, payloads: dict[str, dict]) -> str:
    rows = []
    for category in index["categories"]:
        slug = category["slug"]
        count = len(payloads[slug]["items"])
        rows.append(
            f"| [{category['title_zh']}]({slug}/README.md) | "
            f"{markdown_escape(category['description'])} | {count} 项 |"
        )
    return "\n".join(
        [
            "# Tools 分类",
            "",
            "Tools 收录能直接产出、验证或保护工作结果的 Skill。目录由 `content/data/tools/` 自动生成；真正安装到 Pi/OpenCode 时，每个 Skill 仍保持独立目录。",
            "",
            f"> 最近核验：{index['last_verified']}。在线入口：[Tools](https://123abc-123.github.io/useful-agent-skills/tools/)。",
            "",
            "## 当前子栏目",
            "",
            "| 子栏目 | 覆盖内容 | 数量 |",
            "|---|---|---:|",
            *rows,
            "",
            "## 目录约定",
            "",
            "```text",
            "content/catalog/tools/<category>/README.md   # 自动生成的人类可读目录",
            "content/data/tools/<category>.json           # 唯一数据源",
            "site/tools/<category>/index.html             # 自动生成的网页入口",
            "```",
            "",
            "安装目录保持扁平：`.agents/skills/<skill-name>/SKILL.md`。运行 `python tooling/scripts/build_catalog.py` 可重建本栏目。",
        ]
    )


NOTES = {
    "html-reports": "先从 `create-report` 开始；需要领导汇报时再试 `onepage`。复杂前端构建类 Skill 应先检查 Node 依赖和网络下载。",
    "browser-automation": "优先使用 `playwright-cli` 做可复现检查。MCP 型 Skill 只有在 Pi/OpenCode 已配置对应服务器时才会工作。",
    "evals-observability": "先确定评测目标和数据集，再选择 Phoenix、MLflow 或 Google Agents CLI。训练指标同步到远端前检查项目是否公开。",
    "skill-security": "安全 Skill 给出审计证据和整改建议，不等同于安全认证。任何自动修复、签名或密钥处置仍需人工复核。",
    "coding-agent-upgrades": "建议先装 `context-engineering`、`writing-plans`、`systematic-debugging` 和 `verification-before-completion`。按任务补充 TDD、测试缺口、代码评审或 worktree；强触发 Skill 过多会增加上下文和流程开销。",
}


def render_category_markdown(category: dict, payload: dict) -> str:
    rows = []
    commands = []
    for item in payload["items"]:
        rows.append(
            "| `{name}` | {purpose} | {compatibility} | {status} | {score} | {risk} | [固定源码]({url}) |".format(
                name=markdown_escape(item["name"]),
                purpose=markdown_escape(item["purpose"]),
                compatibility=markdown_escape(item["compatibility"]),
                status=markdown_escape(item["status"]),
                score=item["score"],
                risk=markdown_escape(item["risk"]),
                url=source_url(item),
            )
        )
        commands.extend([f"# {item['name']}", item["install"], ""])
    return "\n".join(
        [
            f"# {category['title_zh']}",
            "",
            f"{category['description']} 机器可读数据见 [`content/data/tools/{category['slug']}.json`](../../../data/tools/{category['slug']}.json)，网页入口见 [{category['title']}](https://123abc-123.github.io/useful-agent-skills/tools/{category['slug']}/)。",
            "",
            f"> 最近核验：{payload['last_verified']}。`passed` 才表示有实机证据；当前运行状态请查看 JSON 或网页卡片。",
            "",
            "## 精选条目",
            "",
            "| Skill | 作用 | 兼容性 | 建议 | 评分 | 风险 | 来源 |",
            "|---|---|---|---|---:|---|---|",
            *rows,
            "",
            "## 安装命令",
            "",
            "```bash",
            *commands,
            "```",
            "",
            "## 采用建议",
            "",
            NOTES[category["slug"]],
            "",
            "分数用于比较工作价值、兼容性、维护、来源和风险，不代表安全认证。安装前仍需审查 `SKILL.md`、脚本、依赖、网络行为与固定 commit。",
        ]
    )


BASE_CSS = r"""
    :root { color-scheme: light; --ink:#152033; --muted:#607087; --line:#dce3ed; --paper:#f6f8fb; --card:#fff; --navy:#14295f; --blue:#315bea; --cyan:#22a6b3; --soft:#edf2ff; --low:#137447; --medium:#966500; --high:#b42318; }
    * { box-sizing:border-box; }
    body { margin:0; font:15px/1.6 system-ui,-apple-system,"Segoe UI",sans-serif; color:var(--ink); background:var(--paper); }
    a { color:var(--blue); text-decoration:none; font-weight:650; } a:hover { text-decoration:underline; }
    header { color:#fff; background:radial-gradient(circle at 80% 10%,rgba(69,203,218,.32),transparent 28%),linear-gradient(135deg,#10204c,#315bea 72%); }
    .hero { max-width:1160px; margin:auto; padding:48px 24px 44px; }
    nav { display:flex; flex-wrap:wrap; gap:18px; margin-bottom:38px; } nav a { color:#eef3ff; }
    .eyebrow { color:#aeeaf0; font-size:12px; font-weight:800; letter-spacing:.14em; text-transform:uppercase; }
    h1 { margin:8px 0 10px; font-size:clamp(32px,5vw,56px); line-height:1.05; letter-spacing:-.045em; }
    .lede { max-width:760px; margin:0; color:#dfe7ff; font-size:17px; }
    main { max-width:1160px; margin:auto; padding:28px 24px 68px; }
    .controls { display:grid; grid-template-columns:minmax(240px,1fr) repeat(3,minmax(140px,200px)); gap:12px; margin-bottom:14px; }
    input,select { width:100%; padding:11px 12px; border:1px solid var(--line); border-radius:10px; background:#fff; color:var(--ink); font:inherit; }
    .summary { margin:10px 0 20px; color:var(--muted); }
    .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(310px,1fr)); gap:15px; }
    article { display:flex; flex-direction:column; padding:19px; border:1px solid var(--line); border-radius:15px; background:var(--card); box-shadow:0 8px 26px rgba(21,32,51,.055); }
    article h2 { margin:0 0 7px; font-size:19px; letter-spacing:-.02em; }
    article p { flex:1; margin:0 0 14px; color:var(--muted); }
    .meta { display:flex; flex-wrap:wrap; gap:7px; margin-bottom:14px; }
    .tag { padding:3px 8px; border-radius:999px; background:var(--soft); color:#2949aa; font-size:12px; }
    .risk-low { color:var(--low); background:#e7f6ee; } .risk-medium { color:var(--medium); background:#fff4d3; } .risk-high { color:var(--high); background:#ffebe9; }
    .actions { display:flex; flex-wrap:wrap; gap:9px; align-items:center; }
    button { padding:7px 10px; border:1px solid #c8d4f5; border-radius:8px; color:#2449b7; background:#f2f5ff; cursor:pointer; font:600 13px/1.2 inherit; }
    button:hover { background:#e7edff; }
    .empty { grid-column:1/-1; padding:40px; text-align:center; color:var(--muted); }
    footer { margin-top:38px; padding-top:20px; border-top:1px solid var(--line); color:var(--muted); }
    @media(max-width:720px){ .controls{grid-template-columns:1fr}.hero{padding-top:30px}nav{margin-bottom:28px}.grid{grid-template-columns:1fr} }
"""


CATEGORY_TEMPLATE = r"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="description" content="@@DESCRIPTION@@">
  <title>@@TITLE@@ · Useful Agent Skills</title>
  <style>@@CSS@@</style>
</head>
<body>
  <header><div class="hero">
    <nav aria-label="目录导航"><a href="../../index.html">Skills</a><a href="../../prompts.html">Prompt Library</a><a href="../index.html">Tools</a><a href="https://github.com/123abc-123/useful-agent-skills">GitHub</a></nav>
    <div class="eyebrow">Tools / @@SLUG@@</div><h1>@@TITLE@@</h1><p class="lede">@@DESCRIPTION@@</p>
  </div></header>
  <main>
    <div class="controls"><input id="query" type="search" placeholder="搜索名称、用途或来源" aria-label="搜索"><select id="kind" aria-label="类型"><option value="">全部类型</option></select><select id="status" aria-label="建议"><option value="">全部建议</option><option value="recommended">推荐</option><option value="trial">小范围试用</option><option value="needs-adaptation">需要适配</option></select><select id="risk" aria-label="风险"><option value="">全部风险</option><option value="low">低风险</option><option value="medium">中风险</option><option value="high">高风险</option></select></div>
    <div id="summary" class="summary">正在读取目录…</div><section id="grid" class="grid" aria-live="polite"></section>
    <footer>数据来自 <a href="https://github.com/123abc-123/useful-agent-skills/blob/main/content/data/tools/@@SLUG@@.json">content/data/tools/@@SLUG@@.json</a>。安装前请检查固定源码、依赖、权限和运行状态。</footer>
  </main>
  <script>
    const labels={low:"低风险",medium:"中风险",high:"高风险",recommended:"推荐",trial:"小范围试用","needs-adaptation":"需要适配"};
    let items=[]; const q=document.querySelector("#query"),kind=document.querySelector("#kind"),status=document.querySelector("#status"),risk=document.querySelector("#risk"),grid=document.querySelector("#grid"),summary=document.querySelector("#summary");
    const esc=v=>String(v).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"})[c]);
    function url(x){const ref=x.pinning_status==="verified"?x.commit:"main";return `https://github.com/${x.source}/blob/${ref}/${x.path}`}
    function render(){const term=q.value.trim().toLowerCase();const found=items.filter(x=>(!term||`${x.name} ${x.purpose} ${x.source} ${x.category}`.toLowerCase().includes(term))&&(!kind.value||x.category===kind.value)&&(!status.value||x.status===status.value)&&(!risk.value||x.risk===risk.value));summary.textContent=`显示 ${found.length} / ${items.length} 项；passed 才表示已有实机测试证据。`;grid.innerHTML=found.map(x=>`<article><h2>${esc(x.name)}</h2><p>${esc(x.purpose)}</p><div class="meta"><span class="tag">${esc(x.category)}</span><span class="tag">评分 ${x.score}</span><span class="tag">${esc(labels[x.status]||x.status)}</span><span class="tag risk-${esc(x.risk)}">${esc(labels[x.risk])}</span><span class="tag">Pi ${esc(x.runtime_pi)}</span><span class="tag">OpenCode ${esc(x.runtime_opencode)}</span></div><div class="actions"><a href="${url(x)}">固定源码</a><a href="https://github.com/${esc(x.source)}">仓库</a><button data-install="${esc(x.install)}">复制安装命令</button></div></article>`).join("")||'<div class="empty">没有符合条件的条目。</div>';document.querySelectorAll("[data-install]").forEach(button=>button.addEventListener("click",async()=>{await navigator.clipboard.writeText(button.dataset.install);button.textContent="已复制";setTimeout(()=>button.textContent="复制安装命令",1200)}))}
    fetch("../../data/tools/@@SLUG@@.json").then(r=>{if(!r.ok)throw new Error(r.status);return r.json()}).then(data=>{items=data.items;[...new Set(items.map(x=>x.category))].sort().forEach(value=>{const option=document.createElement("option");option.value=value;option.textContent=value;kind.appendChild(option)});render()}).catch(()=>summary.textContent="目录读取失败，请前往 GitHub 查看原始数据。");[q,kind,status,risk].forEach(x=>x.addEventListener("input",render));
  </script>
</body></html>
"""


TOOLS_TEMPLATE = r"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="面向算法工程师的 Pi 与 OpenCode 实用工具型 Skills"><title>Tools · Useful Agent Skills</title><style>@@CSS@@
    .stats{display:flex;flex-wrap:wrap;gap:12px;margin-top:24px}.stat{padding:9px 13px;border:1px solid rgba(255,255,255,.22);border-radius:10px;background:rgba(255,255,255,.1)}
    .category-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px}.category{position:relative;min-height:210px}.icon{font-size:30px;color:var(--blue)}.category h2{font-size:23px}.count{margin-top:13px;color:var(--muted)}.open{margin-top:12px}@media(max-width:720px){.category-grid{grid-template-columns:1fr}}
  </style></head><body><header><div class="hero"><nav><a href="../index.html">Skills</a><a href="../prompts.html">Prompt Library</a><a href="./index.html">Tools</a><a href="https://github.com/123abc-123/useful-agent-skills">GitHub</a></nav><div class="eyebrow">Curated for Pi + OpenCode</div><h1>Tools</h1><p class="lede">从“能做什么”出发选择 Skill：增强 Coding Agent、生成报告、验证页面、评测系统、追踪训练或审查供应链。</p><div class="stats">@@STATS@@</div></div></header><main><section class="category-grid">@@CARDS@@</section><footer>目录由 <a href="https://github.com/123abc-123/useful-agent-skills/tree/main/content/data/tools">content/data/tools</a> 自动生成。每个条目都区分源码核验、安装语法和实机运行状态。</footer></main></body></html>
"""


def render_category_page(category: dict) -> str:
    return (
        CATEGORY_TEMPLATE.replace("@@CSS@@", BASE_CSS)
        .replace("@@TITLE@@", html.escape(category["title"]))
        .replace("@@DESCRIPTION@@", html.escape(category["description"]))
        .replace("@@SLUG@@", category["slug"])
    )


def render_tools_page(index: dict, payloads: dict[str, dict]) -> str:
    total = sum(len(value["items"]) for value in payloads.values())
    stats = f'<span class="stat"><strong>{len(index["categories"])}</strong> 个分类</span><span class="stat"><strong>{total}</strong> 个精选工具 Skill</span><span class="stat">核验于 {html.escape(index["last_verified"])}</span>'
    cards = []
    for category in index["categories"]:
        count = len(payloads[category["slug"]]["items"])
        cards.append(
            f'<article class="category"><div class="icon">{html.escape(category["icon"])}</div>'
            f'<h2>{html.escape(category["title_zh"])}</h2><p>{html.escape(category["description"])}</p>'
            f'<div class="count">{count} 个条目</div><div class="open"><a href="./{category["slug"]}/">打开栏目 →</a></div></article>'
        )
    return (
        TOOLS_TEMPLATE.replace("@@CSS@@", BASE_CSS)
        .replace("@@STATS@@", stats)
        .replace("@@CARDS@@", "".join(cards))
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated files are stale")
    args = parser.parse_args()
    index = read_json(DATA_DIR / "index.json")
    payloads = {category["slug"]: read_json(DATA_DIR / f"{category['slug']}.json") for category in index["categories"]}
    stale: list[str] = []

    write_or_check(ROOT / "content" / "catalog" / "tools" / "README.md", render_catalog_index(index, payloads), args.check, stale)
    write_or_check(ROOT / "site" / "tools" / "index.html", render_tools_page(index, payloads), args.check, stale)
    for category in index["categories"]:
        slug = category["slug"]
        write_or_check(ROOT / "content" / "catalog" / "tools" / slug / "README.md", render_category_markdown(category, payloads[slug]), args.check, stale)
        write_or_check(ROOT / "site" / "tools" / slug / "index.html", render_category_page(category), args.check, stale)

    if stale:
        print("Generated catalog files are stale:")
        for path in stale:
            print(f"- {path}")
        print("Run: python tooling/scripts/build_catalog.py")
        return 1
    action = "Checked" if args.check else "Generated"
    print(f"{action} {len(index['categories'])} Tools categories with {sum(len(x['items']) for x in payloads.values())} entries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
