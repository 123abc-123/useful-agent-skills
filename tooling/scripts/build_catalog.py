"""Generate Tools catalog Markdown and GitHub Pages from content/data/tools/*.json."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from build_discovery import outputs as discovery_outputs


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
    scenarios = []
    if category.get('tasks'):
        scenarios = ['## 先选你要解决的问题', '', '| 我的需求 | 推荐路径 |', '|---|---|']
        for task in category['tasks']:
            scenarios.append(f"| {markdown_escape(task['title'])} | [按需求查看首选与备选](https://123abc-123.github.io/useful-agent-skills/tools/{category['slug']}/?task={task['id']}#results) |")
        scenarios += ['', '网页默认筛选编辑评分 ≥85、来源仓库 ≥1,000 Star、来源已核验且未归档的推荐项；不足门槛的候选可手动展开。评分是编辑选型分，Star 是仓库热度，两者都不是实机效果证明。', '']
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
            *scenarios,
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated files are stale")
    args = parser.parse_args()
    index = read_json(DATA_DIR / "index.json")
    payloads = {category["slug"]: read_json(DATA_DIR / f"{category['slug']}.json") for category in index["categories"]}
    stale: list[str] = []

    write_or_check(ROOT / "content" / "catalog" / "tools" / "README.md", render_catalog_index(index, payloads), args.check, stale)
    for path, content in discovery_outputs(index, payloads):
        write_or_check(path, content, args.check, stale)
    for category in index["categories"]:
        slug = category["slug"]
        category['tasks'] = next(g['tasks'] for g in index['navigation']['groups'] if g['id'] == slug)
        write_or_check(ROOT / "content" / "catalog" / "tools" / slug / "README.md", render_category_markdown(category, payloads[slug]), args.check, stale)

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
