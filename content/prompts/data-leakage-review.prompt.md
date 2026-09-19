---
name: data-leakage-review
description: Review an ML dataset and evaluation pipeline for target, temporal, group, duplicate, preprocessing, and test-driven leakage.
category: data
---

# Data Leakage Review

## Variables

- Prediction unit: {{prediction_unit}}
- Prediction time: {{prediction_time}}
- Target: {{target}}
- Available artifacts: {{artifacts}}

## Prompt

Audit the data and evaluation pipeline using the supplied code, queries, schemas, manifests and sample identifiers.

Check:

- whether any feature is created after {{prediction_time}} or derived from {{target}};
- whether users, sessions, devices, documents, groups or near-duplicates cross splits;
- whether preprocessing, vocabulary, imputation, scaling or feature selection is fitted before splitting;
- whether thresholds, prompts, checkpoints or features were chosen using the test set;
- whether joins, caching, sampling or augmentation cross the intended boundary.

Return a table with severity, leakage class, evidence, affected artifact, likely metric effect, remediation and verification method. State the intended split boundary and list checks blocked by missing data.

Do not claim the pipeline is clean when construction code or identifiers are unavailable. Do not modify data or start training.
