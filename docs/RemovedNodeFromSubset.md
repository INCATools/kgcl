# Class: RemovedNodeFromSubset
_Removes a node from a subset, by removing an annotation_





URI: [kgcl:RemovedNodeFromSubset](http://w3id.org/kgcl/RemovedNodeFromSubset)




```mermaid
 classDiagram
      RemoveFromSubset <|-- RemovedNodeFromSubset
      NodeChange <|-- RemovedNodeFromSubset
      
      RemovedNodeFromSubset : about_node
      RemovedNodeFromSubset : about_node_representation
      RemovedNodeFromSubset : change_date
      RemovedNodeFromSubset : contributor
      RemovedNodeFromSubset : creator
      RemovedNodeFromSubset : has_undo
      RemovedNodeFromSubset : id
      RemovedNodeFromSubset : in_subset
      RemovedNodeFromSubset : language
      RemovedNodeFromSubset : new_datatype
      RemovedNodeFromSubset : new_language
      RemovedNodeFromSubset : new_value
      RemovedNodeFromSubset : new_value_type
      RemovedNodeFromSubset : old_datatype
      RemovedNodeFromSubset : old_language
      RemovedNodeFromSubset : old_value
      RemovedNodeFromSubset : old_value_type
      RemovedNodeFromSubset : pull_request
      RemovedNodeFromSubset : see_also
      RemovedNodeFromSubset : was_generated_by
      

```





## Inheritance
* [Change](Change.md)
    * [SimpleChange](SimpleChange.md)
        * [NodeChange](NodeChange.md)
            * **RemovedNodeFromSubset** [ remove from subset]



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [about_node](about_node.md) | [Node](Node.md) | 0..1 | The node that is removed from the subset  | . |
| [about_node_representation](about_node_representation.md) | [xsd:string](xsd:string) | 0..1 | The representation of a node (URI, CURIE, label)   | . |
| [language](language.md) | [language_tag](language_tag.md) | 0..1 | The language tag of a literal  | . |
| [old_value](old_value.md) | [xsd:string](xsd:string) | 0..1 | The value of a property held in the old instance of the ontology  | . |
| [new_value](new_value.md) | [xsd:string](xsd:string) | 0..1 | The value of a property held in the new instance of the ontology  | . |
| [old_value_type](old_value_type.md) | [xsd:string](xsd:string) | 0..1 | The type (IRI or Literal) of an old value  | . |
| [new_value_type](new_value_type.md) | [xsd:string](xsd:string) | 0..1 | The type (IRI or Literal) of a new value  | . |
| [new_language](new_language.md) | [xsd:string](xsd:string) | 0..1 | The new language tag of a literal  | . |
| [old_language](old_language.md) | [xsd:string](xsd:string) | 0..1 | The old language tag of a literal  | . |
| [new_datatype](new_datatype.md) | [xsd:string](xsd:string) | 0..1 | The new datatype of a literal  | . |
| [old_datatype](old_datatype.md) | [xsd:string](xsd:string) | 0..1 | The old datatype of a literal  | . |
| [id](id.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [was_generated_by](was_generated_by.md) | [Activity](Activity.md) | 0..1 | None  | . |
| [see_also](see_also.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [pull_request](pull_request.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [creator](creator.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [change_date](change_date.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [contributor](contributor.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [has_undo](has_undo.md) | [AddToSubset](AddToSubset.md) | 0..1 | A change that reverses this change  | . |
| [in_subset](in_subset.md) | [OntologySubset](OntologySubset.md) | 0..1 | The subset that pertains to this change  | . |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/kgcl







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['kgcl:RemovedNodeFromSubset'] |
| native | ['kgcl:RemovedNodeFromSubset'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: removed node from subset
description: Removes a node from a subset, by removing an annotation
from_schema: https://w3id.org/kgcl
aliases:
- remove term from slim
is_a: node change
mixins:
- remove from subset
slot_usage:
  change description:
    name: change description
    string_serialization: removing {about} from {subset}
  about node:
    name: about node
    description: The node that is removed from the subset
  subset:
    name: subset
    description: The subset from which the node is to be removed

```
</details>

### Induced

<details>
```yaml
name: removed node from subset
description: Removes a node from a subset, by removing an annotation
from_schema: https://w3id.org/kgcl
aliases:
- remove term from slim
is_a: node change
mixins:
- remove from subset
slot_usage:
  change description:
    name: change description
    string_serialization: removing {about} from {subset}
  about node:
    name: about node
    description: The node that is removed from the subset
  subset:
    name: subset
    description: The subset from which the node is to be removed
attributes:
  about node:
    name: about node
    description: The node that is removed from the subset
    from_schema: https://w3id.org/kgcl
    is_a: about
    multivalued: false
    alias: about_node
    owner: removed node from subset
    range: node
  about node representation:
    name: about node representation
    description: 'The representation of a node (URI, CURIE, label) '
    from_schema: https://w3id.org/kgcl
    alias: about_node_representation
    owner: removed node from subset
    range: string
  language:
    name: language
    description: The language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: language
    owner: removed node from subset
    range: language tag
  old value:
    name: old value
    description: The value of a property held in the old instance of the ontology
    from_schema: https://w3id.org/kgcl
    alias: old_value
    owner: removed node from subset
    range: string
  new value:
    name: new value
    description: The value of a property held in the new instance of the ontology
    from_schema: https://w3id.org/kgcl
    alias: new_value
    owner: removed node from subset
    range: string
  old value type:
    name: old value type
    description: The type (IRI or Literal) of an old value
    from_schema: https://w3id.org/kgcl
    alias: old_value_type
    owner: removed node from subset
    range: string
  new value type:
    name: new value type
    description: The type (IRI or Literal) of a new value
    from_schema: https://w3id.org/kgcl
    alias: new_value_type
    owner: removed node from subset
    range: string
  new language:
    name: new language
    description: The new language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: new_language
    owner: removed node from subset
    range: string
  old language:
    name: old language
    description: The old language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: old_language
    owner: removed node from subset
    range: string
  new datatype:
    name: new datatype
    description: The new datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: new_datatype
    owner: removed node from subset
    range: string
  old datatype:
    name: old datatype
    description: The old datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: old_datatype
    owner: removed node from subset
    range: string
  id:
    name: id
    from_schema: https://w3id.org/kgcl/basics
    identifier: true
    alias: id
    owner: removed node from subset
    range: string
  was generated by:
    name: was generated by
    from_schema: https://w3id.org/kgcl/prov
    slot_uri: prov:wasGeneratedBy
    alias: was_generated_by
    owner: removed node from subset
    range: activity
  see also:
    name: see also
    from_schema: https://w3id.org/kgcl
    slot_uri: rdfs:seeAlso
    alias: see_also
    owner: removed node from subset
    range: string
  pull request:
    name: pull request
    from_schema: https://w3id.org/kgcl
    alias: pull_request
    owner: removed node from subset
    range: string
  creator:
    name: creator
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: creator
    owner: removed node from subset
    range: string
  change date:
    name: change date
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:date
    alias: change_date
    owner: removed node from subset
    range: string
  contributor:
    name: contributor
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: contributor
    owner: removed node from subset
    range: string
  has undo:
    name: has undo
    description: A change that reverses this change
    from_schema: https://w3id.org/kgcl
    domain: change
    multivalued: false
    alias: has_undo
    owner: removed node from subset
    range: add to subset
  in subset:
    name: in subset
    description: The subset that pertains to this change
    from_schema: https://w3id.org/kgcl
    alias: in_subset
    owner: removed node from subset
    range: ontology subset

```
</details>