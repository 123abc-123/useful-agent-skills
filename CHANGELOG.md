# 更新记录

## 2026-09-23

- 新增独立“必装 Skill”栏目：通用必装 5 个、按工作内容加装 4 个，以及热门但暂缓安装清单；首页和顶部导航均提供入口。
- 新增抖音天丁榜单、小红书热门清单公开整理与专业榜单的分层证据；内容平台只负责发现，推荐结论仍由具体 `SKILL.md`、评分、来源仓库 Star、维护、许可证、风险和 Pi/OpenCode 适配决定。
- 新增 `content/data/must-have-skills.json` 作为栏目数据源，并把页面纳入统一生成流程和移动端回归检查。
- 榜单复查发现 `vercel-labs/agent-browser` 已进入 skills.sh / Codex 热门前列（约 91.4 万次安装，来源仓库约 4.31 万 Star）。其功能与维护活跃度较强，但当前 Skill 使用 `hidden: true`，OpenCode 存在未关闭的发现兼容问题；同时安装会下载 Chrome、运行浏览器守护进程并动态加载指令，因此先加入观察清单，不进入默认推荐。
- 重新核对 skills.sh、Skillselion、SkillSignal、LinklyAI、Skill Leaderboard 与 Ecosystem Dashboard，并继续区分安装量、GitHub Star、维护状态和兼容性证据。
- `PlainConceptsPlatform/agent-harness` 原仓库已返回 404，从 Harness 与观察清单移除，避免继续导向失效来源。

## 2026-09-20

- 首页完整展示 20 个具体需求入口，每个入口一键直达对应栏目与推荐结果。
- 栏目页将“当前需求 → 首选 Skill → 备选”移到首屏；其他场景与选型依据改为按需展开。
- 首选项强化评分、来源仓库 Star、源码与复制安装命令，备选项缩小层级，减少目录感。
- HTML 报告与可视化栏目新增 `diagram-design`：覆盖 40 余种品牌化架构图、流程图和数据图，来源仓库约 4.1 万 Star，MIT 许可证；上游明确支持 Pi，OpenCode 使用标准 Skill 目录。
- 需求导航新增“画架构图、流程图或数据图”场景，以 `diagram-design` 为首选、`beautiful-mermaid` 为轻量备选；两者的 Pi/OpenCode 实机状态仍为 `not-run`。

## 2026-09-19

- 将首页和 Tools 页面重做为“需求 → 场景 → 首选 Skill＋备选”的选择路径，覆盖 6 组需求、19 个具体场景。
- 新增“高分高热度”默认筛选：编辑评分 ≥85、来源仓库 ≥1,000 Star；Star 显示采集时间并明确只代表仓库热度。
- 新增来源仓库快照、需求导航生成器和浏览器回归测试，覆盖桌面端、390px 移动端、搜索、深链、历史导航、筛选、排序与复制。
- 新增“Coding Agent 增强”栏目，首批收录 11 个上下文、需求澄清、计划、隔离执行、调试、测试、评审和完成验证 Skill；网页支持按子类型筛选。
- Tools 扩展为 5 个栏目、35 个条目，首页增加 Coding Agent 增强入口。
- 将顶层内容归并为 `content/`、`site/` 和 `tooling/` 三层；根目录保留可安装的 `skills/`，公开网页 URL 不变。
- 今日新增 Elastic LLM 可观测、AWS Skill Eval 和 Datadog Agent Observability 三个观察项；均核对了固定 commit、许可证和具体 `SKILL.md`，但未执行第三方脚本或写成 Pi/OpenCode 实机通过。
- 精选清单由 24 项扩展到 32 项，新增代码评审、上下文工程、TDD、本地模型、视觉训练、实验追踪、测试缺口审计和 MCP 安全审计。
- Tools 扩展浏览器自动化、评测与可观测性、Skill 与 Agent 安全等专题。
- 数据升级到 schema v2，每项独立记录 `last_verified`、`pinning_status` 和 `runtime_evidence`。
- 新增 `tooling/scripts/build_catalog.py`，由 `content/data/tools/` 自动生成 Tools Markdown 与网页；CI 检查生成结果是否过期。
- 重做 README 与 Pages 首页，增加快速安装、任务入口、信任说明、运行状态筛选和复制安装命令。
- 新增 `SECURITY.md`、主机运行环境证据和 2026-W38 周报。
- GitHub Actions 固定到具体 commit，Pages 构建改为自动复制全部 Tools 数据。
- 将仓库的内容、结构化数据和站点入口分层，并新增 Tools 一级目录索引。
- HTML 报告栏目移动到 `tools/html-reports` 子目录；旧网页地址保留自动跳转。
- Pages 构建改为递归复制 `site/`，后续新增 Tools 子栏目无需逐个登记页面文件。
- 新增独立的 HTML 报告与可视化栏目、7 项机器可读清单和可搜索 GitHub Pages 页面。
- 首批覆盖通用技术报告、研究报告、中文领导汇报、视觉设计、复杂交互页面、HTML 幻灯片和 Mermaid 图表。
- 每项记录固定 commit、许可证、输出类型、安装状态、Pi/OpenCode 实机状态、适配成本和风险。

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
