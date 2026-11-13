# Visual guide to change types

Each section below shows a small piece of an ontology **before** and **after** a
KGCL change, followed by the KGCL command that makes the change. Changed elements are
highlighted. Arrows point from a term to its parent: solid arrows are `is_a`
(`rdfs:subClassOf`) and dashed arrows are other relationships, such as `part_of`
(`BFO:0000050`).

The examples use real terms from the [Gene Ontology](https://geneontology.org) and
[Uberon](https://obophenotype.github.io/uberon/), but the edits are illustrations,
not changes anyone has requested. For the full list of command forms and their YAML
serializations, see [Command examples](examples.md). For every change type in the
model, see the [class hierarchy](class-hierarchy.md) or the
[schema reference](schema-reference.md).

## Labels

### Rename a term: `NodeRename`

Replaces a term's existing label (`rdfs:label`).

```mermaid
flowchart LR
  subgraph before [Before]
    a1["UBERON:0002398<br/>manus"]
  end
  subgraph after [After]
    a2["UBERON:0002398<br/>hand"]:::changed
  end
  before ==> after
  classDef changed fill:#fff3b0,stroke:#b58900,stroke-width:2px
```

```kgcl
rename UBERON:0002398 from 'manus' to 'hand'
```

### Label an unlabeled term: `NewLabel`

Adds a label to a term that has none. Use `rename` when the term already has a label.
A language tag is optional.

```mermaid
flowchart LR
  subgraph before [Before]
    b1["GO:0005634<br/><i>(no label)</i>"]
  end
  subgraph after [After]
    b2["GO:0005634<br/>nucleus"]:::changed
  end
  before ==> after
  classDef changed fill:#fff3b0,stroke:#b58900,stroke-width:2px
```

```kgcl
add label 'nucleus' to GO:0005634
add label 'noyau'@fr to GO:0005634
```

## Synonyms

### Add a synonym: `NewSynonym`

The synonym scope (`exact`, `narrow`, `broad`, or `related`) is optional.

```mermaid
flowchart LR
  subgraph before [Before]
    c1["GO:0005634<br/>nucleus"]
  end
  subgraph after [After]
    c2["GO:0005634<br/>nucleus<br/><b>exact synonym:</b> cell nucleus"]:::changed
  end
  before ==> after
  classDef changed fill:#fff3b0,stroke:#b58900,stroke-width:2px
```

```kgcl
create exact synonym 'cell nucleus' for GO:0005634
```

The related commands:

```kgcl
remove synonym 'cell nucleus' for GO:0005634
change synonym 'cell nucleus' for GO:0005634 to 'cell nucleus proper'
```

## Definitions

### Add a definition: `NewTextDefinition`

```mermaid
flowchart LR
  subgraph before [Before]
    d1["GO:0005634<br/>nucleus<br/><i>(no definition)</i>"]
  end
  subgraph after [After]
    d2["GO:0005634<br/>nucleus<br/><b>definition:</b> A membrane-bounded organelle<br/>of eukaryotic cells in which chromosomes<br/>are housed and replicated."]:::changed
  end
  before ==> after
  classDef changed fill:#fff3b0,stroke:#b58900,stroke-width:2px
```

```kgcl
add definition 'A membrane-bounded organelle of eukaryotic cells in which chromosomes are housed and replicated.' to GO:0005634
```

The related commands:

```kgcl
change definition of GO:0005634 to 'A membrane-bounded organelle that contains the chromosomes.'
remove definition for GO:0005634
```

## Relationships (edges)

### Add a relationship: `EdgeCreation`

```mermaid
flowchart LR
  subgraph before [Before]
    direction BT
    e1["GO:0005635<br/>nuclear envelope"]
    e2["GO:0005634<br/>nucleus"]
  end
  subgraph after [After]
    direction BT
    e3["GO:0005635<br/>nuclear envelope"]
    e4["GO:0005634<br/>nucleus"]
    e3 -. "part_of" .-> e4
  end
  before ==> after
  linkStyle 0 stroke:#b58900,stroke-width:3px
```

```kgcl
create edge GO:0005635 BFO:0000050 GO:0005634
```

When the predicate is `rdfs:subClassOf`, the change is a `PlaceUnder`, a kind of
`EdgeCreation`.

### Remove a relationship: `EdgeDeletion`

```mermaid
flowchart LR
  subgraph before [Before]
    direction BT
    f1["GO:0005635<br/>nuclear envelope"]
    f2["GO:0005739<br/>mitochondrion"]
    f1 -. "part_of" .-> f2
  end
  subgraph after [After]
    direction BT
    f3["GO:0005635<br/>nuclear envelope"]
    f4["GO:0005739<br/>mitochondrion"]
  end
  before ==> after
  linkStyle 0 stroke:#b58900,stroke-width:3px
```

```kgcl
delete edge GO:0005635 BFO:0000050 GO:0005739
```

When the predicate is `rdfs:subClassOf`, the change is a `RemoveUnder`.

### Change a relationship's type: `PredicateChange`

Keeps the two terms connected, but changes how. Here an `is_a` becomes `part_of`.

```mermaid
flowchart LR
  subgraph before [Before]
    direction BT
    g1["GO:0005635<br/>nuclear envelope"]
    g2["GO:0005634<br/>nucleus"]
    g1 -- "is_a" --> g2
  end
  subgraph after [After]
    direction BT
    g3["GO:0005635<br/>nuclear envelope"]
    g4["GO:0005634<br/>nucleus"]
    g3 -. "part_of" .-> g4
  end
  before ==> after
  linkStyle 1 stroke:#b58900,stroke-width:3px
```

```kgcl
change relationship between GO:0005635 and GO:0005634 from rdfs:subClassOf to BFO:0000050
```

### Move a term to a more specific parent: `NodeDeepening`

Replaces a parent with one of that parent's own descendants. `shallow` does the
reverse, moving a term to a more general parent.

```mermaid
flowchart LR
  subgraph before [Before]
    direction BT
    h1["GO:0031965<br/>nuclear membrane"]
    h2["GO:0031090<br/>organelle membrane"]
    h3["GO:0016020<br/>membrane"]
    h2 -- "is_a" --> h3
    h1 -- "is_a" --> h3
  end
  subgraph after [After]
    direction BT
    h4["GO:0031965<br/>nuclear membrane"]
    h5["GO:0031090<br/>organelle membrane"]
    h6["GO:0016020<br/>membrane"]
    h5 -- "is_a" --> h6
    h4 -- "is_a" --> h5
  end
  before ==> after
  linkStyle 3 stroke:#b58900,stroke-width:3px
```

```kgcl
deepen GO:0031965 from GO:0016020 to GO:0031090
shallow GO:0031965 from GO:0031090 to GO:0016020
```

## Obsoletion

### Obsolete a term and name its replacement: `NodeObsoletionWithDirectReplacement`

Obsoletion marks a term as no longer to be used, without deleting it, so existing
annotations that use the term can still be interpreted. Naming a replacement lets
those annotations be updated automatically. Here, `GO:9999999` stands for an
accidental duplicate of *nucleus*.

```mermaid
flowchart LR
  subgraph before [Before]
    direction BT
    i1["GO:9999999<br/>cell nucleus"]
    i2["GO:0043231<br/>intracellular<br/>membrane-bounded organelle"]
    i3["GO:0005634<br/>nucleus"]
    i1 -- "is_a" --> i2
    i3 -- "is_a" --> i2
  end
  subgraph after [After]
    direction BT
    i4["GO:9999999<br/>obsolete cell nucleus"]:::changed
    i5["GO:0043231<br/>intracellular<br/>membrane-bounded organelle"]
    i6["GO:0005634<br/>nucleus"]
    i6 -- "is_a" --> i5
    i4 -. "replaced by" .-> i6
  end
  before ==> after
  classDef changed fill:#fff3b0,stroke:#b58900,stroke-width:2px
  linkStyle 3 stroke:#b58900,stroke-width:3px
```

```kgcl
obsolete GO:9999999 with replacement GO:0005634
```

Without a replacement: `obsolete GO:9999999`. To reverse an obsoletion:
`unobsolete GO:9999999`.

!!! note
    Exactly how an obsoletion is carried out (for example, prefixing the label with
    "obsolete", removing the term's parent relationships, or adding a
    `term replaced by` annotation) depends on the ontology's obsoletion policy and
    on the tool applying the change. The diagram shows a common OBO-style result.

## Subsets

### Add a term to a subset: `AddNodeToSubset`

Subsets (also called *slims*) are curated selections of terms, such as the generic
GO slim.

```mermaid
flowchart LR
  subgraph before [Before]
    j1["GO:0005634<br/>nucleus"]
  end
  subgraph after [After]
    j2["GO:0005634<br/>nucleus<br/><b>in subset:</b> goslim_generic"]:::changed
  end
  before ==> after
  classDef changed fill:#fff3b0,stroke:#b58900,stroke-width:2px
```

```kgcl
add GO:0005634 to subset goslim_generic
remove GO:0005634 from subset goslim_generic
```

## Creating and deleting terms

These change the set of terms rather than a term's content, so they have no diagram.

| Change type | Command |
| --- | --- |
| `ClassCreation` | `create GO:9999999` |
| `NodeCreation` (with a label) | `create node GO:9999999 'cell nucleus'` |
| `NodeDeletion` | `delete GO:9999999` |

Deleting a term removes it entirely. In most published ontologies, obsoletion is
preferred, because other resources may already refer to the term.
