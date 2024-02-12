
# Class: ObjectPropertyCreation


A node creation where the owl type is 'ObjectProperty'

URI: [kgcl:ObjectPropertyCreation](http://w3id.org/kgcl/ObjectPropertyCreation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NodeCreation]^-[ObjectPropertyCreation&#124;change_description:string%20%3F;name(i):string%20%3F;owl_type(i):OwlTypeEnum%20%3F;about_node_representation(i):string%20%3F;language(i):LanguageTag%20%3F;old_value(i):string%20%3F;new_value(i):string%20%3F;old_value_type(i):string%20%3F;new_value_type(i):string%20%3F;new_language(i):string%20%3F;old_language(i):string%20%3F;new_datatype(i):string%20%3F;old_datatype(i):string%20%3F;id(i):string;type(i):string%20%3F;see_also(i):string%20%3F;pull_request(i):string%20%3F;creator(i):string%20%3F;change_date(i):string%20%3F;contributor(i):string%20%3F;term_tracker_issue(i):string%20%3F],[NodeCreation],[Node],[Change],[Annotation],[Activity])](https://yuml.me/diagram/nofunky;dir:TB/class/[NodeCreation]^-[ObjectPropertyCreation&#124;change_description:string%20%3F;name(i):string%20%3F;owl_type(i):OwlTypeEnum%20%3F;about_node_representation(i):string%20%3F;language(i):LanguageTag%20%3F;old_value(i):string%20%3F;new_value(i):string%20%3F;old_value_type(i):string%20%3F;new_value_type(i):string%20%3F;new_language(i):string%20%3F;old_language(i):string%20%3F;new_datatype(i):string%20%3F;old_datatype(i):string%20%3F;id(i):string;type(i):string%20%3F;see_also(i):string%20%3F;pull_request(i):string%20%3F;creator(i):string%20%3F;change_date(i):string%20%3F;contributor(i):string%20%3F;term_tracker_issue(i):string%20%3F],[NodeCreation],[Node],[Change],[Annotation],[Activity])

## Parents

 *  is_a: [NodeCreation](NodeCreation.md) - a node change in which a new node is created

## Referenced by Class


## Attributes


### Own

 * [ObjectPropertyCreation➞change_description](ObjectPropertyCreation_change_description.md)  <sub>0..1</sub>
     * Description: A string serialization of the change. This should be both human-readable, and parseable.
     * Range: [String](types/String.md)
     * Example: rename UBERON:0002398 from 'manus' to 'hand' None
     * Example: move 'hand' from 'part of' 'hindlimb' to 'part of' 'forelimb' None
     * Example: merge 'cellular metabolic process' into 'metabolic process' None
     * Example: search and replace 'metabolic process' with 'metabolism' in all labels under 'biological process' None
     * Example: search and replace 'metabolic process' with 'metabolism' in all labels under 'biological process' retaining as 'exact synonym' None

### Inherited from NodeCreation:

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
 * [node_id](node_id.md)  <sub>0..1</sub>
     * Description: id of a node to be created
     * Range: [Node](Node.md)
 * [name](name.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [owl_type](owl_type.md)  <sub>0..1</sub>
     * Range: [OwlTypeEnum](OwlTypeEnum.md)
 * [annotation_set](annotation_set.md)  <sub>0..1</sub>
     * Range: [Annotation](Annotation.md)
 * [language](language.md)  <sub>0..1</sub>
     * Description: The language tag of a literal
     * Range: [LanguageTag](types/LanguageTag.md)
