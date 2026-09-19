# 评测与可观测性

Agent/LLM 评测、Tracing、训练监控和测试缺口审计。 机器可读数据见 [`data/tools/evals-observability.json`](../../../data/tools/evals-observability.json)，网页入口见 [Evals & Observability](https://123abc-123.github.io/useful-agent-skills/tools/evals-observability/)。

> 最近核验：2026-09-19。`passed` 才表示有实机证据；当前运行状态请查看 JSON 或网页卡片。

## 精选条目

| Skill | 作用 | 兼容性 | 建议 | 评分 | 风险 | 来源 |
|---|---|---|---|---:|---|---|
| `phoenix-evals` | 为 LLM 与 RAG 应用设计 evaluator、数据集和回归评测。 | 标准 Skill；需要 Python 与 Phoenix 依赖。 | recommended | 92 | medium | [固定源码](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/phoenix-evals/SKILL.md) |
| `phoenix-tracing` | 为 LLM、RAG 与 Agent 调用链添加 tracing 并分析延迟、错误和上下文。 | 标准 Skill；需要 Phoenix/OpenTelemetry 相关依赖。 | recommended | 91 | medium | [固定源码](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/phoenix-tracing/SKILL.md) |
| `google-agents-cli-eval` | 使用数据集、scorer 与实验对 Agent 行为做可重复评测和失败分析。 | 依赖 Google Agents CLI；Pi/OpenCode 可调用 CLI，但尚未实测。 | recommended | 90 | medium | [固定源码](https://github.com/google/agents-cli/blob/5597738f14b5d4a490dfdefa282bc229003b7bbe/skills/google-agents-cli-eval/SKILL.md) |
| `agent-evaluation` | 使用 MLflow 数据集、scorer、trace 和结果分析比较 Agent 版本。 | README 明确支持 OpenCode；Pi 需要实测。 | recommended | 89 | medium | [固定源码](https://github.com/mlflow/skills/blob/85ab69be2df4f92db82ddbf4be9ce63ab3722249/agent-evaluation/SKILL.md) |
| `instrumenting-with-mlflow-tracing` | 为 Python 或 TypeScript LLM 应用接入 MLflow tracing 并验证链路。 | README 明确支持 OpenCode；会修改应用埋点代码。 | trial | 88 | high | [固定源码](https://github.com/mlflow/skills/blob/85ab69be2df4f92db82ddbf4be9ce63ab3722249/instrumenting-with-mlflow-tracing/SKILL.md) |
| `huggingface-trackio` | 记录训练指标、配置异常告警并查询实验结果。 | 可同步 Hugging Face Space；远端 Space 默认公开，需要显式检查隐私设置。 | recommended | 89 | medium | [固定源码](https://github.com/huggingface/skills/blob/abc20ae526d8b4c0e4dff89f904adce28a4a0eb6/skills/huggingface-trackio/SKILL.md) |
| `test-gap-audit` | 只读审计缺失、薄弱或过时的测试，并给出按风险排序的测试建议。 | 纯指令型、默认只读，适合 Pi/OpenCode。 | recommended | 89 | low | [固定源码](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/test-gap-audit/SKILL.md) |

## 安装命令

```bash
# phoenix-evals
npx skills add github/awesome-copilot --skill phoenix-evals -a pi -a opencode --copy

# phoenix-tracing
npx skills add github/awesome-copilot --skill phoenix-tracing -a pi -a opencode --copy

# google-agents-cli-eval
npx skills add google/agents-cli --skill google-agents-cli-eval -a pi -a opencode --copy

# agent-evaluation
npx skills add mlflow/skills --skill agent-evaluation -a pi -a opencode --copy

# instrumenting-with-mlflow-tracing
npx skills add mlflow/skills --skill instrumenting-with-mlflow-tracing -a pi -a opencode --copy

# huggingface-trackio
npx skills add huggingface/skills --skill huggingface-trackio -a pi -a opencode --copy

# test-gap-audit
npx skills add github/awesome-copilot --skill test-gap-audit -a pi -a opencode --copy

```

## 采用建议

先确定评测目标和数据集，再选择 Phoenix、MLflow 或 Google Agents CLI。训练指标同步到远端前检查项目是否公开。

分数用于比较工作价值、兼容性、维护、来源和风险，不代表安全认证。安装前仍需审查 `SKILL.md`、脚本、依赖、网络行为与固定 commit。
