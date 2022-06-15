# Class: EdgeObsoletion
_An edge change in which an edge is obsoleted._





URI: [kgcl:EdgeObsoletion](http://w3id.org/kgcl/EdgeObsoletion)




```mermaid
 classDiagram
      Obsoletion <|-- EdgeObsoletion
      EdgeChange <|-- EdgeObsoletion
      
      EdgeObsoletion : about_edge
      EdgeObsoletion : annotation_set
      EdgeObsoletion : change_date
      EdgeObsoletion : contributor
      EdgeObsoletion : creator
      EdgeObsoletion : datatype
      EdgeObsoletion : has_undo
      EdgeObsoletion : id
      EdgeObsoletion : language
      EdgeObsoletion : new_datatype
      EdgeObsoletion : new_language
      EdgeObsoletion : new_value
      EdgeObsoletion : new_value_type
      EdgeObsoletion : object
      EdgeObsoletion : object_type
      EdgeObsoletion : old_datatype
      EdgeObsoletion : old_language
      EdgeObsoletion : old_value
      EdgeObsoletion : old_value_type
      EdgeObsoletion : predicate
      EdgeObsoletion : pull_request
      EdgeObsoletion : see_also
      EdgeObsoletion : subject
      EdgeObsoletion : was_generated_by
      

```





## Inheritance
* [Change](Change.md)
    * [SimpleChange](SimpleChange.md)
        * [EdgeChange](EdgeChange.md)
            * **EdgeObsoletion** [ obsoletion]



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [subject](subject.md) | [Node](Node.md) | 0..1 | None  | . |
| [predicate](predicate.md) | [Node](Node.md) | 0..1 | None  | . |
| [object](object.md) | [Node](Node.md) | 0..1 | None  | . |
| [annotation_set](annotation_set.md) | [Annotation](Annotation.md) | 0..1 | None  | . |
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
| [has_undo](has_undo.md) | [Obsoletion](Obsoletion.md) | 0..1 | A change that reverses this change  | . |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/kgcl







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['kgcl:EdgeObsoletion'] |
| native | ['kgcl:EdgeObsoletion'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: edge obsoletion
description: An edge change in which an edge is obsoleted.
comments:
- Note there is not yet consensus in how this should be done in rdf/owl implementations.
  Simply marking the edge deprecated with render it visible to most clients. Care
  must be taken because simply adding a deprecation tag to an axiom does not silence
  it -- it is still asserted. It is therefore more common to obsolete an edge by shadowing
  the axiom as an annotation. See the Mondo docs for example
from_schema: https://w3id.org/kgcl
see_also:
- https://mondo.readthedocs.io/en/latest/editors-guide/g-logical-axioms/#excluded-subclassof
aliases:
- relationship obsoletion
is_a: edge change
mixins:
- obsoletion
slots:
- subject
- predicate
- object
- annotation set
slot_usage:
  change description:
    name: change description
    string_serialization: obsoleting edge {edge}

```
</details>

### Induced

<details>
```yaml
name: edge obsoletion
description: An edge change in which an edge is obsoleted.
comments:
- Note there is not yet consensus in how this should be done in rdf/owl implementations.
  Simply marking the edge deprecated with render it visible to most clients. Care
  must be taken because simply adding a deprecation tag to an axiom does not silence
  it -- it is still asserted. It is therefore more common to obsolete an edge by shadowing
  the axiom as an annotation. See the Mondo docs for example
from_schema: https://w3id.org/kgcl
see_also:
- https://mondo.readthedocs.io/en/latest/editors-guide/g-logical-axioms/#excluded-subclassof
aliases:
- relationship obsoletion
is_a: edge change
mixins:
- obsoletion
slot_usage:
  change description:
    name: change description
    string_serialization: obsoleting edge {edge}
attributes:
  subject:
    name: subject
    from_schema: https://w3id.org/kgcl/ontology
    alias: subject
    owner: edge obsoletion
    range: node
  predicate:
    name: predicate
    from_schema: https://w3id.org/kgcl/ontology
    alias: predicate
    owner: edge obsoletion
    range: node
  object:
    name: object
    from_schema: https://w3id.org/kgcl/ontology
    alias: object
    owner: edge obsoletion
    range: node
  annotation set:
    name: annotation set
    from_schema: https://w3id.org/kgcl/ontology
    alias: annotation_set
    owner: edge obsoletion
    range: annotation
  about edge:
    name: about edge
    from_schema: https://w3id.org/kgcl
    is_a: about
    multivalued: false
    alias: about_edge
    owner: edge obsoletion
    range: edge
  object type:
    name: object type
    description: The type (IRI or Literal) of an object
    from_schema: https://w3id.org/kgcl
    alias: object_type
    owner: edge obsoletion
    range: string
  language:
    name: language
    description: The language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: language
    owner: edge obsoletion
    range: language tag
  datatype:
    name: datatype
    description: The datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: datatype
    owner: edge obsoletion
    range: string
  old value:
    name: old value
    description: The value of a property held in the old instance of the ontology
    from_schema: https://w3id.org/kgcl
    alias: old_value
    owner: edge obsoletion
    range: string
  new value:
    name: new value
    description: The value of a property held in the new instance of the ontology
    from_schema: https://w3id.org/kgcl
    alias: new_value
    owner: edge obsoletion
    range: string
  old value type:
    name: old value type
    description: The type (IRI or Literal) of an old value
    from_schema: https://w3id.org/kgcl
    alias: old_value_type
    owner: edge obsoletion
    range: string
  new value type:
    name: new value type
    description: The type (IRI or Literal) of a new value
    from_schema: https://w3id.org/kgcl
    alias: new_value_type
    owner: edge obsoletion
    range: string
  new language:
    name: new language
    description: The new language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: new_language
    owner: edge obsoletion
    range: string
  old language:
    name: old language
    description: The old language tag of a literal
    from_schema: https://w3id.org/kgcl
    alias: old_language
    owner: edge obsoletion
    range: string
  new datatype:
    name: new datatype
    description: The new datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: new_datatype
    owner: edge obsoletion
    range: string
  old datatype:
    name: old datatype
    description: The old datatype of a literal
    from_schema: https://w3id.org/kgcl
    alias: old_datatype
    owner: edge obsoletion
    range: string
  id:
    name: id
    from_schema: https://w3id.org/kgcl/basics
    identifier: true
    alias: id
    owner: edge obsoletion
    range: string
  was generated by:
    name: was generated by
    from_schema: https://w3id.org/kgcl/prov
    slot_uri: prov:wasGeneratedBy
    alias: was_generated_by
    owner: edge obsoletion
    range: activity
  see also:
    name: see also
    from_schema: https://w3id.org/kgcl
    slot_uri: rdfs:seeAlso
    alias: see_also
    owner: edge obsoletion
    range: string
  pull request:
    name: pull request
    from_schema: https://w3id.org/kgcl
    alias: pull_request
    owner: edge obsoletion
    range: string
  creator:
    name: creator
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: creator
    owner: edge obsoletion
    range: string
  change date:
    name: change date
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:date
    alias: change_date
    owner: edge obsoletion
    range: string
  contributor:
    name: contributor
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: contributor
    owner: edge obsoletion
    range: string
  has undo:
    name: has undo
    description: A change that reverses this change
    from_schema: https://w3id.org/kgcl
    domain: change
    multivalued: false
    alias: has_undo
    owner: edge obsoletion
    range: obsoletion

```
</details>