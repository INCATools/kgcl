# Class: PropertyValue
_a property-value pair_





URI: [om:PropertyValue](om:PropertyValue)




```mermaid
 classDiagram
      OntologyElement <|-- PropertyValue
      
      PropertyValue : filler
      PropertyValue : property
      

```





## Inheritance
* [OntologyElement](OntologyElement.md)
    * **PropertyValue**
        * [Annotation](Annotation.md)



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [property](property.md) | [Node](Node.md) | 0..1 | None  | . |
| [filler](filler.md) | [xsd:string](xsd:string) | 0..1 | None  | . |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/kgcl/ontology







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['om:PropertyValue'] |
| native | ['om:PropertyValue'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: property value
description: a property-value pair
from_schema: https://w3id.org/kgcl/ontology
is_a: ontology element
slots:
- property
- filler

```
</details>

### Induced

<details>
```yaml
name: property value
description: a property-value pair
from_schema: https://w3id.org/kgcl/ontology
is_a: ontology element
attributes:
  property:
    name: property
    from_schema: https://w3id.org/kgcl/ontology
    alias: property
    owner: property value
    range: node
  filler:
    name: filler
    from_schema: https://w3id.org/kgcl/ontology
    alias: filler
    owner: property value
    range: string

```
</details>