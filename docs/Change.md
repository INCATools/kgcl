# Class: Change
_Any change perform on an ontology or knowledge graph_



* __NOTE__: this is an abstract class and should not be instantiated directly



URI: [kgcl:Change](http://w3id.org/kgcl/Change)




```mermaid
 classDiagram
      Change <|-- SimpleChange
      Change <|-- ComplexChange
      Change <|-- Transaction
      
      Change : change_date
      Change : contributor
      Change : creator
      Change : has_undo
      Change : id
      Change : pull_request
      Change : see_also
      Change : was_generated_by
      
```





## Inheritance
* **Change**
    * [SimpleChange](SimpleChange.md)
    * [ComplexChange](ComplexChange.md)
    * [Transaction](Transaction.md)



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [id](id.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [was_generated_by](was_generated_by.md) | [Activity](Activity.md) | 0..1 | None  | . |
| [see_also](see_also.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [pull_request](pull_request.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [creator](creator.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [change_date](change_date.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [contributor](contributor.md) | [xsd:string](xsd:string) | 0..1 | None  | . |
| [has_undo](has_undo.md) | [Change](Change.md) | 0..1 | A change that reverses this change  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Change](Change.md) | [has_undo](has_undo.md) | domain | change |
| [Change](Change.md) | [has_undo](has_undo.md) | range | change |
| [SimpleChange](SimpleChange.md) | [has_undo](has_undo.md) | domain | change |
| [SimpleChange](SimpleChange.md) | [has_undo](has_undo.md) | range | change |
| [ComplexChange](ComplexChange.md) | [change_set](change_set.md) | range | change |
| [ComplexChange](ComplexChange.md) | [has_undo](has_undo.md) | domain | change |
| [ComplexChange](ComplexChange.md) | [has_undo](has_undo.md) | range | change |
| [MultiNodeObsoletion](MultiNodeObsoletion.md) | [has_undo](has_undo.md) | domain | change |
| [MultiNodeObsoletion](MultiNodeObsoletion.md) | [has_undo](has_undo.md) | range | change |
| [Transaction](Transaction.md) | [change_set](change_set.md) | range | change |
| [Transaction](Transaction.md) | [has_undo](has_undo.md) | domain | change |
| [Transaction](Transaction.md) | [has_undo](has_undo.md) | range | change |
| [EdgeChange](EdgeChange.md) | [has_undo](has_undo.md) | domain | change |
| [EdgeChange](EdgeChange.md) | [has_undo](has_undo.md) | range | change |
| [EdgeCreation](EdgeCreation.md) | [has_undo](has_undo.md) | domain | change |
| [PlaceUnder](PlaceUnder.md) | [has_undo](has_undo.md) | domain | change |
| [EdgeDeletion](EdgeDeletion.md) | [has_undo](has_undo.md) | domain | change |
| [EdgeDeletion](EdgeDeletion.md) | [has_undo](has_undo.md) | range | change |
| [RemoveUnder](RemoveUnder.md) | [has_undo](has_undo.md) | domain | change |
| [RemoveUnder](RemoveUnder.md) | [has_undo](has_undo.md) | range | change |
| [EdgeObsoletion](EdgeObsoletion.md) | [has_undo](has_undo.md) | domain | change |
| [EdgeRewiring](EdgeRewiring.md) | [has_undo](has_undo.md) | domain | change |
| [EdgeRewiring](EdgeRewiring.md) | [has_undo](has_undo.md) | range | change |
| [MappingCreation](MappingCreation.md) | [has_undo](has_undo.md) | domain | change |
| [NodeMove](NodeMove.md) | [has_undo](has_undo.md) | domain | change |
| [NodeMove](NodeMove.md) | [has_undo](has_undo.md) | range | change |
| [NodeDeepening](NodeDeepening.md) | [has_undo](has_undo.md) | domain | change |
| [NodeDeepening](NodeDeepening.md) | [has_undo](has_undo.md) | range | change |
| [NodeShallowing](NodeShallowing.md) | [has_undo](has_undo.md) | domain | change |
| [NodeShallowing](NodeShallowing.md) | [has_undo](has_undo.md) | range | change |
| [PredicateChange](PredicateChange.md) | [has_undo](has_undo.md) | domain | change |
| [PredicateChange](PredicateChange.md) | [has_undo](has_undo.md) | range | change |
| [EdgeLogicalInterpretationChange](EdgeLogicalInterpretationChange.md) | [has_undo](has_undo.md) | domain | change |
| [EdgeLogicalInterpretationChange](EdgeLogicalInterpretationChange.md) | [has_undo](has_undo.md) | range | change |
| [LogicalAxiomChange](LogicalAxiomChange.md) | [has_undo](has_undo.md) | domain | change |
| [LogicalAxiomChange](LogicalAxiomChange.md) | [has_undo](has_undo.md) | range | change |
| [NodeChange](NodeChange.md) | [has_undo](has_undo.md) | domain | change |
| [NodeChange](NodeChange.md) | [has_undo](has_undo.md) | range | change |
| [NodeRename](NodeRename.md) | [has_textual_diff](has_textual_diff.md) | domain | change |
| [NodeRename](NodeRename.md) | [has_undo](has_undo.md) | domain | change |
| [NodeRename](NodeRename.md) | [has_undo](has_undo.md) | range | change |
| [SetLanguageForName](SetLanguageForName.md) | [has_undo](has_undo.md) | domain | change |
| [SetLanguageForName](SetLanguageForName.md) | [has_undo](has_undo.md) | range | change |
| [NodeAnnotationChange](NodeAnnotationChange.md) | [has_undo](has_undo.md) | domain | change |
| [NodeAnnotationChange](NodeAnnotationChange.md) | [has_undo](has_undo.md) | range | change |
| [NodeAnnotationReplacement](NodeAnnotationReplacement.md) | [has_undo](has_undo.md) | domain | change |
| [NodeAnnotationReplacement](NodeAnnotationReplacement.md) | [has_undo](has_undo.md) | range | change |
| [NodeSynonymChange](NodeSynonymChange.md) | [has_undo](has_undo.md) | domain | change |
| [NodeSynonymChange](NodeSynonymChange.md) | [has_undo](has_undo.md) | range | change |
| [NewSynonym](NewSynonym.md) | [has_undo](has_undo.md) | domain | change |
| [NewSynonym](NewSynonym.md) | [has_undo](has_undo.md) | range | change |
| [NameBecomesSynonym](NameBecomesSynonym.md) | [has_undo](has_undo.md) | domain | change |
| [NameBecomesSynonym](NameBecomesSynonym.md) | [has_undo](has_undo.md) | range | change |
| [RemoveSynonym](RemoveSynonym.md) | [has_undo](has_undo.md) | domain | change |
| [RemoveSynonym](RemoveSynonym.md) | [has_undo](has_undo.md) | range | change |
| [SynonymReplacement](SynonymReplacement.md) | [has_textual_diff](has_textual_diff.md) | domain | change |
| [SynonymReplacement](SynonymReplacement.md) | [has_undo](has_undo.md) | domain | change |
| [SynonymReplacement](SynonymReplacement.md) | [has_undo](has_undo.md) | range | change |
| [SynonymPredicateChange](SynonymPredicateChange.md) | [has_textual_diff](has_textual_diff.md) | domain | change |
| [SynonymPredicateChange](SynonymPredicateChange.md) | [has_undo](has_undo.md) | domain | change |
| [SynonymPredicateChange](SynonymPredicateChange.md) | [has_undo](has_undo.md) | range | change |
| [NodeTextDefinitionChange](NodeTextDefinitionChange.md) | [has_undo](has_undo.md) | domain | change |
| [NodeTextDefinitionChange](NodeTextDefinitionChange.md) | [has_undo](has_undo.md) | range | change |
| [NewTextDefinition](NewTextDefinition.md) | [has_undo](has_undo.md) | domain | change |
| [NewTextDefinition](NewTextDefinition.md) | [has_undo](has_undo.md) | range | change |
| [RemoveTextDefinition](RemoveTextDefinition.md) | [has_undo](has_undo.md) | domain | change |
| [RemoveTextDefinition](RemoveTextDefinition.md) | [has_undo](has_undo.md) | range | change |
| [TextDefinitionReplacement](TextDefinitionReplacement.md) | [has_textual_diff](has_textual_diff.md) | domain | change |
| [TextDefinitionReplacement](TextDefinitionReplacement.md) | [has_undo](has_undo.md) | domain | change |
| [TextDefinitionReplacement](TextDefinitionReplacement.md) | [has_undo](has_undo.md) | range | change |
| [AddNodeToSubset](AddNodeToSubset.md) | [has_undo](has_undo.md) | domain | change |
| [AddNodeToSubset](AddNodeToSubset.md) | [has_undo](has_undo.md) | range | change |
| [RemovedNodeFromSubset](RemovedNodeFromSubset.md) | [has_undo](has_undo.md) | domain | change |
| [NodeObsoletion](NodeObsoletion.md) | [has_undo](has_undo.md) | domain | change |
| [NodeUnobsoletion](NodeUnobsoletion.md) | [has_undo](has_undo.md) | domain | change |
| [NodeCreation](NodeCreation.md) | [has_undo](has_undo.md) | domain | change |
| [ClassCreation](ClassCreation.md) | [has_undo](has_undo.md) | domain | change |
| [NodeDeletion](NodeDeletion.md) | [has_undo](has_undo.md) | domain | change |
| [NodeDeletion](NodeDeletion.md) | [has_undo](has_undo.md) | range | change |
| [NodeDirectMerge](NodeDirectMerge.md) | [has_undo](has_undo.md) | domain | change |
| [NodeObsoletionWithDirectReplacement](NodeObsoletionWithDirectReplacement.md) | [has_undo](has_undo.md) | domain | change |
| [NodeObsoletionWithNoDirectReplacement](NodeObsoletionWithNoDirectReplacement.md) | [has_undo](has_undo.md) | domain | change |
| [Session](Session.md) | [change_set](change_set.md) | range | change |



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/kgcl







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['kgcl:Change'] |
| native | ['kgcl:Change'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: change
description: Any change perform on an ontology or knowledge graph
from_schema: https://w3id.org/kgcl
abstract: true
slots:
- id
- was generated by
- see also
- pull request
- creator
- change date
- contributor
- has undo
slot_usage:
  was generated by:
    name: was generated by
    comments:
    - we use the PROV model to represent the agent making a change
  see also:
    name: see also
    comments:
    - If this change is in relationship to an issue on a system like github, include
      the URL here
  pull request:
    name: pull request
    comments:
    - If this change has a pull request on a system like github, include the URL here
  creator:
    name: creator
    comments:
    - This should be the composition of 'was generated by' and 'was associated with'
  change date:
    name: change date
    comments:
    - This should be the composition of 'was generated by' and 'ended at time'

```
</details>

### Induced

<details>
```yaml
name: change
description: Any change perform on an ontology or knowledge graph
from_schema: https://w3id.org/kgcl
abstract: true
slot_usage:
  was generated by:
    name: was generated by
    comments:
    - we use the PROV model to represent the agent making a change
  see also:
    name: see also
    comments:
    - If this change is in relationship to an issue on a system like github, include
      the URL here
  pull request:
    name: pull request
    comments:
    - If this change has a pull request on a system like github, include the URL here
  creator:
    name: creator
    comments:
    - This should be the composition of 'was generated by' and 'was associated with'
  change date:
    name: change date
    comments:
    - This should be the composition of 'was generated by' and 'ended at time'
attributes:
  id:
    name: id
    from_schema: https://w3id.org/kgcl/basics
    identifier: true
    alias: id
    owner: change
    range: string
  was generated by:
    name: was generated by
    comments:
    - we use the PROV model to represent the agent making a change
    from_schema: https://w3id.org/kgcl/prov
    slot_uri: prov:wasGeneratedBy
    alias: was_generated_by
    owner: change
    range: activity
  see also:
    name: see also
    comments:
    - If this change is in relationship to an issue on a system like github, include
      the URL here
    from_schema: https://w3id.org/kgcl
    slot_uri: rdfs:seeAlso
    alias: see_also
    owner: change
    range: string
  pull request:
    name: pull request
    comments:
    - If this change has a pull request on a system like github, include the URL here
    from_schema: https://w3id.org/kgcl
    alias: pull_request
    owner: change
    range: string
  creator:
    name: creator
    comments:
    - This should be the composition of 'was generated by' and 'was associated with'
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: creator
    owner: change
    range: string
  change date:
    name: change date
    comments:
    - This should be the composition of 'was generated by' and 'ended at time'
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:date
    alias: change_date
    owner: change
    range: string
  contributor:
    name: contributor
    from_schema: https://w3id.org/kgcl
    slot_uri: dcterms:creator
    alias: contributor
    owner: change
    range: string
  has undo:
    name: has undo
    description: A change that reverses this change
    from_schema: https://w3id.org/kgcl
    domain: change
    multivalued: false
    alias: has_undo
    owner: change
    range: change

```
</details>