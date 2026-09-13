---
name: training-failure-debug
description: Diagnose machine-learning training failures such as NaN loss, OOM, non-convergence, distributed hangs, data-loader stalls, checkpoint corruption, or throughput regressions using evidence and minimal reproductions.
---

# Training Failure Debug

Find the first causal divergence before changing multiple knobs. Preserve the failing configuration and evidence.

## Triage

1. Classify the symptom: correctness, numerical stability, memory, convergence, data pipeline, distributed coordination, checkpointing, or performance.
2. Capture the exact command/config, code revision, environment, hardware, seed, first error, and the earliest abnormal step.
3. Reproduce with the smallest representative batch, model, worker count, and step count that retains the failure.
4. Compare against the last known-good run and change one hypothesis at a time.

## Evidence by failure class

- **NaN/Inf:** first bad tensor, loss component, dtype, scale, learning rate, batch content, gradient norm.
- **OOM:** allocated/reserved memory by phase, activation shape, optimizer state, accumulation, fragmentation.
- **Non-convergence:** data/label sanity, overfit-one-batch test, optimization settings, gradient flow, initialization.
- **Hang/stall:** rank logs, collective mismatch, worker stack, I/O wait, timeout and last completed barrier.
- **Throughput regression:** step timing by phase, utilization, input wait, compilation/warm-up, logging and checkpoint cost.

## Finish

Provide the confirmed or leading root cause, supporting evidence, rejected hypotheses, minimal fix, smoke-test command, and full-run verification plan.

Do not start a costly full training run before the minimal reproduction passes. Do not mask numerical failures by silently dropping examples or disabling checks.
