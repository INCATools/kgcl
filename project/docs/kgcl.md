
# kgcl_schema


**metamodel version:** 1.7.0

**version:** 0.0.1


A data model for describing change operations at a high level on an ontology or ontology-like artefact, such as a Knowledge Graph.
* [Browse Schema](https://cmungall.github.io/knowledge-graph-change-language/)
* [GitHub](https://github.com/cmungall/knowledge-graph-change-language)


### Classes

 * [ChangeLanguageElement](ChangeLanguageElement.md) - A broad grouping for all elements of the change language
     * [Change](Change.md) - Any change perform on an ontology or knowledge graph
         * [ComplexChange](ComplexChange.md) - A change that is is a composition of other changes
             * [MultiNodeObsoletion](MultiNodeObsoletion.md) - A complex change consisting of multiple obsoletions.
         * [SimpleChange](SimpleChange.md) - A change that is about a single ontology element
             * [EdgeChange](EdgeChange.md) - A change in which the element that is the focus of the change is an edge.
                 * [EdgeCreation](EdgeCreation.md) - An edge change in which a de-novo edge is created. The edge is potentially annotated in the same action.
                     * [MappingCreation](MappingCreation.md) - A specific kind of edge creation in which the created edge is a mapping.
                     * [PlaceUnder](PlaceUnder.md) - An edge creation where the predicate is owl:subClassOf
                 * [EdgeDeletion](EdgeDeletion.md) - An edge change in which an edge is removed. All edge annotations/properies are removed in the same action.
                     * [RemoveUnder](RemoveUnder.md) - An edge deletion where the predicate is owl:subClassOf
                 * [EdgeLogicalInterpretationChange](EdgeLogicalInterpretationChange.md) - An edge change where the subject, object, and predicate are unchanged, but the logical interpretation changes
                 * [EdgeObsoletion](EdgeObsoletion.md) - An edge change in which an edge is obsoleted.
                 * [EdgeRewiring](EdgeRewiring.md) - An edge change where one node is replaced with another, as in the case of obsoletion with replacement
                 * [NodeMove](NodeMove.md) - A node move is a combination of deleting a parent edge and adding a parent edge, where the predicate is preserved and the object/parent node changes
                     * [NodeDeepening](NodeDeepening.md) - A node move in which a node where the destination is a proper descendant of the original location. Note that here descendant applied not just to subclass, but edges of any predicate in the relational graph
                     * [NodeShallowing](NodeShallowing.md) - The opposite of node deepening
                 * [PredicateChange](PredicateChange.md) - An edge change where the predicate (relationship type) is modified.
             * [LogicalAxiomChange](LogicalAxiomChange.md) - A simple change where a logical axiom is changed, where the logical axiom cannot be represented as an edge
             * [NodeChange](NodeChange.md) - A simple change where the change is about a node
                 * [AddNodeToSubset](AddNodeToSubset.md) - Places a node inside a subset, by annotating that node
                 * [NodeAnnotationChange](NodeAnnotationChange.md) - A node change where the change alters node properties/annotations. TODO
                     * [NodeAnnotationReplacement](NodeAnnotationReplacement.md) - A node annotation change where the change replaces a particular property value. TODO
                 * [NodeCreation](NodeCreation.md) - a node change in which a new node is created
                     * [ClassCreation](ClassCreation.md) - A node creation where the owl type is 'owl:Class'
                     * [ObjectPropertyCreation](ObjectPropertyCreation.md) - A node creation where the owl type is 'ObjectProperty'
                 * [NodeDeletion](NodeDeletion.md) - Deletion of a node from the graph. Note it is recommended nodes are obsoleted and never merged, but this operation exists to represent deletions in ontologies, accidental or otherwise
                 * [NodeMappingChange](NodeMappingChange.md) - A node change where the mappings for that node are altered
                     * [MappingPredicateChange](MappingPredicateChange.md) - A node mapping change where the predicate of a mapping is changed.
                     * [MappingReplacement](MappingReplacement.md) - A node mapping change where the object of a mapping is changed
                     * [NewMapping](NewMapping.md) - A node mapping change where a mapping is added to a node
                     * [RemoveMapping](RemoveMapping.md) - A node mapping change where a mapping is deleted
                 * [NodeMetadataAssertionChange](NodeMetadataAssertionChange.md) - A node change where the metadata assertion (OWL annotations) for that node are altered
                     * [MetadataAssertionPredicateChange](MetadataAssertionPredicateChange.md) - A node metadata assertion change where the predicate of a metadata assertion is changed.
                     * [MetadataAssertionReplacement](MetadataAssertionReplacement.md) - A node metadata assertion change where the object of a metadata assertion is changed
                     * [NewMetadataAssertion](NewMetadataAssertion.md) - A node metadata assertion change where a metadata assertion is added to a node
                     * [RemoveMetadataAssertion](RemoveMetadataAssertion.md) - A node metadata assertion change where a metadata assertion is deleted
                 * [NodeObsoletion](NodeObsoletion.md) - Obsoletion of a node deprecates usage of that node, but does not delete it.
                     * [NodeDirectMerge](NodeDirectMerge.md) - An obsoletion change in which all metadata (including name/label) from the source node is deleted and added to the target node, and edges can automatically be rewired to point to the target node
                     * [NodeObsoletionWithDirectReplacement](NodeObsoletionWithDirectReplacement.md) - An obsoletion change in which information from the obsoleted node is selectively copied to a single target, and edges can automatically be rewired to point to the target node
                     * [NodeObsoletionWithNoDirectReplacement](NodeObsoletionWithNoDirectReplacement.md) - An obsoletion change in which there is no direct replacement
                 * [NodeRename](NodeRename.md) - A node change where the name (aka rdfs:label) of the node changes
                 * [NodeSynonymChange](NodeSynonymChange.md)
                     * [NameBecomesSynonym](NameBecomesSynonym.md) - A node synonym where the name NAME of an node NODE moves to a synonym, and NODE receives a new name. This change consists of compose of (1) a node rename where NAME is replaced by a different name (2) a new synonym
                     * [NewSynonym](NewSynonym.md) - A node synonym change where a de-novo synonym is created
                     * [RemoveSynonym](RemoveSynonym.md) - A node synonym change where a synonym is deleted
                     * [SynonymPredicateChange](SynonymPredicateChange.md) - A node synonym change where the predicate of a synonym is changed. Background: synonyms can be represented by a variety of predicates. For example, many OBO ontologies make use of predicates such as oio:hasExactSynonym, oio:hasRelatedSynonym, etc
                     * [SynonymReplacement](SynonymReplacement.md) - A node synonym change where the text of a synonym is changed
                 * [NodeTextDefinitionChange](NodeTextDefinitionChange.md) - A node change where the text definition is changed
                     * [NewTextDefinition](NewTextDefinition.md) - A node change where a de-novo text definition is created
                     * [RemoveTextDefinition](RemoveTextDefinition.md) - A node change where a text definition is deleted
                     * [TextDefinitionReplacement](TextDefinitionReplacement.md) - A node change where a text definition is modified
                 * [NodeUnobsoletion](NodeUnobsoletion.md) - unobsoletion of a node deprecates usage of that node. Rarely applied.
                 * [RemoveNodeFromSubset](RemoveNodeFromSubset.md) - Removes a node from a subset, by removing an annotation
                 * [SetLanguageForName](SetLanguageForName.md) - A node change where the string value for the name is unchanged but the language tag is set
         * [Transaction](Transaction.md) - A change that is a composition of a set of changes, where those changes are treated as a single unit. Could be a single change, or the results of an ontology diff
     * [ChangeSetSummaryStatistic](ChangeSetSummaryStatistic.md) - A summary statistic for a set of changes of the same type, grouped by zero or more node properties
     * [Configuration](Configuration.md) - The meaning of operations can be configured
     * [Session](Session.md) - A session consists of a set of change sets bundled with the activities that generated those change sets
     * [TextualDiff](TextualDiff.md) - A summarizing of a change on a piece of text. This could be rendered in a number of different ways
 * [OntologyElement](OntologyElement.md) - Any component of an ontology or knowledge graph
     * [Edge](Edge.md) - A relationship between two nodes.
     * [LogicalDefinition](LogicalDefinition.md)
     * [Node](Node.md) - Any named entity in an ontology. May be a class, individual, property
         * [ClassNode](ClassNode.md) - A node that is a class
         * [InstanceNode](InstanceNode.md) - A node that is an individual
     * [OntologySubset](OntologySubset.md)
     * [PropertyValue](PropertyValue.md) - a property-value pair
         * [Annotation](Annotation.md) - owl annotations. Not to be confused with annotations sensu GO
 * [ProvElement](ProvElement.md) - A grouping for prov elements
     * [Activity](Activity.md) - a provence-generating activity
     * [Agent](Agent.md) - a provence-generating agent

### Mixins

 * [AddToSubset](AddToSubset.md) - placing an element inside a subset
 * [AllowsAutomaticReplacementOfEdges](AllowsAutomaticReplacementOfEdges.md) - Applies to an obsoletion in which annotations or edges pointing at the obsoleted node can be automatically rewired to point to a target
 * [ChangeMixin](ChangeMixin.md) - root class for all change mixins
     * [Creation](Creation.md) - Creation of an element.
     * [DatatypeOrLanguageTagChange](DatatypeOrLanguageTagChange.md) - A change in a value assertion where the value remain unchanged but either the datatype or language changes
         * [DatatypeChange](DatatypeChange.md)
         * [LanguageTagChange](LanguageTagChange.md)
     * [Deletion](Deletion.md) - Removal of an element.
     * [Obsoletion](Obsoletion.md) - Obsoletion of an element deprecates usage of that element, but does not delete that element.
         * [AllowsAutomaticReplacementOfEdges](AllowsAutomaticReplacementOfEdges.md) - Applies to an obsoletion in which annotations or edges pointing at the obsoleted node can be automatically rewired to point to a target
     * [SubsetMembershipChange](SubsetMembershipChange.md) - A change in the membership status of a node with respect to a subset (view)
         * [AddToSubset](AddToSubset.md) - placing an element inside a subset
         * [RemoveFromSubset](RemoveFromSubset.md) - removing an element from a subset
     * [Unobsoletion](Unobsoletion.md) - Opposite operation of obsoletion. Rarely performed.
 * [Creation](Creation.md) - Creation of an element.
 * [DatatypeOrLanguageTagChange](DatatypeOrLanguageTagChange.md) - A change in a value assertion where the value remain unchanged but either the datatype or language changes
     * [DatatypeChange](DatatypeChange.md)
     * [LanguageTagChange](LanguageTagChange.md)
 * [Deletion](Deletion.md) - Removal of an element.
 * [Obsoletion](Obsoletion.md) - Obsoletion of an element deprecates usage of that element, but does not delete that element.
     * [AllowsAutomaticReplacementOfEdges](AllowsAutomaticReplacementOfEdges.md) - Applies to an obsoletion in which annotations or edges pointing at the obsoleted node can be automatically rewired to point to a target
 * [RemoveFromSubset](RemoveFromSubset.md) - removing an element from a subset
 * [SubsetMembershipChange](SubsetMembershipChange.md) - A change in the membership status of a node with respect to a subset (view)
     * [AddToSubset](AddToSubset.md) - placing an element inside a subset
     * [RemoveFromSubset](RemoveFromSubset.md) - removing an element from a subset
 * [Unobsoletion](Unobsoletion.md) - Opposite operation of obsoletion. Rarely performed.

### Slots

 * [about](about.md) - The 'focus' entity on which the change operates
     * [Obsoletion➞about](Obsoletion_about.md) - The element that is obsoleted by this change.
     * [about_edge](about_edge.md)
     * [about_node](about_node.md)
         * [NodeDirectMerge➞about_node](NodeDirectMerge_about_node.md)
         * [RemoveNodeFromSubset➞about_node](RemoveNodeFromSubset_about_node.md) - The node that is removed from the subset
 * [about_node_representation](about_node_representation.md) - The representation of a node (URI, CURIE, label) 
 * [acted_on_behalf_of](acted_on_behalf_of.md)
 * [activity_set](activity_set.md)
 * [agent_set](agent_set.md)
 * [annotation_property](annotation_property.md) - An annotation property
 * [annotation_property_type](annotation_property_type.md) - The type of a property (URI, CURIE, label) 
 * [annotation_set](annotation_set.md)
 * [change 1](change_1.md)
     * [NameBecomesSynonym➞change 1](NameBecomesSynonym_change_1.md)
 * [change 2](change_2.md)
     * [NameBecomesSynonym➞change 2](NameBecomesSynonym_change_2.md)
 * [change type](change_type.md)
     * [ChangeSetSummaryStatistic➞change type](ChangeSetSummaryStatistic_change_type.md)
 * [change_date](change_date.md)
     * [Change➞change_date](Change_change_date.md)
 * [change_description](change_description.md) - A string serialization of the change. This should be both human-readable, and parseable.
     * [EdgeCreation➞change_description](EdgeCreation_change_description.md)
         * [MappingCreation➞change_description](MappingCreation_change_description.md)
     * [EdgeDeletion➞change_description](EdgeDeletion_change_description.md)
     * [EdgeObsoletion➞change_description](EdgeObsoletion_change_description.md)
     * [MultiNodeObsoletion➞change_description](MultiNodeObsoletion_change_description.md)
     * [NameBecomesSynonym➞change_description](NameBecomesSynonym_change_description.md)
     * [NodeCreation➞change_description](NodeCreation_change_description.md)
         * [ClassCreation➞change_description](ClassCreation_change_description.md)
         * [ObjectPropertyCreation➞change_description](ObjectPropertyCreation_change_description.md)
     * [NodeDeletion➞change_description](NodeDeletion_change_description.md)
     * [NodeMove➞change_description](NodeMove_change_description.md)
         * [NodeDeepening➞change_description](NodeDeepening_change_description.md)
         * [NodeShallowing➞change_description](NodeShallowing_change_description.md)
     * [NodeObsoletion➞change_description](NodeObsoletion_change_description.md)
         * [NodeDirectMerge➞change_description](NodeDirectMerge_change_description.md)
         * [NodeObsoletionWithDirectReplacement➞change_description](NodeObsoletionWithDirectReplacement_change_description.md)
         * [NodeObsoletionWithNoDirectReplacement➞change_description](NodeObsoletionWithNoDirectReplacement_change_description.md)
     * [NodeRename➞change_description](NodeRename_change_description.md)
     * [NodeUnobsoletion➞change_description](NodeUnobsoletion_change_description.md)
     * [PredicateChange➞change_description](PredicateChange_change_description.md)
     * [RemoveNodeFromSubset➞change_description](RemoveNodeFromSubset_change_description.md)
     * [SetLanguageForName➞change_description](SetLanguageForName_change_description.md)
 * [change_set](change_set.md) - A collection of changes
     * [MultiNodeObsoletion➞associated change set](MultiNodeObsoletion_associated_change_set.md) - All changes associated with a set of obsoletions. This change set is the composed change set rather than the set of individual changes. For example, if previous state is:\n  `A subClassOf B subClassOf C subClassOf D` and we obsolete {B,C}, then the individual changes are `A moves from B to C` and `B moves from C to D`, but the composed change set is `A moves from B to D`"
     * [MultiNodeObsoletion➞change_set](MultiNodeObsoletion_change_set.md)
     * [NodeObsoletion➞associated change set](NodeObsoletion_associated_change_set.md) - All changes forced as a result of this obsoletion. For example, starting with `A subClassOf B subClassOf C`, if we obsolete node B, then we may decide to bundle in a node move change of A from B to C. Note: this change set is not considered a part of the obsoletion, as obsoletion is considered atomic/simple. Instead this is a reference to a change set that may exist elsewhere
     * [associated change set](associated_change_set.md) - All changes associated with a set of obsoletions. This change set is the composed change set rather than the set of individual changes. For example, if previous state is:\n  `A subClassOf B subClassOf C subClassOf D` and we obsolete {B,C}, then the individual changes are `A moves from B to C` and `B moves from C to D`, but the composed change set is `A moves from B to D`"
 * [➞contributor_predicate](configuration__contributor_predicate.md)
 * [➞creator_predicate](configuration__creator_predicate.md)
 * [➞definition_predicate](configuration__definition_predicate.md)
 * [➞main_synonym_predicate](configuration__main_synonym_predicate.md)
 * [➞name_predicate](configuration__name_predicate.md)
 * [➞obsolete_node_label_prefix](configuration__obsolete_node_label_prefix.md) - A prefix to add to the label of an obsolete node. This may include a space at the end.
 * [➞obsolete_subclass_of_shadow_property](configuration__obsolete_subclass_of_shadow_property.md) - specifies the annotation property to be used to create a shadow annotation assertion triple when a subclass edge is deleted.
 * [➞obsoletion_policies](configuration__obsoletion_policies.md)
 * [➞obsoletion_workflow](configuration__obsoletion_workflow.md)
 * [➞synonym_predicates](configuration__synonym_predicates.md)
 * [consider](consider.md)
     * [NodeUnobsoletion➞consider](NodeUnobsoletion_consider.md)
 * [contributor](contributor.md)
 * [count](count.md)
     * [ChangeSetSummaryStatistic➞count](ChangeSetSummaryStatistic_count.md)
 * [creator](creator.md)
     * [Change➞creator](Change_creator.md)
 * [datatype](datatype.md) - The datatype of a literal
 * [description](description.md)
 * [ended_at_time](ended_at_time.md)
 * [filler](filler.md)
 * [filler_type](filler_type.md)
 * [has_direct_replacement](has_direct_replacement.md) - An obsoletion replacement where it IS valid to automatically update annotations/edges pointing at the node with its direct replacement
     * [NodeDirectMerge➞has_direct_replacement](NodeDirectMerge_has_direct_replacement.md)
     * [NodeObsoletionWithDirectReplacement➞has_direct_replacement](NodeObsoletionWithDirectReplacement_has_direct_replacement.md)
 * [has_nondirect_replacement](has_nondirect_replacement.md) - An obsoletion replacement where it is NOT valid to automatically update annotations/edges pointing at the node with its direct replacement
     * [NodeObsoletionWithNoDirectReplacement➞has_nondirect_replacement](NodeObsoletionWithNoDirectReplacement_has_nondirect_replacement.md)
 * [has_textual_diff](has_textual_diff.md) - A representation of character-level changes on a textual literal property. For example, if a text definition may change by only a single character such as addition of a period, it is useful to be able to see this visually.
 * [has_undo](has_undo.md) - A change that reverses this change
     * [Creation➞has_undo](Creation_has_undo.md)
     * [Obsoletion➞has_undo](Obsoletion_has_undo.md)
     * [RemoveFromSubset➞has_undo](RemoveFromSubset_has_undo.md)
     * [Unobsoletion➞has_undo](Unobsoletion_has_undo.md)
 * [id](id.md)
 * [in_subset](in_subset.md) - The subset that pertains to this change
     * [AddToSubset➞in_subset](AddToSubset_in_subset.md) - subset that the element is being placed inside.
     * [RemoveFromSubset➞in_subset](RemoveFromSubset_in_subset.md) - subset that the element is being removed from
 * [language](language.md) - The language tag of a literal
 * [name](name.md)
 * [new_datatype](new_datatype.md) - The new datatype of a literal
 * [new_filler](new_filler.md) - The new filler of an OWL restriction
 * [new_language](new_language.md) - The new language tag of a literal
 * [new_object_type](new_object_type.md) - The type (IRI or Literal) of a new object
 * [new_property](new_property.md) - The new property of an OWL restriction
 * [new_subclass](new_subclass.md) - The new subclass of a subsumption axiom
 * [new_value](new_value.md) - The value of a property held in the new instance of the ontology
     * [LanguageTagChange➞new_value](LanguageTagChange_new_value.md)
     * [NodeRename➞new_value](NodeRename_new_value.md)
 * [new_value_type](new_value_type.md) - The type (IRI or Literal) of a new value
 * [node_id](node_id.md) - id of a node to be created
 * [object](object.md)
     * [MappingCreation➞object](MappingCreation_object.md) - This corresponds to object_id in SSSOM
 * [object_representation](object_representation.md)
 * [object_type](object_type.md) - The type (IRI or Literal) of an object
 * [old_datatype](old_datatype.md) - The old datatype of a literal
 * [old_language](old_language.md) - The old language tag of a literal
 * [old_object_type](old_object_type.md) - The type (IRI or Literal) of an old object
 * [old_value](old_value.md) - The value of a property held in the old instance of the ontology
     * [LanguageTagChange➞old_value](LanguageTagChange_old_value.md)
     * [NodeRename➞old_value](NodeRename_old_value.md)
 * [old_value_type](old_value_type.md) - The type (IRI or Literal) of an old value
 * [owl_type](owl_type.md)
 * [predicate](predicate.md)
     * [MappingCreation➞predicate](MappingCreation_predicate.md) - This corresponds to predicate_id in SSSOM. The value of this is typically a predicate from SKOS
 * [predicate_representation](predicate_representation.md)
 * [predicate_type](predicate_type.md) - The type (IRI or Literal) of an edge's subject
 * [property](property.md)
 * [property_type](property_type.md)
 * [property_value_set](property_value_set.md)
     * [ChangeSetSummaryStatistic➞property_value_set](ChangeSetSummaryStatistic_property_value_set.md) - Summary statistic is grouped by these constraints
 * [pull_request](pull_request.md)
     * [Change➞pull_request](Change_pull_request.md)
 * [qualifier](qualifier.md) - The qualifier of a change operation
 * [replaced by](replaced_by.md)
     * [NodeUnobsoletion➞replaced by](NodeUnobsoletion_replaced_by.md)
 * [see_also](see_also.md)
     * [Change➞see_also](Change_see_also.md)
 * [started_at_time](started_at_time.md)
 * [subclass](subclass.md) - The subclass of a subsumption axiom
 * [subclass_type](subclass_type.md) - The type of a subclass
 * [subject](subject.md)
     * [EdgeChange➞subject](EdgeChange_subject.md)
     * [MappingCreation➞subject](MappingCreation_subject.md) - This corresponds to subject_id in SSSOM
 * [subject_representation](subject_representation.md)
 * [subject_type](subject_type.md) - The type (IRI or Literal) of an edge's subject
 * [subset](subset.md) - The subset from which the node is to be removed
     * [RemoveNodeFromSubset➞subset](RemoveNodeFromSubset_subset.md)
 * [superclass](superclass.md)
 * [superclass_type](superclass_type.md) - The type of a superclass
 * [target](target.md) - The secondary entity on which the change operates
     * [has_replacement](has_replacement.md) - A single node obsoletion event may be accompanied by one or more suggested replacement nodes
 * [term_tracker_issue](term_tracker_issue.md)
     * [Change➞term_tracker_issue](Change_term_tracker_issue.md)
 * [type](type.md)
 * [used](used.md)
 * [was_associated_with](was_associated_with.md)
 * [was_generated_by](was_generated_by.md)
     * [Change➞was_generated_by](Change_was_generated_by.md)
 * [was_informed_by](was_informed_by.md)

### Enums

 * [ObsoletionPolicyEnum](ObsoletionPolicyEnum.md)
 * [OwlTypeEnum](OwlTypeEnum.md)
 * [SynonymScopeEnum](SynonymScopeEnum.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [ChangeClassType](types/ChangeClassType.md)  ([Uriorcurie](types/Uriorcurie.md))  - CURIE for a class within this data model. E.g. kgcl:NodeObsoletion
 * [LanguageTag](types/LanguageTag.md)  (**str**) 
 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
