# Class: ClassNode
_A node that is a class_





URI: [owl:Class](owl:Class)




```mermaid
 classDiagram
      Node <|-- ClassNode
      
      ClassNode : annotation_set
      ClassNode : id
      ClassNode : name
      ClassNode : owl_type
      

```





## Inheritance
* [OntologyElement](OntologyElement.md)
    * [Node](Node.md)
        * **ClassNode**



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [id](id.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [name](name.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [annotation_set](annotation_set.md) | [Annotation](Annotation.md) | 0..1 | None  | . |
| [owl_type](owl_type.md) | [OwlTypeEnum](OwlTypeEnum.md) | 0..1 | None  | . |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/kgcl/ontology







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['owl:Class'] |
| native | ['om:ClassNode'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: class node
description: A node that is a class
from_schema: https://w3id.org/kgcl/ontology
aliases:
- concept
is_a: node
class_uri: owl:Class

```
</details>

### Induced

<details>
```yaml
name: class node
description: A node that is a class
from_schema: https://w3id.org/kgcl/ontology
aliases:
- concept
is_a: node
attributes:
  id:
    name: id
    from_schema: https://w3id.org/kgcl/basics
    identifier: true
    alias: id
    owner: class node
    range: string
  name:
    name: name
    from_schema: https://w3id.org/kgcl/ontology
    alias: name
    owner: class node
    range: string
  annotation set:
    name: annotation set
    from_schema: https://w3id.org/kgcl/ontology
    alias: annotation_set
    owner: class node
    range: annotation
  owl type:
    name: owl type
    from_schema: https://w3id.org/kgcl/ontology
    alias: owl_type
    owner: class node
    range: owl_type_enum
class_uri: owl:Class

```
</details>