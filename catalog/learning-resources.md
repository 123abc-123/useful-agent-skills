# 学习网站与资料

最近核验：2026-09-15。优先列官方规范、官方文档和高质量工程文章。

## Skill、上下文与工具协议

| 资源 | 适合学什么 | 推荐程度 | 链接 |
|---|---|---|---|
| Agent Skills | `SKILL.md` 标准、目录格式、渐进式加载 | 必读 | [agentskills.io](https://agentskills.io/) |
| Agent Skills 源码与规范 | 跟踪规范变化、示例和实现 | 必读 | [GitHub](https://github.com/agentskills/agentskills) |
| Hugging Face Context Engineering Course | Skills、MCP、插件、子 Agent、Hook 和 Nano Harness；含 OpenCode/Pi 相关内容 | 最适合系统入门 | [课程](https://huggingface.co/learn/context-course/unit0/introduction) |
| Hugging Face Agents Course | Agent 基础、框架、用例和实践 | 入门到进阶 | [课程](https://huggingface.co/learn/agents-course/unit1/introduction) |
| Model Context Protocol | MCP 架构、规范、SDK 和服务端开发 | 做内部工具接入时必读 | [官方文档](https://modelcontextprotocol.io/) |
| Skills.sh | 搜索社区 Skill 和查看使用趋势 | 发现入口；安装前单独审查 | [skills.sh](https://www.skills.sh/) |
| Skill 榜单与发现源 | 对比 skills.sh、Codex 榜、近 7 天趋势和聚合榜的统计口径 | 日常发现新 Skill | [本项目整理](discovery-sources.md) |
| Awesome Copilot Skills Catalog | 按类别查看大量标准 Skill | 选型参考 | [目录](https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md) |

## Harness 与 Agent 工程

| 资源 | 重点 | 链接 |
|---|---|---|
| OpenAI Harness Engineering | 如何通过仓库结构、工具、反馈和约束提升 Coding Agent | [文章](https://openai.com/index/harness-engineering/) |
| Anthropic: Effective harnesses for long-running agents | 长任务的状态保存、阶段交接和验证 | [文章](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) |
| Anthropic: Harness design for long-running apps | 长时间运行 Agent 的 Harness 设计 | [文章](https://www.anthropic.com/engineering/harness-design-long-running-apps) |
| Anthropic: Building effective agents | 从 workflow 到 agent 的基本设计原则 | [文章](https://www.anthropic.com/engineering/building-effective-agents) |
| Martin Fowler: Harness Engineering | 从软件工程视角理解 Harness | [文章](https://martinfowler.com/articles/harness-engineering.html) |
| Agents Best Practices | 可直接交给 Agent 阅读的 Harness 架构指南 | [GitHub](https://github.com/DenisSergeevitch/agents-best-practices) |
| Skill Issue（2026-09-11） | 用真实历史 PR 构造较难任务，比较仓库 Skill 对 Coding Agent 的增益与方差 | [arXiv](https://arxiv.org/abs/2609.12742) |

## Pi 与 OpenCode

| 资源 | 内容 | 链接 |
|---|---|---|
| Pi Skills | Skill 搜索路径、格式和使用方式 | [Pi 文档](https://pi.dev/docs/latest/skills) |
| Pi Extensions | 扩展系统和可编程能力 | [Pi 文档](https://pi.dev/docs/latest/extensions) |
| Pi Packages | 可安装包和生态 | [Pi Packages](https://pi.dev/packages) |
| OpenCode Skills | Skill 格式、发现路径和调用 | [OpenCode 文档](https://opencode.ai/docs/skills) |
| OpenCode Agents | 主 Agent、子 Agent 和配置 | [OpenCode 文档](https://opencode.ai/docs/agents) |
| OpenCode Plugins | 插件机制与扩展方式 | [OpenCode 文档](https://opencode.ai/docs/plugins) |
| OpenCode Tools | 内置工具与权限 | [OpenCode 文档](https://dev.opencode.ai/docs/tools/) |
| pi-open-agents | 在 Pi 中统一主 Agent、子 Agent、模型与权限，并兼容 OpenCode Agent 定义 | [GitHub](https://github.com/andrea-tomassi/pi-open-agents) |

## 评测、可观测性与安全

| 资源 | 适合学什么 | 链接 |
|---|---|---|
| OpenAI Evals | 评测设计、任务集和 MLE-bench 等案例 | [Evals](https://evals.openai.com/) |
| Arize Phoenix | LLM/RAG 评测、OpenInference tracing 和调试 | [文档](https://arize.com/docs/phoenix/) |
| OpenInference | 生成式 AI 应用的可观测性语义与 instrumentation | [GitHub](https://github.com/Arize-ai/openinference) |
| OWASP GenAI Security Project | LLM/Agent 风险、威胁模型和防护资料 | [官网](https://genai.owasp.org/) |
| Trail of Bits Skills | 从成熟安全团队的 Skill 中学习审计流程 | [GitHub](https://github.com/trailofbits/skills) |
| Sentry Skillet | Skill 的规范、校验与 eval cases | [GitHub](https://github.com/getsentry/skillet) |

## 推荐学习路线

1. 先读 Agent Skills 规范和 Pi/OpenCode Skills 文档，自己写一个 30 行以内的团队 Skill。
2. 完成 Hugging Face Context Engineering Course 的 Skills、MCP 和 Harness 单元。
3. 读三篇 Harness 工程文章，把当前仓库的命令、权限和验证入口画出来。
4. 用 Phoenix 或现有日志给一个真实 Agent 任务加 trace 和评测。
5. 用 Skillet 或自建测试集，为常用 Skill 加 5 个成功样例和 3 个失败样例。
6. 最后再研究多 Agent；单 Agent 的工具和验证不稳定时，并行只会放大问题。
