# Class: NodeRename
_A node change where the name (aka rdfs:label) of the node changes_





URI: [kgcl:NodeRename](http://w3id.org/kgcl/NodeRename)




```mermaid
 classDiagram
      NodeChange <|-- NodeRename
      
      NodeRename : about_node
      NodeRename : about_node_representation
      NodeRename : change_date
      NodeRename : contributor
      NodeRename : creator
      NodeRename : has_textual_diff
      NodeRename : has_undo
      NodeRename : id
      NodeRename : language
      NodeRename : new_datatype
      NodeRename : new_language
      NodeRename : new_value
      NodeRename : new_value_type
      NodeRename : old_datatype
      NodeRename : old_language
      NodeRename : old_value
      NodeRename : old_value_type
      NodeRename : pull_request
      NodeRename : see_also
      NodeRename : was_generated_by
      

```





## Inheritance
* [Change](Change.md)
    * [SimpleChange](SimpleChange.md)
        * [NodeChange](NodeChange.md)
            * **NodeRename**



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [old_value](old_value.md) | [xsd:string](xsd:string) | 0..1 | The value of a property held in the old instance of the ontology  | . |
| [new_value](new_value.md) | [xsd:string](xsd:string) | 0..1 | The value of a property held in the new instance of the ontology  | . |
| [has_textual_diff](has_textual_diff.md) | [TextualDiff](TextualDiff.md) | 0..1 | A representation of character-level changes on a textual literal property. For example, if a text definition may change by only a single character such as addition of a period, it is useful to be able to see this visually.  | . |
| [new_language](new_language.md) | [xsd:string](xsd:string) | 0..1 | The new language tag of a literal  | . |
| [old_language](old_language.md) | [xsd:string](xsd:string) | 0..1 | The old language tag of a literal  | . |
| [about_node](about_node.md) | [Node](Node.md) | 0..1 | None  | . |
| [about_node_representation](about_node_representation.md) | [xsd:string](xsd:string) | 0..1 | The representation of a node (URI, CURIE, label)   | . |
| [language](language.md) | [language_tag](language_tag.md) | 0..1 | The language tag of a literal  | . |
| [old_value_type](old_value_type.md) | [xsd:string](xsd:string) | 0..1 | The type (IRI or Literal) of an old value  | . |
| [new_value_type](new_value_type.md) | [xsd:string](xsd:string) | 0..1 | The type (IRI or Literal) of a new value  | . |
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
| self | ['kgcl:NodeRename'] |
| native | ['kgcl:NodeRename'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: node rename
description: A node change where the name (aka rdfs:label) of the node changes
examples:
- value: rename UBERON:0002398 from 'manus' to 'hand'
  description: replacing the rdfs:label of 'manus' on an uberon class with the rdfs:label
    'hand'
from_schema: https://w3id.org/kgcl
is_a: node change
slots:
- old value
- new value
- has textual diff
- new language
- old language
slot_usage:
  old value:
    name: old value
    multivalued: false
  new value:
    name: new value
    multivalued: false
  change description:
    name: change description
    string_serialization: rename {about} from {old value} to {new value}

```
</details>

### Induced

<details>
```yaml
name: node rename
description: A node change where the name (aka rdfs:label) of the node changes
examples:
- value: rename UBERON:0002398 from 'manus' to 'hand'
  description: replacing the rdfs:label of 'manus' on an uberon class with the rdfs:label
    'hand'
from_schema: https://w3id.org/kgcl
is_a: node change
slot_usage:
  old value:
    name: old value
    multivalued: false
  new value:
    name: new value
    multivalued: false
  change description:
    name: change description
    string_serialization: rename {about} from {old value} to {new value}
attributes:
  old value:
    name: old value
    description: The value of a property held in the old instance of the ontology
    from_schema: https://w3id.org/kgcl
    multivalued: false
    alias: old_value
    owner: node rename
    range: string
  new value:
    name: new value
    description: The value of a property held in the new instance of the ontology
    from_schema: https://w3id.org/kgcl
    multivalued: false
    alias: new_value
    owner: node rename
    range: string
  has textual diff:
    name: has textual diff
    description: A representation of character-level changes on a textual literal
      property. For example, if a text definition may change by only a single character
      such as addition of a period, it is useful to be able to see this visually.
    comments:
    - this is NOT for representing the diff of the change as a whole.
    from_schema: https://w3id.org/kgcl
    domain: change
    alias: has_textual_diff
    owner: node rename
    range: textual diff
  new language:
    name: new language
    description: The new language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: new_language
    owner: node rename
    range: string
  old language:
    name: old language
    description: The old language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: old_language
    owner: node rename
    range: string
  about node:
    name: about node
    from_schema: https://w3id.org/kgcl
    is_a: about
    multivalued: false
    alias: about_node
    owner: node rename
    range: node
  about node representation:
    name: about node representation
    description: 'The representation of a node (URI, CURIE, label) '
    from_schema: https://w3id.org/kgcl
    alias: about_node_representation
    owner: node rename
    range: string
  language:
    name: language
    description: The language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: language
    owner: node rename
    range: language tag
  old value type:
    name: old value type
    description: The type (IRI or Literal) of an old value
    from_schema: https://w3id.org/kgcl
    alias: old_value_type
    owner: node rename
    range: string
  new value type:
    name: new value type
    description: The type (IRI or Literal) of a new value
    from_schema: https://w3id.org/kgcl
    alias: new_value_type
    owner: node rename
    range: string
  new datatype:
    name: new datatype
    description: The new datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: new_datatype
    owner: node rename
    range: string
  old datatype:
    name: old datatype
    description: The old datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: old_datatype
    owner: node rename
    range: string
  id:
    name: id
    from_schema: https://w3id.org/kgcl/basics
    identifier: true
    alias: id
    owner: node rename
    range: string
  was generated by:
    name: was generated by
    from_schema: https://w3id.org/kgcl/prov
    slot_uri: prov:wasGeneratedBy
    alias: was_generated_by
    owner: node rename
    range: activity
  see also:
    name: see also
    from_schema: https://w3id.org/kgcl
    slot_uri: rdfs:seeAlso
    alias: see_also
    owner: node rename
    range: string
  pull request:
    name: pull request
    from_schema: https://w3id.org/kgcl
    alias: pull_request
    owner: node rename
    range: string
  creator:
    name: creator
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: creator
    owner: node rename
    range: string
  change date:
    name: change date
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:date
    alias: change_date
    owner: node rename
    range: string
  contributor:
    name: contributor
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: contributor
    owner: node rename
    range: string
  has undo:
    name: has undo
    description: A change that reverses this change
    from_schema: https://w3id.org/kgcl
    domain: change
    multivalued: false
    alias: has_undo
    owner: node rename
    range: change

```
</details>