# Agent Skills 分类清单

最近核验：2026-09-18。每一项给出实际用途、来源和 Pi/OpenCode 适配判断。名称为仓库中的 Skill 名或功能组；安装前请以来源仓库当前目录为准。

## 1. 机器学习、数据与科研

| Skill / 项目 | 作用 | 适用场景 | Pi / OpenCode | 成熟度 | 链接 |
|---|---|---|---|---|---|
| `huggingface-datasets` | 创建、读取、处理和发布 Hugging Face Dataset | 数据集构建、清洗、共享 | 标准 | A | [Hugging Face Skills](https://github.com/huggingface/skills) |
| `huggingface-llm-trainer` | 组织大模型训练配置与训练流程 | SFT、微调实验 | 标准 | A | [Hugging Face Skills](https://github.com/huggingface/skills) |
| `trl-training` | 使用 TRL 设计训练与对齐流程 | SFT、偏好优化、RLHF 类任务 | 标准 | A | [Hugging Face Skills](https://github.com/huggingface/skills) |
| `train-sentence-transformers` | 训练与评测文本向量模型 | 检索、聚类、语义匹配 | 标准 | A | [Hugging Face Skills](https://github.com/huggingface/skills) |
| `huggingface-vision-trainer` | 组织视觉模型训练 | 分类、检测和视觉微调 | 标准 | A | [Hugging Face Skills](https://github.com/huggingface/skills) |
| `huggingface-community-evals` | 构建和运行社区评测 | 模型横评、回归评测 | 标准 | A | [Hugging Face Skills](https://github.com/huggingface/skills) |
| `huggingface-local-models` | 管理本地模型使用流程 | 内网、离线推理、原型验证 | 标准 | A | [Hugging Face Skills](https://github.com/huggingface/skills) |
| `huggingface-papers` | 搜索、理解与跟踪论文 | 技术调研、论文分享 | 标准 | A | [Hugging Face Skills](https://github.com/huggingface/skills) |
| `huggingface-spaces` | 创建和维护 Spaces 演示 | 模型 Demo、内部展示 | 标准 | A | [Hugging Face Skills](https://github.com/huggingface/skills) |
| `huggingface-gradio` | 构建 Gradio 应用 | 快速做算法交互界面 | 标准 | A | [Hugging Face Skills](https://github.com/huggingface/skills) |
| `pytorch-lightning` | 规范训练循环、日志和 checkpoint | 可复现训练工程 | 标准 | B | [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) |
| `transformers` | 使用 Transformers 进行训练和推理 | NLP、多模态、LLM 工程 | 标准 | B | [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) |
| `scikit-learn` | 传统机器学习建模与评估 | 表格数据、基线模型 | 标准 | B | [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) |
| `shap` | 解释模型预测与特征贡献 | 可解释性、模型分析 | 标准 | B | [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) |
| `pymc` | 贝叶斯建模和不确定性推断 | 概率模型、A/B 分析 | 标准 | B | [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) |
| `statsmodels` | 统计建模、检验与诊断 | 回归、时间序列、统计报告 | 标准 | B | [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) |
| `torch-geometric` | 图神经网络实验和数据处理 | 图学习、推荐、关系数据 | 标准 | B | [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) |
| `stable-baselines3` | 强化学习训练和评测 | RL 实验与基线 | 标准 | B | [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) |
| `rdkit` | 化学信息学数据与分子处理 | 药物、材料、分子 ML | 标准 | B | [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) |
| `scanpy` | 单细胞数据分析 | 生物信息学 | 标准 | B | [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) |
| `auditing-data-and-ground-truth` | 审计数据来源、标签和真值 | 上线前的数据质量检查 | 标准 | C | [Data Analysis & ML Skills](https://github.com/aiopshwang/data-analysis-ml-agent-skills) |
| `designing-leakage-safe-experiments` | 设计防数据泄漏实验 | 时间切分、用户切分、特征泄漏 | 标准 | C | [Data Analysis & ML Skills](https://github.com/aiopshwang/data-analysis-ml-agent-skills) |
| `validating-models-and-claims` | 验证模型指标与结论是否成立 | 实验复核、评审报告 | 标准 | C | [Data Analysis & ML Skills](https://github.com/aiopshwang/data-analysis-ml-agent-skills) |
| Data Science 生命周期 Skills | 覆盖问题定义、数据质量、复现、评测、隐私和 MLOps | 建立团队算法 SOP | 标准 | C | [Data Science Agent Skills](https://github.com/Emily2040/data-science-agent-skills) |

## 2. 调试、计划与交付

| Skill | 作用 | 适用场景 | Pi / OpenCode | 成熟度 | 链接 |
|---|---|---|---|---|---|
| `systematic-debugging` | 按证据定位根因，避免反复猜修复 | 复杂 Bug、训练异常、线上故障 | 标准 | B | [Superpowers](https://github.com/obra/superpowers) |
| `verification-before-completion` | 完成前运行验证并给出证据 | 防止 Agent 虚报完成 | 标准 | B | [Superpowers](https://github.com/obra/superpowers) |
| `test-driven-development` | 先定义失败测试，再实现功能 | 稳定改动和回归保护 | 标准 | B | [Superpowers](https://github.com/obra/superpowers) |
| `when-stuck` | 卡住时系统切换调查路径 | 减少无效重试 | 标准；旧拆分仓库 | C | [Superpowers Skills](https://github.com/obra/superpowers-skills) |
| `brainstorming` | 在编码前澄清目标和约束 | 新功能、方案探索 | 标准 | B | [Superpowers](https://github.com/obra/superpowers) |
| `writing-plans` | 把目标拆成可执行步骤 | 跨文件、跨模块改造 | 标准 | B | [Superpowers](https://github.com/obra/superpowers) |
| `executing-plans` | 按检查点执行并验证计划 | 长任务、迁移任务 | 标准 | B | [Superpowers](https://github.com/obra/superpowers) |
| `requesting-code-review` | 在合适节点组织代码评审 | PR 前自检、团队评审 | 标准 | B | [Superpowers](https://github.com/obra/superpowers) |
| `receiving-code-review` | 验证并处理评审意见 | 避免盲目接受错误建议 | 标准 | B | [Superpowers](https://github.com/obra/superpowers) |
| `using-git-worktrees` | 用隔离 worktree 并行开发 | 多任务、多 Agent | 标准 | B | [Superpowers](https://github.com/obra/superpowers) |
| `finishing-a-development-branch` | 收尾分支、验证和交付 | PR/合并前 | 标准 | B | [Superpowers](https://github.com/obra/superpowers) |
| `acquire-codebase-knowledge` | 扫描代码库并生成结构化认知 | 接手陌生项目 | 标准 | A | [Awesome Copilot Skills](https://github.com/github/awesome-copilot) |
| `create-technical-spike` | 组织短期技术验证 | 新库选型、性能探索 | 标准 | A | [Awesome Copilot Skills](https://github.com/github/awesome-copilot) |
| `create-implementation-plan` | 生成与仓库对应的实现计划 | 中大型需求 | 标准 | A | [Awesome Copilot Skills](https://github.com/github/awesome-copilot) |
| `create-architectural-decision-record` | 记录架构决策及权衡 | 团队知识沉淀 | 标准 | A | [Awesome Copilot Skills](https://github.com/github/awesome-copilot) |
| `code-review` | 结构化检查 PR 的正确性和风险 | 提交前审查 | 适配 | B | [Sentry Skills](https://github.com/getsentry/skills) |
| `commit` | 组织提交内容和提交信息 | 日常 Git 交付 | 适配 | B | [Sentry Skills](https://github.com/getsentry/skills) |
| `pr-writer` | 根据最终改动撰写 PR | 提高评审效率 | 适配 | B | [Sentry Skills](https://github.com/getsentry/skills) |

## 3. 评测、质量与可观测性

| Skill / 项目 | 作用 | 适用场景 | Pi / OpenCode | 成熟度 | 链接 |
|---|---|---|---|---|---|
| `phoenix-evals` | 构建 LLM、RAG 和 Agent 评测 | 幻觉、相关性、检索质量 | 标准 | A | [Awesome Copilot Skills](https://github.com/github/awesome-copilot) |
| `phoenix-tracing` | 接入 OpenInference tracing | 定位 Agent/RAG 链路问题 | 标准 | A | [Awesome Copilot Skills](https://github.com/github/awesome-copilot) |
| `google-agents-cli-eval` | 构建 Agent 数据集、指标、裁判模型、失败分析与版本对比 | ADK 或其他 Agent 项目的质量闭环 | 标准；依赖 agents-cli | A | [Google Agents CLI](https://github.com/google/agents-cli/blob/main/skills/google-agents-cli-eval/SKILL.md) |
| `google-agents-cli-observability` | 配置 trace、prompt 日志、BigQuery 分析和第三方观测 | Google Cloud/ADK Agent 线上诊断 | 标准；云端功能需审查数据与 IAM | A | [Google Agents CLI](https://github.com/google/agents-cli/blob/main/skills/google-agents-cli-observability/SKILL.md) |
| `agent-evaluation` | 用数据集、scorer、trace 和结果分析评测 Agent | 回归评测、版本对比和失败分析 | 标准；README 明确支持 OpenCode，Pi 待实测 | A | [MLflow Skills](https://github.com/mlflow/skills/blob/main/agent-evaluation/SKILL.md) |
| `instrumenting-with-mlflow-tracing` | 为 Python/TypeScript LLM 应用接入并验证 tracing | 诊断 RAG、Agent 和模型调用链 | 标准；README 明确支持 OpenCode，Pi 待实测 | A | [MLflow Skills](https://github.com/mlflow/skills/blob/main/instrumenting-with-mlflow-tracing/SKILL.md) |
| `pytest-coverage` | 使用 pytest 与 coverage 查缺口 | Python 项目回归测试 | 标准 | A | [Awesome Copilot Skills](https://github.com/github/awesome-copilot) |
| `quality-playbook` | 建立统一质量检查流程 | 团队工程规范 | 标准 | A | [Awesome Copilot Skills](https://github.com/github/awesome-copilot) |
| `sentry-get-started` | 为应用接入 Sentry | 线上错误和性能观测 | 适配；使用生成的客户端插件 | A | [Sentry for AI](https://github.com/getsentry/sentry-for-ai) |
| `sentry-create-alert` | 创建面向实际故障的告警 | 生产监控 | 适配；使用生成的客户端插件 | A | [Sentry for AI](https://github.com/getsentry/sentry-for-ai) |
| Skillet | 从规范构建、校验和评测 Skill | 团队自研 Skill | CLI，可配合 Pi/OpenCode | B | [getsentry/skillet](https://github.com/getsentry/skillet) |

## 4. 安全、供应链与数据库

| Skill | 作用 | 适用场景 | Pi / OpenCode | 成熟度 | 链接 |
|---|---|---|---|---|---|
| `audit-context-building` | 在安全审计前建立代码上下文 | 大型仓库审计 | 适配 | B | [Trail of Bits Skills](https://github.com/trailofbits/skills) |
| `differential-review` | 针对代码差异做安全审查 | PR、版本升级 | 适配 | B | [Trail of Bits Skills](https://github.com/trailofbits/skills) |
| `static-analysis` | 选择和运行静态分析工具 | 漏洞与缺陷扫描 | 适配 | B | [Trail of Bits Skills](https://github.com/trailofbits/skills) |
| `semgrep-rule-creator` | 创建与验证 Semgrep 规则 | 团队自定义安全规则 | 适配 | B | [Trail of Bits Skills](https://github.com/trailofbits/skills) |
| `supply-chain-risk-auditor` | 分析依赖与供应链风险 | 第三方包审查 | 适配 | B | [Trail of Bits Skills](https://github.com/trailofbits/skills) |
| `property-based-testing` | 用性质和生成数据测试程序 | 边界条件复杂的算法 | 适配 | B | [Trail of Bits Skills](https://github.com/trailofbits/skills) |
| `mutation-testing` | 通过代码变异检查测试有效性 | 关键模块测试质量 | 适配 | B | [Trail of Bits Skills](https://github.com/trailofbits/skills) |
| `variant-analysis` | 从一个漏洞寻找同类问题 | 安全修复后的横向排查 | 适配 | B | [Trail of Bits Skills](https://github.com/trailofbits/skills) |
| `insecure-defaults` | 识别危险默认配置 | 服务上线和配置审查 | 适配 | B | [Trail of Bits Skills](https://github.com/trailofbits/skills) |
| `sql-optimization` | 分析 SQL 和查询性能 | 特征计算、数据平台 | 标准 | A | [Awesome Copilot Skills](https://github.com/github/awesome-copilot) |
| `postgresql-code-review` | 检查 PostgreSQL 代码与设计 | 数据库变更评审 | 标准 | A | [Awesome Copilot Skills](https://github.com/github/awesome-copilot) |
| `skill-security` | 静态扫描 Skill 的危险模式 | 安装第三方 Skill 前 | 标准；结果需人工复核 | C | [Superagent Skills](https://github.com/superagent-ai/skills) |
| Agent Skill Scanner | 扫描 Skill 供应链风险 | 批量评估社区 Skill | CLI；结果需人工复核 | C | [agent-skill-scanner](https://github.com/syntax-syndicate/agent-skill-scanner) |

## 5. 浏览器、云与应用工程

| Skill / 项目 | 作用 | 适用场景 | Pi / OpenCode | 成熟度 | 链接 |
|---|---|---|---|---|---|
| Playwright CLI Skills | 让 Agent 用 CLI 做浏览器交互和测试 | E2E、回归、页面取证 | 标准 | A | [Microsoft Playwright CLI](https://github.com/microsoft/playwright-cli) |
| `cloudflare` | Cloudflare 平台综合开发指导 | Workers、部署、平台集成 | 原生支持 Pi/OpenCode | A | [Cloudflare Skills](https://github.com/cloudflare/skills) |
| `agents-sdk` | 使用 Cloudflare Agents SDK | 有状态 Agent、实时应用 | 原生支持 Pi/OpenCode | A | [Cloudflare Skills](https://github.com/cloudflare/skills) |
| `durable-objects` | 使用 Durable Objects 设计有状态服务 | 协作、队列、Agent 状态 | 原生支持 Pi/OpenCode | A | [Cloudflare Skills](https://github.com/cloudflare/skills) |
| `nextjs-on-cloudflare` | 将 Next.js 适配到 Cloudflare | 算法 Demo 与内部平台 | 原生支持 Pi/OpenCode | A | [Cloudflare Skills](https://github.com/cloudflare/skills) |
| `wrangler` | 使用 Wrangler 开发和部署 | Workers 工程 | 原生支持 Pi/OpenCode | A | [Cloudflare Skills](https://github.com/cloudflare/skills) |
| `sandbox-next` / `sandbox-stable` | 使用隔离 Sandbox 运行工作负载 | 代码执行 Agent | 原生支持 Pi/OpenCode | A | [Cloudflare Skills](https://github.com/cloudflare/skills) |
| `mcp-builder` | 设计和实现 MCP 服务 | 把内部工具接给 Agent | 标准 | A | [Microsoft Skills](https://github.com/microsoft/skills) |
| `azure-search-documents-py` | 使用 Azure AI Search Python SDK | 企业检索、RAG | 标准 | A | [Microsoft Skills](https://github.com/microsoft/skills) |
| `python-pypi-package-builder` | 规范构建 Python 包 | 内部算法库发布 | 标准 | A | [Awesome Copilot Skills](https://github.com/github/awesome-copilot) |

## 6. 文档与日常产出

| Skill | 作用 | 适用场景 | Pi / OpenCode | 成熟度 | 链接 |
|---|---|---|---|---|---|
| `docx` | 创建、编辑和检查 Word 文档 | 技术方案、报告 | 标准；检查依赖与许可证 | A | [Anthropic Skills](https://github.com/anthropics/skills) |
| `pdf` | 读取、生成和检查 PDF | 论文、评审材料 | 标准；检查依赖与许可证 | A | [Anthropic Skills](https://github.com/anthropics/skills) |
| `pptx` | 创建和编辑演示文稿 | 技术分享、汇报 | 标准；检查依赖与许可证 | A | [Anthropic Skills](https://github.com/anthropics/skills) |
| `xlsx` | 创建、分析和检查表格 | 实验结果、指标报表 | 标准；检查依赖与许可证 | A | [Anthropic Skills](https://github.com/anthropics/skills) |
| `webapp-testing` | 检查 Web 应用行为 | Demo 和内部工具验收 | 标准；检查依赖与许可证 | A | [Anthropic Skills](https://github.com/anthropics/skills) |
| `skill-creator` | 设计和迭代团队 Skill | 把 SOP 固化成 Skill | 适配 | A | [OpenAI Skills](https://github.com/openai/skills) |

## 7. Harness 与 Skill 元工具

| Skill / 项目 | 作用 | Pi / OpenCode | 成熟度 | 链接 |
|---|---|---|---|---|
| Agents Best Practices | 设计工具、权限、上下文、记忆、编排、评测和观测 | 标准 | B | [agents-best-practices](https://github.com/DenisSergeevitch/agents-best-practices) |
| Agent Harness Skill | 为现有仓库补齐命令、边界、验证和 CI 契约 | 标准 | B | [agent-harness-skill](https://github.com/netresearch/agent-harness-skill) |
| `repo-harness-assessment` | 评估仓库是否适合 Agent 工作 | OpenCode 原生；Pi 可复制 | C | [agent-harness-skills](https://github.com/yfge/agent-harness-skills) |
| `repo-contracts-and-boundaries` | 明确模块边界与可修改范围 | OpenCode 原生；Pi 可复制 | C | [agent-harness-skills](https://github.com/yfge/agent-harness-skills) |
| `validation-harness-design` | 建立可重复的验证入口 | OpenCode 原生；Pi 可复制 | C | [agent-harness-skills](https://github.com/yfge/agent-harness-skills) |
| `runtime-evidence-and-tracing` | 收集运行证据和 tracing | OpenCode 原生；Pi 可复制 | C | [agent-harness-skills](https://github.com/yfge/agent-harness-skills) |
| `work-state-and-delivery` | 管理任务状态和交付证据 | OpenCode 原生；Pi 可复制 | C | [agent-harness-skills](https://github.com/yfge/agent-harness-skills) |
| `agent-skill-stack` | 组织多个 Skill 的协作方式 | 标准 | A | [Awesome Copilot Skills](https://github.com/github/awesome-copilot) |
| Agent Skills Spec | Skill 格式、目录和渐进式加载规范 | Pi/OpenCode 都采用兼容格式 | A | [agentskills.io](https://agentskills.io/) |

## 推荐组合

### 算法实验组合

`huggingface-datasets` + `huggingface-llm-trainer`/`trl-training` + `designing-leakage-safe-experiments` + `phoenix-evals` + `verification-before-completion`

### RAG/Agent 线上组合

`phoenix-tracing` + `phoenix-evals` + Sentry + `systematic-debugging` + `runtime-evidence-and-tracing`

### 接手陌生仓库组合

`acquire-codebase-knowledge` + `repo-harness-assessment` + `create-implementation-plan` + `pytest-coverage` + `requesting-code-review`

### 安全上线组合

`differential-review` + `supply-chain-risk-auditor` + `static-analysis` + `insecure-defaults` + `verification-before-completion`
