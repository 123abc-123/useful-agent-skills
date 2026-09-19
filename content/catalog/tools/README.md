# Tools 分类

Tools 收录能直接产出、验证或保护工作结果的 Skill。目录由 `content/data/tools/` 自动生成；真正安装到 Pi/OpenCode 时，每个 Skill 仍保持独立目录。

> 最近核验：2026-09-19。在线入口：[Tools](https://123abc-123.github.io/useful-agent-skills/tools/)。

## 当前子栏目

| 子栏目 | 覆盖内容 | 数量 |
|---|---|---:|
| [HTML 报告与可视化](html-reports/README.md) | 技术报告、领导汇报、交互式 HTML、幻灯片和架构图。 | 7 项 |
| [浏览器与自动化](browser-automation/README.md) | 真实浏览器检查、UI 调试、页面探索和 Playwright 测试生成。 | 5 项 |
| [评测与可观测性](evals-observability/README.md) | Agent/LLM 评测、Tracing、训练监控和测试缺口审计。 | 7 项 |
| [Skill 与 Agent 安全](skill-security/README.md) | MCP 配置、密钥、供应链完整性和 Agent 安全基线。 | 5 项 |
| [Coding Agent 增强](coding-agent-upgrades/README.md) | 通过上下文、计划、调试、测试、评审和完成验证，让 Coding Agent 更稳定、更少返工。 | 11 项 |

## 目录约定

```text
content/catalog/tools/<category>/README.md   # 自动生成的人类可读目录
content/data/tools/<category>.json           # 唯一数据源
site/tools/<category>/index.html             # 自动生成的网页入口
```

安装目录保持扁平：`.agents/skills/<skill-name>/SKILL.md`。运行 `python tooling/scripts/build_catalog.py` 可重建本栏目。
