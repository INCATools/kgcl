# Class: Configuration
_The meaning of operations can be configured_





URI: [kgcl:Configuration](http://w3id.org/kgcl/Configuration)




```mermaid
 classDiagram
    class Configuration
      Configuration : contributor_predicate
      Configuration : creator_predicate
      Configuration : definition_predicate
      Configuration : main_synonym_predicate
      Configuration : name_predicate
      Configuration : obsoletion_policy
      Configuration : obsoletion_workflow
      Configuration : synonym_predicates
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [name_predicate](name_predicate.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [definition_predicate](definition_predicate.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [main_synonym_predicate](main_synonym_predicate.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [synonym_predicates](synonym_predicates.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [creator_predicate](creator_predicate.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [contributor_predicate](contributor_predicate.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [obsoletion_workflow](obsoletion_workflow.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [obsoletion_policy](obsoletion_policy.md) | [xsd:string](xsd:string) | 0..1 | None  | . |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/kgcl







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['kgcl:Configuration'] |
| native | ['kgcl:Configuration'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: configuration
description: The meaning of operations can be configured
from_schema: https://w3id.org/kgcl
attributes:
  name predicate:
    name: name predicate
    from_schema: https://w3id.org/kgcl
  definition predicate:
    name: definition predicate
    from_schema: https://w3id.org/kgcl
  main synonym predicate:
    name: main synonym predicate
    from_schema: https://w3id.org/kgcl
  synonym predicates:
    name: synonym predicates
    from_schema: https://w3id.org/kgcl
  creator predicate:
    name: creator predicate
    from_schema: https://w3id.org/kgcl
  contributor predicate:
    name: contributor predicate
    from_schema: https://w3id.org/kgcl
  obsoletion workflow:
    name: obsoletion workflow
    from_schema: https://w3id.org/kgcl
  obsoletion policy:
    name: obsoletion policy
    from_schema: https://w3id.org/kgcl

```
</details>

### Induced

<details>
```yaml
name: configuration
description: The meaning of operations can be configured
from_schema: https://w3id.org/kgcl
attributes:
  name predicate:
    name: name predicate
    from_schema: https://w3id.org/kgcl
    alias: name_predicate
    owner: configuration
    range: string
  definition predicate:
    name: definition predicate
    from_schema: https://w3id.org/kgcl
    alias: definition_predicate
    owner: configuration
    range: string
  main synonym predicate:
    name: main synonym predicate
    from_schema: https://w3id.org/kgcl
    alias: main_synonym_predicate
    owner: configuration
    range: string
  synonym predicates:
    name: synonym predicates
    from_schema: https://w3id.org/kgcl
    alias: synonym_predicates
    owner: configuration
    range: string
  creator predicate:
    name: creator predicate
    from_schema: https://w3id.org/kgcl
    alias: creator_predicate
    owner: configuration
    range: string
  contributor predicate:
    name: contributor predicate
    from_schema: https://w3id.org/kgcl
    alias: contributor_predicate
    owner: configuration
    range: string
  obsoletion workflow:
    name: obsoletion workflow
    from_schema: https://w3id.org/kgcl
    alias: obsoletion_workflow
    owner: configuration
    range: string
  obsoletion policy:
    name: obsoletion policy
    from_schema: https://w3id.org/kgcl
    alias: obsoletion_policy
    owner: configuration
    range: string

```
</details>