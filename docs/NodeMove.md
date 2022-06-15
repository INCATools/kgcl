# Class: NodeMove
_A node move is a combination of deleting a parent edge and adding a parent edge, where the predicate is preserved and the object/parent node changes_





URI: [kgcl:NodeMove](http://w3id.org/kgcl/NodeMove)




```mermaid
 classDiagram
      EdgeChange <|-- NodeMove
      
      NodeMove : about_edge
      NodeMove : change_date
      NodeMove : contributor
      NodeMove : creator
      NodeMove : datatype
      NodeMove : has_undo
      NodeMove : id
      NodeMove : language
      NodeMove : new_datatype
      NodeMove : new_language
      NodeMove : new_object_type
      NodeMove : new_value
      NodeMove : new_value_type
      NodeMove : object_type
      NodeMove : old_datatype
      NodeMove : old_language
      NodeMove : old_object_type
      NodeMove : old_value
      NodeMove : old_value_type
      NodeMove : pull_request
      NodeMove : see_also
      NodeMove : was_generated_by
      

```





## Inheritance
* [Change](Change.md)
    * [SimpleChange](SimpleChange.md)
        * [EdgeChange](EdgeChange.md)
            * **NodeMove**
                * [NodeDeepening](NodeDeepening.md)
                * [NodeShallowing](NodeShallowing.md)



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [old_object_type](old_object_type.md) | [xsd:string](xsd:string) | 0..1 | The type (IRI or Literal) of an old object  | . |
| [new_object_type](new_object_type.md) | [xsd:string](xsd:string) | 0..1 | The type (IRI or Literal) of a new object  | . |
| [about_edge](about_edge.md) | [Edge](Edge.md) | 0..1 | None  | . |
| [object_type](object_type.md) | [xsd:string](xsd:string) | 0..1 | The type (IRI or Literal) of an object  | . |
| [language](language.md) | [language_tag](language_tag.md) | 0..1 | The language tag of a literal  | . |
| [datatype](datatype.md) | [xsd:string](xsd:string) | 0..1 | The datatype of a literal  | . |
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
| [has_undo](has_undo.md) | [Change](Change.md) | 0..1 | A change that reverses this change  | . |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/kgcl







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['kgcl:NodeMove'] |
| native | ['kgcl:NodeMove'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: node move
description: A node move is a combination of deleting a parent edge and adding a parent
  edge, where the predicate is preserved and the object/parent node changes
examples:
- value: changing a is-a b to a is-a c
from_schema: https://w3id.org/kgcl
is_a: edge change
slots:
- old object type
- new object type
slot_usage:
  change description:
    name: change description
    string_serialization: move {about edge} from {old value} to {new value}

```
</details>

### Induced

<details>
```yaml
name: node move
description: A node move is a combination of deleting a parent edge and adding a parent
  edge, where the predicate is preserved and the object/parent node changes
examples:
- value: changing a is-a b to a is-a c
from_schema: https://w3id.org/kgcl
is_a: edge change
slot_usage:
  change description:
    name: change description
    string_serialization: move {about edge} from {old value} to {new value}
attributes:
  old object type:
    name: old object type
    description: The type (IRI or Literal) of an old object
    from_schema: https://w3id.org/kgcl
    alias: old_object_type
    owner: node move
    range: string
  new object type:
    name: new object type
    description: The type (IRI or Literal) of a new object
    from_schema: https://w3id.org/kgcl
    alias: new_object_type
    owner: node move
    range: string
  about edge:
    name: about edge
    from_schema: https://w3id.org/kgcl
    is_a: about
    multivalued: false
    alias: about_edge
    owner: node move
    range: edge
  object type:
    name: object type
    description: The type (IRI or Literal) of an object
    from_schema: https://w3id.org/kgcl
    alias: object_type
    owner: node move
    range: string
  language:
    name: language
    description: The language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: language
    owner: node move
    range: language tag
  datatype:
    name: datatype
    description: The datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: datatype
    owner: node move
    range: string
  old value:
    name: old value
    description: The value of a property held in the old instance of the ontology
    from_schema: https://w3id.org/kgcl
    alias: old_value
    owner: node move
    range: string
  new value:
    name: new value
    description: The value of a property held in the new instance of the ontology
    from_schema: https://w3id.org/kgcl
    alias: new_value
    owner: node move
    range: string
  old value type:
    name: old value type
    description: The type (IRI or Literal) of an old value
    from_schema: https://w3id.org/kgcl
    alias: old_value_type
    owner: node move
    range: string
  new value type:
    name: new value type
    description: The type (IRI or Literal) of a new value
    from_schema: https://w3id.org/kgcl
    alias: new_value_type
    owner: node move
    range: string
  new language:
    name: new language
    description: The new language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: new_language
    owner: node move
    range: string
  old language:
    name: old language
    description: The old language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: old_language
    owner: node move
    range: string
  new datatype:
    name: new datatype
    description: The new datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: new_datatype
    owner: node move
    range: string
  old datatype:
    name: old datatype
    description: The old datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: old_datatype
    owner: node move
    range: string
  id:
    name: id
    from_schema: https://w3id.org/kgcl/basics
    identifier: true
    alias: id
    owner: node move
    range: string
  was generated by:
    name: was generated by
    from_schema: https://w3id.org/kgcl/prov
    slot_uri: prov:wasGeneratedBy
    alias: was_generated_by
    owner: node move
    range: activity
  see also:
    name: see also
    from_schema: https://w3id.org/kgcl
    slot_uri: rdfs:seeAlso
    alias: see_also
    owner: node move
    range: string
  pull request:
    name: pull request
    from_schema: https://w3id.org/kgcl
    alias: pull_request
    owner: node move
    range: string
  creator:
    name: creator
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: creator
    owner: node move
    range: string
  change date:
    name: change date
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:date
    alias: change_date
    owner: node move
    range: string
  contributor:
    name: contributor
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: contributor
    owner: node move
    range: string
  has undo:
    name: has undo
    description: A change that reverses this change
    from_schema: https://w3id.org/kgcl
    domain: change
    multivalued: false
    alias: has_undo
    owner: node move
    range: change

```
</details>