# Coding Agent 增强

通过上下文、计划、调试、测试、评审和完成验证，让 Coding Agent 更稳定、更少返工。 机器可读数据见 [`content/data/tools/coding-agent-upgrades.json`](../../../data/tools/coding-agent-upgrades.json)，网页入口见 [Coding Agent Upgrades](https://123abc-123.github.io/useful-agent-skills/tools/coding-agent-upgrades/)。

> 最近核验：2026-09-27。`passed` 才表示有实机证据；当前运行状态请查看 JSON 或网页卡片。

## 先选你要解决的问题

| 我的需求 | 推荐路径 |
|---|---|
| 修 Bug，总在反复猜 | [按需求查看首选与备选](https://123abc-123.github.io/useful-agent-skills/tools/coding-agent-upgrades/?task=debug#results) |
| 接手陌生仓库，先读懂代码 | [按需求查看首选与备选](https://123abc-123.github.io/useful-agent-skills/tools/coding-agent-upgrades/?task=understand#results) |
| 做新功能，先把步骤想清楚 | [按需求查看首选与备选](https://123abc-123.github.io/useful-agent-skills/tools/coding-agent-upgrades/?task=feature#results) |
| 写代码时就防住回归 | [按需求查看首选与备选](https://123abc-123.github.io/useful-agent-skills/tools/coding-agent-upgrades/?task=test#results) |
| 提交前检查，别漏问题 | [按需求查看首选与备选](https://123abc-123.github.io/useful-agent-skills/tools/coding-agent-upgrades/?task=review#results) |
| 多任务并行，隔离代码改动 | [按需求查看首选与备选](https://123abc-123.github.io/useful-agent-skills/tools/coding-agent-upgrades/?task=isolate#results) |

网页默认筛选编辑评分 ≥85、来源仓库 ≥1,000 Star、来源已核验且未归档的推荐项；不足门槛的候选可手动展开。评分是编辑选型分，Star 是仓库热度，两者都不是实机效果证明。

## 精选条目

| Skill | 作用 | 兼容性 | 建议 | 评分 | 风险 | 来源 |
|---|---|---|---|---:|---|---|
| `acquire-codebase-knowledge` | 扫描陌生代码库并生成结构、入口、依赖和架构地图，减少 Agent 在修改前的错误假设。 | 需要 Python 3.8+、Git 和仓库内扫描脚本；先审查脚本，再在目标仓库根目录运行。 | recommended | 90 | medium | [固定源码](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/acquire-codebase-knowledge/SKILL.md) |
| `context-engineering` | 为 Coding Agent 组织规则、架构、相关文件和验证证据，减少上下文污染与重复探索。 | 标准 Skill；可能建议修改 AGENTS.md、规则文件或上下文文档，写入前应检查范围。 | recommended | 92 | medium | [固定源码](https://github.com/addyosmani/agent-skills/blob/c004a74784a08295d52749b04cda634125b9a581/skills/context-engineering/SKILL.md) |
| `brainstorming` | 在实现功能前澄清目标、约束、设计选项和验收条件，降低做错方向的概率。 | 触发范围较强；可纯文本使用，但可选视觉伴侣会启动本地服务并打开浏览器，Pi/OpenCode 需适配该流程。 | trial | 93 | medium | [固定源码](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/brainstorming/SKILL.md) |
| `writing-plans` | 把规格或需求压缩成实现者必须知道的决策：文件、接口签名、测试断言、规格值与验证命令，避免计划变成代码抄写。 | 纯指令型；会创建计划文档并要求计划自检。v6.4.2 上游报告在缺陷探针中保持 9/9，同时显著减少计划时间与 token；该结果不是 Pi/OpenCode 实机证据。 | recommended | 92 | low | [固定源码](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/writing-plans/SKILL.md) |
| `create-implementation-plan` | 为功能、重构、依赖升级或基础设施变更生成与仓库证据对应的实现计划。 | 标准 Skill；会写入计划文件，开始实现前仍需人工确认范围和命令。 | recommended | 88 | low | [固定源码](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/create-implementation-plan/SKILL.md) |
| `using-git-worktrees` | 在执行较大改动前建立隔离工作区，减少并行任务和现有工作树互相污染。 | 需要 Git，可能创建目录、分支和 worktree；执行前确认目标路径和当前未提交改动。 | trial | 90 | medium | [固定源码](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/using-git-worktrees/SKILL.md) |
| `test-driven-development` | 针对功能实现、缺陷修复或直接粘贴的代码，先建立失败测试，再用仓库自己的命令完成红、绿、重构。 | 会修改测试和实现并运行项目命令；新增粘贴代码的触发描述。附加浏览器检查依赖 Chrome DevTools MCP，子 Agent 步骤需宿主支持；根目录 references 需随安装方式单独核对。 | recommended | 92 | medium | [固定源码](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/test-driven-development/SKILL.md) |
| `systematic-debugging` | 要求 Agent 先收集证据、形成假设和最小复现，再修改代码并验证根因。 | 标准 Skill；调查过程中会运行测试和诊断命令，需遵守仓库权限边界。 | recommended | 94 | medium | [固定源码](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/systematic-debugging/SKILL.md) |
| `test-gap-audit` | 只读审计缺失、薄弱、过时或范围错误的测试，并按风险给出具体补测建议。 | 默认只读，但会优先运行随 Skill 提供的 Python coverage_map.py；需先审查脚本，也可退回人工审计。 | recommended | 89 | medium | [固定源码](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/test-gap-audit/SKILL.md) |
| `code-review-and-quality` | 从正确性、可读性、架构、安全和性能审查代码，并通过条件反转实验检查回归测试缺口。 | 标准指令型 Skill；新版会临时修改条件、运行项目测试并从副本恢复，需在隔离工作区执行并核对恢复结果。引用仓库根目录 references，单独复制 Skill 时需补齐对应资料。 | recommended | 91 | medium | [固定源码](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/code-review-and-quality/SKILL.md) |
| `verification-before-completion` | 阻止 Agent 在没有新鲜命令输出时声称任务已经完成、修复或通过。 | 标准 Skill；会运行与完成声明对应的测试、构建或检查命令。 | recommended | 94 | medium | [固定源码](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/verification-before-completion/SKILL.md) |

## 安装命令

```bash
# acquire-codebase-knowledge
npx skills add github/awesome-copilot --skill acquire-codebase-knowledge -a pi -a opencode --copy

# context-engineering
npx skills add addyosmani/agent-skills --skill context-engineering -a pi -a opencode --copy

# brainstorming
npx skills add obra/superpowers --skill brainstorming -a pi -a opencode --copy

# writing-plans
npx skills add obra/superpowers --skill writing-plans -a pi -a opencode --copy

# create-implementation-plan
npx skills add github/awesome-copilot --skill create-implementation-plan -a pi -a opencode --copy

# using-git-worktrees
npx skills add obra/superpowers --skill using-git-worktrees -a pi -a opencode --copy

# test-driven-development
npx skills add addyosmani/agent-skills --skill test-driven-development -a pi -a opencode --copy

# systematic-debugging
npx skills add obra/superpowers --skill systematic-debugging -a pi -a opencode --copy

# test-gap-audit
npx skills add github/awesome-copilot --skill test-gap-audit -a pi -a opencode --copy

# code-review-and-quality
npx skills add addyosmani/agent-skills --skill code-review-and-quality -a pi -a opencode --copy

# verification-before-completion
npx skills add obra/superpowers --skill verification-before-completion -a pi -a opencode --copy

```

## 采用建议

建议先装 `context-engineering`、`writing-plans`、`systematic-debugging` 和 `verification-before-completion`。按任务补充 TDD、测试缺口、代码评审或 worktree；强触发 Skill 过多会增加上下文和流程开销。

分数用于比较工作价值、兼容性、维护、来源和风险，不代表安全认证。安装前仍需审查 `SKILL.md`、脚本、依赖、网络行为与固定 commit。
