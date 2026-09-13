# 案例：训练出现 NaN

## 情境

训练在第 800 step 左右首次出现 NaN。最近同时改过混合精度、学习率和数据增强，完整训练成本较高。

## 运行方法

1. 用 [`training-failure-debug`](../prompts/training-failure-debug.prompt.md) 提供症状、命令、日志和最后一次正常运行。
2. 允许 Agent 读取训练配置、日志和相关代码，先定位第一个异常张量或指标。
3. 需要形成仓库标准流程时，使用 [`training-failure-debug` Skill](../skills/training-failure-debug/SKILL.md)。
4. 每次实验只改变一个能区分假设的变量，并使用短数据片段或少量 step。

## 合格产出

- 把事实、假设和待验证项分开；
- 给出按信息增益排序的诊断实验；
- 记录命令、配置差异、随机种子和关键输出；
- 修复后复现原失败条件，并检查训练质量没有被静默牺牲。

如果 Agent 一次性关闭混合精度、降低学习率并移除增强，即使 NaN 消失，也不能证明根因。
