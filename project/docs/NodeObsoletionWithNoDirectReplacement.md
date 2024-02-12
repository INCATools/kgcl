
# Class: NodeObsoletionWithNoDirectReplacement


An obsoletion change in which there is no direct replacement

URI: [kgcl:NodeObsoletionWithNoDirectReplacement](http://w3id.org/kgcl/NodeObsoletionWithNoDirectReplacement)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyElement],[Node]<has_nondirect_replacement%201..*-%20[NodeObsoletionWithNoDirectReplacement&#124;change_description:string%20%3F;about_node_representation(i):string%20%3F;language(i):LanguageTag%20%3F;old_value(i):string%20%3F;new_value(i):string%20%3F;old_value_type(i):string%20%3F;new_value_type(i):string%20%3F;new_language(i):string%20%3F;old_language(i):string%20%3F;new_datatype(i):string%20%3F;old_datatype(i):string%20%3F;id(i):string;type(i):string%20%3F;see_also(i):string%20%3F;pull_request(i):string%20%3F;creator(i):string%20%3F;change_date(i):string%20%3F;contributor(i):string%20%3F;term_tracker_issue(i):string%20%3F],[NodeObsoletion]^-[NodeObsoletionWithNoDirectReplacement],[NodeObsoletion],[Node],[Change],[Activity])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyElement],[Node]<has_nondirect_replacement%201..*-%20[NodeObsoletionWithNoDirectReplacement&#124;change_description:string%20%3F;about_node_representation(i):string%20%3F;language(i):LanguageTag%20%3F;old_value(i):string%20%3F;new_value(i):string%20%3F;old_value_type(i):string%20%3F;new_value_type(i):string%20%3F;new_language(i):string%20%3F;old_language(i):string%20%3F;new_datatype(i):string%20%3F;old_datatype(i):string%20%3F;id(i):string;type(i):string%20%3F;see_also(i):string%20%3F;pull_request(i):string%20%3F;creator(i):string%20%3F;change_date(i):string%20%3F;contributor(i):string%20%3F;term_tracker_issue(i):string%20%3F],[NodeObsoletion]^-[NodeObsoletionWithNoDirectReplacement],[NodeObsoletion],[Node],[Change],[Activity])

## Parents

 *  is_a: [NodeObsoletion](NodeObsoletion.md) - Obsoletion of a node deprecates usage of that node, but does not delete it.

## Referenced by Class


## Attributes


### Own

 * [NodeObsoletionWithNoDirectReplacement➞has_nondirect_replacement](NodeObsoletionWithNoDirectReplacement_has_nondirect_replacement.md)  <sub>1..\*</sub>
     * Description: An obsoletion replacement where it is NOT valid to automatically update annotations/edges pointing at the node with its direct replacement
     * Range: [Node](Node.md)
 * [NodeObsoletionWithNoDirectReplacement➞change_description](NodeObsoletionWithNoDirectReplacement_change_description.md)  <sub>0..1</sub>
     * Description: A string serialization of the change. This should be both human-readable, and parseable.
     * Range: [String](types/String.md)
     * Example: rename UBERON:0002398 from 'manus' to 'hand' None
     * Example: move 'hand' from 'part of' 'hindlimb' to 'part of' 'forelimb' None
     * Example: merge 'cellular metabolic process' into 'metabolic process' None
     * Example: search and replace 'metabolic process' with 'metabolism' in all labels under 'biological process' None
     * Example: search and replace 'metabolic process' with 'metabolism' in all labels under 'biological process' retaining as 'exact synonym' None

### Inherited from NodeObsoletion:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [Change➞was_generated_by](Change_was_generated_by.md)  <sub>0..1</sub>
     * Range: [Activity](Activity.md)
 * [Change➞see_also](Change_see_also.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [Change➞pull_request](Change_pull_request.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [Change➞creator](Change_creator.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [Change➞change_date](Change_change_date.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [contributor](contributor.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [has_undo](has_undo.md)  <sub>0..1</sub>
     * Description: A change that reverses this change
     * Range: [Change](Change.md)
 * [Change➞term_tracker_issue](Change_term_tracker_issue.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [old_value](old_value.md)  <sub>0..1</sub>
     * Description: The value of a property held in the old instance of the ontology
     * Range: [String](types/String.md)
 * [new_value](new_value.md)  <sub>0..1</sub>
     * Description: The value of a property held in the new instance of the ontology
     * Range: [String](types/String.md)
 * [old_value_type](old_value_type.md)  <sub>0..1</sub>
     * Description: The type (IRI or Literal) of an old value
     * Range: [String](types/String.md)
 * [new_value_type](new_value_type.md)  <sub>0..1</sub>
     * Description: The type (IRI or Literal) of a new value
     * Range: [String](types/String.md)
 * [new_language](new_language.md)  <sub>0..1</sub>
     * Description: The new language tag of a literal
     * Range: [String](types/String.md)
 * [old_language](old_language.md)  <sub>0..1</sub>
     * Description: The old language tag of a literal
     * Range: [String](types/String.md)
 * [new_datatype](new_datatype.md)  <sub>0..1</sub>
     * Description: The new datatype of a literal
     * Range: [String](types/String.md)
 * [old_datatype](old_datatype.md)  <sub>0..1</sub>
     * Description: The old datatype of a literal
     * Range: [String](types/String.md)
 * [about_node](about_node.md)  <sub>0..1</sub>
     * Range: [Node](Node.md)
 * [about_node_representation](about_node_representation.md)  <sub>0..1</sub>
     * Description: The representation of a node (URI, CURIE, label) 
     * Range: [String](types/String.md)
 * [language](language.md)  <sub>0..1</sub>
     * Description: The language tag of a literal
     * Range: [LanguageTag](types/LanguageTag.md)
 * [has_direct_replacement](has_direct_replacement.md)  <sub>0..1</sub>
     * Description: An obsoletion replacement where it IS valid to automatically update annotations/edges pointing at the node with its direct replacement
     * Range: [Node](Node.md)
 * [NodeObsoletion➞associated change set](NodeObsoletion_associated_change_set.md)  <sub>0..\*</sub>
     * Description: All changes forced as a result of this obsoletion. For example, starting with `A subClassOf B subClassOf C`, if we obsolete node B, then we may decide to bundle in a node move change of A from B to C. Note: this change set is not considered a part of the obsoletion, as obsoletion is considered atomic/simple. Instead this is a reference to a change set that may exist elsewhere
     * Range: [Change](Change.md)
