# Agent Skills for KGCL

[Agent Skills](https://agentskills.io) that teach AI agents (Claude Code and other
agents that read `SKILL.md` files) to use KGCL. Each skill handles one kind of task:

| Skill | Use it to |
| --- | --- |
| [`kgcl-request-changes`](kgcl-request-changes/SKILL.md) | Turn a requested edit to an ontology or knowledge graph into KGCL commands, including Ontobot issues. Changes that should happen. |
| [`kgcl-describe-changes`](kgcl-describe-changes/SKILL.md) | Describe edits that already happened (between two releases, in a pull request) as KGCL, for release notes or a changelog. Changes that did happen. |
| [`kgcl-validate-convert`](kgcl-validate-convert/SKILL.md) | Check KGCL commands, convert between commands and YAML, JSON or RDF, and apply KGCL with OAK. |

Each skill folder is self-contained, so a skill can be installed on its own. They
share two files, kept identical in every folder:

- `references/kgcl-commands.md`: every command form the parser accepts, with its
  change type and known limits.
- `scripts/check_kgcl.py`: checks commands line by line (needs `pip install kgcl-schema`).

## Installing

For Claude Code, copy the skill folders into `~/.claude/skills/` (all projects) or
`.claude/skills/` in a project:

```bash
cp -r skills/kgcl-* ~/.claude/skills/
```

Other agents that support Agent Skills have their own skills directory; see their
documentation.

## Editing

`tests/test_skills.py` checks that every line in a ```` ```kgcl ```` block parses and
renders back unchanged, that each skill's `name` matches its folder, and that the
shared files are identical. After editing a shared file, copy it to the other skills:

```bash
for d in skills/kgcl-*/; do cp skills/kgcl-request-changes/references/kgcl-commands.md "$d/references/"; done
for d in skills/kgcl-*/; do cp skills/kgcl-validate-convert/scripts/check_kgcl.py "$d/scripts/"; done
```

Write examples that should not parse in a plain code block, not a `kgcl` one.
