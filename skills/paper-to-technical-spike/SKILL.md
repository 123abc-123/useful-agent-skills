---
name: paper-to-technical-spike
description: Convert a research paper or technical method into a bounded engineering spike with explicit claims, required components, assumptions, minimal implementation, evaluation criteria, cost, and a go/no-go recommendation.
---

# Paper to Technical Spike

Translate the paper's claimed contribution into the smallest experiment that can change an engineering decision.

## Workflow

1. Record the paper version, official links, code repository, license, and the exact claim relevant to the current product or research problem.
2. Separate the contribution from standard components, training scale, proprietary data, hidden preprocessing, and evaluation advantages.
3. Map assumptions to the local setting: task, data, model size, hardware, latency, memory, privacy, and integration constraints.
4. Define a minimal baseline and one focused implementation of the claimed mechanism.
5. Choose an evaluation that can falsify the useful claim. Include quality, compute, latency, memory, and failure cases as needed.
6. Time-box the spike and list stop conditions for missing assets, incompatible licensing, excessive compute, or failure to beat the baseline.

## Deliverable

Produce a short technical spike containing: claim, evidence from the source, local applicability, implementation delta, experiment matrix, acceptance criteria, effort/cost estimate, risks, and `go`, `revise`, or `stop` recommendation.

Distinguish reported paper results from reproduced results. Do not present an unofficial implementation as the authors' code or claim reproducibility before running the defined experiment.
