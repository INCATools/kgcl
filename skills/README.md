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
- `scripts/check_kgcl.py`: checks commands line by line, and with `--yaml PATH` writes
  them as KGCL YAML (needs `pip install kgcl-schema`).

`with xrefs` and RDF output need a kgcl-schema newer than 0.8.0, the latest PyPI release
when these skills were written; until the next release, install from GitHub with
`pip install git+https://github.com/INCATools/kgcl.git`.

## Installing

For Claude Code, copy the skill folders into `~/.claude/skills/` (all projects) or
`.claude/skills/` in a project:

```bash
cp -r skills/kgcl-* ~/.claude/skills/
```

Other agents that support Agent Skills have their own skills directory; see their
documentation.

## Test cases

Each skill has a test case in `evals/<case>/`, in the layout the
[skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) skill and `claude plugin eval` read:

- `prompt.md`: the task, as a user would type it, with run settings on top
- `files/`: the input files, copied into the run's folder by `place-files.sh`
- `case.yaml`: what a good result looks like
- `graders/`: one checkable statement per file
- `grade.py`: checks the same statements against a run's output files directly
  (`python grade.py <output folder> [grading.json]`, needs `kgcl-schema`)

To run a case with and without its skill using Claude Code, from the skill's folder:
`claude plugin eval . --allow-tools Write,Edit,Bash --scaffold`. These are real model
runs and are billed. When the skills were written, all three cases passed with the
skills; without them, the Ontobot case failed the check that every bullet is a valid
command.

## Editing

`tests/test_skills.py` checks that every line in a ```` ```kgcl ```` block parses and
renders back unchanged, that each skill's `name` matches its folder, and that the
shared files are identical. After editing a shared file, copy it to the other skills:

```bash
for d in skills/kgcl-*/; do cp skills/kgcl-request-changes/references/kgcl-commands.md "$d/references/"; done
for d in skills/kgcl-*/; do cp skills/kgcl-validate-convert/scripts/check_kgcl.py "$d/scripts/"; done
```

Write examples that should not parse in a plain code block, not a `kgcl` one.
