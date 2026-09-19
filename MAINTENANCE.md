# 维护与每日更新规则

## 每日检索范围

每日任务优先搜索以下来源：

- GitHub 新仓库、Release、Topic 和近期活跃项目；
- `skills.sh` 热门榜、趋势榜和 Skill 详情；
- Skillselion Codex 榜、SkillSignal 近 7 天榜、LinklyAI 聚合数据等二次发现源；
- Agent Skills 规范及官方实现；
- Pi、OpenCode、Hugging Face、Microsoft、GitHub、Cloudflare、Trail of Bits、Sentry 等官方或工程团队仓库；
- 榜单与发现目录，但不把安装量、增长率或排名直接当作推荐依据；
- Harness、context engineering、agent evals、observability、skill security 等关键词。
- Prompt library、prompt patterns、prompt evaluation、prompt regression 和 red teaming 工具。
- HTML report、interactive report、data visualization、HTML slides、dashboard 和 architecture diagram Skill。

建议组合查询：

```text
site:github.com SKILL.md agent skills created:>YYYY-MM-DD
site:github.com agent harness skill OpenCode
site:github.com agent skill Pi coding agent
site:github.com machine learning agent skills
site:github.com LLM eval tracing skill
site:github.com agent skill security scanner
site:skills.sh agent skill trending
site:github.com agent skills leaderboard weekly installs
site:github.com prompt library prompt evaluation agent
site:github.com SKILL.md HTML report visualization slides
```

榜单来源和各自统计口径见 `catalog/discovery-sources.md`。每日任务至少交叉检查一个原始榜单、一个二次趋势来源和候选 Skill 的 GitHub 原仓库。

## 收录流程

1. 找到候选项目后，打开仓库和具体 `SKILL.md`，不依据搜索摘要下结论。
2. 记录候选来自总安装榜、近 7 天榜、增长榜还是 GitHub 搜索，避免混淆指标。
3. 检查维护者、许可证、最近提交、Release、Issue 和实际文件。
4. 检查脚本、依赖、外部下载、网络调用、凭据读取和高权限命令。
5. 判断 Pi/OpenCode 属于原生、标准或需要适配。
6. 写明它解决的具体工作问题，并与现有条目去重。
7. 新且证据不足的项目先放入 `catalog/watchlist.md`。
8. 运行 `python scripts/validate_catalog.py`。
9. 只有发现有意义变化时才提交；纯排名波动不更新。

## 精选清单的数据规则

`data/recommended-skills.json` 是精选层的机器可读数据。新增或更新精选项时必须同步检查：

- 精确 `SKILL.md` 路径；
- 审查时观察到的 40 位第三方 commit，以及是否能通过 GitHub API 和网页双重解析；
- SPDX 许可证标识；
- 按 `SCORING.md` 计算的分数与独立风险等级；
- `source_path`、`install_syntax`、`runtime_pi` 和 `runtime_opencode` 状态；
- `catalog/recommended-stack.md` 中的用途、命令和风险说明。

第三方默认分支变化不应自动覆盖固定 commit。先比较差异，再更新 commit 和核验日期。commit 未通过双重解析时，将 `pinning_status` 保持为 `pending-upstream-commit-verification`，对外链接使用 `main` 的精确路径。

## Prompt Library 数据规则

`data/prompts.json` 是原创 Prompt 的机器可读索引。新增或修改模板时必须：

- 使用 `prompts/<name>.prompt.md`，并包含 `name`、`description`、`category` frontmatter；
- 让索引中的变量与模板内全部 `{{variable}}` 精确一致；
- 写明输入、输出结构、证据要求和信息不足时的行为；
- 添加至少一个应满足和一个不应发生的回归案例；
- 不复制许可证不明的第三方 Prompt，不写入密钥、客户数据或内部路径；
- 运行 `python scripts/validate_catalog.py`。

## Tools 子栏目数据规则

Tools 使用一致的三层结构，其中 JSON 是唯一数据源：

```text
data/tools/<category>.json           # 人工维护
catalog/tools/<category>/README.md   # 自动生成
docs/tools/<category>/index.html     # 自动生成
```

新增或更新工具子栏目时必须：

- 修改 JSON 后运行 `python scripts/build_catalog.py`，保持分类说明、结构化数据和网页卡片一致；
- 记录固定 commit、许可证、输出类型、适配说明、评分、状态和风险；
- 分别记录 `source_path`、`install_syntax`、`runtime_pi` 和 `runtime_opencode`；
- 实机未运行时保持 `not-run`，不把源码可移植推断写成通过；
- 页面或数据结构变化后检查桌面、移动端、搜索、筛选和复制功能；
- 保留已经公开的旧 URL 跳转，避免外部链接失效。

Tools 只负责分类。真正安装到 Pi/OpenCode 时，仍使用 `.agents/skills/<skill-name>/SKILL.md`，不在安装目录中复制 `tools/<category>/` 层级。

## 更新准则

有意义变化包括：

- 新增值得试用的 Skill 或高质量学习资源；
- 项目新增 Pi/OpenCode 官方支持；
- 重要 Release 改变安装方式、能力或兼容性；
- 项目停止维护、归档、改名或出现重大安全问题；
- 链接失效或原有描述已经不准确。

每日自动任务应保持安静，未发现有意义变化时不提交、不通知。发现候选但证据不足时，只更新观察清单并注明原因。任何第三方脚本都不能因为自动更新任务而被直接执行。

每周一可以生成一次 `reports/weekly/` 简报，汇总新增、上升、降级、移除和 Pi/OpenCode 兼容性变化。没有有意义变化时不创建空报告。

## 人工复核重点

- Skill 中是否要求忽略上层指令或绕过权限；
- 是否读取 SSH key、云凭据、浏览器 cookie、环境变量或大范围用户目录；
- 是否使用 `curl | sh`、远程脚本、不可固定版本的依赖；
- 是否把内容上传到第三方服务；
- 是否包含删除、发布、部署、合并、付费等高影响动作；
- 是否把特定 Agent 的工具名伪装成通用兼容。
