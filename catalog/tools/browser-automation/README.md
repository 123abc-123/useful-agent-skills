# 浏览器与自动化

真实浏览器检查、UI 调试、页面探索和 Playwright 测试生成。 机器可读数据见 [`data/tools/browser-automation.json`](../../../data/tools/browser-automation.json)，网页入口见 [Browser & Automation](https://123abc-123.github.io/useful-agent-skills/tools/browser-automation/)。

> 最近核验：2026-09-19。`passed` 才表示有实机证据；当前运行状态请查看 JSON 或网页卡片。

## 精选条目

| Skill | 作用 | 兼容性 | 建议 | 评分 | 风险 | 来源 |
|---|---|---|---|---:|---|---|
| `playwright-cli` | 让 Agent 通过命令行操作真实浏览器、保存页面状态并执行可复现的 UI 检查。 | 独立 CLI；Pi/OpenCode 可通过 Shell 调用，首次使用需要安装浏览器运行时。 | recommended | 91 | medium | [固定源码](https://github.com/microsoft/playwright-cli/blob/12228454ed024c9ac89abd59df3b706ed9135fd9/skills/playwright-cli/SKILL.md) |
| `browser-testing-with-devtools` | 通过 Chrome DevTools MCP 检查 DOM、控制台、网络请求、性能和真实视觉输出。 | 需要配置 Chrome DevTools MCP；通用工作流可移植。 | trial | 88 | medium | [固定源码](https://github.com/addyosmani/agent-skills/blob/c004a74784a08295d52749b04cda634125b9a581/skills/browser-testing-with-devtools/SKILL.md) |
| `playwright-explore-website` | 探索网站的核心用户流程、记录定位器与预期结果，并据此提出测试用例。 | 需要 Playwright MCP；指令较短，适合按团队规则扩展。 | trial | 84 | medium | [固定源码](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/playwright-explore-website/SKILL.md) |
| `playwright-generate-test` | 先在真实浏览器中完成场景，再生成并迭代执行 Playwright TypeScript 测试。 | 需要 Playwright MCP、Node 和测试项目写权限。 | trial | 87 | medium | [固定源码](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/playwright-generate-test/SKILL.md) |
| `chrome-devtools` | 用 Chrome DevTools MCP 完成页面交互、截图、网络分析和性能剖析。 | 工具名依赖 Chrome DevTools MCP，需要在 Pi/OpenCode 中配置对应 MCP。 | needs-adaptation | 86 | medium | [固定源码](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/chrome-devtools/SKILL.md) |

## 安装命令

```bash
# playwright-cli
npx skills add microsoft/playwright-cli --skill playwright-cli -a pi -a opencode --copy

# browser-testing-with-devtools
npx skills add addyosmani/agent-skills --skill browser-testing-with-devtools -a pi -a opencode --copy

# playwright-explore-website
npx skills add github/awesome-copilot --skill playwright-explore-website -a pi -a opencode --copy

# playwright-generate-test
npx skills add github/awesome-copilot --skill playwright-generate-test -a pi -a opencode --copy

# chrome-devtools
npx skills add github/awesome-copilot --skill chrome-devtools -a pi -a opencode --copy

```

## 采用建议

优先使用 `playwright-cli` 做可复现检查。MCP 型 Skill 只有在 Pi/OpenCode 已配置对应服务器时才会工作。

分数用于比较工作价值、兼容性、维护、来源和风险，不代表安全认证。安装前仍需审查 `SKILL.md`、脚本、依赖、网络行为与固定 commit。
