# Skill 榜单与发现源

最近核验：2026-09-23。

抖音视频中提到的“本周 Codex Skill 安装榜”确实有对应的数据生态。最主要的原始来源是 `skills.sh`，其他网站通常是在其数据之上增加 Codex 筛选、近 7 天变化、质量评分或其他平台数据。

网页已经新增独立的[必装 Skill 栏目](https://123abc-123.github.io/useful-agent-skills/must-have-skills/)。它把内容平台当作发现信号，把原始仓库和结构化评分作为推荐依据。

## 内容平台榜单

| 来源 | 用途 | 采用边界 | 链接 |
|---|---|---|---|
| 抖音 · 天丁“本周 Codex Skill 安装榜” | 发现中文社区近期关注的 Skill 与榜单话题 | 短视频结论需回到 skills.sh 和原始仓库复核 | [视频](https://v.douyin.com/MqBahOecs54/) |
| 小红书热门“必装 Skill”清单 | 观察高收藏需求、常见疑问与盲装风险 | 当前使用公开二次整理作为入口，不把收藏量写成质量分 | [公开整理](https://post.smzdm.com/p/aomxd849/) |

社交平台链接可能受登录、地区或短链有效期影响。维护时记录可访问的原始链接；取不到原帖结构时必须标成二次来源。

## 推荐跟踪的榜单

| 来源 | 能看到什么 | 数据口径与判断 | 使用方式 | 链接 |
|---|---|---|---|---|
| skills.sh Leaderboard | 热门、趋势和 Skill 详情 | Skills CLI 的匿名安装遥测；属于安装热度，不是效果评分 | 每日发现的首要来源 | [榜单](https://www.skills.sh/) · [排名说明](https://www.skills.sh/docs) |
| Skillselion Codex Skills | Codex 可用 Skill、总安装量、近期增长和分类筛选 | 每日从来源仓库和 skills.sh 刷新；属于二次整理 | 快速筛出 Codex 候选 | [Codex 榜](https://skillselion.com/codex-skills) |
| SkillSignal Rankings | 总榜、近 7 天、增长、近期收录、质量信号和 Codex 筛选 | 将热度、增速、活跃度和元数据质量分开；质量分不是安全认证 | 比较多个维度，避免只看总安装量 | [榜单](https://skill-signal.org/rankings) |
| LinklyAI Best Skills | skills.sh、GitHub 和多个社区的每日聚合榜及开放 CSV | 多平台聚合，适合发现跨平台趋势；需回到原仓库核验 | 用于发现突然增长的候选项 | [GitHub](https://github.com/LinklyAI/best-skills) |
| Skill Leaderboard / Codex | 面向 Codex 的排行和近期变化 | 第三方聚合；指标命名和数据映射需要与原仓库交叉检查 | 只作为补充发现源 | [Codex 榜](https://www.skillleaderboard.com/agent/codex) |
| Skills.sh Ecosystem Dashboard | 安装量 Top 30 和生态统计可视化 | skills.sh 数据的第三方可视化 | 查看整体生态分布 | [Dashboard](https://skills-dashboard.olshansky.info/) |

## 发现目录

| 来源 | 价值 | 注意事项 | 链接 |
|---|---|---|---|
| GitHub Topic 与代码搜索 | 能最早发现刚发布的 `SKILL.md` | 新仓库证据少，先放观察清单 | [GitHub Code Search](https://github.com/search?q=path%3ASKILL.md&type=code) |
| Awesome Copilot Skills | GitHub 维护的大型分类目录 | 部分内容包含 Copilot 专用约定 | [目录](https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md) |
| skills.sh | 同时提供搜索、排行榜和安装入口 | 官方文档明确提示无法保证每个 Skill 的质量或安全 | [网站](https://www.skills.sh/) |
| Awesome Agent Skills | 覆盖大量社区仓库 | 链接被收录不代表通过审计 | [junminhong 索引](https://github.com/junminhong/awesome-agent-skills) |
| Pi Packages | 观察 Pi 原生扩展和包 | Package 不一定是标准 Skill | [Pi Packages](https://pi.dev/packages) |

## 如何正确读榜单

1. **安装量只说明被安装过**：它不说明是否持续使用、是否适合算法工程，也不等于任务成功率。
2. **周增量适合发现新东西**：突然增长可能来自版本发布、社交传播或营销，应检查增长发生的原因。
3. **不同网站不能直接比较数值**：有的网站统计 Skill 安装，有的统计仓库，有的混入 GitHub star 或多平台数据。
4. **榜单可能被刷或重复计数**：检查是否折叠 fork、重复 Skill、重命名仓库和批量安装。
5. **最终回到原仓库**：阅读具体 `SKILL.md`、脚本、依赖、许可证、提交历史和 Issue。

## 每日搜索的使用顺序

```text
skills.sh 趋势/热门
        ↓
Codex 与近 7 天榜单交叉验证
        ↓
打开原始 GitHub 仓库和具体 SKILL.md
        ↓
检查用途、维护、许可证、安全和 Pi/OpenCode 适配
        ↓
成熟项目进入分类清单；证据不足进入观察清单
```

## 推荐关注的指标

| 指标 | 作用 | 不应被解释为 |
|---|---|---|
| 总安装量 | 判断生态采用度 | Skill 质量或安全性 |
| 近 7 天安装增量 | 发现近期热门项目 | 长期稳定性 |
| 周环比增长 | 发现快速上升项目 | 真实生产使用量 |
| 最近提交与 Release | 判断维护活跃度 | 内容一定正确 |
| Issue 与安全报告 | 发现已知问题 | 没有 Issue 就没有风险 |
| Pi/OpenCode 明确支持 | 降低适配成本 | 可以不审查脚本 |
