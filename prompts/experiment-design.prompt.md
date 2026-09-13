---
name: experiment-design
description: Turn a machine-learning idea into a bounded experiment with a falsifiable hypothesis, baseline, metrics, controls, budget, and decision rule.
category: evaluation
---

# Experiment Design

## Variables

- Hypothesis: {{hypothesis}}
- Decision supported by the experiment: {{decision}}
- Compute/time budget: {{budget}}
- Constraints: {{constraints}}

## Prompt

Design the smallest experiment that can support or reject the hypothesis.

Specify:

1. a falsifiable hypothesis and expected mechanism;
2. a competitive baseline and the single intended difference;
3. dataset version, split unit, time boundary and leakage controls;
4. primary metric, diagnostic metrics and release threshold;
5. minimum ablation or control needed for attribution;
6. seeds, uncertainty estimate and important slices;
7. latency, memory, cost and other operational trade-offs;
8. smoke test, full run budget and stopping conditions.

Return an experiment card, execution matrix, result table template and decision rule. Highlight assumptions that still need evidence.

Keep the design within {{budget}}. Do not expand to a large benchmark suite unless the stated decision requires it.
