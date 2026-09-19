---
name: rag-eval-design
description: Design a layered RAG evaluation that separates retrieval, context construction, generation, citation, and end-to-end task failures.
category: evaluation
---

# RAG Evaluation Design

## Variables

- Product decision: {{decision}}
- Query population: {{query_population}}
- Available traces/data: {{artifacts}}
- Constraints: {{constraints}}

## Prompt

Design an evaluation that can locate where the RAG system fails.

Separate:

1. corpus and indexing coverage;
2. retrieval recall and ranking;
3. filtering, reranking and context construction;
4. answer correctness, faithfulness and completeness;
5. citation validity;
6. latency, cost and failure recovery;
7. end-to-end user task success.

Define the evaluation unit, sampling strategy, labeled dataset fields, deterministic checks, human review rubric and any LLM judge. Require judge calibration against human labels before treating judge scores as release evidence.

Return a dataset schema, metric table, failure taxonomy, minimum sample plan, slice definitions and release gate tied to {{decision}}.

Do not collapse every failure into one answer-quality score. Mark unavailable ground truth explicitly.
