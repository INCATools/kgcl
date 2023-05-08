
# Class: node creation


a node change in which a new node is created

URI: [kgcl:NodeCreation](http://w3id.org/kgcl/NodeCreation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Annotation]<annotation%20set%200..1-++[NodeCreation&#124;name:string%20%3F;owl_type:owl_type_enum%20%3F;change_description:string%20%3F;about_node_representation(i):string%20%3F;language(i):language_tag%20%3F;old_value(i):string%20%3F;new_value(i):string%20%3F;old_value_type(i):string%20%3F;new_value_type(i):string%20%3F;new_language(i):string%20%3F;old_language(i):string%20%3F;new_datatype(i):string%20%3F;old_datatype(i):string%20%3F;id(i):string;type(i):string%20%3F;see_also(i):string%20%3F;pull_request(i):string%20%3F;creator(i):string%20%3F;change_date(i):string%20%3F;contributor(i):string%20%3F],[Node]<node%20id%200..1-%20[NodeCreation],[NodeCreation]uses%20-.->[Creation],[NodeCreation]^-[ClassCreation],[NodeChange]^-[NodeCreation],[NodeChange],[Node],[Creation],[ClassCreation],[Change],[Annotation],[Activity])](https://yuml.me/diagram/nofunky;dir:TB/class/[Annotation]<annotation%20set%200..1-++[NodeCreation&#124;name:string%20%3F;owl_type:owl_type_enum%20%3F;change_description:string%20%3F;about_node_representation(i):string%20%3F;language(i):language_tag%20%3F;old_value(i):string%20%3F;new_value(i):string%20%3F;old_value_type(i):string%20%3F;new_value_type(i):string%20%3F;new_language(i):string%20%3F;old_language(i):string%20%3F;new_datatype(i):string%20%3F;old_datatype(i):string%20%3F;id(i):string;type(i):string%20%3F;see_also(i):string%20%3F;pull_request(i):string%20%3F;creator(i):string%20%3F;change_date(i):string%20%3F;contributor(i):string%20%3F],[Node]<node%20id%200..1-%20[NodeCreation],[NodeCreation]uses%20-.->[Creation],[NodeCreation]^-[ClassCreation],[NodeChange]^-[NodeCreation],[NodeChange],[Node],[Creation],[ClassCreation],[Change],[Annotation],[Activity])

## Parents

 *  is_a: [NodeChange](NodeChange.md) - A simple change where the change is about a node

## Uses Mixin

 *  mixin: [Creation](Creation.md) - Creation of an element.

## Children

 * [ClassCreation](ClassCreation.md) - A node creation where the owl type is 'class'

## Referenced by Class


## Attributes


### Own

 * [node id](node_id.md)  <sub>0..1</sub>
     * Description: id of a node to be created
     * Range: [Node](Node.md)
 * [name](name.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [owl type](owl_type.md)  <sub>0..1</sub>
     * Range: [owl_type_enum](owl_type_enum.md)
 * [annotation set](annotation_set.md)  <sub>0..1</sub>
     * Range: [Annotation](Annotation.md)
 * [language](language.md)  <sub>0..1</sub>
     * Description: The language tag of a literal
     * Range: [LanguageTag](types/LanguageTag.md)
 * [node creation➞change description](node_creation_change_description.md)  <sub>0..1</sub>
     * Description: A string serialization of the change. This should be both human-readable, and parseable.
     * Range: [String](types/String.md)
     * Example: rename UBERON:0002398 from 'manus' to 'hand' None
     * Example: move 'hand' from 'part of' 'hindlimb' to 'part of' 'forelimb' None
     * Example: merge 'cellular metabolic process' into 'metabolic process' None
     * Example: search and replace 'metabolic process' with 'metabolism' in all labels under 'biological process' None
     * Example: search and replace 'metabolic process' with 'metabolism' in all labels under 'biological process' retaining as 'exact synonym' None

### Inherited from node change:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [type](type.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [change➞was generated by](change_was_generated_by.md)  <sub>0..1</sub>
     * Range: [Activity](Activity.md)
 * [change➞see also](change_see_also.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [change➞pull request](change_pull_request.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [change➞creator](change_creator.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [change➞change date](change_change_date.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [contributor](contributor.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [has undo](has_undo.md)  <sub>0..1</sub>
     * Description: A change that reverses this change
     * Range: [Change](Change.md)
 * [old value](old_value.md)  <sub>0..1</sub>
     * Description: The value of a property held in the old instance of the ontology
     * Range: [String](types/String.md)
 * [new value](new_value.md)  <sub>0..1</sub>
     * Description: The value of a property held in the new instance of the ontology
     * Range: [String](types/String.md)
 * [old value type](old_value_type.md)  <sub>0..1</sub>
     * Description: The type (IRI or Literal) of an old value
     * Range: [String](types/String.md)
 * [new value type](new_value_type.md)  <sub>0..1</sub>
     * Description: The type (IRI or Literal) of a new value
     * Range: [String](types/String.md)
 * [new language](new_language.md)  <sub>0..1</sub>
     * Description: The new language tag of a literal
     * Range: [String](types/String.md)
 * [old language](old_language.md)  <sub>0..1</sub>
     * Description: The old language tag of a literal
     * Range: [String](types/String.md)
 * [new datatype](new_datatype.md)  <sub>0..1</sub>
     * Description: The new datatype of a literal
     * Range: [String](types/String.md)
 * [old datatype](old_datatype.md)  <sub>0..1</sub>
     * Description: The old datatype of a literal
     * Range: [String](types/String.md)
 * [about node](about_node.md)  <sub>0..1</sub>
     * Range: [Node](Node.md)
 * [about node representation](about_node_representation.md)  <sub>0..1</sub>
     * Description: The representation of a node (URI, CURIE, label) 
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **See also:** | | [http://wiki.geneontology.org/index.php/Guidelines_for_creating_a_GO_term](http://wiki.geneontology.org/index.php/Guidelines_for_creating_a_GO_term) |
