-- # Class: "ChangeLanguageElement" Description: "A broad grouping for all elements of the change language"
--     * Slot: id Description: 
-- # Class: "Change" Description: "Any change perform on an ontology or knowledge graph"
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: Change_id Description: Autocreated FK slot
--     * Slot: SimpleChange_id Description: Autocreated FK slot
--     * Slot: ComplexChange_id Description: Autocreated FK slot
--     * Slot: MultiNodeObsoletion_id Description: Autocreated FK slot
--     * Slot: Transaction_id Description: Autocreated FK slot
--     * Slot: EdgeChange_id Description: Autocreated FK slot
--     * Slot: EdgeCreation_id Description: Autocreated FK slot
--     * Slot: PlaceUnder_id Description: Autocreated FK slot
--     * Slot: EdgeDeletion_id Description: Autocreated FK slot
--     * Slot: RemoveUnder_id Description: Autocreated FK slot
--     * Slot: EdgeObsoletion_id Description: Autocreated FK slot
--     * Slot: EdgeRewiring_id Description: Autocreated FK slot
--     * Slot: MappingCreation_id Description: Autocreated FK slot
--     * Slot: NodeMove_id Description: Autocreated FK slot
--     * Slot: NodeDeepening_id Description: Autocreated FK slot
--     * Slot: NodeShallowing_id Description: Autocreated FK slot
--     * Slot: PredicateChange_id Description: Autocreated FK slot
--     * Slot: EdgeLogicalInterpretationChange_id Description: Autocreated FK slot
--     * Slot: LogicalAxiomChange_id Description: Autocreated FK slot
--     * Slot: NodeChange_id Description: Autocreated FK slot
--     * Slot: NodeRename_id Description: Autocreated FK slot
--     * Slot: SetLanguageForName_id Description: Autocreated FK slot
--     * Slot: NodeAnnotationChange_id Description: Autocreated FK slot
--     * Slot: NodeAnnotationReplacement_id Description: Autocreated FK slot
--     * Slot: NodeSynonymChange_id Description: Autocreated FK slot
--     * Slot: NewSynonym_id Description: Autocreated FK slot
--     * Slot: NameBecomesSynonym_id Description: Autocreated FK slot
--     * Slot: RemoveSynonym_id Description: Autocreated FK slot
--     * Slot: SynonymReplacement_id Description: Autocreated FK slot
--     * Slot: SynonymPredicateChange_id Description: Autocreated FK slot
--     * Slot: NodeMappingChange_id Description: Autocreated FK slot
--     * Slot: NewMapping_id Description: Autocreated FK slot
--     * Slot: RemoveMapping_id Description: Autocreated FK slot
--     * Slot: MappingReplacement_id Description: Autocreated FK slot
--     * Slot: MappingPredicateChange_id Description: Autocreated FK slot
--     * Slot: NodeMetadataAssertionChange_id Description: Autocreated FK slot
--     * Slot: NewMetadataAssertion_id Description: Autocreated FK slot
--     * Slot: RemoveMetadataAssertion_id Description: Autocreated FK slot
--     * Slot: MetadataAssertionReplacement_id Description: Autocreated FK slot
--     * Slot: MetadataAssertionPredicateChange_id Description: Autocreated FK slot
--     * Slot: NodeTextDefinitionChange_id Description: Autocreated FK slot
--     * Slot: NewTextDefinition_id Description: Autocreated FK slot
--     * Slot: RemoveTextDefinition_id Description: Autocreated FK slot
--     * Slot: TextDefinitionReplacement_id Description: Autocreated FK slot
--     * Slot: AddNodeToSubset_id Description: Autocreated FK slot
--     * Slot: RemoveNodeFromSubset_id Description: Autocreated FK slot
--     * Slot: NodeObsoletion_id Description: Autocreated FK slot
--     * Slot: NodeUnobsoletion_id Description: Autocreated FK slot
--     * Slot: NodeCreation_id Description: Autocreated FK slot
--     * Slot: ClassCreation_id Description: Autocreated FK slot
--     * Slot: ObjectPropertyCreation_id Description: Autocreated FK slot
--     * Slot: NodeDeletion_id Description: Autocreated FK slot
--     * Slot: NodeDirectMerge_id Description: Autocreated FK slot
--     * Slot: NodeObsoletionWithDirectReplacement_id Description: Autocreated FK slot
--     * Slot: NodeObsoletionWithNoDirectReplacement_id Description: Autocreated FK slot
--     * Slot: Session_id Description: Autocreated FK slot
-- # Class: "SimpleChange" Description: "A change that is about a single ontology element"
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "ComplexChange" Description: "A change that is is a composition of other changes"
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "MultiNodeObsoletion" Description: "A complex change consisting of multiple obsoletions."
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "Transaction" Description: "A change that is a composition of a set of changes, where those changes are treated as a single unit. Could be a single change, or the results of an ontology diff"
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "ChangeSetSummaryStatistic" Description: "A summary statistic for a set of changes of the same type, grouped by zero or more node properties"
--     * Slot: id Description: 
-- # Class: "ChangeMixin" Description: "root class for all change mixins"
--     * Slot: id Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "Obsoletion" Description: "Obsoletion of an element deprecates usage of that element, but does not delete that element."
--     * Slot: id Description: 
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_id Description: The element that is obsoleted by this change.
--     * Slot: has_undo_id Description: A change that reverses this change
-- # Class: "DatatypeOrLanguageTagChange" Description: "A change in a value assertion where the value remain unchanged but either the datatype or language changes"
--     * Slot: id Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "LanguageTagChange" Description: ""
--     * Slot: id Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "DatatypeChange" Description: ""
--     * Slot: id Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "AllowsAutomaticReplacementOfEdges" Description: "Applies to an obsoletion in which annotations or edges pointing at the obsoleted node can be automatically rewired to point to a target"
--     * Slot: id Description: 
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_id Description: The element that is obsoleted by this change.
--     * Slot: has_undo_id Description: A change that reverses this change
-- # Class: "Unobsoletion" Description: "Opposite operation of obsoletion. Rarely performed."
--     * Slot: id Description: 
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_id Description: The 'focus' entity on which the change operates
--     * Slot: has_undo_id Description: A change that reverses this change
-- # Class: "Deletion" Description: "Removal of an element."
--     * Slot: id Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "Creation" Description: "Creation of an element."
--     * Slot: id Description: 
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_id Description: The 'focus' entity on which the change operates
--     * Slot: has_undo_id Description: A change that reverses this change
-- # Class: "SubsetMembershipChange" Description: "A change in the membership status of a node with respect to a subset (view)"
--     * Slot: id Description: 
--     * Slot: in_subset Description: The subset that pertains to this change
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "AddToSubset" Description: "placing an element inside a subset"
--     * Slot: id Description: 
--     * Slot: in_subset Description: subset that the element is being placed inside.
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "RemoveFromSubset" Description: "removing an element from a subset"
--     * Slot: id Description: 
--     * Slot: in_subset Description: subset that the element is being removed from
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_id Description: The 'focus' entity on which the change operates
--     * Slot: has_undo_id Description: A change that reverses this change
-- # Class: "EdgeChange" Description: "A change in which the element that is the focus of the change is an edge."
--     * Slot: object_type Description: The type (IRI or Literal) of an object
--     * Slot: language Description: The language tag of a literal
--     * Slot: datatype Description: The datatype of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: about_edge_id Description: 
-- # Class: "EdgeCreation" Description: "An edge change in which a de-novo edge is created. The edge is potentially annotated in the same action."
--     * Slot: subject Description: 
--     * Slot: predicate Description: 
--     * Slot: object Description: 
--     * Slot: subject_type Description: The type (IRI or Literal) of an edge's subject
--     * Slot: predicate_type Description: The type (IRI or Literal) of an edge's subject
--     * Slot: object_type Description: The type (IRI or Literal) of an object
--     * Slot: language Description: The language tag of a literal
--     * Slot: datatype Description: The datatype of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: annotation_set_id Description: 
--     * Slot: about_edge_id Description: 
--     * Slot: has_undo_id Description: A change that reverses this change
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "PlaceUnder" Description: "An edge creation where the predicate is owl:subClassOf"
--     * Slot: subject Description: 
--     * Slot: predicate Description: 
--     * Slot: object Description: 
--     * Slot: subject_type Description: The type (IRI or Literal) of an edge's subject
--     * Slot: predicate_type Description: The type (IRI or Literal) of an edge's subject
--     * Slot: object_type Description: The type (IRI or Literal) of an object
--     * Slot: language Description: The language tag of a literal
--     * Slot: datatype Description: The datatype of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: annotation_set_id Description: 
--     * Slot: about_edge_id Description: 
--     * Slot: has_undo_id Description: A change that reverses this change
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "EdgeDeletion" Description: "An edge change in which an edge is removed. All edge annotations/properies are removed in the same action."
--     * Slot: subject Description: 
--     * Slot: predicate Description: 
--     * Slot: object Description: 
--     * Slot: subject_type Description: The type (IRI or Literal) of an edge's subject
--     * Slot: predicate_type Description: The type (IRI or Literal) of an edge's subject
--     * Slot: object_type Description: The type (IRI or Literal) of an object
--     * Slot: language Description: The language tag of a literal
--     * Slot: datatype Description: The datatype of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: annotation_set_id Description: 
--     * Slot: about_edge_id Description: 
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "RemoveUnder" Description: "An edge deletion where the predicate is owl:subClassOf  "
--     * Slot: subject Description: 
--     * Slot: predicate Description: 
--     * Slot: object Description: 
--     * Slot: subject_type Description: The type (IRI or Literal) of an edge's subject
--     * Slot: predicate_type Description: The type (IRI or Literal) of an edge's subject
--     * Slot: object_type Description: The type (IRI or Literal) of an object
--     * Slot: language Description: The language tag of a literal
--     * Slot: datatype Description: The datatype of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: annotation_set_id Description: 
--     * Slot: about_edge_id Description: 
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "EdgeObsoletion" Description: "An edge change in which an edge is obsoleted."
--     * Slot: subject Description: 
--     * Slot: predicate Description: 
--     * Slot: object Description: 
--     * Slot: object_type Description: The type (IRI or Literal) of an object
--     * Slot: language Description: The language tag of a literal
--     * Slot: datatype Description: The datatype of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: annotation_set_id Description: 
--     * Slot: about_edge_id Description: 
--     * Slot: has_undo_id Description: A change that reverses this change
--     * Slot: about_id Description: The element that is obsoleted by this change.
-- # Class: "EdgeRewiring" Description: "An edge change where one node is replaced with another, as in the case of obsoletion with replacement"
--     * Slot: object_type Description: The type (IRI or Literal) of an object
--     * Slot: language Description: The language tag of a literal
--     * Slot: datatype Description: The datatype of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: about_edge_id Description: 
-- # Class: "MappingCreation" Description: "A specific kind of edge creation in which the created edge is a mapping."
--     * Slot: subject Description: This corresponds to subject_id in SSSOM
--     * Slot: predicate Description: This corresponds to predicate_id in SSSOM. The value of this is typically a predicate from SKOS
--     * Slot: object Description: This corresponds to object_id in SSSOM
--     * Slot: subject_type Description: The type (IRI or Literal) of an edge's subject
--     * Slot: predicate_type Description: The type (IRI or Literal) of an edge's subject
--     * Slot: object_type Description: The type (IRI or Literal) of an object
--     * Slot: language Description: The language tag of a literal
--     * Slot: datatype Description: The datatype of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: annotation_set_id Description: 
--     * Slot: about_edge_id Description: 
--     * Slot: has_undo_id Description: A change that reverses this change
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "NodeMove" Description: "A node move is a combination of deleting a parent edge and adding a parent edge, where the predicate is preserved and the object/parent node changes"
--     * Slot: old_object_type Description: The type (IRI or Literal) of an old object
--     * Slot: new_object_type Description: The type (IRI or Literal) of a new object
--     * Slot: object_type Description: The type (IRI or Literal) of an object
--     * Slot: language Description: The language tag of a literal
--     * Slot: datatype Description: The datatype of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: about_edge_id Description: 
-- # Class: "NodeDeepening" Description: "A node move in which a node where the destination is a proper descendant of the original location. Note that here descendant applied not just to subclass, but edges of any predicate in the relational graph"
--     * Slot: old_object_type Description: The type (IRI or Literal) of an old object
--     * Slot: new_object_type Description: The type (IRI or Literal) of a new object
--     * Slot: object_type Description: The type (IRI or Literal) of an object
--     * Slot: language Description: The language tag of a literal
--     * Slot: datatype Description: The datatype of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: about_edge_id Description: 
-- # Class: "NodeShallowing" Description: "The opposite of node deepening"
--     * Slot: old_object_type Description: The type (IRI or Literal) of an old object
--     * Slot: new_object_type Description: The type (IRI or Literal) of a new object
--     * Slot: object_type Description: The type (IRI or Literal) of an object
--     * Slot: language Description: The language tag of a literal
--     * Slot: datatype Description: The datatype of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: about_edge_id Description: 
-- # Class: "PredicateChange" Description: "An edge change where the predicate (relationship type) is modified."
--     * Slot: object_type Description: The type (IRI or Literal) of an object
--     * Slot: language Description: The language tag of a literal
--     * Slot: datatype Description: The datatype of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: about_edge_id Description: 
-- # Class: "EdgeLogicalInterpretationChange" Description: "An edge change where the subject, object, and predicate are unchanged, but the logical interpretation changes"
--     * Slot: object_type Description: The type (IRI or Literal) of an object
--     * Slot: language Description: The language tag of a literal
--     * Slot: datatype Description: The datatype of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: about_edge_id Description: 
-- # Class: "LogicalAxiomChange" Description: "A simple change where a logical axiom is changed, where the logical axiom cannot be represented as an edge"
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "NodeChange" Description: "A simple change where the change is about a node"
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "NodeRename" Description: "A node change where the name (aka rdfs:label) of the node changes"
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: has_textual_diff_id Description: A representation of character-level changes on a textual literal property. For example, if a text definition may change by only a single character such as addition of a period, it is useful to be able to see this visually.
-- # Class: "SetLanguageForName" Description: "A node change where the string value for the name is unchanged but the language tag is set"
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "NodeAnnotationChange" Description: "A node change where the change alters node properties/annotations. TODO"
--     * Slot: annotation_property Description: An annotation property
--     * Slot: annotation_property_type Description: The type of a property (URI, CURIE, label) 
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "NodeAnnotationReplacement" Description: "A node annotation change where the change replaces a particular property value. TODO"
--     * Slot: annotation_property Description: An annotation property
--     * Slot: annotation_property_type Description: The type of a property (URI, CURIE, label) 
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "NodeSynonymChange" Description: ""
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "NewSynonym" Description: "A node synonym change where a de-novo synonym is created"
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: language Description: The language tag of a literal
--     * Slot: qualifier Description: The qualifier of a change operation
--     * Slot: predicate Description: 
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "NameBecomesSynonym" Description: "A node synonym where the name NAME of an node NODE moves to a synonym, and NODE receives a new name. This change consists of compose of (1) a node rename where NAME is replaced by a different name (2) a new synonym"
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "RemoveSynonym" Description: "A node synonym change where a synonym is deleted"
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "SynonymReplacement" Description: "A node synonym change where the text of a synonym is changed"
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: qualifier Description: The qualifier of a change operation
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: has_textual_diff_id Description: A representation of character-level changes on a textual literal property. For example, if a text definition may change by only a single character such as addition of a period, it is useful to be able to see this visually.
-- # Class: "SynonymPredicateChange" Description: "A node synonym change where the predicate of a synonym is changed. Background: synonyms can be represented by a variety of predicates. For example, many OBO ontologies make use of predicates such as oio:hasExactSynonym, oio:hasRelatedSynonym, etc"
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: target Description: The secondary entity on which the change operates
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: has_textual_diff_id Description: A representation of character-level changes on a textual literal property. For example, if a text definition may change by only a single character such as addition of a period, it is useful to be able to see this visually.
-- # Class: "NodeMappingChange" Description: "A node change where the mappings for that node are altered"
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "NewMapping" Description: "A node mapping change where a mapping is added to a node"
--     * Slot: object Description: 
--     * Slot: predicate Description: 
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "RemoveMapping" Description: "A node mapping change where a mapping is deleted"
--     * Slot: object Description: 
--     * Slot: predicate Description: 
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "MappingReplacement" Description: "A node mapping change where the object of a mapping is changed"
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "MappingPredicateChange" Description: "A node mapping change where the predicate of a mapping is changed."
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "NodeMetadataAssertionChange" Description: "A node change where the metadata assertion (OWL annotations) for that node are altered"
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "NewMetadataAssertion" Description: "A node metadata assertion change where a metadata assertion is added to a node"
--     * Slot: object Description: 
--     * Slot: predicate Description: 
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "RemoveMetadataAssertion" Description: "A node metadata assertion change where a metadata assertion is deleted"
--     * Slot: object Description: 
--     * Slot: predicate Description: 
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "MetadataAssertionReplacement" Description: "A node metadata assertion change where the object of a metadata assertion is changed"
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "MetadataAssertionPredicateChange" Description: "A node metadata assertion change where the predicate of a metadata assertion is changed."
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "NodeTextDefinitionChange" Description: "A node change where the text definition is changed"
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "NewTextDefinition" Description: "A node change where a de-novo text definition is created"
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "RemoveTextDefinition" Description: "A node change where a text definition is deleted"
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
-- # Class: "TextDefinitionReplacement" Description: "A node change where a text definition is modified"
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: has_textual_diff_id Description: A representation of character-level changes on a textual literal property. For example, if a text definition may change by only a single character such as addition of a period, it is useful to be able to see this visually.
-- # Class: "AddNodeToSubset" Description: "Places a node inside a subset, by annotating that node"
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: in_subset Description: subset that the element is being placed inside.
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "RemoveNodeFromSubset" Description: "Removes a node from a subset, by removing an annotation"
--     * Slot: about_node Description: The node that is removed from the subset
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: in_subset Description: The subset from which the node is to be removed
--     * Slot: has_undo_id Description: A change that reverses this change
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "NodeObsoletion" Description: "Obsoletion of a node deprecates usage of that node, but does not delete it."
--     * Slot: has_direct_replacement Description: An obsoletion replacement where it IS valid to automatically update annotations/edges pointing at the node with its direct replacement
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: MultiNodeObsoletion_id Description: Autocreated FK slot
--     * Slot: has_undo_id Description: A change that reverses this change
--     * Slot: about_id Description: The element that is obsoleted by this change.
-- # Class: "NodeUnobsoletion" Description: "unobsoletion of a node deprecates usage of that node. Rarely applied."
--     * Slot: has_direct_replacement Description: An obsoletion replacement where it IS valid to automatically update annotations/edges pointing at the node with its direct replacement
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: has_undo_id Description: A change that reverses this change
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "NodeCreation" Description: "a node change in which a new node is created"
--     * Slot: node_id Description: id of a node to be created
--     * Slot: name Description: 
--     * Slot: owl_type Description: 
--     * Slot: language Description: The language tag of a literal
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: annotation_set_id Description: 
--     * Slot: has_undo_id Description: A change that reverses this change
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "ClassCreation" Description: "A node creation where the owl type is 'owl:Class'"
--     * Slot: superclass Description: 
--     * Slot: node_id Description: id of a node to be created
--     * Slot: name Description: 
--     * Slot: owl_type Description: 
--     * Slot: language Description: The language tag of a literal
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: annotation_set_id Description: 
--     * Slot: has_undo_id Description: A change that reverses this change
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "ObjectPropertyCreation" Description: "A node creation where the owl type is 'ObjectProperty'"
--     * Slot: node_id Description: id of a node to be created
--     * Slot: name Description: 
--     * Slot: owl_type Description: 
--     * Slot: language Description: The language tag of a literal
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: annotation_set_id Description: 
--     * Slot: has_undo_id Description: A change that reverses this change
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "NodeDeletion" Description: "Deletion of a node from the graph. Note it is recommended nodes are obsoleted and never merged, but this operation exists to represent deletions in ontologies, accidental or otherwise"
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: has_undo Description: A change that reverses this change
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: about_id Description: The 'focus' entity on which the change operates
-- # Class: "NodeDirectMerge" Description: "An obsoletion change in which all metadata (including name/label) from the source node is deleted and added to the target node, and edges can automatically be rewired to point to the target node"
--     * Slot: has_direct_replacement Description: An obsoletion replacement where it IS valid to automatically update annotations/edges pointing at the node with its direct replacement
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: has_undo_id Description: A change that reverses this change
--     * Slot: about_id Description: The element that is obsoleted by this change.
-- # Class: "NodeObsoletionWithDirectReplacement" Description: "An obsoletion change in which information from the obsoleted node is selectively copied to a single target, and edges can automatically be rewired to point to the target node"
--     * Slot: has_direct_replacement Description: An obsoletion replacement where it IS valid to automatically update annotations/edges pointing at the node with its direct replacement
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: has_undo_id Description: A change that reverses this change
--     * Slot: about_id Description: The element that is obsoleted by this change.
-- # Class: "NodeObsoletionWithNoDirectReplacement" Description: "An obsoletion change in which there is no direct replacement"
--     * Slot: has_direct_replacement Description: An obsoletion replacement where it IS valid to automatically update annotations/edges pointing at the node with its direct replacement
--     * Slot: about_node Description: 
--     * Slot: about_node_representation Description: The representation of a node (URI, CURIE, label) 
--     * Slot: language Description: The language tag of a literal
--     * Slot: old_value Description: The value of a property held in the old instance of the ontology
--     * Slot: new_value Description: The value of a property held in the new instance of the ontology
--     * Slot: old_value_type Description: The type (IRI or Literal) of an old value
--     * Slot: new_value_type Description: The type (IRI or Literal) of a new value
--     * Slot: new_language Description: The new language tag of a literal
--     * Slot: old_language Description: The old language tag of a literal
--     * Slot: new_datatype Description: The new datatype of a literal
--     * Slot: old_datatype Description: The old datatype of a literal
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: see_also Description: 
--     * Slot: pull_request Description: 
--     * Slot: term_tracker_issue Description: 
--     * Slot: creator Description: 
--     * Slot: change_date Description: 
--     * Slot: contributor Description: 
--     * Slot: change_description Description: A string serialization of the change. This should be both human-readable, and parseable.
--     * Slot: has_undo_id Description: A change that reverses this change
--     * Slot: about_id Description: The element that is obsoleted by this change.
-- # Class: "TextualDiff" Description: "A summarizing of a change on a piece of text. This could be rendered in a number of different ways"
--     * Slot: id Description: 
-- # Class: "Configuration" Description: "The meaning of operations can be configured"
--     * Slot: id Description: 
--     * Slot: name_predicate Description: 
--     * Slot: definition_predicate Description: 
--     * Slot: main_synonym_predicate Description: 
--     * Slot: synonym_predicates Description: 
--     * Slot: creator_predicate Description: 
--     * Slot: contributor_predicate Description: 
--     * Slot: obsolete_node_label_prefix Description: A prefix to add to the label of an obsolete node. This may include a space at the end.
--     * Slot: obsoletion_workflow Description: 
--     * Slot: obsolete_subclass_of_shadow_property Description: specifies the annotation property to be used to create a shadow annotation assertion triple when a subclass edge is deleted.
-- # Class: "Session" Description: "A session consists of a set of change sets bundled with the activities that generated those change sets"
--     * Slot: id Description: 
-- # Class: "OntologyElement" Description: "Any component of an ontology or knowledge graph"
--     * Slot: id Description: 
-- # Class: "PropertyValue" Description: "a property-value pair"
--     * Slot: id Description: 
--     * Slot: property Description: 
--     * Slot: filler Description: 
-- # Class: "Annotation" Description: "owl annotations. Not to be confused with annotations sensu GO"
--     * Slot: id Description: 
--     * Slot: property Description: 
--     * Slot: filler Description: 
--     * Slot: property_type Description: 
--     * Slot: filler_type Description: 
--     * Slot: annotation_set_id Description: 
-- # Class: "Node" Description: "Any named entity in an ontology. May be a class, individual, property"
--     * Slot: id Description: 
--     * Slot: name Description: 
--     * Slot: owl_type Description: 
--     * Slot: annotation_set_id Description: 
-- # Class: "ClassNode" Description: "A node that is a class"
--     * Slot: id Description: 
--     * Slot: name Description: 
--     * Slot: owl_type Description: 
--     * Slot: annotation_set_id Description: 
-- # Class: "InstanceNode" Description: "A node that is an individual"
--     * Slot: id Description: 
--     * Slot: name Description: 
--     * Slot: owl_type Description: 
--     * Slot: annotation_set_id Description: 
-- # Class: "Edge" Description: "A relationship between two nodes.Currently the only kinds of edges supported in KGCL:  * A subClassOf B <==> Edge(subject=A, predicate=owl:subClassOf, object=B)  * A subClassOf P some B <==> Edge(subject=A, predicate=P, object=B)  * P subPropertyOf Q <==> Edge(subject=P, predicate=owl:subPropertyOf, object=Q)These represent the most common kind of pairwise relationship between classes, and classes are the dominant node type in ontologies.In future a wider variety of OWL axiom types will be supportedn through the use of an additional edge property/slot to indicate the interpretation of the axiom, following owlstar (https://github.com/cmungall/owlstar).For example: * `A subClassOf R only B <==> Edge(subject=A, predicate=P, object=B, interpretation=AllOnly)` * `A Annotation(P,B) <==> Edge(subject=A, predicate=P, object=B, interpretation=annotationAssertion)`Note that not all axioms are intended to map to edges. Axioms/triples where the object is a literal would be represented as node properties. Complex OWL axioms involving nesting would have their own dedicated construct, or may be represented generically. These are out of scope for the current version of KGCL"
--     * Slot: id Description: 
--     * Slot: subject Description: 
--     * Slot: predicate Description: 
--     * Slot: object Description: 
--     * Slot: subject_representation Description: 
--     * Slot: predicate_representation Description: 
--     * Slot: object_representation Description: 
--     * Slot: annotation_set_id Description: 
-- # Class: "LogicalDefinition" Description: ""
--     * Slot: id Description: 
-- # Class: "OntologySubset" Description: ""
--     * Slot: id Description: 
--     * Slot: name Description: 
--     * Slot: owl_type Description: 
--     * Slot: annotation_set_id Description: 
-- # Class: "ProvElement" Description: "A grouping for prov elements"
--     * Slot: id Description: 
-- # Class: "Activity" Description: "a provence-generating activity"
--     * Slot: id Description: 
--     * Slot: started_at_time Description: 
--     * Slot: ended_at_time Description: 
--     * Slot: was_informed_by Description: 
--     * Slot: was_associated_with Description: 
--     * Slot: used Description: 
--     * Slot: description Description: 
--     * Slot: Session_id Description: Autocreated FK slot
-- # Class: "Agent" Description: "a provence-generating agent"
--     * Slot: id Description: 
--     * Slot: acted_on_behalf_of Description: 
--     * Slot: was_informed_by Description: 
-- # Class: "NodeObsoletion_has_nondirect_replacement" Description: ""
--     * Slot: NodeObsoletion_id Description: Autocreated FK slot
--     * Slot: has_nondirect_replacement_id Description: An obsoletion replacement where it is NOT valid to automatically update annotations/edges pointing at the node with its direct replacement
-- # Class: "NodeUnobsoletion_has_nondirect_replacement" Description: ""
--     * Slot: NodeUnobsoletion_id Description: Autocreated FK slot
--     * Slot: has_nondirect_replacement_id Description: An obsoletion replacement where it is NOT valid to automatically update annotations/edges pointing at the node with its direct replacement
-- # Class: "NodeDirectMerge_has_nondirect_replacement" Description: ""
--     * Slot: NodeDirectMerge_id Description: Autocreated FK slot
--     * Slot: has_nondirect_replacement_id Description: An obsoletion replacement where it is NOT valid to automatically update annotations/edges pointing at the node with its direct replacement
-- # Class: "NodeObsoletionWithDirectReplacement_has_nondirect_replacement" Description: ""
--     * Slot: NodeObsoletionWithDirectReplacement_id Description: Autocreated FK slot
--     * Slot: has_nondirect_replacement_id Description: An obsoletion replacement where it is NOT valid to automatically update annotations/edges pointing at the node with its direct replacement
-- # Class: "NodeObsoletionWithNoDirectReplacement_has_nondirect_replacement" Description: ""
--     * Slot: NodeObsoletionWithNoDirectReplacement_id Description: Autocreated FK slot
--     * Slot: has_nondirect_replacement_id Description: An obsoletion replacement where it is NOT valid to automatically update annotations/edges pointing at the node with its direct replacement
-- # Class: "Configuration_obsoletion_policies" Description: ""
--     * Slot: Configuration_id Description: Autocreated FK slot
--     * Slot: obsoletion_policies Description: 

