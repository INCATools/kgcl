

CREATE TABLE "Activity" (
	id TEXT NOT NULL, 
	started_at_time TEXT, 
	ended_at_time TEXT, 
	was_informed_by TEXT, 
	was_associated_with TEXT, 
	used TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(was_associated_with) REFERENCES "Agent" (id)
);

CREATE TABLE "Agent" (
	id TEXT NOT NULL, 
	acted_on_behalf_of TEXT, 
	was_informed_by TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(acted_on_behalf_of) REFERENCES "Agent" (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id)
);

CREATE TABLE "ChangeSetSummaryStatistic" (
	change_type TEXT, 
	count INTEGER, 
	property_value_set TEXT, 
	PRIMARY KEY (change_type, count, property_value_set)
);

CREATE TABLE "ClassNode" (
	id TEXT NOT NULL, 
	name TEXT, 
	annotation_set TEXT, 
	owl_type VARCHAR(16), 
	PRIMARY KEY (id)
);

CREATE TABLE "Configuration" (
	name_predicate TEXT, 
	definition_predicate TEXT, 
	main_synonym_predicate TEXT, 
	synonym_predicates TEXT, 
	creator_predicate TEXT, 
	contributor_predicate TEXT, 
	obsolete_node_label_prefix TEXT, 
	obsoletion_workflow TEXT, 
	obsoletion_policies VARCHAR(26), 
	obsolete_subclass_of_shadow_property TEXT, 
	PRIMARY KEY (name_predicate, definition_predicate, main_synonym_predicate, synonym_predicates, creator_predicate, contributor_predicate, obsolete_node_label_prefix, obsoletion_workflow, obsoletion_policies, obsolete_subclass_of_shadow_property)
);

CREATE TABLE "InstanceNode" (
	id TEXT NOT NULL, 
	name TEXT, 
	annotation_set TEXT, 
	owl_type VARCHAR(16), 
	PRIMARY KEY (id)
);

CREATE TABLE "LanguageTagChange" (
	old_value TEXT, 
	new_value TEXT, 
	PRIMARY KEY (old_value, new_value)
);

CREATE TABLE "Node" (
	id TEXT NOT NULL, 
	name TEXT, 
	annotation_set TEXT, 
	owl_type VARCHAR(16), 
	PRIMARY KEY (id)
);

CREATE TABLE "Session" (
	change_set TEXT, 
	activity_set TEXT, 
	PRIMARY KEY (change_set, activity_set)
);

CREATE TABLE "AddNodeToSubset" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	in_subset TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "Annotation" (
	property TEXT, 
	filler TEXT, 
	annotation_set TEXT, 
	property_type TEXT, 
	filler_type TEXT, 
	PRIMARY KEY (property, filler, annotation_set, property_type, filler_type), 
	FOREIGN KEY(property) REFERENCES "Node" (id)
);

CREATE TABLE "ClassCreation" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	node_id TEXT, 
	name TEXT, 
	owl_type VARCHAR(16), 
	annotation_set TEXT, 
	language TEXT, 
	superclass TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(node_id) REFERENCES "Node" (id), 
	FOREIGN KEY(superclass) REFERENCES "Node" (id)
);

CREATE TABLE "Edge" (
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	subject_representation TEXT, 
	predicate_representation TEXT, 
	object_representation TEXT, 
	annotation_set TEXT, 
	PRIMARY KEY (subject, predicate, object, subject_representation, predicate_representation, object_representation, annotation_set), 
	FOREIGN KEY(subject) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id)
);

CREATE TABLE "EdgeCreation" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_edge TEXT, 
	language TEXT, 
	datatype TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	subject_type TEXT, 
	predicate_type TEXT, 
	object_type TEXT, 
	annotation_set TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id)
);

CREATE TABLE "EdgeDeletion" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_edge TEXT, 
	language TEXT, 
	datatype TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	subject_type TEXT, 
	predicate_type TEXT, 
	object_type TEXT, 
	annotation_set TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id)
);

CREATE TABLE "EdgeLogicalInterpretationChange" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_edge TEXT, 
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	subject TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id)
);

