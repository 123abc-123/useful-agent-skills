# 更新记录

## 2026-09-18

- 新增 MLflow 官方 Agent 评测与 tracing Skills；固定源码 commit 已通过 API 和网页双重核验，Pi/OpenCode 实机状态仍为 `not-run`。
- 新增 `agent-skill-eval` 与 `agent-skills-creator` 观察项，分别用于真实 Harness 对照评测和 Skill 生命周期审计。
- Prompt 工具导航新增 `agent-skill-eval`，补充启用/禁用 Skill 的 pass@k、成本、耗时与误触发评测路径。
- 复核 skills.sh、Skillselion、SkillSignal、LinklyAI、Skill Leaderboard 与 Skills.sh Dashboard；继续只把榜单作为候选发现依据。

## 2026-09-15

- 新增 Google Agents CLI 的 Agent 评测与可观测性 Skill；固定源码 commit 已通过 API 和网页双重核验，实机状态仍为 `not-run`。
- 新增 `pi-open-agents` 观察项，关注 Pi/OpenCode 共用 Agent 定义、模型路由和权限控制。
- 新增 2026-09-11 发布的 Skill 优化实证论文 `Skill Issue`。
- 核验 skills.sh、Skillselion、SkillSignal、LinklyAI、Skill Leaderboard 与 Skills.sh Dashboard；热度变化只作为候选发现证据。

## 2026-09-13

- 新增 10 个面向算法工程的原创 Prompt、机器可读索引和可搜索网页。
- 新增开源 Prompt 库、课程、Pattern 与评测工具导航。
- 新增 Prompt 变量一致性和回归案例结构校验。
- 新增数据泄漏、训练 NaN 与论文技术验证三个可复现实战案例。
- 新增 20 项机器可读精选清单、评分规则、精确 `SKILL.md` 路径、固定 commit 和真实测试状态字段。
- 新增五个无脚本算法工程 Skill：数据泄漏审计、实验评审、模型评测报告、训练故障定位、论文技术验证。
- 新增 Pi/OpenCode 安装命令、实机测试记录模板、贡献指南和 MIT 许可证。
- 新增 GitHub Actions 结构/链接检查与可搜索的 GitHub Pages 页面。
- 将主要 Superpowers 推荐更新到持续维护的 `obra/superpowers` 主仓库。
- 新增 Skill 安装榜、Codex 榜、近 7 天趋势榜和多平台聚合榜来源。
- 每日检索加入榜单交叉验证，同时明确热度不等于质量或安全。
- 创建面向算法工程师的 Skill 分类清单。
- 加入 Pi 与 OpenCode 兼容性说明。
- 加入 Harness 专题、学习资源、观察清单和安全审查规则。
- 首批覆盖机器学习、实验评测、调试交付、安全、浏览器、云、文档和 Harness 元工具。
