---
name: training-failure-debug
description: Diagnose a training failure by finding the first causal divergence and proposing a minimal reproduction and verification plan.
category: debugging
---

# Training Failure Debug

## Variables

- Symptom: {{symptom}}
- Exact command/config: {{command}}
- Logs and metrics: {{logs}}
- Last known-good run: {{last_good_run}}

## Prompt

Investigate {{symptom}} without changing multiple variables at once.

First capture the code revision, environment, hardware, dependency versions, seed, earliest abnormal step and complete first error. Compare the failing run with {{last_good_run}}.

Choose evidence based on the failure class:

- NaN/Inf: first bad tensor, loss component, dtype, scale, gradient norm and batch;
- OOM: allocated/reserved memory by phase, activation shape, optimizer state and accumulation;
- non-convergence: label/data sanity, overfit-one-batch test, gradient flow and optimization settings;
- hang: rank logs, collectives, workers, I/O wait and last completed barrier;
- throughput regression: timing by phase, utilization, input wait, warm-up, logging and checkpoints.

Return ranked hypotheses, evidence for and against each one, the next minimal test, confirmed root cause when available, minimal fix and full-run verification plan.

Do not start a costly full run before a representative smoke test passes. Preserve the failing configuration.
