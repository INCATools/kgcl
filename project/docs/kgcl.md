
# kgcl_schema


**metamodel version:** 1.7.0

**version:** 0.0.1


A data model for describing change operations at a high level on an ontology or ontology-like artefact, such as a Knowledge Graph.

* [Browse Schema](https://cmungall.github.io/knowledge-graph-change-language/)
* [GitHub](https://github.com/cmungall/knowledge-graph-change-language)


### Classes

 * [Activity](Activity.md) - a provence-generating activity
 * [Agent](Agent.md) - a provence-generating agent
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
             * [EdgeLogicalInterpretationChange](EdgeLogicalInterpretationChange.md) - An edge change where the subjet, object, and predicate are unchanged, but the logical interpretation changes
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
                 * [ClassCreation](ClassCreation.md) - A node creation where the owl type is 'class'
             * [NodeDeletion](NodeDeletion.md) - Deletion of a node from the graph. Note it is recommended nodes are obsoleted and never merged, but this operation exists to represent deletions in ontologies, accidental or otherwise
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
             * [RemovedNodeFromSubset](RemovedNodeFromSubset.md) - Removes a node from a subset, by removing an annotation
             * [SetLanguageForName](SetLanguageForName.md) - A node change where the string value for the name is unchanged but the language tag is set
     * [Transaction](Transaction.md) - A change that is a composition of a set of changes, where those changes are treated as a single unit. Could be a single change, or the results of an ontology diff
 * [ChangeSetSummaryStatistic](ChangeSetSummaryStatistic.md) - A summary statistic for a set of changes of the same type, grouped by zero or more node properties
 * [Configuration](Configuration.md) - The meaning of operations can be configured
 * [OntologyElement](OntologyElement.md) - Any component of an ontology or knowledge graph
     * [Edge](Edge.md) - A relationship between two nodes.
     * [LogicalDefinition](LogicalDefinition.md)
     * [Node](Node.md) - Any named entity in an ontology. May be a class, individual, property
         * [ClassNode](ClassNode.md) - A node that is a class
         * [InstanceNode](InstanceNode.md) - A node that is an individual
     * [OntologySubset](OntologySubset.md)
     * [PropertyValue](PropertyValue.md) - a property-value pair
         * [Annotation](Annotation.md) - owl annotations. Not to be confused with annotations sensu GO
 * [Session](Session.md) - A session consists of a set of change sets bundled with the activities that generated those change sets
 * [TextualDiff](TextualDiff.md) - A summarizing of a change on a piece of text. This could be rendered in a number of different ways

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
     * [about edge](about_edge.md)
     * [about node](about_node.md)
         * [node direct merge➞about node](node_direct_merge_about_node.md)
         * [removed node from subset➞about node](removed_node_from_subset_about_node.md) - The node that is removed from the subset
     * [obsoletion➞about](obsoletion_about.md) - The element that is obsoleted by this change.
 * [about node representation](about_node_representation.md) - The representation of a node (URI, CURIE, label) 
 * [acted on behalf of](acted_on_behalf_of.md)
 * [activity set](activity_set.md)
 * [agent set](agent_set.md)
 * [annotation property](annotation_property.md) - An annotation property
 * [annotation property type](annotation_property_type.md) - The type of a property (URI, CURIE, label) 
 * [annotation set](annotation_set.md)
 * [change 1](change_1.md)
     * [name becomes synonym➞change 1](name_becomes_synonym_change_1.md)
 * [change 2](change_2.md)
     * [name becomes synonym➞change 2](name_becomes_synonym_change_2.md)
 * [change date](change_date.md)
     * [change➞change date](change_change_date.md)
 * [change description](change_description.md) - A string serialization of the change. This should be both human-readable, and parseable.
     * [edge creation➞change description](edge_creation_change_description.md)
         * [mapping creation➞change description](mapping_creation_change_description.md)
     * [edge deletion➞change description](edge_deletion_change_description.md)
     * [edge obsoletion➞change description](edge_obsoletion_change_description.md)
     * [multi node obsoletion➞change description](multi_node_obsoletion_change_description.md)
     * [name becomes synonym➞change description](name_becomes_synonym_change_description.md)
     * [node creation➞change description](node_creation_change_description.md)
         * [class creation➞change description](class_creation_change_description.md)
     * [node deletion➞change description](node_deletion_change_description.md)
     * [node move➞change description](node_move_change_description.md)
         * [node deepening➞change description](node_deepening_change_description.md)
         * [node shallowing➞change description](node_shallowing_change_description.md)
     * [node obsoletion➞change description](node_obsoletion_change_description.md)
         * [node direct merge➞change description](node_direct_merge_change_description.md)
         * [node obsoletion with direct replacement➞change description](node_obsoletion_with_direct_replacement_change_description.md)
         * [node obsoletion with no direct replacement➞change description](node_obsoletion_with_no_direct_replacement_change_description.md)
     * [node rename➞change description](node_rename_change_description.md)
     * [node unobsoletion➞change description](node_unobsoletion_change_description.md)
     * [predicate change➞change description](predicate_change_change_description.md)
     * [removed node from subset➞change description](removed_node_from_subset_change_description.md)
     * [set language for name➞change description](set_language_for_name_change_description.md)
 * [change set](change_set.md) - A collection of changes
     * [associated change set](associated_change_set.md) - All changes associated with a set of obsoletions. This change set is the composed change set rather than the set of individual changes. For example, if previous state is:
     * [multi node obsoletion➞associated change set](multi_node_obsoletion_associated_change_set.md) - All changes associated with a set of obsoletions. This change set is the composed change set rather than the set of individual changes. For example, if previous state is:
     * [multi node obsoletion➞change set](multi_node_obsoletion_change_set.md)
     * [node obsoletion➞associated change set](node_obsoletion_associated_change_set.md) - All changes forced as a result of this obsoletion. For example, starting with `A subClassOf B subClassOf C`, if we obsolete node B, then we may decide to bundle in a node move change of A from B to C. Note: this change set is not considered a part of the obsoletion, as obsoletion is considered atomic/simple. Instead this is a reference to a change set that may exist elsewhere
 * [change type](change_type.md)
     * [change set summary statistic➞change type](change_set_summary_statistic_change_type.md)
 * [➞contributor predicate](configuration__contributor_predicate.md)
 * [➞creator predicate](configuration__creator_predicate.md)
 * [➞definition predicate](configuration__definition_predicate.md)
 * [➞main synonym predicate](configuration__main_synonym_predicate.md)
 * [➞name predicate](configuration__name_predicate.md)
 * [➞obsoletion policy](configuration__obsoletion_policy.md)
 * [➞obsoletion workflow](configuration__obsoletion_workflow.md)
 * [➞synonym predicates](configuration__synonym_predicates.md)
 * [consider](consider.md)
     * [node unobsoletion➞consider](node_unobsoletion_consider.md)
 * [contributor](contributor.md)
 * [count](count.md)
     * [change set summary statistic➞count](change_set_summary_statistic_count.md)
 * [creator](creator.md)
     * [change➞creator](change_creator.md)
 * [datatype](datatype.md) - The datatype of a literal
 * [description](description.md)
 * [ended at time](ended_at_time.md)
 * [filler](filler.md)
 * [filler type](filler_type.md)
 * [has direct replacement](has_direct_replacement.md) - An obsoletion replacement where it IS valid to automatically update annotations/edges pointing at the node with its direct replacement
     * [node direct merge➞has direct replacement](node_direct_merge_has_direct_replacement.md)
     * [node obsoletion with direct replacement➞has direct replacement](node_obsoletion_with_direct_replacement_has_direct_replacement.md)
 * [has nondirect replacement](has_nondirect_replacement.md) - An obsoletion replacement where it is NOT valid to automatically update annotations/edges pointing at the node with its direct replacement
     * [node obsoletion with no direct replacement➞has nondirect replacement](node_obsoletion_with_no_direct_replacement_has_nondirect_replacement.md)
 * [has textual diff](has_textual_diff.md) - A representation of character-level changes on a textual literal property. For example, if a text definition may change by only a single character such as addition of a period, it is useful to be able to see this visually.
 * [has undo](has_undo.md) - A change that reverses this change
     * [creation➞has undo](creation_has_undo.md)
     * [obsoletion➞has undo](obsoletion_has_undo.md)
     * [remove from subset➞has undo](remove_from_subset_has_undo.md)
     * [unobsoletion➞has undo](unobsoletion_has_undo.md)
 * [id](id.md)
 * [in subset](in_subset.md) - The subset that pertains to this change
     * [add to subset➞in subset](add_to_subset_in_subset.md) - subset that the element is being placed inside.
     * [remove from subset➞in subset](remove_from_subset_in_subset.md) - subset that the element is being removed from
 * [language](language.md) - The language tag of a literal
 * [name](name.md)
 * [new datatype](new_datatype.md) - The new datatype of a literal
 * [new filler](new_filler.md) - The new filler of an OWL restriction
 * [new language](new_language.md) - The new language tag of a literal
 * [new object type](new_object_type.md) - The type (IRI or Literal) of a new object
 * [new property](new_property.md) - The new property of an OWL restriction
 * [new subclass](new_subclass.md) - The new subclass of a subsumption axiom
 * [new value](new_value.md) - The value of a property held in the new instance of the ontology
     * [language tag change➞new value](language_tag_change_new_value.md)
     * [node rename➞new value](node_rename_new_value.md)
 * [new value type](new_value_type.md) - The type (IRI or Literal) of a new value
 * [node id](node_id.md) - id of a node to be created
 * [object](object.md)
     * [mapping creation➞object](mapping_creation_object.md) - This corresponds to object_id in SSSOM
 * [object representation](object_representation.md)
 * [object type](object_type.md) - The type (IRI or Literal) of an object
 * [old datatype](old_datatype.md) - The old datatype of a literal
 * [old language](old_language.md) - The old language tag of a literal
 * [old object type](old_object_type.md) - The type (IRI or Literal) of an old object
 * [old value](old_value.md) - The value of a property held in the old instance of the ontology
     * [language tag change➞old value](language_tag_change_old_value.md)
     * [node rename➞old value](node_rename_old_value.md)
 * [old value type](old_value_type.md) - The type (IRI or Literal) of an old value
 * [owl type](owl_type.md)
 * [predicate](predicate.md)
     * [mapping creation➞predicate](mapping_creation_predicate.md) - This corresponds to predicate_id in SSSOM. The value of this is typically a predicate from SKOS
 * [predicate representation](predicate_representation.md)
 * [predicate type](predicate_type.md) - The type (IRI or Literal) of an edge's subject
 * [property](property.md)
 * [property type](property_type.md)
 * [property value set](property_value_set.md)
     * [change set summary statistic➞property value set](change_set_summary_statistic_property_value_set.md) - Summary statistic is grouped by these constraints
 * [pull request](pull_request.md)
     * [change➞pull request](change_pull_request.md)
 * [qualifier](qualifier.md) - The qualifier of a change operation
 * [replaced by](replaced_by.md)
     * [node unobsoletion➞replaced by](node_unobsoletion_replaced_by.md)
 * [see also](see_also.md)
     * [change➞see also](change_see_also.md)
 * [started at time](started_at_time.md)
 * [subclass](subclass.md) - The subclass of a subsumption axiom
 * [subclass type](subclass_type.md) - The type of a subclass
 * [subject](subject.md)
     * [edge change➞subject](edge_change_subject.md)
     * [mapping creation➞subject](mapping_creation_subject.md) - This corresponds to subject_id in SSSOM
 * [subject representation](subject_representation.md)
 * [subject type](subject_type.md) - The type (IRI or Literal) of an edge's subject
 * [subset](subset.md) - The subset from which the node is to be removed
     * [removed node from subset➞subset](removed_node_from_subset_subset.md)
 * [superclass](superclass.md)
 * [superclass type](superclass_type.md) - The type of a superclass
 * [target](target.md) - The secondary entity on which the change operates
     * [has replacement](has_replacement.md) - A single node obsoletion event may be accompanied by one or more suggested replacement nodes
 * [type](type.md)
 * [used](used.md)
 * [was associated with](was_associated_with.md)
 * [was generated by](was_generated_by.md)
     * [change➞was generated by](change_was_generated_by.md)
 * [was informed by](was_informed_by.md)

### Enums

 * [owl_type_enum](owl_type_enum.md)
 * [synonym_scope_enum](synonym_scope_enum.md)

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

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [ChangeClassType](types/ChangeClassType.md)  ([Uriorcurie](types/Uriorcurie.md))  - CURIE for a class within this datamodel. E.g. kgcl:NodeObsoletion
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [LanguageTag](types/LanguageTag.md)  (**str**) 
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
