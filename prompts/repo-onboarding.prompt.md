---
name: repo-onboarding
description: Build an evidence-linked map of an unfamiliar algorithm or machine-learning repository before proposing changes.
category: codebase
---

# Repository Onboarding

## Variables

- Goal: {{goal}}
- Focus area: {{focus}}
- Constraints: {{constraints}}

## Prompt

Inspect the repository to build the minimum accurate mental model needed for the stated goal.

Trace:

1. entry points and primary commands;
2. configuration loading and overrides;
3. data ingestion, preprocessing and storage;
4. model construction, training, evaluation and inference;
5. artifact, checkpoint and metric locations;
6. tests, smoke checks and CI;
7. external services, credentials and costly operations.

For every material conclusion, cite a file path, symbol, command or configuration key. Distinguish observed facts from inferences. Identify missing or stale documentation.

Return:

- repository map;
- end-to-end execution flow;
- commands relevant to {{goal}};
- safe modification boundaries;
- risks and unanswered questions;
- the next three files to inspect or change.

Do not modify files or run expensive training. If a command may download models, access secrets, write externally or consume paid compute, describe it without running it unless separately authorized.
