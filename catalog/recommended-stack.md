# 算法工程师精选 Skill 组合

最近核验：2026-09-13。机器可读数据见 [`data/recommended-skills.json`](../data/recommended-skills.json)，评分规则见 [`SCORING.md`](../SCORING.md)。本次 GitHub 分支接口返回的 commit 无法通过 commit API 和网页同时解析，因此 commit 暂时仅保留为观察元数据；点击链接使用 `main` 的精确路径，自动任务会在两种入口都通过后再标记固定版本。

## 先安装本仓库的五个工作流

```bash
npx skills add 123abc-123/useful-agent-skills \
  --skill data-leakage-audit \
  --skill experiment-review \
  --skill model-eval-report \
  --skill training-failure-debug \
  --skill paper-to-technical-spike \
  -a pi -a opencode --copy
```

这些 Skill 不带可执行脚本，不会自行启动训练或修改数据：

| Skill | 适合什么时候用 | 源码 |
|---|---|---|
| `data-leakage-audit` | 指标异常好、重新切分后下降、上线效果差，或实验进入评审前 | [SKILL.md](../skills/data-leakage-audit/SKILL.md) |
| `experiment-review` | 实验开跑前检查设计，或跑完后判断结论是否成立 | [SKILL.md](../skills/experiment-review/SKILL.md) |
| `model-eval-report` | 将多个 run、slice、延迟和失败案例整理成评审报告 | [SKILL.md](../skills/model-eval-report/SKILL.md) |
| `training-failure-debug` | NaN、OOM、不收敛、分布式挂起或吞吐下降 | [SKILL.md](../skills/training-failure-debug/SKILL.md) |
| `paper-to-technical-spike` | 判断一篇论文是否值得在当前业务或研究环境落地 | [SKILL.md](../skills/paper-to-technical-spike/SKILL.md) |

## 外部精选组合

下面的命令语法已按照当前 [Skills CLI](https://github.com/vercel-labs/skills) 官方文档核验。具体源码路径也已通过 GitHub 文件树核对。Pi/OpenCode 实机状态仍为 `not-run`，因此安装后应先在测试项目验证。

### 1. 数据、训练与检索

```bash
npx skills add huggingface/skills \
  --skill huggingface-datasets \
  --skill huggingface-community-evals \
  --skill trl-training \
  --skill train-sentence-transformers \
  -a pi -a opencode --copy
```

| Skill | 精确源码 | 分数 | 风险 |
|---|---|---:|---|
| `huggingface-datasets` | [精确路径](https://github.com/huggingface/skills/blob/main/skills/huggingface-datasets/SKILL.md) | 92 | 中：网络与数据下载 |
| `huggingface-community-evals` | [精确路径](https://github.com/huggingface/skills/blob/main/skills/huggingface-community-evals/SKILL.md) | 90 | 中：模型执行和依赖 |
| `trl-training` | [精确路径](https://github.com/huggingface/skills/blob/main/skills/trl-training/SKILL.md) | 91 | 中：训练与云资源 |
| `train-sentence-transformers` | [精确路径](https://github.com/huggingface/skills/blob/main/skills/train-sentence-transformers/SKILL.md) | 93 | 中：训练与模型上传 |

补充候选：[`pytorch-lightning`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/pytorch-lightning/SKILL.md) 和 [`scikit-learn`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scikit-learn/SKILL.md)。

```bash
npx skills add K-Dense-AI/scientific-agent-skills \
  --skill pytorch-lightning --skill scikit-learn \
  -a pi -a opencode --copy
```

### 2. 调试、代码理解和交付

```bash
npx skills add obra/superpowers \
  --skill systematic-debugging \
  --skill verification-before-completion \
  -a pi -a opencode --copy

npx skills add github/awesome-copilot \
  --skill acquire-codebase-knowledge \
  --skill create-implementation-plan \
  -a pi -a opencode --copy
```

| Skill | 精确源码 | 分数 | 风险 |
|---|---|---:|---|
| `systematic-debugging` | [精确路径](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md) | 94 | 低 |
| `verification-before-completion` | [精确路径](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md) | 94 | 低 |
| `acquire-codebase-knowledge` | [精确路径](https://github.com/github/awesome-copilot/blob/main/skills/acquire-codebase-knowledge/SKILL.md) | 90 | 低 |
| `create-implementation-plan` | [精确路径](https://github.com/github/awesome-copilot/blob/main/skills/create-implementation-plan/SKILL.md) | 89 | 低 |

### 3. LLM、RAG 和 Agent 评测

```bash
npx skills add github/awesome-copilot \
  --skill phoenix-evals --skill phoenix-tracing \
  -a pi -a opencode --copy
```

| Skill | 精确源码 | 分数 | 风险 |
|---|---|---:|---|
| `phoenix-evals` | [精确路径](https://github.com/github/awesome-copilot/blob/main/skills/phoenix-evals/SKILL.md) | 92 | 中：依赖、模型和服务凭据 |
| `phoenix-tracing` | [精确路径](https://github.com/github/awesome-copilot/blob/main/skills/phoenix-tracing/SKILL.md) | 91 | 中：trace 可能包含业务数据 |

### 4. Harness、浏览器和供应链

```bash
npx skills add netresearch/agent-harness-skill \
  --skill agent-harness -a pi -a opencode --copy

npx skills add microsoft/playwright-cli \
  --skill playwright-cli -a pi -a opencode --copy

npx skills add \
  https://github.com/trailofbits/skills/tree/main/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor \
  -a pi -a opencode --copy
```

| Skill | 精确源码 | 分数 | 风险 |
|---|---|---:|---|
| `agent-harness` | [精确路径](https://github.com/netresearch/agent-harness-skill/blob/main/skills/agent-harness/SKILL.md) | 83 | 低 |
| `playwright-cli` | [精确路径](https://github.com/microsoft/playwright-cli/blob/main/skills/playwright-cli/SKILL.md) | 89 | 中：浏览器可产生外部副作用 |
| `supply-chain-risk-auditor` | [精确路径](https://github.com/trailofbits/skills/blob/main/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md) | 86 | 中：会调用审计工具和网络 |

## 团队试点顺序

1. 第一周只安装 `systematic-debugging`、`verification-before-completion` 和本仓库五个算法 Skill。
2. 用 10 个真实历史任务记录成功率、返工次数、耗时和误触发。
3. 第二周按业务增加 Hugging Face 或 Phoenix 组合。
4. 实机通过后，把 `data/recommended-skills.json` 中对应的 `runtime_pi` 或 `runtime_opencode` 改为 `passed`，并附测试记录。
5. 团队使用时固定到已审查 commit；升级前检查差异。

## 当前验证矩阵

| 检查 | 状态 |
|---|---|
| 第三方 `SKILL.md` 精确路径 | 已核验 |
| Skills CLI 的 Pi/OpenCode 参数与目录 | 已核验 |
| 本仓库五个 Skill 的结构 | 自动校验 |
| Pi 实机加载与行为测试 | 尚未运行 |
| OpenCode 实机加载与行为测试 | 尚未运行 |

实机状态保持诚实比填一个“兼容”标签更重要。测试记录模板见 [`tests/runtime/README.md`](../tests/runtime/README.md)。
