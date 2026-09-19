# 目录索引

`content/catalog/` 保存人工整理的分类说明、推荐理由和采用边界。可安装 Skill 仍放在仓库根目录的 `skills/<skill-name>/`，分类目录不会改变 Pi/OpenCode 的发现路径。

| 分类 | 内容 | 入口 |
|---|---|---|
| 精选组合 | 评分较高、用途明确的安装组合 | [recommended-stack.md](recommended-stack.md) |
| 完整分类 | 算法、训练、评测、调试、安全、云与文档 | [skills.md](skills.md) |
| Tools | 报告、可视化及后续工具型子栏目 | [tools/](tools/README.md) |
| Prompt | 开源 Prompt 库和工程工具 | [prompt-libraries.md](prompt-libraries.md) |
| Harness | Agent Harness 的组成、方案和采用建议 | [harness.md](harness.md) |
| 学习 | Skill、MCP、Agent、评测与安全课程 | [learning-resources.md](learning-resources.md) |
| 发现 | 榜单、趋势榜和搜索渠道 | [discovery-sources.md](discovery-sources.md) |
| 观察 | 证据不足或仍需适配的候选项目 | [watchlist.md](watchlist.md) |

## 目录与安装位置

```text
content/catalog/               # 给人阅读的分类与判断
content/data/                  # 网页和自动化读取的结构化数据
site/                          # GitHub Pages
skills/<skill-name>/SKILL.md   # 本仓库自己维护的可安装 Skill
```

第三方 Skill 只在 `content/catalog/` 和 `content/data/` 中记录，不把其源码复制进本仓库。需要试用时，使用固定来源安装到项目的 `.agents/skills/<skill-name>/`。
