# Class: NodeUnobsoletion
_unobsoletion of a node deprecates usage of that node. Rarely applied._





URI: [kgcl:NodeUnobsoletion](http://w3id.org/kgcl/NodeUnobsoletion)




```mermaid
 classDiagram
      Unobsoletion <|-- NodeUnobsoletion
      NodeChange <|-- NodeUnobsoletion
      
      NodeUnobsoletion : about_node
      NodeUnobsoletion : about_node_representation
      NodeUnobsoletion : change_date
      NodeUnobsoletion : contributor
      NodeUnobsoletion : creator
      NodeUnobsoletion : has_undo
      NodeUnobsoletion : id
      NodeUnobsoletion : language
      NodeUnobsoletion : new_datatype
      NodeUnobsoletion : new_language
      NodeUnobsoletion : new_value
      NodeUnobsoletion : new_value_type
      NodeUnobsoletion : old_datatype
      NodeUnobsoletion : old_language
      NodeUnobsoletion : old_value
      NodeUnobsoletion : old_value_type
      NodeUnobsoletion : pull_request
      NodeUnobsoletion : see_also
      NodeUnobsoletion : was_generated_by
      

```





## Inheritance
* [Change](Change.md)
    * [SimpleChange](SimpleChange.md)
        * [NodeChange](NodeChange.md)
            * **NodeUnobsoletion** [ unobsoletion]



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [about_node](about_node.md) | [Node](Node.md) | 0..1 | None  | . |
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
| [has_undo](has_undo.md) | [Obsoletion](Obsoletion.md) | 0..1 | A change that reverses this change  | . |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/kgcl







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['kgcl:NodeUnobsoletion'] |
| native | ['kgcl:NodeUnobsoletion'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: node unobsoletion
description: unobsoletion of a node deprecates usage of that node. Rarely applied.
from_schema: https://w3id.org/kgcl
see_also:
- http://wiki.geneontology.org/index.php/Restoring_an_Obsolete_Ontology_Term
aliases:
- node undeprecation
- class unobsoletion
- term unobsoletion
- concept unobsoletion
is_a: node change
mixins:
- unobsoletion
slot_usage:
  change description:
    name: change description
    string_serialization: unobsoleting {about}
  replaced by:
    name: replaced by
    range: node
  consider:
    name: consider
    range: node

```
</details>

### Induced

<details>
```yaml
name: node unobsoletion
description: unobsoletion of a node deprecates usage of that node. Rarely applied.
from_schema: https://w3id.org/kgcl
see_also:
- http://wiki.geneontology.org/index.php/Restoring_an_Obsolete_Ontology_Term
aliases:
- node undeprecation
- class unobsoletion
- term unobsoletion
- concept unobsoletion
is_a: node change
mixins:
- unobsoletion
slot_usage:
  change description:
    name: change description
    string_serialization: unobsoleting {about}
  replaced by:
    name: replaced by
    range: node
  consider:
    name: consider
    range: node
attributes:
  about node:
    name: about node
    from_schema: https://w3id.org/kgcl
    is_a: about
    multivalued: false
    alias: about_node
    owner: node unobsoletion
    range: node
  about node representation:
    name: about node representation
    description: 'The representation of a node (URI, CURIE, label) '
    from_schema: https://w3id.org/kgcl
    alias: about_node_representation
    owner: node unobsoletion
    range: string
  language:
    name: language
    description: The language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: language
    owner: node unobsoletion
    range: language tag
  old value:
    name: old value
    description: The value of a property held in the old instance of the ontology
    from_schema: https://w3id.org/kgcl
    alias: old_value
    owner: node unobsoletion
    range: string
  new value:
    name: new value
    description: The value of a property held in the new instance of the ontology
    from_schema: https://w3id.org/kgcl
    alias: new_value
    owner: node unobsoletion
    range: string
  old value type:
    name: old value type
    description: The type (IRI or Literal) of an old value
    from_schema: https://w3id.org/kgcl
    alias: old_value_type
    owner: node unobsoletion
    range: string
  new value type:
    name: new value type
    description: The type (IRI or Literal) of a new value
    from_schema: https://w3id.org/kgcl
    alias: new_value_type
    owner: node unobsoletion
    range: string
  new language:
    name: new language
    description: The new language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: new_language
    owner: node unobsoletion
    range: string
  old language:
    name: old language
    description: The old language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: old_language
    owner: node unobsoletion
    range: string
  new datatype:
    name: new datatype
    description: The new datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: new_datatype
    owner: node unobsoletion
    range: string
  old datatype:
    name: old datatype
    description: The old datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: old_datatype
    owner: node unobsoletion
    range: string
  id:
    name: id
    from_schema: https://w3id.org/kgcl/basics
    identifier: true
    alias: id
    owner: node unobsoletion
    range: string
  was generated by:
    name: was generated by
    from_schema: https://w3id.org/kgcl/prov
    slot_uri: prov:wasGeneratedBy
    alias: was_generated_by
    owner: node unobsoletion
    range: activity
  see also:
    name: see also
    from_schema: https://w3id.org/kgcl
    slot_uri: rdfs:seeAlso
    alias: see_also
    owner: node unobsoletion
    range: string
  pull request:
    name: pull request
    from_schema: https://w3id.org/kgcl
    alias: pull_request
    owner: node unobsoletion
    range: string
  creator:
    name: creator
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: creator
    owner: node unobsoletion
    range: string
  change date:
    name: change date
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:date
    alias: change_date
    owner: node unobsoletion
    range: string
  contributor:
    name: contributor
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: contributor
    owner: node unobsoletion
    range: string
  has undo:
    name: has undo
    description: A change that reverses this change
    from_schema: https://w3id.org/kgcl
    domain: change
    multivalued: false
    alias: has_undo
    owner: node unobsoletion
    range: obsoletion

```
</details>