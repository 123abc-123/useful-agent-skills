# Useful Agent Skills for Algorithm Engineers

面向算法工程师的 Agent Skill 与 Agent Harness 实用清单，重点考虑 **Pi Coding Agent** 和 **OpenCode**。这里不按 star 数堆链接，而是按真实工作环节整理：数据、训练、评测、调试、代码审查、安全、自动化、可观测性与 Harness 工程。

> 最近核验：2026-09-13。Skill 本质上是会被 Agent 读取的指令和代码，使用第三方 Skill 前请先审查 `SKILL.md`、脚本、依赖和网络行为。

## 从这里开始

| 目标 | 推荐入口 |
|---|---|
| 直接安装一组经过筛选的 Skill | [算法工程师精选组合](catalog/recommended-stack.md) |
| 找适合算法工程的 Skill | [分类清单](catalog/skills.md) |
| 理解 Harness、搭建团队工作流 | [Harness 专题](catalog/harness.md) |
| 系统学习 Skill、MCP、Agent、评测 | [学习资源](catalog/learning-resources.md) |
| 查看安装榜、趋势榜和发现渠道 | [榜单与发现源](catalog/discovery-sources.md) |
| 关注新项目和低成熟度项目 | [观察清单](catalog/watchlist.md) |
| 了解收录与每日更新规则 | [维护规则](MAINTENANCE.md) |

可搜索的网页目录源码位于 [`docs/index.html`](docs/index.html)，部署成功后由 GitHub Pages 提供。页面直接读取机器可读的 [`data/recommended-skills.json`](data/recommended-skills.json)。

## 最值得先试的 12 组

1. [Hugging Face Skills](https://github.com/huggingface/skills)：数据集、训练、评测、论文、Spaces 与本地模型。
2. [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills)：科研与机器学习工具链覆盖面广。
3. [Superpowers](https://github.com/obra/superpowers)：系统调试、计划、验证、代码评审与 Git worktree。
4. [GitHub Awesome Copilot Skills](https://github.com/github/awesome-copilot)：代码库理解、技术调研、实现计划、Phoenix 评测与 tracing。
5. [Trail of Bits Skills](https://github.com/trailofbits/skills)：静态分析、供应链、模糊测试、属性测试和安全审计。
6. [Playwright CLI](https://github.com/microsoft/playwright-cli)：让 Coding Agent 执行浏览器测试和页面检查。
7. [Cloudflare Skills](https://github.com/cloudflare/skills)：明确支持 Pi 与 OpenCode 的云端部署和 Agent SDK Skill。
8. [Sentry for AI](https://github.com/getsentry/sentry-for-ai)：错误追踪、告警、AI 应用调试。
9. [Agents Best Practices](https://github.com/DenisSergeevitch/agents-best-practices)：完整的 Agent Harness 架构知识。
10. [Agent Harness Skill](https://github.com/netresearch/agent-harness-skill)：给代码仓库补齐可验证的 Agent Harness。
11. [Skillet](https://github.com/getsentry/skillet)：创建、校验和评测自己的 Skill。
12. [Agent Skills 规范](https://agentskills.io/)：理解 `SKILL.md` 的标准结构和可移植性。

## Pi 与 OpenCode 怎么安装

两者都能读取开放格式的 `SKILL.md`。团队仓库优先使用项目级目录，便于版本管理和代码审查：

```text
.agents/skills/<skill-name>/SKILL.md
```

也可使用各自目录：

```text
# Pi
.pi/skills/<skill-name>/SKILL.md
~/.pi/agent/skills/<skill-name>/SKILL.md

# OpenCode
.opencode/skills/<skill-name>/SKILL.md
~/.config/opencode/skills/<skill-name>/SKILL.md
```

使用 Skills CLI 同时安装到 Pi 与 OpenCode：

```bash
npx skills add <owner>/<repo> --skill <skill-name> -a pi -a opencode --copy
```

本仓库已经提供五个无脚本的算法工程 Skill：

```bash
npx skills add 123abc-123/useful-agent-skills \
  --skill data-leakage-audit \
  --skill experiment-review \
  --skill model-eval-report \
  --skill training-failure-debug \
  --skill paper-to-technical-spike \
  -a pi -a opencode --copy
```

安装第三方 Skill 的推荐过程：

1. 只复制当前确实需要的 Skill，不要一次安装整个集合。
2. 阅读 `SKILL.md`，检查它会调用哪些命令、脚本、MCP 服务和网络地址。
3. 检查许可证、最近提交、Issue，以及是否把其他 Agent 的专用工具名写死。
4. 在测试仓库运行，观察实际工具调用，再进入正式项目。
5. 固定到已审查的 commit；更新时重新看 diff。

## 标签说明

| 标签 | 含义 |
|---|---|
| `原生` | 项目文档明确列出 Pi 或 OpenCode |
| `标准` | 使用通用 `SKILL.md`，通常可直接复制，但仍需试运行 |
| `适配` | 含特定 Agent 的命令、Hook、插件结构或工具名，需要改写 |
| `A` | 官方厂商或标准组织维护 |
| `B` | 成熟社区或知名工程团队维护 |
| `C` | 新项目或低采用度项目，只建议评估 |

## 适合内部分享的三个主题

- **从 Prompt 到 Harness**：模型之外，工具、权限、上下文、记忆、评测和可观测性如何决定 Agent 的可靠性。
- **算法实验的 Agent 化**：用 Skill 固化数据审计、防泄漏实验、训练、评测、复现和报告流程。
- **Skill 供应链安全**：Skill 是可执行工作流，安装前如何做来源检查、最小权限、脚本审查和版本固定。

## 说明

本项目是精选目录，不代表对第三方代码的安全背书。链接、兼容性和活跃度会随项目变化；每日任务只提交有明确价值并通过检查的变更。

榜单中的“安装量”“增长量”“GitHub star”和“质量评分”是不同指标。榜单只用于发现候选 Skill，不能替代源码、安全、许可证和实际效果审查。
