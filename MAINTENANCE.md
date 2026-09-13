# 维护与每日更新规则

## 每日检索范围

每日任务优先搜索以下来源：

- GitHub 新仓库、Release、Topic 和近期活跃项目；
- `skills.sh` 热门榜、趋势榜和 Skill 详情；
- Skillselion Codex 榜、SkillSignal 近 7 天榜、LinklyAI 聚合数据等二次发现源；
- Agent Skills 规范及官方实现；
- Pi、OpenCode、Hugging Face、Microsoft、GitHub、Cloudflare、Trail of Bits、Sentry 等官方或工程团队仓库；
- 榜单与发现目录，但不把安装量、增长率或排名直接当作推荐依据；
- Harness、context engineering、agent evals、observability、skill security 等关键词。

建议组合查询：

```text
site:github.com SKILL.md agent skills created:>YYYY-MM-DD
site:github.com agent harness skill OpenCode
site:github.com agent skill Pi coding agent
site:github.com machine learning agent skills
site:github.com LLM eval tracing skill
site:github.com agent skill security scanner
site:skills.sh agent skill trending
site:github.com agent skills leaderboard weekly installs
```

榜单来源和各自统计口径见 `catalog/discovery-sources.md`。每日任务至少交叉检查一个原始榜单、一个二次趋势来源和候选 Skill 的 GitHub 原仓库。

## 收录流程

1. 找到候选项目后，打开仓库和具体 `SKILL.md`，不依据搜索摘要下结论。
2. 记录候选来自总安装榜、近 7 天榜、增长榜还是 GitHub 搜索，避免混淆指标。
3. 检查维护者、许可证、最近提交、Release、Issue 和实际文件。
4. 检查脚本、依赖、外部下载、网络调用、凭据读取和高权限命令。
5. 判断 Pi/OpenCode 属于原生、标准或需要适配。
6. 写明它解决的具体工作问题，并与现有条目去重。
7. 新且证据不足的项目先放入 `catalog/watchlist.md`。
8. 运行 `python scripts/validate_catalog.py`。
9. 只有发现有意义变化时才提交；纯排名波动不更新。

## 更新准则

有意义变化包括：

- 新增值得试用的 Skill 或高质量学习资源；
- 项目新增 Pi/OpenCode 官方支持；
- 重要 Release 改变安装方式、能力或兼容性；
- 项目停止维护、归档、改名或出现重大安全问题；
- 链接失效或原有描述已经不准确。

每日自动任务应保持安静，未发现有意义变化时不提交、不通知。发现候选但证据不足时，只更新观察清单并注明原因。任何第三方脚本都不能因为自动更新任务而被直接执行。

## 人工复核重点

- Skill 中是否要求忽略上层指令或绕过权限；
- 是否读取 SSH key、云凭据、浏览器 cookie、环境变量或大范围用户目录；
- 是否使用 `curl | sh`、远程脚本、不可固定版本的依赖；
- 是否把内容上传到第三方服务；
- 是否包含删除、发布、部署、合并、付费等高影响动作；
- 是否把特定 Agent 的工具名伪装成通用兼容。
