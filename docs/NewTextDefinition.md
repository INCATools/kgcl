# Class: NewTextDefinition
_A node change where a de-novo text definition is created_





URI: [kgcl:NewTextDefinition](http://w3id.org/kgcl/NewTextDefinition)




```mermaid
 classDiagram
      NodeTextDefinitionChange <|-- NewTextDefinition
      
      NewTextDefinition : about_node
      NewTextDefinition : about_node_representation
      NewTextDefinition : change_date
      NewTextDefinition : contributor
      NewTextDefinition : creator
      NewTextDefinition : has_undo
      NewTextDefinition : id
      NewTextDefinition : language
      NewTextDefinition : new_datatype
      NewTextDefinition : new_language
      NewTextDefinition : new_value
      NewTextDefinition : new_value_type
      NewTextDefinition : old_datatype
      NewTextDefinition : old_language
      NewTextDefinition : old_value
      NewTextDefinition : old_value_type
      NewTextDefinition : pull_request
      NewTextDefinition : see_also
      NewTextDefinition : was_generated_by
      

```





## Inheritance
* [Change](Change.md)
    * [SimpleChange](SimpleChange.md)
        * [NodeChange](NodeChange.md)
            * [NodeTextDefinitionChange](NodeTextDefinitionChange.md)
                * **NewTextDefinition**



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [new_value](new_value.md) | [xsd:string](xsd:string) | 0..1 | The value of a property held in the new instance of the ontology  | . |
| [about_node](about_node.md) | [Node](Node.md) | 0..1 | None  | . |
| [about_node_representation](about_node_representation.md) | [xsd:string](xsd:string) | 0..1 | The representation of a node (URI, CURIE, label)   | . |
| [language](language.md) | [language_tag](language_tag.md) | 0..1 | The language tag of a literal  | . |
| [old_value](old_value.md) | [xsd:string](xsd:string) | 0..1 | The value of a property held in the old instance of the ontology  | . |
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
| [has_undo](has_undo.md) | [Change](Change.md) | 0..1 | A change that reverses this change  | . |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/kgcl







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['kgcl:NewTextDefinition'] |
| native | ['kgcl:NewTextDefinition'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: new text definition
description: A node change where a de-novo text definition is created
from_schema: https://w3id.org/kgcl
is_a: node text definition change
slots:
- new value

```
</details>

### Induced

<details>
```yaml
name: new text definition
description: A node change where a de-novo text definition is created
from_schema: https://w3id.org/kgcl
is_a: node text definition change
attributes:
  new value:
    name: new value
    description: The value of a property held in the new instance of the ontology
    from_schema: https://w3id.org/kgcl
    alias: new_value
    owner: new text definition
    range: string
  about node:
    name: about node
    from_schema: https://w3id.org/kgcl
    is_a: about
    multivalued: false
    alias: about_node
    owner: new text definition
    range: node
  about node representation:
    name: about node representation
    description: 'The representation of a node (URI, CURIE, label) '
    from_schema: https://w3id.org/kgcl
    alias: about_node_representation
    owner: new text definition
    range: string
  language:
    name: language
    description: The language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: language
    owner: new text definition
    range: language tag
  old value:
    name: old value
    description: The value of a property held in the old instance of the ontology
    from_schema: https://w3id.org/kgcl
    alias: old_value
    owner: new text definition
    range: string
  old value type:
    name: old value type
    description: The type (IRI or Literal) of an old value
    from_schema: https://w3id.org/kgcl
    alias: old_value_type
    owner: new text definition
    range: string
  new value type:
    name: new value type
    description: The type (IRI or Literal) of a new value
    from_schema: https://w3id.org/kgcl
    alias: new_value_type
    owner: new text definition
    range: string
  new language:
    name: new language
    description: The new language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: new_language
    owner: new text definition
    range: string
  old language:
    name: old language
    description: The old language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: old_language
    owner: new text definition
    range: string
  new datatype:
    name: new datatype
    description: The new datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: new_datatype
    owner: new text definition
    range: string
  old datatype:
    name: old datatype
    description: The old datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: old_datatype
    owner: new text definition
    range: string
  id:
    name: id
    from_schema: https://w3id.org/kgcl/basics
    identifier: true
    alias: id
    owner: new text definition
    range: string
  was generated by:
    name: was generated by
    from_schema: https://w3id.org/kgcl/prov
    slot_uri: prov:wasGeneratedBy
    alias: was_generated_by
    owner: new text definition
    range: activity
  see also:
    name: see also
    from_schema: https://w3id.org/kgcl
    slot_uri: rdfs:seeAlso
    alias: see_also
    owner: new text definition
    range: string
  pull request:
    name: pull request
    from_schema: https://w3id.org/kgcl
    alias: pull_request
    owner: new text definition
    range: string
  creator:
    name: creator
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: creator
    owner: new text definition
    range: string
  change date:
    name: change date
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:date
    alias: change_date
    owner: new text definition
    range: string
  contributor:
    name: contributor
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: contributor
    owner: new text definition
    range: string
  has undo:
    name: has undo
    description: A change that reverses this change
    from_schema: https://w3id.org/kgcl
    domain: change
    multivalued: false
    alias: has_undo
    owner: new text definition
    range: change

```
</details>