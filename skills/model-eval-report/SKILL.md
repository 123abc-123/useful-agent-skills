---
name: model-eval-report
description: Turn model evaluation artifacts into a concise, evidence-linked comparison report covering baselines, uncertainty, slices, regressions, operational metrics, failure examples, and release recommendations.
---

# Model Evaluation Report

Use existing evaluation outputs as the source of truth. Preserve metric names, units, dataset versions, run identifiers, and links to artifacts.

## Required analysis

1. Identify the evaluated model, baseline, dataset/split, code revision, environment, and evaluation time.
2. Verify metric direction and comparability before calculating deltas.
3. Present primary metrics with absolute values and deltas. Include uncertainty only when the data supports it.
4. Show important slices, worst regressions, latency, throughput, memory, and cost when available.
5. Summarize representative failure examples and group recurring failure modes.
6. Map evidence to the release criterion and state `ship`, `hold`, or `insufficient evidence`.

## Output structure

- Executive decision and scope;
- evaluation configuration;
- baseline comparison;
- slice and regression analysis;
- operational impact;
- failure taxonomy with evidence links;
- limitations and required follow-up.

Mark missing information as missing. Do not infer values from charts without saying they were visually estimated, and do not combine results produced by incompatible evaluation protocols.
