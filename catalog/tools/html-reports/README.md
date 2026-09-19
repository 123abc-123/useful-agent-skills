# HTML 报告与可视化

技术报告、领导汇报、交互式 HTML、幻灯片和架构图。 机器可读数据见 [`data/tools/html-reports.json`](../../../data/tools/html-reports.json)，网页入口见 [HTML Reports & Visuals](https://123abc-123.github.io/useful-agent-skills/tools/html-reports/)。

> 最近核验：2026-09-19。`passed` 才表示有实机证据；当前运行状态请查看 JSON 或网页卡片。

## 精选条目

| Skill | 作用 | 兼容性 | 建议 | 评分 | 风险 | 来源 |
|---|---|---|---|---:|---|---|
| `create-report` | 生成带证据链、结论、风险和行动项的独立 HTML 技术或决策报告。 | 标准 Agent Skill；需要文件写入和浏览器渲染检查。 | recommended | 90 | medium | [固定源码](https://github.com/maxedapps/agent-skills/blob/1e68803563573e5d195a1c54981a39a99c92779f/skills/create-report/SKILL.md) |
| `html-research-reports` | 把代码库、Git 历史、网页和协作资料整理成技术深挖、周报、事故复盘或决策备忘录。 | 静态报告规则可移植；Claude Code 监听器与自动回传需要移除或改为剪贴板。 | needs-adaptation | 86 | medium | [固定源码](https://github.com/f-labs-io/agent-html-skills/blob/d4f259ea4959aecd1240a10c60a950dfb6d1a3f5/plugins/html-skills/skills/html-research-reports/SKILL.md) |
| `onepage` | 把路线图、架构说明、项目状态和研究结论制作成适合领导阅读的展示型 HTML。 | 标准 Skill 目录；有 Windows 安装说明，但 Pi/OpenCode 尚未实测。 | trial | 82 | low | [固定源码](https://github.com/wjhuang88/onepage-skill/blob/71d5e2af03719bedb285c37143434a53ee604488/skills/onepage/SKILL.md) |
| `frontend-design` | 为网页、Dashboard 和报告建立有主题依据的字体、色彩、布局与响应式视觉系统。 | 指令型 Skill，通常可移植；来源以 Claude 为主，许可证需单独审查。 | trial | 88 | low | [固定源码](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/frontend-design/SKILL.md) |
| `web-artifacts-builder` | 用 React、Tailwind 和 shadcn/ui 构建多组件交互页面，并打包成一个 HTML 文件。 | 依赖 Bash、Node、Vite、Parcel 和 npm 安装；Windows 与 Pi/OpenCode 需要适配。 | needs-adaptation | 84 | high | [固定源码](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/web-artifacts-builder/SKILL.md) |
| `html-slides` | 生成适合技术分享、培训和路演的零构建、可交互 HTML 幻灯片。 | 明确提供非 Claude Agent 的问答降级方式；Pi/OpenCode 尚未实测。 | trial | 83 | low | [固定源码](https://github.com/bluedusk/html-slides/blob/d8289f4c317905cc5d0ca265d32b791e6cb387b7/SKILL.md) |
| `beautiful-mermaid` | 为报告生成主题一致的流程图、时序图、架构图和 ER 图，并导出 SVG 或 PNG。 | 标准 Skill 配合 Node CLI；适合作为报告 Skill 的辅助组件。 | trial | 81 | medium | [固定源码](https://github.com/okooo5km/beautiful-mermaid-cli/blob/5d4411697796aa2dcceffec5901c65e76fee7357/skills/beautiful-mermaid/SKILL.md) |

## 安装命令

```bash
# create-report
npx skills add maxedapps/agent-skills --skill create-report -a pi -a opencode --copy

# html-research-reports
npx skills add f-labs-io/agent-html-skills --skill html-research-reports -a pi -a opencode --copy

# onepage
npx skills add wjhuang88/onepage-skill --skill onepage -a pi -a opencode --copy

# frontend-design
npx skills add anthropics/skills --skill frontend-design -a pi -a opencode --copy

# web-artifacts-builder
npx skills add anthropics/skills --skill web-artifacts-builder -a pi -a opencode --copy

# html-slides
npx skills add bluedusk/html-slides -a pi -a opencode --copy

# beautiful-mermaid
npx skills add okooo5km/beautiful-mermaid-cli --skill beautiful-mermaid -a pi -a opencode --copy

```

## 采用建议

先从 `create-report` 开始；需要领导汇报时再试 `onepage`。复杂前端构建类 Skill 应先检查 Node 依赖和网络下载。

分数用于比较工作价值、兼容性、维护、来源和风险，不代表安全认证。安装前仍需审查 `SKILL.md`、脚本、依赖、网络行为与固定 commit。
