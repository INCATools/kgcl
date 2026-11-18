---
tags: [skill-creator]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

I curate Mondo. Using the attached mondo-extract.obo to look up IDs, draft the body of a GitHub issue for the mondo repo so that ontobot will make these edits: add 'cortical visual impairment' as an exact synonym and 'CVI' as a related synonym of cortical blindness; 'Parkinson disease, juvenile onset' is a duplicate of juvenile Parkinson disease, so retire it; and rename Parkinson disease to Parkinson's disease. Include a quick bulleted rationale too so the reviewers know why. Save the issue body as issue.md. Don't file anything.

Input files: mondo-extract.obo
