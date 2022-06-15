# Class: ClassCreation
_A node creation where the owl type is 'class'_





URI: [kgcl:ClassCreation](http://w3id.org/kgcl/ClassCreation)




```mermaid
 classDiagram
      NodeCreation <|-- ClassCreation
      
      ClassCreation : about_node
      ClassCreation : about_node_representation
      ClassCreation : annotation_set
      ClassCreation : change_date
      ClassCreation : contributor
      ClassCreation : creator
      ClassCreation : has_undo
      ClassCreation : id
      ClassCreation : language
      ClassCreation : name
      ClassCreation : new_datatype
      ClassCreation : new_language
      ClassCreation : new_value
      ClassCreation : new_value_type
      ClassCreation : node_id
      ClassCreation : old_datatype
      ClassCreation : old_language
      ClassCreation : old_value
      ClassCreation : old_value_type
      ClassCreation : owl_type
      ClassCreation : pull_request
      ClassCreation : see_also
      ClassCreation : superclass
      ClassCreation : was_generated_by
      

```





## Inheritance
* [Change](Change.md)
    * [SimpleChange](SimpleChange.md)
        * [NodeChange](NodeChange.md)
            * [NodeCreation](NodeCreation.md) [ creation]
                * **ClassCreation**



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [superclass](superclass.md) | [Node](Node.md) | 0..1 | None  | . |
| [node_id](node_id.md) | [Node](Node.md) | 0..1 | id of a node to be created  | . |
| [name](name.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [owl_type](owl_type.md) | [OwlTypeEnum](OwlTypeEnum.md) | 0..1 | None  | . |
| [annotation_set](annotation_set.md) | [Annotation](Annotation.md) | 0..1 | None  | . |
| [language](language.md) | [language_tag](language_tag.md) | 0..1 | The language tag of a literal  | . |
| [about_node](about_node.md) | [Node](Node.md) | 0..1 | None  | . |
| [about_node_representation](about_node_representation.md) | [xsd:string](xsd:string) | 0..1 | The representation of a node (URI, CURIE, label)   | . |
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
| [has_undo](has_undo.md) | [Deletion](Deletion.md) | 0..1 | A change that reverses this change  | . |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/kgcl







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['kgcl:ClassCreation'] |
| native | ['kgcl:ClassCreation'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: class creation
description: A node creation where the owl type is 'class'
todos:
- restrict owltype value
from_schema: https://w3id.org/kgcl
is_a: node creation
slots:
- superclass
slot_usage:
  change description:
    name: change description
    string_serialization: creating {about}

```
</details>

### Induced

<details>
```yaml
name: class creation
description: A node creation where the owl type is 'class'
todos:
- restrict owltype value
from_schema: https://w3id.org/kgcl
is_a: node creation
slot_usage:
  change description:
    name: change description
    string_serialization: creating {about}
attributes:
  superclass:
    name: superclass
    from_schema: https://w3id.org/kgcl
    alias: superclass
    owner: class creation
    range: node
  node id:
    name: node id
    description: id of a node to be created
    todos:
    - consider using 'about' instead
    from_schema: https://w3id.org/kgcl
    alias: node_id
    owner: class creation
    range: node
  name:
    name: name
    from_schema: https://w3id.org/kgcl/ontology
    alias: name
    owner: class creation
    range: string
  owl type:
    name: owl type
    from_schema: https://w3id.org/kgcl/ontology
    alias: owl_type
    owner: class creation
    range: owl_type_enum
  annotation set:
    name: annotation set
    from_schema: https://w3id.org/kgcl/ontology
    alias: annotation_set
    owner: class creation
    range: annotation
  language:
    name: language
    description: The language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: language
    owner: class creation
    range: language tag
  about node:
    name: about node
    from_schema: https://w3id.org/kgcl
    is_a: about
    multivalued: false
    alias: about_node
    owner: class creation
    range: node
  about node representation:
    name: about node representation
    description: 'The representation of a node (URI, CURIE, label) '
    from_schema: https://w3id.org/kgcl
    alias: about_node_representation
    owner: class creation
    range: string
  old value:
    name: old value
    description: The value of a property held in the old instance of the ontology
    from_schema: https://w3id.org/kgcl
    alias: old_value
    owner: class creation
    range: string
  new value:
    name: new value
    description: The value of a property held in the new instance of the ontology
    from_schema: https://w3id.org/kgcl
    alias: new_value
    owner: class creation
    range: string
  old value type:
    name: old value type
    description: The type (IRI or Literal) of an old value
    from_schema: https://w3id.org/kgcl
    alias: old_value_type
    owner: class creation
    range: string
  new value type:
    name: new value type
    description: The type (IRI or Literal) of a new value
    from_schema: https://w3id.org/kgcl
    alias: new_value_type
    owner: class creation
    range: string
  new language:
    name: new language
    description: The new language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: new_language
    owner: class creation
    range: string
  old language:
    name: old language
    description: The old language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: old_language
    owner: class creation
    range: string
  new datatype:
    name: new datatype
    description: The new datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: new_datatype
    owner: class creation
    range: string
  old datatype:
    name: old datatype
    description: The old datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: old_datatype
    owner: class creation
    range: string
  id:
    name: id
    from_schema: https://w3id.org/kgcl/basics
    identifier: true
    alias: id
    owner: class creation
    range: string
  was generated by:
    name: was generated by
    from_schema: https://w3id.org/kgcl/prov
    slot_uri: prov:wasGeneratedBy
    alias: was_generated_by
    owner: class creation
    range: activity
  see also:
    name: see also
    from_schema: https://w3id.org/kgcl
    slot_uri: rdfs:seeAlso
    alias: see_also
    owner: class creation
    range: string
  pull request:
    name: pull request
    from_schema: https://w3id.org/kgcl
    alias: pull_request
    owner: class creation
    range: string
  creator:
    name: creator
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: creator
    owner: class creation
    range: string
  change date:
    name: change date
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:date
    alias: change_date
    owner: class creation
    range: string
  contributor:
    name: contributor
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: contributor
    owner: class creation
    range: string
  has undo:
    name: has undo
    description: A change that reverses this change
    from_schema: https://w3id.org/kgcl
    domain: change
    multivalued: false
    alias: has_undo
    owner: class creation
    range: deletion

```
</details>