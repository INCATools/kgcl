# Command examples

One example of each change type, written as a KGCL command and as YAML. The
examples are generated from the test suite (`tests/cases.py`), so every command on
this page is known to parse. For before-and-after diagrams of the most common
changes, see the [visual guide to change types](change-types.md).

## Labels

### Rename a node (replace its label)

Class: [`NodeRename`](https://w3id.org/kgcl/NodeRename)

```kgcl
rename GO:0005635 from 'nuclear envelope' to 'foo bar'
```

```yaml
id: CHANGE:001
type: NodeRename
old_value: nuclear envelope
new_value: foo bar
about_node: GO:0005635
about_node_representation: curie
```

### Add a label to an unlabeled node

Class: [`NewLabel`](https://w3id.org/kgcl/NewLabel)

```kgcl
add label 'nucleus' to GO:0005634
```

```yaml
id: CHANGE:001
type: NewLabel
new_value: nucleus
about_node: GO:0005634
about_node_representation: curie
```

## Synonyms

### Add a synonym

Class: [`NewSynonym`](https://w3id.org/kgcl/NewSynonym)

```kgcl
create exact synonym 'foo' for GO:0005634
```

```yaml
id: CHANGE:001
type: NewSynonym
new_value: foo
about_node: GO:0005634
about_node_representation: curie
qualifier: exact
```

### Remove a synonym

Class: [`RemoveSynonym`](https://w3id.org/kgcl/RemoveSynonym)

```kgcl
remove synonym 'foo' for GO:0005634
```

```yaml
id: CHANGE:001
type: RemoveSynonym
old_value: foo
about_node: GO:0005634
about_node_representation: curie
```

### Replace the text of a synonym

Class: [`SynonymReplacement`](https://w3id.org/kgcl/SynonymReplacement)

```kgcl
change synonym 'cell nucleus' for GO:0005634 to 'cell NUCLEUS'
```

```yaml
id: CHANGE:001
type: SynonymReplacement
old_value: cell nucleus
new_value: cell NUCLEUS
about_node: GO:0005634
about_node_representation: label
```

## Definitions

### Add a definition

Class: [`NewTextDefinition`](https://w3id.org/kgcl/NewTextDefinition)

```kgcl
add definition 'this is dummy description' to GO:0005635
```

```yaml
id: CHANGE:001
type: NewTextDefinition
new_value: this is dummy description
about_node: GO:0005635
about_node_representation: curie
```

### Change a definition

Class: [`NodeTextDefinitionChange`](https://w3id.org/kgcl/NodeTextDefinitionChange)

```kgcl
change definition of GO:0005635 to 'this is dummy description'
```

```yaml
id: CHANGE:001
type: NodeTextDefinitionChange
new_value: this is dummy description
about_node: GO:0005635
about_node_representation: curie
```

### Remove a definition

Class: [`RemoveTextDefinition`](https://w3id.org/kgcl/RemoveTextDefinition)

```kgcl
remove definition for GO:0005634
```

```yaml
id: CHANGE:001
type: RemoveTextDefinition
about_node: GO:0005634
about_node_representation: curie
```

## Relationships (edges)

### Create an edge

Class: [`EdgeCreation`](https://w3id.org/kgcl/EdgeCreation)

```kgcl
create edge GO:0005634 BFO:0000050 GO:0009411
```

```yaml
id: CHANGE:001
type: EdgeCreation
object_type: curie
subject: GO:0005634
predicate: BFO:0000050
object: GO:0009411
subject_type: curie
predicate_type: curie
```

### Place a node under another node (create an is_a edge)

Class: [`PlaceUnder`](https://w3id.org/kgcl/PlaceUnder)

```kgcl
create edge GO:0005634 rdfs:subClassOf GO:0009411
```

```yaml
id: CHANGE:001
type: PlaceUnder
object_type: curie
subject: GO:0005634
predicate: rdfs:subClassOf
object: GO:0009411
subject_type: curie
predicate_type: curie
```

### Delete an edge

Class: [`EdgeDeletion`](https://w3id.org/kgcl/EdgeDeletion)

```kgcl
delete edge GO:0005635 BFO:0000050 GO:0005634
```

```yaml
id: CHANGE:001
type: EdgeDeletion
object_type: curie
subject: GO:0005635
predicate: BFO:0000050
object: GO:0005634
subject_type: curie
predicate_type: curie
```

### Remove a node from under another node (delete an is_a edge)

Class: [`RemoveUnder`](https://w3id.org/kgcl/RemoveUnder)

```kgcl
delete edge GO:0005634 rdfs:subClassOf GO:0043231
```

```yaml
id: CHANGE:001
type: RemoveUnder
object_type: curie
subject: GO:0005634
predicate: rdfs:subClassOf
object: GO:0043231
subject_type: curie
predicate_type: curie
```

### Change the predicate (relationship type) of an edge

Class: [`PredicateChange`](https://w3id.org/kgcl/PredicateChange)

```kgcl
change relationship between GO:0005635 and GO:0005634 from BFO:0000050 to rdfs:subClassOf
```

```yaml
id: CHANGE:001
type: PredicateChange
old_value: BFO:0000050
new_value: rdfs:subClassOf
old_value_type: curie
new_value_type: curie
about_edge:
  subject: GO:0005635
  predicate: BFO:0000050
  object: GO:0005634
  subject_representation: curie
  predicate_representation: curie
  object_representation: curie
```

### Move a node under a more specific parent

Class: [`NodeDeepening`](https://w3id.org/kgcl/NodeDeepening)

```kgcl
deepen GO:0005739 from GO:0043231 to GO:0005634
```

```yaml
id: CHANGE:001
type: NodeDeepening
old_value: GO:0043231
new_value: GO:0005634
about_edge:
  subject: GO:0005739
  object: GO:0043231
  subject_representation: curie
  object_representation: curie
old_object_type: curie
new_object_type: curie
```

### Move a node under a more general parent

Class: [`NodeShallowing`](https://w3id.org/kgcl/NodeShallowing)

```kgcl
shallow GO:0005739 from GO:0005634 to GO:0043231
```

```yaml
id: CHANGE:001
type: NodeShallowing
old_value: GO:0005634
new_value: GO:0043231
about_edge:
  subject: GO:0005739
  object: GO:0005634
  subject_representation: curie
  object_representation: curie
old_object_type: curie
new_object_type: curie
```

## Obsoletion

### Obsolete a node

Class: [`NodeObsoletion`](https://w3id.org/kgcl/NodeObsoletion)

```kgcl
obsolete GO:0005634
```

```yaml
id: CHANGE:001
type: NodeObsoletion
about_node: GO:0005634
about_node_representation: curie
```

### Obsolete a node and name its replacement

Class: [`NodeObsoletionWithDirectReplacement`](https://w3id.org/kgcl/NodeObsoletionWithDirectReplacement)

```kgcl
obsolete GO:0005634 with replacement GO:999
```

```yaml
id: CHANGE:001
type: NodeObsoletionWithDirectReplacement
about_node: GO:0005634
about_node_representation: curie
has_direct_replacement: GO:999
```

## Subsets

### Add a node to a subset

Class: [`AddNodeToSubset`](https://w3id.org/kgcl/AddNodeToSubset)

```kgcl
add GO:0005634 to subset foo
```

```yaml
id: CHANGE:001
type: AddNodeToSubset
about_node: GO:0005634
about_node_representation: curie
in_subset: foo
```

### Remove a node from a subset

Class: [`RemoveNodeFromSubset`](https://w3id.org/kgcl/RemoveNodeFromSubset)

```kgcl
remove GO:0005634 from subset foo
```

```yaml
id: CHANGE:001
type: RemoveNodeFromSubset
about_node: GO:0005634
about_node_representation: curie
in_subset: foo
```

## Creating nodes

### Create a class

Class: [`ClassCreation`](https://w3id.org/kgcl/ClassCreation)

```kgcl
create GO:9999999
```

```yaml
id: CHANGE:001
type: ClassCreation
about_node: GO:9999999
about_node_representation: curie
```

### Create a node with a label

Class: [`NodeCreation`](https://w3id.org/kgcl/NodeCreation)

```kgcl
create node GO:9999999 'foo'
```

```yaml
id: CHANGE:001
type: NodeCreation
about_node: GO:9999999
about_node_representation: curie
name: foo
```
