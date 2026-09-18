# HTML 报告与可视化 Skills

最近核验：2026-09-19。这个栏目收录能生成精美 HTML、技术报告、领导汇报、交互式可视化和 HTML 幻灯片的 Skill。机器可读数据见 [`data/html-report-skills.json`](../data/html-report-skills.json)，网页入口见 [HTML Reports & Visuals](../docs/html-reports.html)。

## 优先选择

| 需求 | 首选 | 原因 |
|---|---|---|
| 技术调研、评估、决策和项目状态报告 | `create-report` | 强调证据、结论、风险、行动项、打印与浏览器 QA |
| 中文领导汇报、架构和路线图展示 | `onepage` | 单文件、中文字体、打印友好，视觉上接近网页版本的 PPT |
| 多来源技术深挖、周报和事故复盘 | `html-research-reports` | 报告类型完整，含引用、敏感信息清理和长文导航 |
| 页面视觉优化 | `frontend-design` | 专注字体、色彩、布局、响应式和避免模板化视觉 |
| 复杂可操作 Dashboard | `web-artifacts-builder` | React、Tailwind、shadcn/ui，能打包为单文件 |
| 技术分享和培训 | `html-slides` | 零构建、键盘导航、动画和多种技术演示组件 |
| 架构图和流程图 | `beautiful-mermaid` | 将 Mermaid 输出为更适合报告的 SVG/PNG |

## 精选清单

| Skill | 作用 | Pi / OpenCode | 状态 | 分数 | 风险 | 固定源码 |
|---|---|---|---|---:|---|---|
| `create-report` | 证据驱动的技术、决策和状态 HTML 报告 | 标准 Skill；需要文件写入和浏览器 QA | 推荐试用 | 90 | 中 | [固定 commit](https://github.com/maxedapps/agent-skills/blob/1e68803563573e5d195a1c54981a39a99c92779f/skills/create-report/SKILL.md) |
| `html-research-reports` | 调研、周报、事故复盘、技术深挖和决策备忘录 | 静态规则可移植；Claude 监听器需移除 | 需要适配 | 86 | 中 | [固定 commit](https://github.com/f-labs-io/agent-html-skills/blob/d4f259ea4959aecd1240a10c60a950dfb6d1a3f5/plugins/html-skills/skills/html-research-reports/SKILL.md) |
| `onepage` | 中文友好的展示型领导汇报 | 标准 Skill；Pi/OpenCode 待实测 | 小范围试用 | 82 | 低 | [固定 commit](https://github.com/wjhuang88/onepage-skill/blob/71d5e2af03719bedb285c37143434a53ee604488/skills/onepage/SKILL.md) |
| `frontend-design` | 给网页或报告增加明确视觉方向 | 指令型 Skill，通常可移植；审查上游许可证 | 小范围试用 | 88 | 低 | [固定 commit](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/frontend-design/SKILL.md) |
| `web-artifacts-builder` | 构建复杂交互式单文件 HTML | Bash、Node 和构建链需要适配 | 需要适配 | 84 | 高 | [固定 commit](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/web-artifacts-builder/SKILL.md) |
| `html-slides` | 技术汇报、培训和路演的 HTML 幻灯片 | 有非 Claude Agent 降级方式；待实测 | 小范围试用 | 83 | 低 | [固定 commit](https://github.com/bluedusk/html-slides/blob/d8289f4c317905cc5d0ca265d32b791e6cb387b7/SKILL.md) |
| `beautiful-mermaid` | 为报告生成美化后的流程图和架构图 | Node CLI 辅助 Skill；待实测 | 小范围试用 | 81 | 中 | [固定 commit](https://github.com/okooo5km/beautiful-mermaid-cli/blob/5d4411697796aa2dcceffec5901c65e76fee7357/skills/beautiful-mermaid/SKILL.md) |

分数表示对“算法工程师使用 Pi/OpenCode 生成可分享 HTML”的综合适合度，不是视觉效果或安全认证。所有运行状态仍为 `not-run`。

## 安装示例

先试通用报告：

```bash
npx skills add maxedapps/agent-skills \
  --skill create-report \
  -a pi -a opencode --copy
```

再按需要增加研究报告和图表：

```bash
npx skills add f-labs-io/agent-html-skills \
  --skill html-research-reports \
  -a pi -a opencode --copy

npx skills add okooo5km/beautiful-mermaid-cli \
  --skill beautiful-mermaid \
  -a pi -a opencode --copy
```

`onepage`、Anthropic 两项和 `html-slides` 的来源路径已经核验，但上述 Pi/OpenCode 安装命令还未实机运行，应先在测试仓库执行。

## 推荐工作流

```text
代码、实验数据、网页资料
          ↓
报告结构：create-report / html-research-reports / onepage
          ↓
视觉方向：frontend-design
          ↓
图表与架构：beautiful-mermaid
          ↓
浏览器检查：桌面、手机、打印、深色模式、无脚本
          ↓
交付：一个可离线打开的 report.html
```

## 采用前检查

- 报告中的数字和结论是否能回到原始证据；
- 是否清理密钥、Cookie、连接串、客户信息和内部 URL；
- 外部字体、CDN、图片和脚本在离线环境是否仍可用；
- HTML 是否正确转义来自日志、网页、Issue 和聊天记录的内容；
- 是否完成手机宽度、打印、深色模式、键盘和内容溢出检查；
- Skill 是否会自动执行 npm 安装、启动监听端口、提交 Git 或推送 GitHub Pages。
