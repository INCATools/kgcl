# KGCL command reference

Every command form that the KGCL parser (`kgcl-schema`) accepts, with the change
type it produces. Each command is one line. The grammar is
`src/kgcl_schema/grammar/kgcl.lark` in <https://github.com/INCATools/kgcl>.

This file is shared by the KGCL skills; the copies in each skill are identical.

## Contents

- [Writing values and terms](#writing-values-and-terms)
- [Labels](#labels)
- [Synonyms](#synonyms)
- [Definitions](#definitions)
- [Relationships (edges)](#relationships-edges)
- [Annotations](#annotations)
- [Obsoletion](#obsoletion)
- [Subsets](#subsets)
- [Creating and deleting terms](#creating-and-deleting-terms)
- [Change types with no command](#change-types-with-no-command)
- [Known limitations](#known-limitations)

## Writing values and terms

**Terms** (the things being changed) can be written three ways:

| Form | Example | Use |
| --- | --- | --- |
| CURIE | `GO:0005634` | Preferred. Unambiguous, and every tool handles it. |
| IRI in angle brackets | `<http://purl.obolibrary.org/obo/GO_0005634>` | When the prefix is not a well-known one. The parser contracts IRIs with known prefixes back to CURIEs. |
| Label in single quotes | `'nucleus'` | Last resort. Labels can be ambiguous and tools may not resolve them. |

**Text values** (labels, synonyms, definitions) go in single quotes: `'cell nucleus'`.
Labels and synonyms may carry a language tag: `'noyau'@fr`.

**Annotation values** in `change annotation` use double quotes and may carry a language
tag: `"old"@en`.

**Relationship types** (predicates) are terms too: `rdfs:subClassOf` for is_a,
`BFO:0000050` for part_of.

## Labels

| Command | Change type |
| --- | --- |
| `rename GO:0005634 from 'nucleus' to 'cell nucleus'` | `NodeRename` |
| `add label 'nucleus' to GO:0005634` | `NewLabel` |

- `rename` replaces an existing label; `add label` is for a term that has none.
- Include the term and the old label in a `rename`. `rename 'nucleus' to 'cell nucleus'`
  also parses, but it records no term at all, only the two strings.
- Language tags: `add label 'noyau'@fr to GO:0005634`.

```kgcl
rename UBERON:0002398 from 'manus' to 'hand'
add label 'noyau'@fr to GO:0005634
```

## Synonyms

| Command | Change type |
| --- | --- |
| `create exact synonym 'cell nucleus' for GO:0005634` | `NewSynonym` |
| `remove synonym 'cell nucleus' for GO:0005634` | `RemoveSynonym` |
| `change synonym 'cell nucleus' for GO:0005634 to 'cell nucleus proper'` | `SynonymReplacement` |

- The scope (`exact`, `narrow`, `broad`, `related`) is optional on `create`. Include it
  when known, since otherwise the tool applying the change picks one.
- Sources go at the end of `create ... synonym` as cross-references (stored as
  `oboInOwl:hasDbXref`), separated by commas: `with xrefs PMID:12345, GOC:go_curators`.
- Language tags: `create exact synonym 'noyau'@fr for GO:0005634`.

```kgcl
create exact synonym 'cell nucleus' for GO:0005634
create related synonym 'CVI' for MONDO:0001385
change synonym 'cell nucleus' for GO:0005634 to 'cell nucleus proper'
```

## Definitions

| Command | Change type |
| --- | --- |
| `add definition '...' to GO:0005634` | `NewTextDefinition` |
| `change definition of GO:0005634 to '...'` | `NodeTextDefinitionChange` |
| `change definition of GO:0005634 from '...' to '...'` | `NodeTextDefinitionChange` |
| `remove definition for GO:0005634` | `RemoveTextDefinition` |

- Many ontologies require a definition to cite a source. Add it with
  `with xrefs ...` at the end of `add definition`.
- `change definition` does not take xrefs.

```kgcl
add definition 'A membrane-bounded organelle of eukaryotic cells in which chromosomes are housed and replicated.' to GO:0005634 with xrefs GOC:go_curators, ISBN:0198547684
remove definition for GO:0005634
```

## Relationships (edges)

Edges are written subject, predicate, object: `GO:0005635 BFO:0000050 GO:0005634` reads
"nuclear envelope part_of nucleus".

| Command | Change type |
| --- | --- |
| `create edge GO:0005635 BFO:0000050 GO:0005634` | `EdgeCreation` |
| `create edge GO:0005634 rdfs:subClassOf GO:0043231` | `PlaceUnder` (is_a) |
| `delete edge GO:0005635 BFO:0000050 GO:0005634` | `EdgeDeletion` |
| `delete edge GO:0005634 rdfs:subClassOf GO:0043231` | `RemoveUnder` (is_a) |
| `change relationship between GO:0005635 and GO:0005634 from rdfs:subClassOf to BFO:0000050` | `PredicateChange` |
| `deepen GO:0031965 from GO:0016020 to GO:0031090` | `NodeDeepening` |
| `shallow GO:0031965 from GO:0031090 to GO:0016020` | `NodeShallowing` |
| `move GO:0005634 BFO:0000050 GO:0043231 from GO:0043231 to GO:0005739` | `NodeMove` |

- `deepen` moves a term from a parent to one of that parent's descendants; `shallow`
  is the reverse. Both are is_a moves.
- `move` changes the object of one edge: the edge `GO:0005634 BFO:0000050 GO:0043231`
  becomes `GO:0005634 BFO:0000050 GO:0005739`. Write the old object in both places.

```kgcl
create edge GO:0005635 BFO:0000050 GO:0005634
delete edge GO:0005634 rdfs:subClassOf GO:0043231
deepen GO:0031965 from GO:0016020 to GO:0031090
```

## Annotations

| Command | Change type |
| --- | --- |
| `change annotation of GO:0005634 with rdfs:comment from "old"@en to "new"@en` | `NodeAnnotationChange` |

Values are in double quotes, each with an optional language tag.

## Obsoletion

| Command | Change type |
| --- | --- |
| `obsolete GO:9999999` | `NodeObsoletion` |
| `obsolete GO:9999999 with replacement GO:0005634` | `NodeObsoletionWithDirectReplacement` |
| `unobsolete GO:9999999` | `NodeUnobsoletion` |

Obsoletion marks a term as not to be used without deleting it. Name a replacement when
there is one, so that existing annotations can be updated. Exactly what an obsoletion
does to the file (prefixing the label with "obsolete", removing parent edges, adding
`term replaced by`) is set by the ontology's own policy and the tool applying it, so a
single `obsolete` command stands for all of that.

## Subsets

| Command | Change type |
| --- | --- |
| `add GO:0005634 to subset goslim_generic` | `AddNodeToSubset` |
| `remove GO:0005634 from subset goslim_generic` | `RemoveNodeFromSubset` |

## Creating and deleting terms

| Command | Change type |
| --- | --- |
| `create GO:9999999` | `ClassCreation` |
| `create node GO:9999999 'cell nucleus'` | `NodeCreation` (with a label) |
| `create object property BFO:0000050` | `ObjectPropertyCreation` |
| `delete GO:9999999` | `NodeDeletion` |
| `delete class GO:9999999` | `ClassDeletion` |
| `delete object property BFO:0000050` | `ObjectPropertyDeletion` |

A new term usually needs several commands: create it, label it, define it, and place it.

```kgcl
create node GO:9999999 'cell nucleus'
add definition 'A nucleus of a cell.' to GO:9999999 with xrefs GOC:go_curators
create edge GO:9999999 rdfs:subClassOf GO:0043231
```

Deleting removes a term entirely. Published ontologies almost always obsolete instead,
because other resources may already use the term.

## Change types with no command

The KGCL data model has more change types than the command language can write. These
have no command; write them in the data model, as YAML or JSON (see the
`kgcl-validate-convert` skill). Loading a YAML file has been tried for
`NodeDirectMerge`; the others are untested.

`NodeDirectMerge`, `MultiNodeObsoletion`, `NodeObsoletionWithNoDirectReplacement`,
`NameBecomesSynonym`, `SynonymPredicateChange`, `TextDefinitionReplacement`,
`NewMapping`, `RemoveMapping`, `MappingReplacement`, `MappingPredicateChange`,
`MappingCreation`, `NewMetadataAssertion`, `RemoveMetadataAssertion`,
`MetadataAssertionReplacement`, `MetadataAssertionPredicateChange`,
`NodeAnnotationReplacement`, `NodeSynonymChange`, `NodeMappingChange`,
`NodeMetadataAssertionChange`, `SetLanguageForName`, `EdgeObsoletion`, `EdgeRewiring`,
`EdgeLogicalInterpretationChange`, `LogicalAxiomChange`, `Transaction`.

Do not invent command syntax for these. Either write the YAML form, or express the
change with the commands above (a merge, for example, is often written as an
`obsolete ... with replacement` plus moving any synonyms), and say which you did.

## Known limitations

- **No apostrophes in quoted text.** There is no escape for `'` inside a single-quoted
  value, and double or triple quotes are not accepted there either. A label such as
  `Parkinson's disease` cannot be written as a command. Write that change in YAML or
  JSON, and tell the user why. (Tracked in
  [kgcl#40](https://github.com/INCATools/kgcl/issues/40).) A label change can also be
  written as `change annotation of GO:0031965 with rdfs:label from "old" to "new's"`,
  since annotation values use double quotes, but that records a `NodeAnnotationChange`
  rather than a `NodeRename`, and Ontobot turns `"` into `'`, which breaks it.
- **`change synonym` drops the scope.** `change exact synonym ...` parses, but the scope
  is not recorded. Leave it out. (Tracked in
  [kgcl#117](https://github.com/INCATools/kgcl/issues/117).)
- **Tools support different subsets.** Not every tool that applies KGCL handles every
  command (for example, OAK's OBO backend skips `deepen` and `shallow`). Check the tool's output for
  skipped changes.
- **Tools may bundle an older parser.** `with xrefs` is recent; OAK 0.6.23 (with
  kgcl-schema 0.6.9) rejects it. A dry run with the tool shows whether its parser
  accepts the commands.