CREATE TABLE "ChangeLanguageElement" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Change" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	"Change_id" TEXT, 
	"SimpleChange_id" TEXT, 
	"ComplexChange_id" TEXT, 
	"MultiNodeObsoletion_id" TEXT, 
	"Transaction_id" TEXT, 
	"EdgeChange_id" TEXT, 
	"EdgeCreation_id" TEXT, 
	"PlaceUnder_id" TEXT, 
	"EdgeDeletion_id" TEXT, 
	"RemoveUnder_id" TEXT, 
	"EdgeObsoletion_id" TEXT, 
	"EdgeRewiring_id" TEXT, 
	"MappingCreation_id" TEXT, 
	"NodeMove_id" TEXT, 
	"NodeDeepening_id" TEXT, 
	"NodeShallowing_id" TEXT, 
	"PredicateChange_id" TEXT, 
	"EdgeLogicalInterpretationChange_id" TEXT, 
	"LogicalAxiomChange_id" TEXT, 
	"NodeChange_id" TEXT, 
	"NodeRename_id" TEXT, 
	"SetLanguageForName_id" TEXT, 
	"NodeAnnotationChange_id" TEXT, 
	"NodeAnnotationReplacement_id" TEXT, 
	"NodeSynonymChange_id" TEXT, 
	"NewSynonym_id" TEXT, 
	"NameBecomesSynonym_id" TEXT, 
	"RemoveSynonym_id" TEXT, 
	"SynonymReplacement_id" TEXT, 
	"SynonymPredicateChange_id" TEXT, 
	"NodeMappingChange_id" TEXT, 
	"NewMapping_id" TEXT, 
	"RemoveMapping_id" TEXT, 
	"MappingReplacement_id" TEXT, 
	"MappingPredicateChange_id" TEXT, 
	"NodeMetadataAssertionChange_id" TEXT, 
	"NewMetadataAssertion_id" TEXT, 
	"RemoveMetadataAssertion_id" TEXT, 
	"MetadataAssertionReplacement_id" TEXT, 
	"MetadataAssertionPredicateChange_id" TEXT, 
	"NodeTextDefinitionChange_id" TEXT, 
	"NewTextDefinition_id" TEXT, 
	"RemoveTextDefinition_id" TEXT, 
	"TextDefinitionReplacement_id" TEXT, 
	"AddNodeToSubset_id" TEXT, 
	"RemoveNodeFromSubset_id" TEXT, 
	"NodeObsoletion_id" TEXT, 
	"NodeUnobsoletion_id" TEXT, 
	"NodeCreation_id" TEXT, 
	"ClassCreation_id" TEXT, 
	"ObjectPropertyCreation_id" TEXT, 
	"NodeDeletion_id" TEXT, 
	"NodeDirectMerge_id" TEXT, 
	"NodeObsoletionWithDirectReplacement_id" TEXT, 
	"NodeObsoletionWithNoDirectReplacement_id" TEXT, 
	"Session_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY("Change_id") REFERENCES "Change" (id), 
	FOREIGN KEY("SimpleChange_id") REFERENCES "SimpleChange" (id), 
	FOREIGN KEY("ComplexChange_id") REFERENCES "ComplexChange" (id), 
	FOREIGN KEY("MultiNodeObsoletion_id") REFERENCES "MultiNodeObsoletion" (id), 
	FOREIGN KEY("Transaction_id") REFERENCES "Transaction" (id), 
	FOREIGN KEY("EdgeChange_id") REFERENCES "EdgeChange" (id), 
	FOREIGN KEY("EdgeCreation_id") REFERENCES "EdgeCreation" (id), 
	FOREIGN KEY("PlaceUnder_id") REFERENCES "PlaceUnder" (id), 
	FOREIGN KEY("EdgeDeletion_id") REFERENCES "EdgeDeletion" (id), 
	FOREIGN KEY("RemoveUnder_id") REFERENCES "RemoveUnder" (id), 
	FOREIGN KEY("EdgeObsoletion_id") REFERENCES "EdgeObsoletion" (id), 
	FOREIGN KEY("EdgeRewiring_id") REFERENCES "EdgeRewiring" (id), 
	FOREIGN KEY("MappingCreation_id") REFERENCES "MappingCreation" (id), 
	FOREIGN KEY("NodeMove_id") REFERENCES "NodeMove" (id), 
	FOREIGN KEY("NodeDeepening_id") REFERENCES "NodeDeepening" (id), 
	FOREIGN KEY("NodeShallowing_id") REFERENCES "NodeShallowing" (id), 
	FOREIGN KEY("PredicateChange_id") REFERENCES "PredicateChange" (id), 
	FOREIGN KEY("EdgeLogicalInterpretationChange_id") REFERENCES "EdgeLogicalInterpretationChange" (id), 
	FOREIGN KEY("LogicalAxiomChange_id") REFERENCES "LogicalAxiomChange" (id), 
	FOREIGN KEY("NodeChange_id") REFERENCES "NodeChange" (id), 
	FOREIGN KEY("NodeRename_id") REFERENCES "NodeRename" (id), 
	FOREIGN KEY("SetLanguageForName_id") REFERENCES "SetLanguageForName" (id), 
	FOREIGN KEY("NodeAnnotationChange_id") REFERENCES "NodeAnnotationChange" (id), 
	FOREIGN KEY("NodeAnnotationReplacement_id") REFERENCES "NodeAnnotationReplacement" (id), 
	FOREIGN KEY("NodeSynonymChange_id") REFERENCES "NodeSynonymChange" (id), 
	FOREIGN KEY("NewSynonym_id") REFERENCES "NewSynonym" (id), 
	FOREIGN KEY("NameBecomesSynonym_id") REFERENCES "NameBecomesSynonym" (id), 
	FOREIGN KEY("RemoveSynonym_id") REFERENCES "RemoveSynonym" (id), 
	FOREIGN KEY("SynonymReplacement_id") REFERENCES "SynonymReplacement" (id), 
	FOREIGN KEY("SynonymPredicateChange_id") REFERENCES "SynonymPredicateChange" (id), 
	FOREIGN KEY("NodeMappingChange_id") REFERENCES "NodeMappingChange" (id), 
	FOREIGN KEY("NewMapping_id") REFERENCES "NewMapping" (id), 
	FOREIGN KEY("RemoveMapping_id") REFERENCES "RemoveMapping" (id), 
	FOREIGN KEY("MappingReplacement_id") REFERENCES "MappingReplacement" (id), 
	FOREIGN KEY("MappingPredicateChange_id") REFERENCES "MappingPredicateChange" (id), 
	FOREIGN KEY("NodeMetadataAssertionChange_id") REFERENCES "NodeMetadataAssertionChange" (id), 
	FOREIGN KEY("NewMetadataAssertion_id") REFERENCES "NewMetadataAssertion" (id), 
	FOREIGN KEY("RemoveMetadataAssertion_id") REFERENCES "RemoveMetadataAssertion" (id), 
	FOREIGN KEY("MetadataAssertionReplacement_id") REFERENCES "MetadataAssertionReplacement" (id), 
	FOREIGN KEY("MetadataAssertionPredicateChange_id") REFERENCES "MetadataAssertionPredicateChange" (id), 
	FOREIGN KEY("NodeTextDefinitionChange_id") REFERENCES "NodeTextDefinitionChange" (id), 
	FOREIGN KEY("NewTextDefinition_id") REFERENCES "NewTextDefinition" (id), 
	FOREIGN KEY("RemoveTextDefinition_id") REFERENCES "RemoveTextDefinition" (id), 
	FOREIGN KEY("TextDefinitionReplacement_id") REFERENCES "TextDefinitionReplacement" (id), 
	FOREIGN KEY("AddNodeToSubset_id") REFERENCES "AddNodeToSubset" (id), 
	FOREIGN KEY("RemoveNodeFromSubset_id") REFERENCES "RemoveNodeFromSubset" (id), 
	FOREIGN KEY("NodeObsoletion_id") REFERENCES "NodeObsoletion" (id), 
	FOREIGN KEY("NodeUnobsoletion_id") REFERENCES "NodeUnobsoletion" (id), 
	FOREIGN KEY("NodeCreation_id") REFERENCES "NodeCreation" (id), 
	FOREIGN KEY("ClassCreation_id") REFERENCES "ClassCreation" (id), 
	FOREIGN KEY("ObjectPropertyCreation_id") REFERENCES "ObjectPropertyCreation" (id), 
	FOREIGN KEY("NodeDeletion_id") REFERENCES "NodeDeletion" (id), 
	FOREIGN KEY("NodeDirectMerge_id") REFERENCES "NodeDirectMerge" (id), 
	FOREIGN KEY("NodeObsoletionWithDirectReplacement_id") REFERENCES "NodeObsoletionWithDirectReplacement" (id), 
	FOREIGN KEY("NodeObsoletionWithNoDirectReplacement_id") REFERENCES "NodeObsoletionWithNoDirectReplacement" (id), 
	FOREIGN KEY("Session_id") REFERENCES "Session" (id)
);
CREATE TABLE "SimpleChange" (
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "ComplexChange" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "MultiNodeObsoletion" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "Transaction" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "ChangeSetSummaryStatistic" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Deletion" (
	id INTEGER NOT NULL, 
	has_undo TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "AddToSubset" (
	id INTEGER NOT NULL, 
	in_subset TEXT, 
	has_undo TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(in_subset) REFERENCES "OntologySubset" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "EdgeChange" (
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	about_edge_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(about_edge_id) REFERENCES "Edge" (id)
);
CREATE TABLE "EdgeCreation" (
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	subject_type TEXT, 
	predicate_type TEXT, 
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	change_description TEXT, 
	annotation_set_id INTEGER, 
	about_edge_id INTEGER, 
	has_undo_id INTEGER, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(annotation_set_id) REFERENCES "Annotation" (id), 
	FOREIGN KEY(about_edge_id) REFERENCES "Edge" (id), 
	FOREIGN KEY(has_undo_id) REFERENCES "Deletion" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "PlaceUnder" (
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	subject_type TEXT, 
	predicate_type TEXT, 
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	change_description TEXT, 
	annotation_set_id INTEGER, 
	about_edge_id INTEGER, 
	has_undo_id INTEGER, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(annotation_set_id) REFERENCES "Annotation" (id), 
	FOREIGN KEY(about_edge_id) REFERENCES "Edge" (id), 
	FOREIGN KEY(has_undo_id) REFERENCES "Deletion" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "EdgeDeletion" (
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	subject_type TEXT, 
	predicate_type TEXT, 
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	annotation_set_id INTEGER, 
	about_edge_id INTEGER, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(annotation_set_id) REFERENCES "Annotation" (id), 
	FOREIGN KEY(about_edge_id) REFERENCES "Edge" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "RemoveUnder" (
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	subject_type TEXT, 
	predicate_type TEXT, 
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	annotation_set_id INTEGER, 
	about_edge_id INTEGER, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(annotation_set_id) REFERENCES "Annotation" (id), 
	FOREIGN KEY(about_edge_id) REFERENCES "Edge" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "EdgeRewiring" (
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	about_edge_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(about_edge_id) REFERENCES "Edge" (id)
);
CREATE TABLE "MappingCreation" (
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	subject_type TEXT, 
	predicate_type TEXT, 
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	change_description TEXT, 
	annotation_set_id INTEGER, 
	about_edge_id INTEGER, 
	has_undo_id INTEGER, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(annotation_set_id) REFERENCES "Annotation" (id), 
	FOREIGN KEY(about_edge_id) REFERENCES "Edge" (id), 
	FOREIGN KEY(has_undo_id) REFERENCES "Deletion" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "NodeMove" (
	old_object_type TEXT, 
	new_object_type TEXT, 
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	about_edge_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(about_edge_id) REFERENCES "Edge" (id)
);
CREATE TABLE "NodeDeepening" (
	old_object_type TEXT, 
	new_object_type TEXT, 
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	about_edge_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(about_edge_id) REFERENCES "Edge" (id)
);
CREATE TABLE "NodeShallowing" (
	old_object_type TEXT, 
	new_object_type TEXT, 
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	about_edge_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(about_edge_id) REFERENCES "Edge" (id)
);
CREATE TABLE "PredicateChange" (
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	about_edge_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(about_edge_id) REFERENCES "Edge" (id)
);
CREATE TABLE "EdgeLogicalInterpretationChange" (
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	about_edge_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(about_edge_id) REFERENCES "Edge" (id)
);
CREATE TABLE "LogicalAxiomChange" (
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "NodeChange" (
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "NodeRename" (
	old_value TEXT, 
	new_value TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	has_textual_diff_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(has_textual_diff_id) REFERENCES "TextualDiff" (id)
);
CREATE TABLE "SetLanguageForName" (
	old_value TEXT, 
	new_value TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "NodeAnnotationChange" (
	annotation_property TEXT, 
	annotation_property_type TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "NodeAnnotationReplacement" (
	annotation_property TEXT, 
	annotation_property_type TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "NodeSynonymChange" (
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "NewSynonym" (
	new_value TEXT, 
	language TEXT, 
	qualifier TEXT, 
	predicate TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	old_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "NameBecomesSynonym" (
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "RemoveSynonym" (
	old_value TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "SynonymReplacement" (
	old_value TEXT, 
	new_value TEXT, 
	qualifier TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	has_textual_diff_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(has_textual_diff_id) REFERENCES "TextualDiff" (id)
);
CREATE TABLE "SynonymPredicateChange" (
	old_value TEXT, 
	new_value TEXT, 
	target TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	has_textual_diff_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(has_textual_diff_id) REFERENCES "TextualDiff" (id)
);
CREATE TABLE "NodeMappingChange" (
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "NewMapping" (
	object TEXT, 
	predicate TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "RemoveMapping" (
	object TEXT, 
	predicate TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "MappingReplacement" (
	old_value TEXT, 
	new_value TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "MappingPredicateChange" (
	old_value TEXT, 
	new_value TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "NodeMetadataAssertionChange" (
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "NewMetadataAssertion" (
	object TEXT, 
	predicate TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "RemoveMetadataAssertion" (
	object TEXT, 
	predicate TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "MetadataAssertionReplacement" (
	old_value TEXT, 
	new_value TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "MetadataAssertionPredicateChange" (
	old_value TEXT, 
	new_value TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "NodeTextDefinitionChange" (
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "NewTextDefinition" (
	new_value TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "RemoveTextDefinition" (
	old_value TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id)
);
CREATE TABLE "TextDefinitionReplacement" (
	old_value TEXT, 
	new_value TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	has_textual_diff_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(has_textual_diff_id) REFERENCES "TextualDiff" (id)
);
CREATE TABLE "AddNodeToSubset" (
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	in_subset TEXT, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(in_subset) REFERENCES "OntologySubset" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "RemoveNodeFromSubset" (
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	change_description TEXT, 
	in_subset TEXT, 
	has_undo_id INTEGER, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(in_subset) REFERENCES "OntologySubset" (id), 
	FOREIGN KEY(has_undo_id) REFERENCES "AddToSubset" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "NodeObsoletion" (
	has_direct_replacement TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	change_description TEXT, 
	"MultiNodeObsoletion_id" TEXT, 
	has_undo_id INTEGER, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_direct_replacement) REFERENCES "Node" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY("MultiNodeObsoletion_id") REFERENCES "MultiNodeObsoletion" (id), 
	FOREIGN KEY(has_undo_id) REFERENCES "Obsoletion" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "NodeCreation" (
	node_id TEXT, 
	name TEXT, 
	owl_type VARCHAR(16), 
	language TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	change_description TEXT, 
	annotation_set_id INTEGER, 
	has_undo_id INTEGER, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(node_id) REFERENCES "Node" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(annotation_set_id) REFERENCES "Annotation" (id), 
	FOREIGN KEY(has_undo_id) REFERENCES "Deletion" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "ClassCreation" (
	superclass TEXT, 
	node_id TEXT, 
	name TEXT, 
	owl_type VARCHAR(16), 
	language TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	change_description TEXT, 
	annotation_set_id INTEGER, 
	has_undo_id INTEGER, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(superclass) REFERENCES "Node" (id), 
	FOREIGN KEY(node_id) REFERENCES "Node" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(annotation_set_id) REFERENCES "Annotation" (id), 
	FOREIGN KEY(has_undo_id) REFERENCES "Deletion" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "ObjectPropertyCreation" (
	node_id TEXT, 
	name TEXT, 
	owl_type VARCHAR(16), 
	language TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	change_description TEXT, 
	annotation_set_id INTEGER, 
	has_undo_id INTEGER, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(node_id) REFERENCES "Node" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(annotation_set_id) REFERENCES "Annotation" (id), 
	FOREIGN KEY(has_undo_id) REFERENCES "Deletion" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "NodeDeletion" (
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	change_description TEXT, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "TextualDiff" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Configuration" (
	id INTEGER NOT NULL, 
	name_predicate TEXT, 
	definition_predicate TEXT, 
	main_synonym_predicate TEXT, 
	synonym_predicates TEXT, 
	creator_predicate TEXT, 
	contributor_predicate TEXT, 
	obsolete_node_label_prefix TEXT, 
	obsoletion_workflow TEXT, 
	obsolete_subclass_of_shadow_property TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Session" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "OntologyElement" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Annotation" (
	id INTEGER NOT NULL, 
	property TEXT, 
	filler TEXT, 
	property_type TEXT, 
	filler_type TEXT, 
	annotation_set_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(property) REFERENCES "Node" (id), 
	FOREIGN KEY(annotation_set_id) REFERENCES "Annotation" (id)
);
CREATE TABLE "Node" (
	id TEXT NOT NULL, 
	name TEXT, 
	owl_type VARCHAR(16), 
	annotation_set_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(annotation_set_id) REFERENCES "Annotation" (id)
);
CREATE TABLE "LogicalDefinition" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ProvElement" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Activity" (
	id TEXT NOT NULL, 
	started_at_time TEXT, 
	ended_at_time TEXT, 
	was_informed_by TEXT, 
	was_associated_with TEXT, 
	used TEXT, 
	description TEXT, 
	"Session_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(was_associated_with) REFERENCES "Agent" (id), 
	FOREIGN KEY("Session_id") REFERENCES "Session" (id)
);
CREATE TABLE "Agent" (
	id TEXT NOT NULL, 
	acted_on_behalf_of TEXT, 
	was_informed_by TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(acted_on_behalf_of) REFERENCES "Agent" (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id)
);
CREATE TABLE "ChangeMixin" (
	id INTEGER NOT NULL, 
	has_undo TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "Obsoletion" (
	id INTEGER NOT NULL, 
	old_value TEXT, 
	new_value TEXT, 
	about_id INTEGER, 
	has_undo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id), 
	FOREIGN KEY(has_undo_id) REFERENCES "Obsoletion" (id)
);
CREATE TABLE "DatatypeOrLanguageTagChange" (
	id INTEGER NOT NULL, 
	has_undo TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "LanguageTagChange" (
	id INTEGER NOT NULL, 
	has_undo TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "DatatypeChange" (
	id INTEGER NOT NULL, 
	has_undo TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "Creation" (
	id INTEGER NOT NULL, 
	old_value TEXT, 
	new_value TEXT, 
	about_id INTEGER, 
	has_undo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id), 
	FOREIGN KEY(has_undo_id) REFERENCES "Deletion" (id)
);
CREATE TABLE "PropertyValue" (
	id INTEGER NOT NULL, 
	property TEXT, 
	filler TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(property) REFERENCES "Node" (id)
);
CREATE TABLE "ClassNode" (
	id TEXT NOT NULL, 
	name TEXT, 
	owl_type VARCHAR(16), 
	annotation_set_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(annotation_set_id) REFERENCES "Annotation" (id)
);
CREATE TABLE "InstanceNode" (
	id TEXT NOT NULL, 
	name TEXT, 
	owl_type VARCHAR(16), 
	annotation_set_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(annotation_set_id) REFERENCES "Annotation" (id)
);
CREATE TABLE "Edge" (
	id INTEGER NOT NULL, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	subject_representation TEXT, 
	predicate_representation TEXT, 
	object_representation TEXT, 
	annotation_set_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id), 
	FOREIGN KEY(annotation_set_id) REFERENCES "Annotation" (id)
);
CREATE TABLE "OntologySubset" (
	id TEXT NOT NULL, 
	name TEXT, 
	owl_type VARCHAR(16), 
	annotation_set_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(annotation_set_id) REFERENCES "Annotation" (id)
);
CREATE TABLE "NodeObsoletion_has_nondirect_replacement" (
	"NodeObsoletion_id" TEXT, 
	has_nondirect_replacement_id TEXT, 
	PRIMARY KEY ("NodeObsoletion_id", has_nondirect_replacement_id), 
	FOREIGN KEY("NodeObsoletion_id") REFERENCES "NodeObsoletion" (id), 
	FOREIGN KEY(has_nondirect_replacement_id) REFERENCES "Node" (id)
);
CREATE TABLE "Configuration_obsoletion_policies" (
	"Configuration_id" INTEGER, 
	obsoletion_policies VARCHAR(26), 
	PRIMARY KEY ("Configuration_id", obsoletion_policies), 
	FOREIGN KEY("Configuration_id") REFERENCES "Configuration" (id)
);
CREATE TABLE "AllowsAutomaticReplacementOfEdges" (
	id INTEGER NOT NULL, 
	old_value TEXT, 
	new_value TEXT, 
	about_id INTEGER, 
	has_undo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id), 
	FOREIGN KEY(has_undo_id) REFERENCES "Obsoletion" (id)
);
CREATE TABLE "Unobsoletion" (
	id INTEGER NOT NULL, 
	old_value TEXT, 
	new_value TEXT, 
	about_id INTEGER, 
	has_undo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id), 
	FOREIGN KEY(has_undo_id) REFERENCES "Obsoletion" (id)
);
CREATE TABLE "SubsetMembershipChange" (
	id INTEGER NOT NULL, 
	in_subset TEXT, 
	has_undo TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(in_subset) REFERENCES "OntologySubset" (id), 
	FOREIGN KEY(has_undo) REFERENCES "Change" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "RemoveFromSubset" (
	id INTEGER NOT NULL, 
	in_subset TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	about_id INTEGER, 
	has_undo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(in_subset) REFERENCES "OntologySubset" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id), 
	FOREIGN KEY(has_undo_id) REFERENCES "AddToSubset" (id)
);
CREATE TABLE "EdgeObsoletion" (
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	change_description TEXT, 
	annotation_set_id INTEGER, 
	about_edge_id INTEGER, 
	has_undo_id INTEGER, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(annotation_set_id) REFERENCES "Annotation" (id), 
	FOREIGN KEY(about_edge_id) REFERENCES "Edge" (id), 
	FOREIGN KEY(has_undo_id) REFERENCES "Obsoletion" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "NodeUnobsoletion" (
	has_direct_replacement TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	change_description TEXT, 
	has_undo_id INTEGER, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_direct_replacement) REFERENCES "Node" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo_id) REFERENCES "Obsoletion" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "NodeDirectMerge" (
	has_direct_replacement TEXT NOT NULL, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	change_description TEXT, 
	has_undo_id INTEGER, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_direct_replacement) REFERENCES "Node" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo_id) REFERENCES "Obsoletion" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "NodeObsoletionWithDirectReplacement" (
	has_direct_replacement TEXT NOT NULL, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	change_description TEXT, 
	has_undo_id INTEGER, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_direct_replacement) REFERENCES "Node" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo_id) REFERENCES "Obsoletion" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "NodeObsoletionWithNoDirectReplacement" (
	has_direct_replacement TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	term_tracker_issue TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	change_description TEXT, 
	has_undo_id INTEGER, 
	about_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_direct_replacement) REFERENCES "Node" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_undo_id) REFERENCES "Obsoletion" (id), 
	FOREIGN KEY(about_id) REFERENCES "OntologyElement" (id)
);
CREATE TABLE "NodeUnobsoletion_has_nondirect_replacement" (
	"NodeUnobsoletion_id" TEXT, 
	has_nondirect_replacement_id TEXT, 
	PRIMARY KEY ("NodeUnobsoletion_id", has_nondirect_replacement_id), 
	FOREIGN KEY("NodeUnobsoletion_id") REFERENCES "NodeUnobsoletion" (id), 
	FOREIGN KEY(has_nondirect_replacement_id) REFERENCES "Node" (id)
);
CREATE TABLE "NodeDirectMerge_has_nondirect_replacement" (
	"NodeDirectMerge_id" TEXT, 
	has_nondirect_replacement_id TEXT, 
	PRIMARY KEY ("NodeDirectMerge_id", has_nondirect_replacement_id), 
	FOREIGN KEY("NodeDirectMerge_id") REFERENCES "NodeDirectMerge" (id), 
	FOREIGN KEY(has_nondirect_replacement_id) REFERENCES "Node" (id)
);
CREATE TABLE "NodeObsoletionWithDirectReplacement_has_nondirect_replacement" (
	"NodeObsoletionWithDirectReplacement_id" TEXT, 
	has_nondirect_replacement_id TEXT, 
	PRIMARY KEY ("NodeObsoletionWithDirectReplacement_id", has_nondirect_replacement_id), 
	FOREIGN KEY("NodeObsoletionWithDirectReplacement_id") REFERENCES "NodeObsoletionWithDirectReplacement" (id), 
	FOREIGN KEY(has_nondirect_replacement_id) REFERENCES "Node" (id)
);
CREATE TABLE "NodeObsoletionWithNoDirectReplacement_has_nondirect_replacement" (
	"NodeObsoletionWithNoDirectReplacement_id" TEXT, 
	has_nondirect_replacement_id TEXT NOT NULL, 
	PRIMARY KEY ("NodeObsoletionWithNoDirectReplacement_id", has_nondirect_replacement_id), 
	FOREIGN KEY("NodeObsoletionWithNoDirectReplacement_id") REFERENCES "NodeObsoletionWithNoDirectReplacement" (id), 
	FOREIGN KEY(has_nondirect_replacement_id) REFERENCES "Node" (id)
);