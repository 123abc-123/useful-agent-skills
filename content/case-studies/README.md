# 可复现实战案例

这些案例展示如何把本仓库的 Prompt 和 Skill 放进算法工程工作流。它们是可复现的演练设计，不是假装已经发生过的生产结果，也不填写未经测量的“节省时间”数字。

| 场景 | 使用内容 | 产出 |
|---|---|---|
| [时间和实体泄漏审计](data-leakage-audit.md) | `data-leakage-review` Prompt + `data-leakage-audit` Skill | 泄漏假设、证据位置、修复与重跑计划 |
| [训练出现 NaN](training-nan-debug.md) | `training-failure-debug` Prompt/Skill | 首个异常点、最小实验、修复证据 |
| [论文转技术验证](paper-to-spike.md) | `paper-to-spike` Prompt + `paper-to-technical-spike` Skill | 有预算和退出条件的验证计划 |

团队运行案例时，可以把最终报告放入自己的内部仓库，并记录 Agent、模型版本、代码 commit、数据版本、耗时和人工修订。涉及内部数据的报告不应提交到本公开仓库。
