---
name: model-comparison
description: Compare a candidate model with a baseline using comparable metrics, slices, uncertainty, operational cost, and explicit release criteria.
category: evaluation
---

# Model Comparison

## Variables

- Baseline: {{baseline}}
- Candidate: {{candidate}}
- Release criteria: {{release_criteria}}
- Available artifacts: {{artifacts}}

## Prompt

Determine whether {{candidate}} should replace or complement {{baseline}}.

Verify that the runs use compatible data, preprocessing, prompts, thresholds, code, environment and evaluation protocol. Present absolute metrics and deltas with metric direction. Include uncertainty only when supported by repeated runs or sample-level results.

Analyze:

- primary quality metrics;
- important slices and worst regressions;
- calibration and threshold behavior when relevant;
- latency, throughput, memory, model size and cost;
- representative failure examples;
- missing evidence and confounders.

Map each item in {{release_criteria}} to evidence and return one decision: ship, hold, limited rollout or insufficient evidence. Provide the smallest follow-up tests that could change the decision.

Do not average incompatible datasets or hide regressions behind an aggregate score.
