# Knowledge Graph Change Language

A data model for describing change operations at a high level on an ontology or ontology-like artefact, such as a Knowledge Graph.

* [Browse Schema](https://cmungall.github.io/knowledge-graph-change-language/)
* [GitHub](https://github.com/cmungall/knowledge-graph-change-language)

URI: https://w3id.org/kgcl
Name: kgcl

## Classes

| Class | Description |
| --- | --- |
| [Activity](Activity.md) | a provence-generating activity |
| [AddNodeToSubset](AddNodeToSubset.md) | Places a node inside a subset, by annotating that node |
| [AddToSubset](AddToSubset.md) | placing an element inside a subset |
| [Agent](Agent.md) | a provence-generating agent |
| [AllowsAutomaticReplacementOfEdges](AllowsAutomaticReplacementOfEdges.md) | Applies to an obsoletion in which annotations or edges pointing at the obsoleted node can be automatically rewired to point to a target |
| [Annotation](Annotation.md) | owl annotations. Not to be confused with annotations sensu GO |
| [Change](Change.md) | Any change perform on an ontology or knowledge graph |
| [ChangeMixin](ChangeMixin.md) | root class for all change mixins |
| [ChangeSetSummaryStatistic](ChangeSetSummaryStatistic.md) | A summary statistic for a set of changes of the same type, grouped by zero or more node properties |
| [ClassCreation](ClassCreation.md) | A node creation where the owl type is 'class' |
| [ClassNode](ClassNode.md) | A node that is a class |
| [ComplexChange](ComplexChange.md) | A change that is is a composition of other changes |
| [Configuration](Configuration.md) | The meaning of operations can be configured |
| [Creation](Creation.md) | Creation of an element. |
| [DatatypeChange](DatatypeChange.md) | None |
| [DatatypeOrLanguageTagChange](DatatypeOrLanguageTagChange.md) | A change in a value assertion where the value remain unchanged but either the datatype or language changes |
| [Deletion](Deletion.md) | Removal of an element. |
| [Edge](Edge.md) | A relationship between two nodes.
Currently the only kinds of edges supported in KGCL:

  * A subClassOf B <==> Edge(subject=A, predicate=owl:subClassOf, object=B)
  * A subClassOf P some B <==> Edge(subject=A, predicate=P, object=B)
  * P subPropertyOf Q <==> Edge(subject=P, predicate=owl:subPropertyOf, object=Q)

These represent the most common kind of pairwise relationship between classes, and classes are the dominant node type in ontologies.
  
In future a wider variety of OWL axiom types will be supportedn through the use of an additional edge property/slot to indicate the interpretation of the axiom, following owlstar (https://github.com/cmungall/owlstar).
For example:
 * `A subClassOf R only B <==> Edge(subject=A, predicate=P, object=B, interpretation=AllOnly)`
 * `A Annotation(P,B) <==> Edge(subject=A, predicate=P, object=B, interpretation=annotationAssertion)`

Note that not all axioms are intended to map to edges. Axioms/triples where the object is a literal would be represented as node properties. Complex OWL axioms involving nesting would have their own dedicated construct, or may be represented generically. These are out of scope for the current version of KGCL |
| [EdgeChange](EdgeChange.md) | A change in which the element that is the focus of the change is an edge. |
| [EdgeCreation](EdgeCreation.md) | An edge change in which a de-novo edge is created. The edge is potentially annotated in the same action. |
| [EdgeDeletion](EdgeDeletion.md) | An edge change in which an edge is removed. All edge annotations/properies are removed in the same action. |
| [EdgeLogicalInterpretationChange](EdgeLogicalInterpretationChange.md) | An edge change where the subjet, object, and predicate are unchanged, but the logical interpretation changes |
| [EdgeObsoletion](EdgeObsoletion.md) | An edge change in which an edge is obsoleted. |
| [EdgeRewiring](EdgeRewiring.md) | An edge change where one node is replaced with another, as in the case of obsoletion with replacement |
| [InstanceNode](InstanceNode.md) | A node that is an individual |
| [LanguageTagChange](LanguageTagChange.md) | None |
| [LogicalAxiomChange](LogicalAxiomChange.md) | A simple change where a logical axiom is changed, where the logical axiom cannot be represented as an edge

   |
| [LogicalDefinition](LogicalDefinition.md) | None |
| [MappingCreation](MappingCreation.md) | A specific kind of edge creation in which the created edge is a mapping. |
| [MultiNodeObsoletion](MultiNodeObsoletion.md) | A complex change consisting of multiple obsoletions. |
| [NameBecomesSynonym](NameBecomesSynonym.md) | A node synonym where the name NAME of an node NODE moves to a synonym, and NODE receives a new name. This change consists of compose of (1) a node rename where NAME is replaced by a different name (2) a new synonym |
| [NewSynonym](NewSynonym.md) | A node synonym change where a de-novo synonym is created |
| [NewTextDefinition](NewTextDefinition.md) | A node change where a de-novo text definition is created |
| [Node](Node.md) | Any named entity in an ontology. May be a class, individual, property |
| [NodeAnnotationChange](NodeAnnotationChange.md) | A node change where the change alters node properties/annotations. TODO |
| [NodeAnnotationReplacement](NodeAnnotationReplacement.md) | A node annotation change where the change replaces a particular property value. TODO |
| [NodeChange](NodeChange.md) | A simple change where the change is about a node |
| [NodeCreation](NodeCreation.md) | a node change in which a new node is created |
| [NodeDeepening](NodeDeepening.md) | A node move in which a node where the destination is a proper descendant of the original location. Note that here descendant applied not just to subclass, but edges of any predicate in the relational graph |
| [NodeDeletion](NodeDeletion.md) | Deletion of a node from the graph. Note it is recommended nodes are obsoleted and never merged, but this operation exists to represent deletions in ontologies, accidental or otherwise |
| [NodeDirectMerge](NodeDirectMerge.md) | An obsoletion change in which all metadata (including name/label) from the source node is deleted and added to the target node, and edges can automatically be rewired to point to the target node |
| [NodeMove](NodeMove.md) | A node move is a combination of deleting a parent edge and adding a parent edge, where the predicate is preserved and the object/parent node changes |
| [NodeObsoletion](NodeObsoletion.md) | Obsoletion of a node deprecates usage of that node, but does not delete it. |
| [NodeObsoletionWithDirectReplacement](NodeObsoletionWithDirectReplacement.md) | An obsoletion change in which information from the obsoleted node is selectively copied to a single target, and edges can automatically be rewired to point to the target node |
| [NodeObsoletionWithNoDirectReplacement](NodeObsoletionWithNoDirectReplacement.md) | An obsoletion change in which there is no direct replacement |
| [NodeRename](NodeRename.md) | A node change where the name (aka rdfs:label) of the node changes |
| [NodeShallowing](NodeShallowing.md) | The opposite of node deepening |
| [NodeSynonymChange](NodeSynonymChange.md) | None |
| [NodeTextDefinitionChange](NodeTextDefinitionChange.md) | A node change where the text definition is changed |
| [NodeUnobsoletion](NodeUnobsoletion.md) | unobsoletion of a node deprecates usage of that node. Rarely applied. |
| [Obsoletion](Obsoletion.md) | Obsoletion of an element deprecates usage of that element, but does not delete that element. |
| [OntologyElement](OntologyElement.md) | Any component of an ontology or knowledge graph |
| [OntologySubset](OntologySubset.md) | None |
| [PlaceUnder](PlaceUnder.md) | An edge creation where the predicate is owl:subClassOf |
| [PredicateChange](PredicateChange.md) | An edge change where the predicate (relationship type) is modified. |
| [PropertyValue](PropertyValue.md) | a property-value pair |
| [RemoveFromSubset](RemoveFromSubset.md) | removing an element from a subset |
| [RemoveSynonym](RemoveSynonym.md) | A node synonym change where a synonym is deleted |
| [RemoveTextDefinition](RemoveTextDefinition.md) | A node change where a text definition is deleted |
| [RemoveUnder](RemoveUnder.md) | An edge deletion where the predicate is owl:subClassOf
   |
| [RemovedNodeFromSubset](RemovedNodeFromSubset.md) | Removes a node from a subset, by removing an annotation |
| [Session](Session.md) | A session consists of a set of change sets bundled with the activities that generated those change sets |
| [SetLanguageForName](SetLanguageForName.md) | A node change where the string value for the name is unchanged but the language tag is set |
| [SimpleChange](SimpleChange.md) | A change that is about a single ontology element |
| [SubsetMembershipChange](SubsetMembershipChange.md) | A change in the membership status of a node with respect to a subset (view) |
| [SynonymPredicateChange](SynonymPredicateChange.md) | A node synonym change where the predicate of a synonym is changed. Background: synonyms can be represented by a variety of predicates. For example, many OBO ontologies make use of predicates such as oio:hasExactSynonym, oio:hasRelatedSynonym, etc |
| [SynonymReplacement](SynonymReplacement.md) | A node synonym change where the text of a synonym is changed |
| [TextDefinitionReplacement](TextDefinitionReplacement.md) | A node change where a text definition is modified |
| [TextualDiff](TextualDiff.md) | A summarizing of a change on a piece of text. This could be rendered in a number of different ways |
| [Transaction](Transaction.md) | A change that is a composition of a set of changes, where those changes are treated as a single unit. Could be a single change, or the results of an ontology diff |
| [Unobsoletion](Unobsoletion.md) | Opposite operation of obsoletion. Rarely performed. |


## Slots

| Slot | Description |
| --- | --- |
| [about](about.md) | The 'focus' entity on which the change operates |
| [about_edge](about_edge.md) | None |
| [about_node](about_node.md) | None |
| [about_node_representation](about_node_representation.md) | The representation of a node (URI, CURIE, label)  |
| [acted_on_behalf_of](acted_on_behalf_of.md) | None |
| [activity_set](activity_set.md) | None |
| [agent_set](agent_set.md) | None |
| [annotation_property](annotation_property.md) | An annotation property |
| [annotation_property_type](annotation_property_type.md) | The type of a property (URI, CURIE, label)  |
| [annotation_set](annotation_set.md) | None |
| [change_date](change_date.md) | None |
| [change_description](change_description.md) | A string serialization of the change. This should be both human-readable, and parseable. |
| [change_set](change_set.md) | A collection of changes |
| [contributor](contributor.md) | None |
| [contributor_predicate](contributor_predicate.md) | None |
| [creator](creator.md) | None |
| [creator_predicate](creator_predicate.md) | None |
| [datatype](datatype.md) | The datatype of a literal |
| [definition_predicate](definition_predicate.md) | None |
| [description](description.md) | None |
| [ended_at_time](ended_at_time.md) | None |
| [filler](filler.md) | None |
| [filler_type](filler_type.md) | None |
| [has_direct_replacement](has_direct_replacement.md) | An obsoletion replacement where it IS valid to automatically update annotations/edges pointing at the node with its direct replacement |
| [has_nondirect_replacement](has_nondirect_replacement.md) | An obsoletion replacement where it is NOT valid to automatically update annotations/edges pointing at the node with its direct replacement |
| [has_replacement](has_replacement.md) | A single node obsoletion event may be accompanied by one or more suggested replacement nodes |
| [has_textual_diff](has_textual_diff.md) | A representation of character-level changes on a textual literal property. For example, if a text definition may change by only a single character such as addition of a period, it is useful to be able to see this visually. |
| [has_undo](has_undo.md) | A change that reverses this change |
| [id](id.md) | None |
| [in_subset](in_subset.md) | The subset that pertains to this change |
| [language](language.md) | The language tag of a literal |
| [main_synonym_predicate](main_synonym_predicate.md) | None |
| [name](name.md) | None |
| [name_predicate](name_predicate.md) | None |
| [new_datatype](new_datatype.md) | The new datatype of a literal |
| [new_filler](new_filler.md) | The new filler of an OWL restriction |
| [new_language](new_language.md) | The new language tag of a literal |
| [new_object_type](new_object_type.md) | The type (IRI or Literal) of a new object |
| [new_property](new_property.md) | The new property of an OWL restriction |
| [new_subclass](new_subclass.md) | The new subclass of a subsumption axiom |
| [new_value](new_value.md) | The value of a property held in the new instance of the ontology |
| [new_value_type](new_value_type.md) | The type (IRI or Literal) of a new value |
| [node_id](node_id.md) | id of a node to be created |
| [object](object.md) | None |
| [object_representation](object_representation.md) | None |
| [object_type](object_type.md) | The type (IRI or Literal) of an object |
| [obsoletion_policy](obsoletion_policy.md) | None |
| [obsoletion_workflow](obsoletion_workflow.md) | None |
| [old_datatype](old_datatype.md) | The old datatype of a literal |
| [old_language](old_language.md) | The old language tag of a literal |
| [old_object_type](old_object_type.md) | The type (IRI or Literal) of an old object |
| [old_value](old_value.md) | The value of a property held in the old instance of the ontology |
| [old_value_type](old_value_type.md) | The type (IRI or Literal) of an old value |
| [owl_type](owl_type.md) | None |
| [predicate](predicate.md) | None |
| [predicate_representation](predicate_representation.md) | None |
| [predicate_type](predicate_type.md) | The type (IRI or Literal) of an edge's subject |
| [property](property.md) | None |
| [property_type](property_type.md) | None |
| [property_value_set](property_value_set.md) | None |
| [pull_request](pull_request.md) | None |
| [qualifier](qualifier.md) | The qualifier of a change operation |
| [see_also](see_also.md) | None |
| [started_at_time](started_at_time.md) | None |
| [subclass](subclass.md) | The subclass of a subsumption axiom |
| [subclass_type](subclass_type.md) | The type of a subclass |
| [subject](subject.md) | None |
| [subject_representation](subject_representation.md) | None |
| [subject_type](subject_type.md) | The type (IRI or Literal) of an edge's subject |
| [superclass](superclass.md) | None |
| [superclass_type](superclass_type.md) | The type of a superclass |
| [synonym_predicates](synonym_predicates.md) | None |
| [target](target.md) | The secondary entity on which the change operates |
| [used](used.md) | None |
| [was_associated_with](was_associated_with.md) | None |
| [was_generated_by](was_generated_by.md) | None |
| [was_informed_by](was_informed_by.md) | None |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [OwlTypeEnum](OwlTypeEnum.md) | None |
| [SynonymScopeEnum](SynonymScopeEnum.md) | None |


## Subsets

| Subset | Description |
| --- | --- |
