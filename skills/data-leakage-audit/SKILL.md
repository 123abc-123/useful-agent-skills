---
name: data-leakage-audit
description: Audit machine-learning datasets, splits, features, preprocessing, and evaluation for target, temporal, group, duplicate, or pipeline leakage before trusting model metrics.
---

# Data Leakage Audit

Establish how each example, label, feature, and fitted transform reaches training and evaluation. Base conclusions on code, schemas, queries, manifests, timestamps, and sample identifiers rather than naming patterns alone.

## Workflow

1. Identify the prediction unit, target, prediction time, evaluation population, and deployment decision.
2. Trace dataset construction from raw sources through joins, filters, labeling, splitting, preprocessing, feature generation, sampling, and caching.
3. Check each leakage class:
   - target-derived features or post-outcome information;
   - future information crossing the prediction timestamp;
   - the same user, group, document, session, device, or near-duplicate across splits;
   - transforms, vocabularies, imputers, scalers, feature selection, or augmentation fitted before splitting;
   - test-driven threshold, prompt, hyperparameter, checkpoint, or feature decisions;
   - labels or metadata indirectly encoding split membership.
4. Measure overlap when identifiers or hashes are available. For approximate duplicates, state the similarity method and threshold.
5. Separate confirmed leakage, credible risks, and checks blocked by missing evidence.
6. Propose the smallest correction and the metric that must be rerun.

## Output

Report a table with severity, leakage class, evidence, affected code/data, expected metric direction, remediation, and verification command. State the intended split boundary explicitly.

Do not mutate datasets, rerun expensive training, or discard results unless the user has requested those actions. Do not claim a dataset is leakage-free when relevant construction code or identifiers are unavailable.
