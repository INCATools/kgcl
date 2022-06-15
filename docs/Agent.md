# Class: Agent
_a provence-generating agent_





URI: [prov:Agent](http://www.w3.org/ns/prov#Agent)




```mermaid
 classDiagram
    class Agent
      Agent : acted_on_behalf_of
      Agent : id
      Agent : was_informed_by
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [id](id.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [acted_on_behalf_of](acted_on_behalf_of.md) | [Agent](Agent.md) | 0..1 | None  | . |
| [was_informed_by](was_informed_by.md) | [Activity](Activity.md) | 0..1 | None  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Activity](Activity.md) | [was_associated_with](was_associated_with.md) | range | agent |
| [Agent](Agent.md) | [acted_on_behalf_of](acted_on_behalf_of.md) | range | agent |



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/kgcl/prov







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['prov:Agent'] |
| native | ['prov:Agent'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: agent
description: a provence-generating agent
from_schema: https://w3id.org/kgcl/prov
slots:
- id
- acted on behalf of
- was informed by
class_uri: prov:Agent

```
</details>

### Induced

<details>
```yaml
name: agent
description: a provence-generating agent
from_schema: https://w3id.org/kgcl/prov
attributes:
  id:
    name: id
    from_schema: https://w3id.org/kgcl/basics
    identifier: true
    alias: id
    owner: agent
    range: string
  acted on behalf of:
    name: acted on behalf of
    from_schema: https://w3id.org/kgcl/prov
    slot_uri: prov:actedOnBehalfOf
    alias: acted_on_behalf_of
    owner: agent
    range: agent
  was informed by:
    name: was informed by
    from_schema: https://w3id.org/kgcl/prov
    slot_uri: prov:wasInformedBy
    alias: was_informed_by
    owner: agent
    range: activity
class_uri: prov:Agent

```
</details>