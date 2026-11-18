---
tags: [skill-creator]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

A curator sent me changes-from-curator.txt with ontology edits for GO they want made. Check which lines are valid KGCL, fix what you can, and give me the fixed set as KGCL JSON in changes.json. Write a line-by-line report in report.md saying what was wrong with each line and what you did.

Input files: changes-from-curator.txt
