---
name: paper-to-spike
description: Convert a paper into a time-boxed technical spike that tests the claim relevant to the current system and ends with a go or no-go decision.
category: research
---

# Paper to Technical Spike

## Variables

- Paper or method: {{paper}}
- Current system/problem: {{system}}
- Time and compute budget: {{budget}}
- Decision: {{decision}}

## Prompt

Read the supplied paper, official code and relevant repository context. Identify the exact claim that could change {{decision}} and the assumptions required for it to transfer to {{system}}.

Produce:

- claim and mechanism in plain language;
- required model, data, loss, training and inference components;
- differences between the paper setting and the current system;
- license, dependency, hardware and data constraints;
- the smallest baseline and implementation that tests the key claim;
- success, failure and stopping criteria;
- artifacts and measurements to retain;
- estimated effort and major risks.

End with go, no-go or needs-evidence, and explain which result from the spike would change that decision.

Do not propose reproducing the entire paper when a smaller discriminating experiment is available. Separate paper claims, author evidence and your inference.
