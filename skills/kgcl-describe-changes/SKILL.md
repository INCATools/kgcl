---
name: kgcl-describe-changes
description: Describe changes that have already been made to an ontology or knowledge graph as KGCL (Knowledge Graph Change Language), e.g. for release notes, a changelog, a pull request summary, or a record of curation work. Use this whenever someone asks what changed between two versions or releases of an ontology (GO, Mondo, Uberon, CL, any OBO/OWL file), wants a diff of ontology files explained or summarized, wants to document the edits in a PR or commit, or needs a structured, machine-readable log of past ontology edits — even if they never say "KGCL". For proposing changes that haven't happened yet, use kgcl-request-changes instead.
---

# Describing past ontology changes with KGCL

KGCL can record changes after the fact as well as request them. A retrospective
description answers "what happened between version O1 and O2?" with the most
parsimonious list of changes that turns O1 into O2, in terms a curator recognizes:
"GO:0031965 was moved under GO:0031090", not "one subClassOf axiom was deleted and
another added".

This skill covers **retrospective** changes. For edits someone wants made, use the
`kgcl-request-changes` skill. The commands are the same either way; what differs is
where the changes come from and how much provenance they carry.

Command syntax and the change type each command produces are in
[references/kgcl-commands.md](references/kgcl-commands.md). Read it before writing
commands.

## Workflow

1. **Get a raw list of differences.** Pick the best source available:
   - **Two ontology files** (two releases, or a file before and after a PR): use OAK if
     it is installed (`pip install oaklib`). It writes KGCL commands directly:

     ```bash
     runoak -i simpleobo:old.obo diff -X simpleobo:new.obo --output-type kgcl -o diff.kgcl.txt
     ```

     The `simpleobo:` prefix selects OAK's OBO-format reader; for other formats, see
     `runoak diff --help` and the OAK documentation. `--output-type json`
     and `yaml` give the KGCL data model with more detail. `--statistics` gives counts by
     change type, useful for a release summary of a large ontology. OAK compares terms,
     labels, synonyms, definitions, and relationships; it does not compare every OWL
     axiom (ROBOT's `diff` does).
   - **A git diff or PR** of an ontology file: if both versions can be checked out, run
     the OAK diff on them. Otherwise read the textual diff and write the commands
     yourself; in `.obo` files each `[Term]` stanza shows its `name:`, `def:`,
     `synonym:`, `is_a:` and `relationship:` lines directly.
   - **A description of edits** (an editor's notes, a list of tickets): write the
     commands from it, and say which changes you inferred rather than read.
2. **Consolidate to the highest-level change.** Diff tools report atomic changes, and
   the same intent can show up as several lines. Merge them where the ontology state
   supports it:
   - a `delete edge` and a `create edge` with the same subject and predicate are a single
     move: `deepen` if the new parent is a descendant of the old one, `shallow` if it is
     an ancestor, otherwise `move`;
   - when a term was obsoleted, the label change to "obsolete ..." and the removal of its
     parent edges are part of the obsoletion under the usual OBO policy; one
     `obsolete ... with replacement ...` describes all of it;
   - a `change relationship` replaces a `delete edge` plus `create edge` between the same
     two terms with a different predicate.

   Check each merge against the files (for `deepen`, confirm the new parent really is a
   descendant of the old one). If unsure, keep the atomic changes; they are still
   correct.
3. **Check details the diff tool may drop.** For example, OAK writes
   `create synonym '...' for X` without the scope, even when the file says `EXACT`. Add
   the scope and xrefs from the new file when they matter to the reader.
4. **Validate** every command with the bundled script (see below).
5. **Present** the result for its audience:
   - for people (release notes, PR description): group commands by kind (new terms,
     obsoletions, label and synonym changes, hierarchy changes), each group in a
     ```` ```kgcl ```` block with a one-line plain-language summary and counts;
   - for machines (a changelog file, input to another tool): KGCL YAML or JSON with
     provenance (below).

## Validating

```bash
python scripts/check_kgcl.py -f diff.kgcl.txt
python scripts/check_kgcl.py -f changes.kgcl.txt --yaml changes.yaml
python scripts/check_kgcl.py -f release-notes.md     # checks only the ```kgcl blocks
```

The script needs the `kgcl-schema` package (`pip install kgcl-schema`). It prints OK
and the change type for each command, or FAIL with the parser's message. With `--yaml`,
it also writes the changes as KGCL YAML, the starting point for a machine-readable
record: add provenance fields to that file rather than writing the YAML by hand. A diff of
labels containing apostrophes will produce commands that can't parse; those changes
have to be recorded in YAML or JSON (see the `kgcl-validate-convert` skill).

## Provenance

A retrospective record is more useful with who, when and why. The command language has
no place for these, but the KGCL data model does; each change in YAML or JSON can carry:

| Field | Meaning |
| --- | --- |
| `creator` | Who made the change (an ORCID IRI is best) |
| `contributor` | Others who contributed |
| `change_date` | When it was made |
| `change_description` | Free-text reason |
| `term_tracker_issue` | URL of the issue that requested it |
| `pull_request` | URL of the pull request that made it |
| `see_also` | Any other related URL |

```yaml
change_set:
  - type: NodeRename
    about_node: GO:0005634
    old_value: nucleus
    new_value: cell nucleus
    change_date: "2024-01-15"
    term_tracker_issue: https://github.com/example-org/example-ontology/issues/101
    pull_request: https://github.com/example-org/example-ontology/pull/102
```

Fill these only from the record (commit metadata, PR, issue); leave them out rather than
guess. The `kgcl-validate-convert` skill shows how to load and check such a file.

## Example

OAK's diff between two versions of a small GO extract:

```kgcl
rename GO:9999999 from 'cell nucleus' to 'obsolete cell nucleus'
delete edge GO:9999999 rdfs:subClassOf GO:0043231
obsolete GO:9999999 with replacement GO:0005634
delete edge GO:0031965 rdfs:subClassOf GO:0016020
create edge GO:0031965 rdfs:subClassOf GO:0031090
create synonym 'cell nucleus' for GO:0005634
```

After consolidation (GO:0031090 is a subclass of GO:0016020, and the synonym is `EXACT`
in the new file):

```kgcl
obsolete GO:9999999 with replacement GO:0005634
deepen GO:0031965 from GO:0016020 to GO:0031090
create exact synonym 'cell nucleus' for GO:0005634
```

Summary for release notes: one term obsoleted and merged into *nucleus*; *nuclear
membrane* moved under *organelle membrane*; one exact synonym added.
