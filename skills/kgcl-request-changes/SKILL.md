---
name: kgcl-request-changes
description: Turn a requested edit to an ontology or knowledge graph into KGCL (Knowledge Graph Change Language) commands, such as "rename GO:0005634 from 'nucleus' to 'cell nucleus'" or "obsolete X with replacement Y". Use this whenever someone wants to propose, request, draft or plan changes to an ontology (GO, Mondo, Uberon, ENVO, CL, or any OBO or OWL ontology) or a knowledge graph — new terms, labels, synonyms, definitions, parent classes, relationships, obsoletions, merges, subsets — including writing an Ontobot ("Hey ontobot!, apply:") GitHub issue or turning a free-text term request into structured changes, even if they never say "KGCL". For describing changes that have already happened, use kgcl-describe-changes instead.
---

# Requesting ontology changes with KGCL

KGCL describes changes to ontologies and knowledge graphs the way curators think about
them — *rename this term*, *add a synonym*, *move this class under a different parent* —
as one-line commands that people can read and machines can parse. A list of KGCL
commands is a precise change request: a reviewer can see exactly what will happen, and
a tool such as Ontobot or OAK can apply it.

This skill covers **prospective** changes: edits that someone wants made. For a record
of edits that were already made (a diff, a release note, a summary of a PR), use the
`kgcl-describe-changes` skill.

Command syntax, with the change type each command produces, is in
[references/kgcl-commands.md](references/kgcl-commands.md). Read it before writing
commands; it is short, and it lists the limits (no apostrophes, types with no command).

## Workflow

1. **Pin down every term by ID.** Commands should refer to terms by CURIE
   (`GO:0005634`), not by label. If the user names terms only by label, look the IDs
   up (in the ontology file, with `runoak -i <ontology> info '<label>'` if OAK is
   available, or by asking). If a term can't be identified, say so instead of guessing
   an ID. A new term needs an ID too: use the one the user or ontology provides, or a
   clearly marked placeholder, and say that it is one.
2. **Pick the most specific change type.** Each request maps to the narrowest command
   that says what is meant:
   - moving a term to a more specific parent is one `deepen`, not a `delete edge` plus a
     `create edge`;
   - replacing a label is `rename`, not `add label`;
   - retiring a term is `obsolete ... with replacement ...` when a replacement exists,
     not `delete`.
   This keeps the request readable and lets the applying tool follow the ontology's own
   conventions (an obsoletion, for example, also handles the label and parents per the
   ontology's policy).
3. **Include the old value when the command allows it.** `rename GO:0005634 from
   'nucleus' to 'cell nucleus'` lets a reviewer and a tool confirm the term is in the
   expected state. The same goes for `deepen`/`shallow` (old parent) and
   `change relationship` (old predicate).
4. **Break compound requests into one command per change.** "Add a new term for X under
   Y with definition Z" is a `create node`, an `add definition`, and a
   `create edge ... rdfs:subClassOf ...`. Order matters: create a term before
   commands that use it.
5. **Record sources.** Definitions and synonyms take cross-references at the end:
   `with xrefs PMID:..., GOC:...`. Use the sources the user gives; don't make up
   citations. If an ontology requires a source and none was given, point that out.
6. **Validate.** Run every command through the parser before presenting it (see below).
   Don't hand over a command that hasn't parsed.
7. **Check that the applying tool can handle each command**, when you know which tool
   will apply the request. Two things go wrong:
   - **The tool's parser is older.** Tools bundle their own copy of `kgcl-schema`, which
     may predate recent syntax. OAK 0.6.23, for example, ships kgcl-schema 0.6.9 and
     rejects the whole patch if any command uses `with xrefs`. A dry run catches this:
     `runoak -i <ontology> apply --dry-run "..."` parses with OAK's own copy.
   - **The tool skips a change type**, with only a warning. OAK's OBO backend skips
     `deepen` and `shallow`. A dry run does not catch this; apply to a copy of the file
     and compare.

   Fall back to plainer commands where needed: a `deepen` becomes
   `delete edge X rdfs:subClassOf OLD` plus `create edge X rdfs:subClassOf NEW`, and
   xrefs the tool can't take have to be added by hand (say so).
8. **Present** the commands in a ```` ```kgcl ```` code block, one per line, with a
   short plain-language note on anything the user should check (placeholder IDs,
   assumptions about scope, changes that couldn't be written as commands).

## Validating

The parser is in the `kgcl-schema` Python package (`pip install kgcl-schema`). Check
all commands at once, one per line, with the bundled script:

```bash
python scripts/check_kgcl.py -f changes.txt
python scripts/check_kgcl.py "create exact synonym 'cell nucleus' for GO:0005634"
```

It prints OK and the change type for each command, or FAIL with the parser's message,
and notes when the parser reads a command differently than written. Confirm that each
change type is the one intended: a `create edge` with `rdfs:subClassOf` should come back
as `PlaceUnder`, for instance.

## When a change can't be written as a command

- **Apostrophes in text** (`Parkinson's disease`): the command language has no way to
  quote them. Write that change in the KGCL data model instead, as YAML or JSON, and
  tell the user why. A rename, for example:

  ```yaml
  change_set:
    - type: NodeRename
      about_node: MONDO:0005180
      old_value: Parkinson disease
      new_value: Parkinson's disease
  ```

  Other change types use the same fields as the YAML that
  `kgcl-parse "<similar command>"` prints. Ontobot and most appliers only take
  commands, so such a change has to be made by hand or with a tool that reads KGCL
  YAML or JSON.
- **Change types with no command** (merges, mappings, metadata assertions, and others
  listed in the reference): don't invent syntax. Either express the change with existing
  commands and say so, or write the YAML form.

## Ontobot issues

Many OBO ontologies (including GO, Mondo, Uberon, ENVO, CL and PATO) run
[Ontobot](https://github.com/INCATools/ontobot-change-agent), a GitHub Action that
applies KGCL commands from an issue and opens a pull request for a curator to review.
The issue body must contain the trigger phrase followed by a bulleted list of commands
(`-` or `*` bullets):

```markdown
Hey ontobot!, apply:

- create exact synonym 'cortical visual impairment' for MONDO:0001385
- create related synonym 'CVI' for MONDO:0001385
```

The `!` is optional. Things to know about how Ontobot reads the body:

- **Every bulleted line in the body is run as a command**, wherever it appears. Write
  any explanation for the curators as plain paragraphs, never as a bulleted list.
- **It deletes `<` and `>` from the body**, so IRIs in angle brackets break. Use CURIEs.
- **It turns `"` into `'`**, so `change annotation` values in double quotes won't
  survive.

The checker script reads an issue body the same way (`check_kgcl.py -f issue.md`), so
stray bullets show up as failures and angle brackets as warnings.

Opening an issue publishes the request and may start an automated pull request, so
write the issue text for the user and confirm with them before filing it anywhere.
Check that the target repository actually uses Ontobot (look for an Ontobot workflow in
`.github/workflows/`) before relying on the trigger phrase.

## Example

Request: "In GO, 'nuclear membrane' should be under 'organelle membrane', not directly
under 'membrane', and could you add 'cell nucleus' as an exact synonym of 'nucleus'?"

```kgcl
deepen GO:0031965 from GO:0016020 to GO:0031090
create exact synonym 'cell nucleus' for GO:0005634
```

Notes for the user: IDs looked up as GO:0031965 (nuclear membrane), GO:0016020
(membrane), GO:0031090 (organelle membrane), GO:0005634 (nucleus). No source was given
for the synonym; add `with xrefs ...` if the ontology requires one.
