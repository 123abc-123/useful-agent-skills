---
name: weekly-ai-tech-share
description: Research and rank recent AI techniques, agent tools, skills, and engineering practices for a concise internal technical sharing session.
category: research
---

# Weekly AI Technology Share

## Variables

- Audience: {{audience}}
- Time window: {{time_window}}
- Allowed tools/platforms: {{allowed_tools}}
- Focus: {{focus}}

## Prompt

Research developments from {{time_window}} that are relevant to {{audience}} and compatible with {{allowed_tools}}.

Use primary sources such as official repositories, documentation, releases and papers. For each candidate record:

- what changed and the event date;
- the concrete work problem it solves;
- maturity, license and maintenance signals;
- installation or trial cost;
- permissions, network, data and security implications;
- compatibility evidence;
- a 30-minute proof-of-value exercise.

Rank candidates by expected work value, evidence quality, adoption cost and risk. Installation counts and social attention are discovery signals only.

Return at most five candidates, followed by one recommended 10-minute sharing topic with demo steps, expected result and source links. Exclude items that only rename an existing idea or lack a verifiable source.
