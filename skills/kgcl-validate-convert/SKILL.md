---
name: kgcl-validate-convert
description: Check, parse, and convert KGCL (Knowledge Graph Change Language) ontology change descriptions — validate KGCL commands, find out why one fails to parse, convert between the command form and KGCL YAML, JSON or RDF, render YAML/JSON changes back into commands, or apply KGCL to an ontology file with OAK. Use this whenever someone has KGCL commands or a KGCL YAML/JSON file and wants to know if it is valid, what it means, or needs it in another format, or wants to use the kgcl-schema Python package (kgcl-parse, parse_statement, render) in code.
---

# Validating and converting KGCL

KGCL changes exist in two forms that carry the same information:

- **Commands** (the controlled natural language): one line each, for people.
  `rename GO:0005634 from 'nucleus' to 'cell nucleus'`
- **The data model**, serialized as YAML, JSON or RDF: one object per change, with a
  `type` (the change class) and its fields. This form can also hold provenance
  (`creator`, `change_date`, `pull_request`, ...) and change types that have no command.

The `kgcl-schema` Python package (`pip install kgcl-schema`) parses commands into the
data model and renders them back. Command syntax is in
[references/kgcl-commands.md](references/kgcl-commands.md).

`with xrefs` and RDF output (`kgcl-parse -O rdf`, `to_rdf`) are newer than the latest
release on PyPI (0.8.0). Until the next release, install from GitHub to use them:
`pip install git+https://github.com/INCATools/kgcl.git`. The checker script prints the
installed version (a GitHub install reports `0.0.0`).

## Check commands

Use the bundled script; it checks each line separately and reports every failure, not
just the first:

```bash
python scripts/check_kgcl.py -f changes.txt          # one command per line
python scripts/check_kgcl.py "obsolete GO:0005634"   # or as arguments
python scripts/check_kgcl.py -f issue.md             # an Ontobot issue body works as is
```

For each command it prints the change type, or the parser's error. A command can parse
and still be wrong, so check that the reported type is the one intended:

| Symptom | Likely cause |
| --- | --- |
| Error at a letter right after a `'` | An apostrophe inside quoted text. There is no escape; use YAML or JSON for that change. |
| Error at a `"` | Double quotes are only for annotation values in `change annotation`. Use single quotes. |
| Error at the first word | Unknown verb or typo (`obsolete`, not `deprecate`; `create edge`, not `add edge`). |
| `NodeRename` with no term in the YAML | `rename 'a' to 'b'` without `GO:... from`. Add the term. |
| `about_node_representation: label` where a CURIE was meant | The term was written in quotes. Use the bare CURIE or `<full IRI>`. |
| "parser reads it as" with a CURIE in place of an IRI | Harmless: known IRIs are shortened to CURIEs. |

## Convert commands to YAML, JSON or RDF

```bash
kgcl-parse "obsolete GO:0005634" "create exact synonym 'cell nucleus' for GO:0005634"   # YAML
kgcl-parse -O json -o changes.json "obsolete GO:0005634"
kgcl-parse -O rdf "obsolete GO:0005634"                                                 # Turtle
```

`kgcl-parse` takes each argument as one or more commands (one per line) and stops at the
first command that doesn't parse, so check with the script first. The parser gives each
change an ID like `kgcl_change_id_0`; replace these if the IDs need to be stable.

In Python:

```python
from kgcl_schema.grammar.parser import parse, parse_statement
from kgcl_schema.grammar.render_operations import render
from kgcl_schema.datamodel.kgcl import Session
from kgcl_schema.utils import to_yaml, to_json, to_jsonld, to_rdf

change = parse_statement("rename GO:0005634 from 'nucleus' to 'cell nucleus'")
type(change).__name__        # 'NodeRename'
render(change)               # back to the command
session = Session(change_set=parse(multi_line_text))
to_yaml(session)
```

`to_rdf(session, prefix_map={...})` accepts extra prefixes; common OBO and Bioregistry
prefixes are known already. JSON-LD is available from Python (`to_jsonld`), not from
`kgcl-parse`.

## Load YAML or JSON and render commands

A KGCL file is a session with a `change_set` list. Each change needs `type`; other
fields depend on the type (see the YAML that `kgcl-parse` produces for an example of
each, or the [schema reference](https://incatools.github.io/kgcl/)).

```yaml
change_set:
  - type: NodeObsoletionWithDirectReplacement
    about_node: GO:9999999
    has_direct_replacement: GO:0005634
  - type: NewSynonym
    about_node: GO:0005634
    new_value: cell nucleus
    qualifier: exact
```

```python
from kgcl_schema.utils import from_yaml, from_json
from kgcl_schema.grammar.render_operations import render

session = from_yaml("changes.yaml")
for change in session.change_set:
    print(render(change))
```

Loading assigns every change a new `uuid:` ID, replacing any `id` in the file. Change
types with no command (see the reference) load fine, but `render` returns `None` for
them; describe those in words.

## Apply changes to an ontology

KGCL itself doesn't edit files; tools do. With [OAK](https://github.com/INCATools/ontology-access-kit)
(`pip install oaklib`):

```bash
runoak -i simpleobo:edit.obo apply --dry-run "create exact synonym 'cell nucleus' for GO:0005634"
runoak -i simpleobo:edit.obo apply "create exact synonym 'cell nucleus' for GO:0005634" -o edit-new.obo
```

Two things to check:

- **The tool's parser may be older** than the `kgcl-schema` you validated with, since a
  tool uses whatever version is installed alongside it. An OAK 0.6.23 install with
  kgcl-schema 0.6.9 rejects `with xrefs` and fails the whole patch. `--dry-run` parses
  with the tool's copy, so it catches this.
- **Unsupported change types may be skipped** with only a warning (OAK's OBO backend
  skips `deepen` and `shallow`). A dry run won't show this. Read the tool's output, and
  diff the result against the input to confirm each change was made.
Writing a file in place overwrites it, so write to a new file, or confirm with the user
first. Other appliers: [KGCL-Java](https://github.com/gouttegd/kgcl-java) and its ROBOT
plugin, and [Ontobot](https://github.com/INCATools/ontobot-change-agent) for GitHub
issues.
