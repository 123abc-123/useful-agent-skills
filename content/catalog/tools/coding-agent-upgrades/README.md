# Coding Agent 增强

通过上下文、计划、调试、测试、评审和完成验证，让 Coding Agent 更稳定、更少返工。 机器可读数据见 [`content/data/tools/coding-agent-upgrades.json`](../../../data/tools/coding-agent-upgrades.json)，网页入口见 [Coding Agent Upgrades](https://123abc-123.github.io/useful-agent-skills/tools/coding-agent-upgrades/)。

> 最近核验：2026-09-19。`passed` 才表示有实机证据；当前运行状态请查看 JSON 或网页卡片。

## 精选条目

| Skill | 作用 | 兼容性 | 建议 | 评分 | 风险 | 来源 |
|---|---|---|---|---:|---|---|
| `acquire-codebase-knowledge` | 扫描陌生代码库并生成结构、入口、依赖和架构地图，减少 Agent 在修改前的错误假设。 | 需要 Python 3.8+、Git 和仓库内扫描脚本；先审查脚本，再在目标仓库根目录运行。 | recommended | 90 | medium | [固定源码](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/acquire-codebase-knowledge/SKILL.md) |
| `context-engineering` | 为 Coding Agent 组织规则、架构、相关文件和验证证据，减少上下文污染与重复探索。 | 标准 Skill；可能建议修改 AGENTS.md、规则文件或上下文文档，写入前应检查范围。 | recommended | 92 | medium | [固定源码](https://github.com/addyosmani/agent-skills/blob/c004a74784a08295d52749b04cda634125b9a581/skills/context-engineering/SKILL.md) |
| `brainstorming` | 在实现功能前澄清目标、约束、设计选项和验收条件，降低做错方向的概率。 | 触发范围较强；可纯文本使用，但可选视觉伴侣会启动本地服务并打开浏览器，Pi/OpenCode 需适配该流程。 | trial | 93 | medium | [固定源码](https://github.com/obra/superpowers/blob/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/brainstorming/SKILL.md) |
| `writing-plans` | 把规格或需求拆成对应具体文件、验证命令和交付检查点的实施计划。 | 纯指令型；会创建计划文档，适合多文件或多阶段任务。 | recommended | 92 | low | [固定源码](https://github.com/obra/superpowers/blob/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/writing-plans/SKILL.md) |
| `create-implementation-plan` | 为功能、重构、依赖升级或基础设施变更生成与仓库证据对应的实现计划。 | 标准 Skill；会写入计划文件，开始实现前仍需人工确认范围和命令。 | recommended | 88 | low | [固定源码](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/create-implementation-plan/SKILL.md) |
| `using-git-worktrees` | 在执行较大改动前建立隔离工作区，减少并行任务和现有工作树互相污染。 | 需要 Git，可能创建目录、分支和 worktree；执行前确认目标路径和当前未提交改动。 | trial | 90 | medium | [固定源码](https://github.com/obra/superpowers/blob/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/using-git-worktrees/SKILL.md) |
| `test-driven-development` | 要求 Agent 先建立失败测试，再按红、绿、重构循环实现功能或修复缺陷。 | 标准 Skill；会修改测试和实现代码并运行项目命令，适合已有测试入口的仓库。 | recommended | 92 | medium | [固定源码](https://github.com/addyosmani/agent-skills/blob/c004a74784a08295d52749b04cda634125b9a581/skills/test-driven-development/SKILL.md) |
| `systematic-debugging` | 要求 Agent 先收集证据、形成假设和最小复现，再修改代码并验证根因。 | 标准 Skill；调查过程中会运行测试和诊断命令，需遵守仓库权限边界。 | recommended | 94 | medium | [固定源码](https://github.com/obra/superpowers/blob/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/systematic-debugging/SKILL.md) |
| `test-gap-audit` | 只读审计缺失、薄弱、过时或范围错误的测试，并按风险给出具体补测建议。 | 默认只读，但会优先运行随 Skill 提供的 Python coverage_map.py；需先审查脚本，也可退回人工审计。 | recommended | 89 | medium | [固定源码](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/test-gap-audit/SKILL.md) |
| `code-review-and-quality` | 从正确性、可读性、架构、安全和性能多个维度审查人类或 Agent 生成的代码。 | 纯指令型；默认适合作为合并前只读审查流程。 | recommended | 91 | low | [固定源码](https://github.com/addyosmani/agent-skills/blob/c004a74784a08295d52749b04cda634125b9a581/skills/code-review-and-quality/SKILL.md) |
| `verification-before-completion` | 阻止 Agent 在没有新鲜命令输出时声称任务已经完成、修复或通过。 | 标准 Skill；会运行与完成声明对应的测试、构建或检查命令。 | recommended | 94 | medium | [固定源码](https://github.com/obra/superpowers/blob/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/verification-before-completion/SKILL.md) |

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
