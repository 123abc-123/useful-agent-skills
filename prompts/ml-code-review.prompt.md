---
name: ml-code-review
description: Review an algorithm or ML code change for correctness, leakage, reproducibility, evaluation validity, performance, and operational risk.
category: quality
---

# ML Code Review

## Variables

- Change or diff: {{change}}
- Intended behavior: {{goal}}
- Validation evidence: {{evidence}}
- Deployment context: {{context}}

## Prompt

Review {{change}} against {{goal}} using repository context and {{evidence}}.

Prioritize defects that can change data, labels, metrics, model behavior or production reliability:

- train/eval mode and gradient boundaries;
- tensor shape, dtype, device and numerical stability;
- data leakage, split contamination and preprocessing fit;
- seed control, config capture and reproducibility;
- metric implementation, denominator, masking and aggregation;
- checkpoint compatibility and migration;
- distributed behavior, memory, latency and I/O;
- missing tests for realistic failure modes.

For each finding give severity, exact file/line or symbol, failure mechanism, triggering example and a concrete correction. Distinguish blocking findings from optional improvements.

Do not report generic style preferences as defects. If evidence is insufficient, state the command or artifact needed to verify the concern.
