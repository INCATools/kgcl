# Class: AddToSubset
_placing an element inside a subset_




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [kgcl:AddToSubset](http://w3id.org/kgcl/AddToSubset)




```mermaid
 classDiagram
      SubsetMembershipChange <|-- AddToSubset
      
      AddToSubset : in_subset
      

```





## Inheritance
* [ChangeMixin](ChangeMixin.md)
    * [SubsetMembershipChange](SubsetMembershipChange.md)
        * **AddToSubset**



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [in_subset](in_subset.md) | [OntologySubset](OntologySubset.md) | 0..1 | subset that the element is being placed inside.  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [RemovedNodeFromSubset](RemovedNodeFromSubset.md) | [has_undo](has_undo.md) | range | add to subset |



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/kgcl







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['kgcl:AddToSubset'] |
| native | ['kgcl:AddToSubset'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: add to subset
description: placing an element inside a subset
from_schema: https://w3id.org/kgcl
is_a: subset membership change
mixin: true
slot_usage:
  in subset:
    name: in subset
    description: subset that the element is being placed inside.

```
</details>

### Induced

<details>
```yaml
name: add to subset
description: placing an element inside a subset
from_schema: https://w3id.org/kgcl
is_a: subset membership change
mixin: true
slot_usage:
  in subset:
    name: in subset
    description: subset that the element is being placed inside.
attributes:
  in subset:
    name: in subset
    description: subset that the element is being placed inside.
    from_schema: https://w3id.org/kgcl
    alias: in_subset
    owner: add to subset
    range: ontology subset

```
</details>