CREATE TABLE "EdgeObsoletion" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_edge TEXT, 
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	annotation_set TEXT, 
	change_description TEXT, 
	about TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id)
);

CREATE TABLE "EdgeRewiring" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_edge TEXT, 
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	subject TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id)
);

CREATE TABLE "LogicalAxiomChange" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id)
);

CREATE TABLE "MappingCreation" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_edge TEXT, 
	language TEXT, 
	datatype TEXT, 
	subject_type TEXT, 
	predicate_type TEXT, 
	object_type TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	annotation_set TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id)
);

CREATE TABLE "MappingPredicateChange" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "MappingReplacement" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "MetadataAssertionPredicateChange" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "MetadataAssertionReplacement" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "MultiNodeObsoletion" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id)
);

CREATE TABLE "NewMapping" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	object TEXT, 
	predicate TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id)
);

CREATE TABLE "NewMetadataAssertion" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	object TEXT, 
	predicate TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id)
);

CREATE TABLE "NewSynonym" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	new_value TEXT, 
	language TEXT, 
	qualifier TEXT, 
	predicate TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id)
);

CREATE TABLE "NewTextDefinition" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	new_value TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "NodeAnnotationChange" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	annotation_property TEXT, 
	annotation_property_type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "NodeAnnotationReplacement" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	annotation_property TEXT, 
	annotation_property_type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "NodeCreation" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	node_id TEXT, 
	name TEXT, 
	owl_type VARCHAR(16), 
	annotation_set TEXT, 
	language TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(node_id) REFERENCES "Node" (id)
);

CREATE TABLE "NodeDeepening" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_edge TEXT, 
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	subject TEXT, 
	old_object_type TEXT, 
	new_object_type TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id)
);

CREATE TABLE "NodeDeletion" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "NodeDirectMerge" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	has_nondirect_replacement TEXT, 
	about TEXT, 
	has_direct_replacement TEXT NOT NULL, 
	about_node TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(has_direct_replacement) REFERENCES "Node" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "NodeMappingChange" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "NodeMetadataAssertionChange" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "NodeMove" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_edge TEXT, 
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	subject TEXT, 
	old_object_type TEXT, 
	new_object_type TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id)
);

CREATE TABLE "NodeObsoletionWithDirectReplacement" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	has_nondirect_replacement TEXT, 
	about TEXT, 
	has_direct_replacement TEXT NOT NULL, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(has_direct_replacement) REFERENCES "Node" (id)
);

CREATE TABLE "NodeObsoletionWithNoDirectReplacement" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	has_direct_replacement TEXT, 
	about TEXT, 
	has_nondirect_replacement TEXT NOT NULL, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(has_direct_replacement) REFERENCES "Node" (id)
);

CREATE TABLE "NodeRename" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	has_textual_diff TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "NodeShallowing" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_edge TEXT, 
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	subject TEXT, 
	old_object_type TEXT, 
	new_object_type TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id)
);

CREATE TABLE "NodeSynonymChange" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "NodeUnobsoletion" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	change_description TEXT, 
	replaced_by TEXT, 
	consider TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(replaced_by) REFERENCES "Node" (id), 
	FOREIGN KEY(consider) REFERENCES "Node" (id)
);

CREATE TABLE "ObjectPropertyCreation" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	node_id TEXT, 
	name TEXT, 
	owl_type VARCHAR(16), 
	annotation_set TEXT, 
	language TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(node_id) REFERENCES "Node" (id)
);

CREATE TABLE "PlaceUnder" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_edge TEXT, 
	language TEXT, 
	datatype TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	subject_type TEXT, 
	predicate_type TEXT, 
	object_type TEXT, 
	annotation_set TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id)
);

CREATE TABLE "PredicateChange" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_edge TEXT, 
	object_type TEXT, 
	language TEXT, 
	datatype TEXT, 
	subject TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id)
);

CREATE TABLE "PropertyValue" (
	property TEXT, 
	filler TEXT, 
	PRIMARY KEY (property, filler), 
	FOREIGN KEY(property) REFERENCES "Node" (id)
);

CREATE TABLE "RemoveMapping" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	object TEXT, 
	predicate TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id)
);

CREATE TABLE "RemoveMetadataAssertion" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	object TEXT, 
	predicate TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id)
);

