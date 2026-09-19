# Skill 与 Agent 安全

MCP 配置、密钥、供应链完整性和 Agent 安全基线。 机器可读数据见 [`data/tools/skill-security.json`](../../../data/tools/skill-security.json)，网页入口见 [Skill Security](https://123abc-123.github.io/useful-agent-skills/tools/skill-security/)。

> 最近核验：2026-09-19。`passed` 才表示有实机证据；当前运行状态请查看 JSON 或网页卡片。

## 精选条目

| Skill | 作用 | 兼容性 | 建议 | 评分 | 风险 | 来源 |
|---|---|---|---|---:|---|---|
| `supply-chain-risk-auditor` | 评估依赖维护者、发布流程、版本固定和供应链风险。 | 可能调用生态查询工具；使用前审查依赖与网络行为。 | recommended | 86 | medium | [固定源码](https://github.com/trailofbits/skills/blob/123037ec8aed26f0d86327cc39137ee5043e5deb/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md) |
| `mcp-security-audit` | 检查 MCP 配置中的明文密钥、Shell 注入、未固定版本和未批准服务器。 | 默认以配置审计为主；修复操作应单独授权。 | recommended | 88 | low | [固定源码](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/mcp-security-audit/SKILL.md) |
| `agent-supply-chain` | 为 Agent 插件和工具生成 SHA-256 完整性清单并检测篡改或未跟踪文件。 | 需要读取目标目录并生成清单；签名步骤依赖外部工具。 | trial | 87 | low | [固定源码](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/agent-supply-chain/SKILL.md) |
| `agent-owasp-compliance` | 按照 OWASP Agentic Security Initiative 风险检查 Agent 的权限、信任边界、审计和供应链控制。 | 以审计和报告为主；结论需要结合实际部署环境复核。 | trial | 86 | low | [固定源码](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/agent-owasp-compliance/SKILL.md) |
| `secret-scanning` | 配置 GitHub Secret Scanning、Push Protection、自定义模式和泄露凭据处置流程。 | 部分能力依赖 GitHub Advanced Security 或 GitHub MCP。 | needs-adaptation | 84 | medium | [固定源码](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/secret-scanning/SKILL.md) |

## 安装命令

```bash
# supply-chain-risk-auditor
npx skills add trailofbits/skills --skill supply-chain-risk-auditor -a pi -a opencode --copy

# mcp-security-audit
npx skills add github/awesome-copilot --skill mcp-security-audit -a pi -a opencode --copy

# agent-supply-chain
npx skills add github/awesome-copilot --skill agent-supply-chain -a pi -a opencode --copy

# agent-owasp-compliance
npx skills add github/awesome-copilot --skill agent-owasp-compliance -a pi -a opencode --copy

# secret-scanning
npx skills add github/awesome-copilot --skill secret-scanning -a pi -a opencode --copy

```

## 采用建议

安全 Skill 给出审计证据和整改建议，不等同于安全认证。任何自动修复、签名或密钥处置仍需人工复核。

分数用于比较工作价值、兼容性、维护、来源和风险，不代表安全认证。安装前仍需审查 `SKILL.md`、脚本、依赖、网络行为与固定 commit。
