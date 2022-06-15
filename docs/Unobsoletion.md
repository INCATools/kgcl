# Class: Unobsoletion
_Opposite operation of obsoletion. Rarely performed._




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [kgcl:Unobsoletion](http://w3id.org/kgcl/Unobsoletion)




```mermaid
 classDiagram
      ChangeMixin <|-- Unobsoletion
      
      

```





## Inheritance
* [ChangeMixin](ChangeMixin.md)
    * **Unobsoletion**



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/kgcl







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['kgcl:Unobsoletion'] |
| native | ['kgcl:Unobsoletion'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: unobsoletion
description: Opposite operation of obsoletion. Rarely performed.
from_schema: https://w3id.org/kgcl
see_also:
- http://wiki.geneontology.org/index.php/Restoring_an_Obsolete_Ontology_Term
is_a: change mixin
mixin: true
slot_usage:
  has undo:
    name: has undo
    range: obsoletion

```
</details>

### Induced

<details>
```yaml
name: unobsoletion
description: Opposite operation of obsoletion. Rarely performed.
from_schema: https://w3id.org/kgcl
see_also:
- http://wiki.geneontology.org/index.php/Restoring_an_Obsolete_Ontology_Term
is_a: change mixin
mixin: true
slot_usage:
  has undo:
    name: has undo
    range: obsoletion

```
</details>