CREATE TABLE "RemoveNodeFromSubset" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	change_description TEXT, 
	about_node TEXT, 
	subset TEXT, 
	in_subset TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "RemoveSynonym" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "RemoveTextDefinition" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "RemoveUnder" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_edge TEXT, 
	language TEXT, 
	datatype TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	subject_type TEXT, 
	predicate_type TEXT, 
	object_type TEXT, 
	annotation_set TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(subject) REFERENCES "Node" (id), 
	FOREIGN KEY(predicate) REFERENCES "Node" (id), 
	FOREIGN KEY(object) REFERENCES "Node" (id)
);

CREATE TABLE "SetLanguageForName" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "SynonymPredicateChange" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	has_textual_diff TEXT, 
	target TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "SynonymReplacement" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	has_textual_diff TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "TextDefinitionReplacement" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	has_textual_diff TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id)
);

CREATE TABLE "Transaction" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id)
);

CREATE TABLE "NameBecomesSynonym" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	change_1 TEXT, 
	change_2 TEXT, 
	change_description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(change_1) REFERENCES "NodeRename" (id), 
	FOREIGN KEY(change_2) REFERENCES "NewSynonym" (id)
);

CREATE TABLE "NodeObsoletion" (
	id TEXT NOT NULL, 
	type TEXT, 
	was_generated_by TEXT, 
	see_also TEXT, 
	pull_request TEXT, 
	creator TEXT, 
	change_date TEXT, 
	contributor TEXT, 
	has_undo TEXT, 
	term_tracker_issue TEXT, 
	old_value TEXT, 
	new_value TEXT, 
	old_value_type TEXT, 
	new_value_type TEXT, 
	new_language TEXT, 
	old_language TEXT, 
	new_datatype TEXT, 
	old_datatype TEXT, 
	about_node TEXT, 
	about_node_representation TEXT, 
	language TEXT, 
	has_direct_replacement TEXT, 
	has_nondirect_replacement TEXT, 
	change_description TEXT, 
	about TEXT, 
	"MultiNodeObsoletion_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(about_node) REFERENCES "Node" (id), 
	FOREIGN KEY(has_direct_replacement) REFERENCES "Node" (id), 
	FOREIGN KEY("MultiNodeObsoletion_id") REFERENCES "MultiNodeObsoletion" (id)
);

CREATE TABLE "MultiNodeObsoletion_associated_change_set" (
	backref_id TEXT, 
	associated_change_set TEXT, 
	PRIMARY KEY (backref_id, associated_change_set), 
	FOREIGN KEY(backref_id) REFERENCES "MultiNodeObsoletion" (id)
);

CREATE TABLE "NodeDirectMerge_associated_change_set" (
	backref_id TEXT, 
	associated_change_set TEXT, 
	PRIMARY KEY (backref_id, associated_change_set), 
	FOREIGN KEY(backref_id) REFERENCES "NodeDirectMerge" (id)
);

CREATE TABLE "NodeObsoletionWithDirectReplacement_associated_change_set" (
	backref_id TEXT, 
	associated_change_set TEXT, 
	PRIMARY KEY (backref_id, associated_change_set), 
	FOREIGN KEY(backref_id) REFERENCES "NodeObsoletionWithDirectReplacement" (id)
);

CREATE TABLE "NodeObsoletionWithNoDirectReplacement_associated_change_set" (
	backref_id TEXT, 
	associated_change_set TEXT, 
	PRIMARY KEY (backref_id, associated_change_set), 
	FOREIGN KEY(backref_id) REFERENCES "NodeObsoletionWithNoDirectReplacement" (id)
);

CREATE TABLE "Transaction_change_set" (
	backref_id TEXT, 
	change_set TEXT, 
	PRIMARY KEY (backref_id, change_set), 
	FOREIGN KEY(backref_id) REFERENCES "Transaction" (id)
);

CREATE TABLE "NodeObsoletion_associated_change_set" (
	backref_id TEXT, 
	associated_change_set TEXT, 
	PRIMARY KEY (backref_id, associated_change_set), 
	FOREIGN KEY(backref_id) REFERENCES "NodeObsoletion" (id)
);
