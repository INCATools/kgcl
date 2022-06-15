# Class: MappingCreation
_A specific kind of edge creation in which the created edge is a mapping._





URI: [kgcl:MappingCreation](http://w3id.org/kgcl/MappingCreation)




```mermaid
 classDiagram
      Creation <|-- MappingCreation
      EdgeCreation <|-- MappingCreation
      
      MappingCreation : about_edge
      MappingCreation : annotation_set
      MappingCreation : change_date
      MappingCreation : contributor
      MappingCreation : creator
      MappingCreation : datatype
      MappingCreation : has_undo
      MappingCreation : id
      MappingCreation : language
      MappingCreation : new_datatype
      MappingCreation : new_language
      MappingCreation : new_value
      MappingCreation : new_value_type
      MappingCreation : object
      MappingCreation : object_type
      MappingCreation : old_datatype
      MappingCreation : old_language
      MappingCreation : old_value
      MappingCreation : old_value_type
      MappingCreation : predicate
      MappingCreation : predicate_type
      MappingCreation : pull_request
      MappingCreation : see_also
      MappingCreation : subject
      MappingCreation : subject_type
      MappingCreation : was_generated_by
      

```





## Inheritance
* [Change](Change.md)
    * [SimpleChange](SimpleChange.md)
        * [EdgeChange](EdgeChange.md)
            * [EdgeCreation](EdgeCreation.md) [ creation]
                * **MappingCreation** [ creation]



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [subject](subject.md) | [Node](Node.md) | 0..1 | This corresponds to subject_id in SSSOM  | . |
| [predicate](predicate.md) | [Node](Node.md) | 0..1 | This corresponds to predicate_id in SSSOM. The value of this is typically a predicate from SKOS  | . |
| [object](object.md) | [Node](Node.md) | 0..1 | This corresponds to object_id in SSSOM  | . |
| [annotation_set](annotation_set.md) | [Annotation](Annotation.md) | 0..1 | None  | . |
| [subject_type](subject_type.md) | [xsd:string](xsd:string) | 0..1 | The type (IRI or Literal) of an edge's subject  | . |
| [predicate_type](predicate_type.md) | [xsd:string](xsd:string) | 0..1 | The type (IRI or Literal) of an edge's subject  | . |
| [object_type](object_type.md) | [xsd:string](xsd:string) | 0..1 | The type (IRI or Literal) of an object  | . |
| [about_edge](about_edge.md) | [Edge](Edge.md) | 0..1 | None  | . |
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
| [has_undo](has_undo.md) | [Deletion](Deletion.md) | 0..1 | A change that reverses this change  | . |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/kgcl







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['kgcl:MappingCreation'] |
| native | ['kgcl:MappingCreation'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: mapping creation
description: A specific kind of edge creation in which the created edge is a mapping.
todos:
- decide whether to make a corresponding change to the datamodel
from_schema: https://w3id.org/kgcl
aliases:
- xref creation
is_a: edge creation
mixins:
- creation
slots:
- subject
- predicate
- object
- annotation set
slot_usage:
  change description:
    name: change description
    string_serialization: creating mapping {edge}
  subject:
    name: subject
    description: This corresponds to subject_id in SSSOM
  predicate:
    name: predicate
    description: This corresponds to predicate_id in SSSOM. The value of this is typically
      a predicate from SKOS
  object:
    name: object
    description: This corresponds to object_id in SSSOM

```
</details>

### Induced

<details>
```yaml
name: mapping creation
description: A specific kind of edge creation in which the created edge is a mapping.
todos:
- decide whether to make a corresponding change to the datamodel
from_schema: https://w3id.org/kgcl
aliases:
- xref creation
is_a: edge creation
mixins:
- creation
slot_usage:
  change description:
    name: change description
    string_serialization: creating mapping {edge}
  subject:
    name: subject
    description: This corresponds to subject_id in SSSOM
  predicate:
    name: predicate
    description: This corresponds to predicate_id in SSSOM. The value of this is typically
      a predicate from SKOS
  object:
    name: object
    description: This corresponds to object_id in SSSOM
attributes:
  subject:
    name: subject
    description: This corresponds to subject_id in SSSOM
    from_schema: https://w3id.org/kgcl/ontology
    alias: subject
    owner: mapping creation
    range: node
  predicate:
    name: predicate
    description: This corresponds to predicate_id in SSSOM. The value of this is typically
      a predicate from SKOS
    from_schema: https://w3id.org/kgcl/ontology
    alias: predicate
    owner: mapping creation
    range: node
  object:
    name: object
    description: This corresponds to object_id in SSSOM
    from_schema: https://w3id.org/kgcl/ontology
    alias: object
    owner: mapping creation
    range: node
  annotation set:
    name: annotation set
    from_schema: https://w3id.org/kgcl/ontology
    alias: annotation_set
    owner: mapping creation
    range: annotation
  subject type:
    name: subject type
    description: The type (IRI or Literal) of an edge's subject
    from_schema: https://w3id.org/kgcl
    alias: subject_type
    owner: mapping creation
    range: string
  predicate type:
    name: predicate type
    description: The type (IRI or Literal) of an edge's subject
    from_schema: https://w3id.org/kgcl
    alias: predicate_type
    owner: mapping creation
    range: string
  object type:
    name: object type
    description: The type (IRI or Literal) of an object
    from_schema: https://w3id.org/kgcl
    alias: object_type
    owner: mapping creation
    range: string
  about edge:
    name: about edge
    from_schema: https://w3id.org/kgcl
    is_a: about
    multivalued: false
    alias: about_edge
    owner: mapping creation
    range: edge
  language:
    name: language
    description: The language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: language
    owner: mapping creation
    range: language tag
  datatype:
    name: datatype
    description: The datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: datatype
    owner: mapping creation
    range: string
  old value:
    name: old value
    description: The value of a property held in the old instance of the ontology
    from_schema: https://w3id.org/kgcl
    alias: old_value
    owner: mapping creation
    range: string
  new value:
    name: new value
    description: The value of a property held in the new instance of the ontology
    from_schema: https://w3id.org/kgcl
    alias: new_value
    owner: mapping creation
    range: string
  old value type:
    name: old value type
    description: The type (IRI or Literal) of an old value
    from_schema: https://w3id.org/kgcl
    alias: old_value_type
    owner: mapping creation
    range: string
  new value type:
    name: new value type
    description: The type (IRI or Literal) of a new value
    from_schema: https://w3id.org/kgcl
    alias: new_value_type
    owner: mapping creation
    range: string
  new language:
    name: new language
    description: The new language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: new_language
    owner: mapping creation
    range: string
  old language:
    name: old language
    description: The old language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: old_language
    owner: mapping creation
    range: string
  new datatype:
    name: new datatype
    description: The new datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: new_datatype
    owner: mapping creation
    range: string
  old datatype:
    name: old datatype
    description: The old datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: old_datatype
    owner: mapping creation
    range: string
  id:
    name: id
    from_schema: https://w3id.org/kgcl/basics
    identifier: true
    alias: id
    owner: mapping creation
    range: string
  was generated by:
    name: was generated by
    from_schema: https://w3id.org/kgcl/prov
    slot_uri: prov:wasGeneratedBy
    alias: was_generated_by
    owner: mapping creation
    range: activity
  see also:
    name: see also
    from_schema: https://w3id.org/kgcl
    slot_uri: rdfs:seeAlso
    alias: see_also
    owner: mapping creation
    range: string
  pull request:
    name: pull request
    from_schema: https://w3id.org/kgcl
    alias: pull_request
    owner: mapping creation
    range: string
  creator:
    name: creator
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: creator
    owner: mapping creation
    range: string
  change date:
    name: change date
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:date
    alias: change_date
    owner: mapping creation
    range: string
  contributor:
    name: contributor
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: contributor
    owner: mapping creation
    range: string
  has undo:
    name: has undo
    description: A change that reverses this change
    from_schema: https://w3id.org/kgcl
    domain: change
    multivalued: false
    alias: has_undo
    owner: mapping creation
    range: deletion

```
</details>