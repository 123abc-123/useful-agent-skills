# 观察清单

这些项目有价值，但当前较新、采用度较低、兼容性未完全确认，或更像完整框架而非可直接复制的 Skill。建议在沙箱仓库评估，不直接作为团队标准。

| 项目 | 为什么关注 | 当前限制 | 链接 |
|---|---|---|---|
| Agent Harness Skills | OpenCode 原生，按评估、契约、验证、trace、交付拆分得很清楚 | 项目较新，真实案例仍少 | [GitHub](https://github.com/yfge/agent-harness-skills) |
| Better Harness | 自动审计仓库 Harness，社区关注增长较快 | 未明确支持 Pi/OpenCode，需要适配 | [GitHub](https://github.com/QoderAI/better-harness) |
| Data Analysis & ML Agent Skills | 强调证据、防泄漏、结论验证和失败诊断 | 社区采用度低，需要验证内容深度 | [GitHub](https://github.com/aiopshwang/data-analysis-ml-agent-skills) |
| Data Science Agent Skills | 覆盖数据科学生命周期和治理 | 社区项目，需逐项审查 | [GitHub](https://github.com/Emily2040/data-science-agent-skills) |
| Agent Skill Scanner | 尝试自动发现 Skill 中的恶意或危险行为 | 扫描无法替代人工审查 | [GitHub](https://github.com/syntax-syndicate/agent-skill-scanner) |
| Superagent Skills / `skill-security` | 把正则、AST、taint 和 YARA 用到 Skill 审查 | 社区实现，误报漏报需评估 | [GitHub](https://github.com/superagent-ai/skills) |
| khasky/awesome-agent-skills | 含评审、调试、安全和文本处理等便携 Skill | 逐项质量与维护状态不同 | [GitHub](https://github.com/khasky/awesome-agent-skills) |
| junminhong/awesome-agent-skills | 大型链接索引，适合发现新来源 | 收录不等于验证或推荐 | [GitHub](https://github.com/junminhong/awesome-agent-skills) |
| madebywild/agent-harness | 跨客户端同步 Harness 配置的思路 | Pi/OpenCode 支持不明确 | [GitHub](https://github.com/madebywild/agent-harness) |
| SUNRNEHUI/agent-harness | 运行时中立契约值得跟踪 | 新项目，当前适配器有限 | [GitHub](https://github.com/SUNRNEHUI/agent-harness) |
| pi-open-agents | 用同一套定义管理 Pi 主 Agent、子 Agent、模型、权限和 OpenCode 兼容配置 | MIT、新项目约 16 stars；涉及子进程与工具权限，需先做隔离实测 | [GitHub](https://github.com/andrea-tomassi/pi-open-agents) |
| agent-skill-eval | 通过真实 OpenCode、Codex 或 Claude Harness 做启用/禁用 Skill 的基线对比，记录 pass@k、状态差异、token、成本和耗时 | 新项目、采用度低；需要已认证的 Agent CLI 和裁判模型 API，执行时使用跳过权限参数且暂不支持 Pi | [GitHub](https://github.com/tardigrde/agent-skill-eval) |
| agent-skills-creator | 覆盖 Skill 创建、审计、路由评测和结构验证，适合学习完整生命周期 | 依赖 Bash、Ruby 和 Perl；尚无 Pi/OpenCode 实机证据，Windows 可移植性需验证 | [GitHub](https://github.com/mblode/agent-skills/blob/main/skills/agent-skills-creator/SKILL.md) |
| `eval-driven-dev` | 为 Python LLM 应用建立真实模型调用、数据注入和 evaluator 驱动的质量闭环 | 安装脚本会升级自身与依赖并启动后台 Web 服务，自动副作用较大；需在隔离项目审查后试用 | [固定源码](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/eval-driven-dev/SKILL.md) |
| Elastic `observability-llm-obs` | 从 Elastic 中已有的 APM/OTLP 遥测回答 LLM 延迟、错误率、token、成本字段、响应质量和 Agent 调用链问题 | Apache-2.0；需要 Elastic CLI ≥ 0.2 和已采集遥测的 Elasticsearch/Kibana 环境，尚无 Pi/OpenCode 实机证据 | [固定源码](https://github.com/elastic/agent-skills/blob/baa511126ba2dc37b52e273b52734f8e4e0d323c/plugins/observability/skills/llm-obs/SKILL.md) |
| AWS `skill-eval` | 从安全、功能质量、触发精度和成本效率四个维度评测 Agent Skill，适合安装前审计和版本对比 | MIT-0；项目较新、采用度仍低，完整评测需要额外运行环境，尚未验证 Pi/OpenCode | [固定源码](https://github.com/aws-samples/sample-agent-skill-eval/blob/13b2277b300d2beafa09bbbe425ca0cc41f34c8d/SKILL.md) |
| Datadog `agent-observability-trace-rca` | 沿生产 LLM trace 的 span 树从评测失败、运行错误或结构异常定位根因 | MIT；需要 Datadog LLM Observability MCP 或 Pup 后端及凭据，工具绑定较强，需隔离评估 | [固定源码](https://github.com/datadog-labs/agent-skills/blob/7f8b08f4fa57211ac1b2b42d9771c9e0c4d79124/agent-observability/agent-observability-trace-rca/SKILL.md) |
| Vercel `agent-browser` | skills.sh 约 91.4 万次安装、来源仓库约 4.31 万 Star；提供浏览器、Electron、探索测试、HAR 与截图工作流 | Apache-2.0；安装会下载 Chrome，CLI 会启动浏览器守护进程并在运行时提供动态 Skill。当前 `SKILL.md` 含 `hidden: true`，OpenCode 有未关闭的无法发现问题，先留在观察清单 | [Skill 源码](https://github.com/vercel-labs/agent-browser/blob/main/skills/agent-browser/SKILL.md) · [兼容性 Issue](https://github.com/vercel-labs/agent-browser/issues/1337) |

## 晋级条件

观察项目进入主清单前，至少满足：

- 有真实 `SKILL.md` 或明确可运行的 Harness，而非只有链接汇总；
- 许可证清楚，维护者和来源可追溯；
- 最近仍有维护，Issue 中没有未处理的重大安全问题；
- 能说明具体节省哪一步工作，而非只有泛化宣传；
- 在 Pi 或 OpenCode 上能直接运行，或适配成本清楚；
- 对脚本、依赖、网络和敏感信息行为完成审查。
