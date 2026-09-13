---
name: experiment-review
description: Review a machine-learning experiment plan or result for hypothesis quality, baselines, split design, metrics, uncertainty, reproducibility, confounders, and whether the stated claim follows from the evidence.
---

# Experiment Review

Review the experiment at the level needed for the decision it is meant to support.

## Before the run

- Restate the hypothesis, expected mechanism, primary metric, acceptance threshold, and decision that follows.
- Check that the baseline is competitive and differs only where the hypothesis requires.
- Inspect split units, time boundaries, leakage risks, sampling, slices, seeds, and compute budget.
- Distinguish primary metrics from diagnostics. Identify trade-offs such as latency, memory, cost, calibration, and fairness.
- Define the minimum ablation or control needed to attribute an effect.

## After the run

- Verify that compared runs use the same data, code, environment, preprocessing, and evaluation protocol.
- Report effect size and uncertainty where repeated runs or sample-level results permit it.
- Examine important slices and failure examples, not only the aggregate metric.
- Check for cherry-picked checkpoints, thresholds, datasets, seeds, or qualitative examples.
- Separate what the evidence establishes from plausible explanations that remain untested.

## Output

Return: decision, strongest evidence, blocking issues, non-blocking improvements, required reruns, and a claim table with `supported`, `partially supported`, or `unsupported` status.

Never invent missing metrics or treat a small metric increase as meaningful without considering variance and operational cost.
