# Class: NameBecomesSynonym
_A node synonym where the name NAME of an node NODE moves to a synonym, and NODE receives a new name. This change consists of compose of (1) a node rename where NAME is replaced by a different name (2) a new synonym_





URI: [kgcl:NameBecomesSynonym](http://w3id.org/kgcl/NameBecomesSynonym)




```mermaid
 classDiagram
      NodeSynonymChange <|-- NameBecomesSynonym
      
      NameBecomesSynonym : about_node
      NameBecomesSynonym : about_node_representation
      NameBecomesSynonym : change_date
      NameBecomesSynonym : contributor
      NameBecomesSynonym : creator
      NameBecomesSynonym : has_undo
      NameBecomesSynonym : id
      NameBecomesSynonym : language
      NameBecomesSynonym : new_datatype
      NameBecomesSynonym : new_language
      NameBecomesSynonym : new_value
      NameBecomesSynonym : new_value_type
      NameBecomesSynonym : old_datatype
      NameBecomesSynonym : old_language
      NameBecomesSynonym : old_value
      NameBecomesSynonym : old_value_type
      NameBecomesSynonym : pull_request
      NameBecomesSynonym : see_also
      NameBecomesSynonym : was_generated_by
      

```





## Inheritance
* [Change](Change.md)
    * [SimpleChange](SimpleChange.md)
        * [NodeChange](NodeChange.md)
            * [NodeSynonymChange](NodeSynonymChange.md)
                * **NameBecomesSynonym**



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
| [has_undo](has_undo.md) | [Change](Change.md) | 0..1 | A change that reverses this change  | . |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/kgcl







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['kgcl:NameBecomesSynonym'] |
| native | ['kgcl:NameBecomesSynonym'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: name becomes synonym
description: A node synonym where the name NAME of an node NODE moves to a synonym,
  and NODE receives a new name. This change consists of compose of (1) a node rename
  where NAME is replaced by a different name (2) a new synonym
from_schema: https://w3id.org/kgcl
is_a: node synonym change
slot_usage:
  change 1:
    name: change 1
    range: node rename
  change 2:
    name: change 2
    description: ''
    range: new synonym
  change description:
    name: change description
    string_serialization: synonym {synonym} becomes new name of {about}, and name
      {name} becomes a synonym

```
</details>

### Induced

<details>
```yaml
name: name becomes synonym
description: A node synonym where the name NAME of an node NODE moves to a synonym,
  and NODE receives a new name. This change consists of compose of (1) a node rename
  where NAME is replaced by a different name (2) a new synonym
from_schema: https://w3id.org/kgcl
is_a: node synonym change
slot_usage:
  change 1:
    name: change 1
    range: node rename
  change 2:
    name: change 2
    description: ''
    range: new synonym
  change description:
    name: change description
    string_serialization: synonym {synonym} becomes new name of {about}, and name
      {name} becomes a synonym
attributes:
  about node:
    name: about node
    from_schema: https://w3id.org/kgcl
    is_a: about
    multivalued: false
    alias: about_node
    owner: name becomes synonym
    range: node
  about node representation:
    name: about node representation
    description: 'The representation of a node (URI, CURIE, label) '
    from_schema: https://w3id.org/kgcl
    alias: about_node_representation
    owner: name becomes synonym
    range: string
  language:
    name: language
    description: The language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: language
    owner: name becomes synonym
    range: language tag
  old value:
    name: old value
    description: The value of a property held in the old instance of the ontology
    from_schema: https://w3id.org/kgcl
    alias: old_value
    owner: name becomes synonym
    range: string
  new value:
    name: new value
    description: The value of a property held in the new instance of the ontology
    from_schema: https://w3id.org/kgcl
    alias: new_value
    owner: name becomes synonym
    range: string
  old value type:
    name: old value type
    description: The type (IRI or Literal) of an old value
    from_schema: https://w3id.org/kgcl
    alias: old_value_type
    owner: name becomes synonym
    range: string
  new value type:
    name: new value type
    description: The type (IRI or Literal) of a new value
    from_schema: https://w3id.org/kgcl
    alias: new_value_type
    owner: name becomes synonym
    range: string
  new language:
    name: new language
    description: The new language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: new_language
    owner: name becomes synonym
    range: string
  old language:
    name: old language
    description: The old language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: old_language
    owner: name becomes synonym
    range: string
  new datatype:
    name: new datatype
    description: The new datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: new_datatype
    owner: name becomes synonym
    range: string
  old datatype:
    name: old datatype
    description: The old datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: old_datatype
    owner: name becomes synonym
    range: string
  id:
    name: id
    from_schema: https://w3id.org/kgcl/basics
    identifier: true
    alias: id
    owner: name becomes synonym
    range: string
  was generated by:
    name: was generated by
    from_schema: https://w3id.org/kgcl/prov
    slot_uri: prov:wasGeneratedBy
    alias: was_generated_by
    owner: name becomes synonym
    range: activity
  see also:
    name: see also
    from_schema: https://w3id.org/kgcl
    slot_uri: rdfs:seeAlso
    alias: see_also
    owner: name becomes synonym
    range: string
  pull request:
    name: pull request
    from_schema: https://w3id.org/kgcl
    alias: pull_request
    owner: name becomes synonym
    range: string
  creator:
    name: creator
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: creator
    owner: name becomes synonym
    range: string
  change date:
    name: change date
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:date
    alias: change_date
    owner: name becomes synonym
    range: string
  contributor:
    name: contributor
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: contributor
    owner: name becomes synonym
    range: string
  has undo:
    name: has undo
    description: A change that reverses this change
    from_schema: https://w3id.org/kgcl
    domain: change
    multivalued: false
    alias: has_undo
    owner: name becomes synonym
    range: change

```
</details>