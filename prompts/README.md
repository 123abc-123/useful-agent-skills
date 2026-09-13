# Algorithm Engineering Prompt Library

这里保存适合 Pi、OpenCode 和通用 LLM 的一次性任务 Prompt。Prompt 需要用户主动复制或引用；Skill 可以由 Agent 根据任务描述自动发现并加载。

## 分类

| Prompt | 用途 | 文件 |
|---|---|---|
| Repository Onboarding | 快速理解陌生算法仓库 | [repo-onboarding](repo-onboarding.prompt.md) |
| Data Leakage Review | 审查数据切分与特征泄漏 | [data-leakage-review](data-leakage-review.prompt.md) |
| Experiment Design | 设计可验证的机器学习实验 | [experiment-design](experiment-design.prompt.md) |
| Training Failure Debug | 定位训练 NaN、OOM 和挂起 | [training-failure-debug](training-failure-debug.prompt.md) |
| Model Comparison | 比较模型版本并给出发布结论 | [model-comparison](model-comparison.prompt.md) |
| RAG Eval Design | 建立检索与生成分层评测 | [rag-eval-design](rag-eval-design.prompt.md) |
| Paper to Spike | 把论文转成最小技术验证 | [paper-to-spike](paper-to-spike.prompt.md) |
| ML Code Review | 审查算法 PR 的数据和实验风险 | [ml-code-review](ml-code-review.prompt.md) |
| Inference Performance | 分析推理延迟、吞吐和显存 | [inference-performance](inference-performance.prompt.md) |
| Weekly AI Tech Share | 生成有证据的内部技术分享 | [weekly-ai-tech-share](weekly-ai-tech-share.prompt.md) |

## 使用方法

1. 打开模板，把双花括号变量替换为当前任务信息。
2. 将仓库、日志、指标或论文作为可访问上下文提供给 Agent。
3. 保留模板要求的证据链接和“不足信息”状态。
4. 对长期使用的 Prompt 建立回归测试；不要仅凭一次好结果修改模板。

机器可读索引位于 [data/prompts.json](../data/prompts.json)。模板均为本仓库原创，不包含第三方 Prompt 文本。
