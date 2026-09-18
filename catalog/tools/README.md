# Tools 分类

Tools 用于归档“能直接产出或增强工作结果”的工具型 Skill。这里负责分类和选型；真正安装到 Pi/OpenCode 时，每个 Skill 仍保持独立目录。

## 当前子栏目

| 子栏目 | 覆盖内容 | 状态 |
|---|---|---|
| [HTML 报告与可视化](html-reports/README.md) | 技术报告、领导汇报、交互 HTML、幻灯片、架构图 | 已上线 |
| 浏览器与自动化 | 浏览器测试、页面取证、工作流自动化 | 使用 [完整分类清单](../skills.md) |
| Skill 创建与评测 | 创建、校验、路由评测和回归测试 | 使用 [完整分类清单](../skills.md) |
| 可观测性 | tracing、日志、评测结果分析 | 使用 [完整分类清单](../skills.md) |
| 安全扫描 | Skill、依赖和供应链审查 | 使用 [完整分类清单](../skills.md) |

新的工具类资源只有在条目足够形成独立筛选和维护规则时才建立子栏目，避免为单个链接创建空目录。

## 推荐目录形态

```text
catalog/tools/<category>/README.md   # 人工分类、说明和采用建议
data/tools/<category>.json           # 机器可读数据
docs/tools/<category>/index.html     # GitHub Pages 子栏目
```

安装目录保持扁平：

```text
.agents/skills/create-report/SKILL.md
.agents/skills/onepage/SKILL.md
.agents/skills/beautiful-mermaid/SKILL.md
```

不要安装成 `.agents/skills/tools/html-reports/<skill>/`。部分 Harness 会递归扫描，但扁平的单 Skill 目录更符合跨平台使用和 Skills CLI 的识别方式。
