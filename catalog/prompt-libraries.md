# 开源 Prompt 库与工程工具

最近核验：2026-09-13。开源 Prompt 项目大致分为四类：可复制模板、提示工程教程、可执行 Pattern、评测与版本管理。收录不代表可以把社区 Prompt 直接放进生产环境。

| 项目 | 类型 | 适合用途 | 许可证 | 链接 |
|---|---|---|---|---|
| DAIR.AI Prompt Engineering Guide | 教程与案例 | 学习提示结构、上下文、RAG、Agent 和常见技术 | MIT | [GitHub](https://github.com/dair-ai/Prompt-Engineering-Guide) |
| Fabric | 可执行 Prompt Patterns | 分析、总结、写作、安全、代码和研究工作流 | MIT | [GitHub](https://github.com/danielmiessler/fabric) |
| OpenAI Cookbook | API 示例与评测方法 | Prompt evaluation flywheel、结构化输出和 Agent 应用 | MIT | [GitHub](https://github.com/openai/openai-cookbook) |
| Anthropic Courses | 交互课程 | 提示结构、示例、工具使用、复杂 Prompt 和评测 | 以仓库许可证为准 | [GitHub](https://github.com/anthropics/courses) |
| prompts.chat | 大型社区模板库 | 发现通用角色和任务模板 | Prompt 数据 CC0，站点源码 MIT | [GitHub](https://github.com/f/prompts.chat) |
| Promptfoo | Prompt/Agent 测试工具 | 测试用例、模型对比、回归检查和 red teaming | MIT | [GitHub](https://github.com/promptfoo/promptfoo) |
| Microsoft Prompt Engine | Prompt 组合代码库 | few-shot、代码生成和多轮 Prompt 组装 | MIT | [GitHub](https://github.com/microsoft/prompt-engine) |
| Anthropic Prompt Tutorial | 交互式练习 | 从基础结构到幻觉控制和复杂行业案例 | 查看仓库当前许可证 | [GitHub](https://github.com/anthropics/prompt-eng-interactive-tutorial) |

## 使用判断

- 教程类项目适合学习方法，不应把示例当成适用于所有模型的固定规则。
- 模板类项目适合发现任务表达方式，使用前应改成自己的输入、证据和输出契约。
- Pattern 类项目可能配套 CLI、脚本和网络调用，运行前按工具软件审查。
- Prompt 进入长期使用前，应至少保存成功案例、失败案例、模型版本和回归结果。
- 不要把密钥、客户数据、未公开代码或隐私信息直接填进第三方在线 Prompt 网站。

## 本仓库 Prompt Library

本仓库提供面向算法工程的原创模板，见 [prompts/README.md](../prompts/README.md)。模板采用 MIT 许可证，使用双花括号变量，并标明输入、输出和边界。
