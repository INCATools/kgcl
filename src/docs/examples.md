# KGCL Commands.

## Example: Rename node.
Class: [`NodeRename`](https://w3id.org/kgcl/NodeRename) </br>Command: `rename GO:0005635 from 'nuclear envelope' to 'foo bar'`</br>YAML:
```
id: CHANGE:001
old_value: nuclear envelope
new_value: foo bar
about_node: GO:0005635
about_node_representation: curie

```
## Example: Obsolete node.
Class: [`NodeObsoletion`](https://w3id.org/kgcl/NodeObsoletion) </br>Command: `obsolete GO:0005634`</br>YAML:
```
id: CHANGE:001
about_node: GO:0005634
about_node_representation: curie

```
## Example: Replacement of node after obsoletion.
Class: [`NodeObsoletionWithDirectReplacement`](https://w3id.org/kgcl/NodeObsoletionWithDirectReplacement) </br>Command: `obsolete GO:0005634 with replacement GO:999`</br>YAML:
```
id: CHANGE:001
about_node: GO:0005634
about_node_representation: curie
has_direct_replacement: GO:999

```
## Example: Addition of a new synonym.
Class: [`NewSynonym`](https://w3id.org/kgcl/NewSynonym) </br>Command: `create exact synonym 'foo' for GO:0005634`</br>YAML:
```
id: CHANGE:001
new_value: foo
about_node: GO:0005634
about_node_representation: curie
qualifier: exact

```
## Example: Creation of new class.
Class: [`ClassCreation`](https://w3id.org/kgcl/ClassCreation) </br>Command: `create GO:9999999`</br>YAML:
```
id: CHANGE:001
about_node_representation: curie
node_id: GO:9999999

```
## Example: Creation of new node.
Class: [`NodeCreation`](https://w3id.org/kgcl/NodeCreation) </br>Command: `create node GO:9999999 'foo'`</br>YAML:
```
id: CHANGE:001
about_node: GO:9999999
about_node_representation: curie
node_id: GO:9999999
name: foo

```
## Example: Creation of new edge.
Class: [`EdgeCreation`](https://w3id.org/kgcl/EdgeCreation) </br>Command: `create edge GO:0005634 BFO:0000050 GO:0009411`</br>YAML:
```
id: CHANGE:001
object_type: curie
subject: GO:0005634
predicate: BFO:0000050
object: GO:0009411
subject_type: curie
predicate_type: curie

```
## Example: Place node under another node.
Class: [`PlaceUnder`](https://w3id.org/kgcl/PlaceUnder) </br>Command: `create edge GO:0005634 rdfs:subClassOf GO:0009411`</br>YAML:
```
id: CHANGE:001
object_type: curie
subject: GO:0005634
predicate: rdfs:subClassOf
object: GO:0009411
subject_type: curie
predicate_type: curie

```
## Example: Change predicate.
Class: [`PredicateChange`](https://w3id.org/kgcl/PredicateChange) </br>Command: `change relationship between GO:0005635 and GO:0005634 from BFO:0000050 to rdfs:subClassOf`</br>YAML:
```
id: CHANGE:001
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
## Example: Remove node from under another node.
Class: [`RemoveUnder`](https://w3id.org/kgcl/RemoveUnder) </br>Command: `delete edge GO:0005634 rdfs:subClassOf GO:0043231`</br>YAML:
```
id: CHANGE:001
object_type: curie
subject: GO:0005634
predicate: rdfs:subClassOf
object: GO:0043231
subject_type: curie
predicate_type: curie

```
## Example: Deletion of an edge.
Class: [`EdgeDeletion`](https://w3id.org/kgcl/EdgeDeletion) </br>Command: `delete edge GO:0005635 BFO:0000050 GO:0005634`</br>YAML:
```
id: CHANGE:001
object_type: curie
subject: GO:0005635
predicate: BFO:0000050
object: GO:0005634
subject_type: curie
predicate_type: curie

```
## Example: Deepening of a node.
Class: [`NodeDeepening`](https://w3id.org/kgcl/NodeDeepening) </br>Command: `deepen GO:0005739 from GO:0043231 to GO:0005634`</br>YAML:
```
id: CHANGE:001
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
