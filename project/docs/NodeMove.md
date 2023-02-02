
# Class: NodeMove


A node move is a combination of deleting a parent edge and adding a parent edge, where the predicate is preserved and the object/parent node changes

URI: [kgcl:NodeMove](http://w3id.org/kgcl/NodeMove)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NodeShallowing],[NodeMove&#124;old_object_type:string%20%3F;new_object_type:string%20%3F;change_description:string%20%3F;object_type(i):string%20%3F;language(i):LanguageTag%20%3F;datatype(i):string%20%3F;old_value(i):string%20%3F;new_value(i):string%20%3F;old_value_type(i):string%20%3F;new_value_type(i):string%20%3F;new_language(i):string%20%3F;old_language(i):string%20%3F;new_datatype(i):string%20%3F;old_datatype(i):string%20%3F;id(i):string;type(i):string%20%3F;see_also(i):string%20%3F;pull_request(i):string%20%3F;creator(i):string%20%3F;change_date(i):string%20%3F;contributor(i):string%20%3F;term_tracker_issue(i):string%20%3F]^-[NodeShallowing],[NodeMove]^-[NodeDeepening],[EdgeChange]^-[NodeMove],[NodeDeepening],[Node],[EdgeChange],[Edge],[Change],[Activity])](https://yuml.me/diagram/nofunky;dir:TB/class/[NodeShallowing],[NodeMove&#124;old_object_type:string%20%3F;new_object_type:string%20%3F;change_description:string%20%3F;object_type(i):string%20%3F;language(i):LanguageTag%20%3F;datatype(i):string%20%3F;old_value(i):string%20%3F;new_value(i):string%20%3F;old_value_type(i):string%20%3F;new_value_type(i):string%20%3F;new_language(i):string%20%3F;old_language(i):string%20%3F;new_datatype(i):string%20%3F;old_datatype(i):string%20%3F;id(i):string;type(i):string%20%3F;see_also(i):string%20%3F;pull_request(i):string%20%3F;creator(i):string%20%3F;change_date(i):string%20%3F;contributor(i):string%20%3F;term_tracker_issue(i):string%20%3F]^-[NodeShallowing],[NodeMove]^-[NodeDeepening],[EdgeChange]^-[NodeMove],[NodeDeepening],[Node],[EdgeChange],[Edge],[Change],[Activity])

## Parents

 *  is_a: [EdgeChange](EdgeChange.md) - A change in which the element that is the focus of the change is an edge.

## Children

 * [NodeDeepening](NodeDeepening.md) - A node move in which a node where the destination is a proper descendant of the original location. Note that here descendant applied not just to subclass, but edges of any predicate in the relational graph
 * [NodeShallowing](NodeShallowing.md) - The opposite of node deepening

## Referenced by Class


## Attributes


### Own

 * [old_object_type](old_object_type.md)  <sub>0..1</sub>
     * Description: The type (IRI or Literal) of an old object
     * Range: [String](types/String.md)
 * [new_object_type](new_object_type.md)  <sub>0..1</sub>
     * Description: The type (IRI or Literal) of a new object
     * Range: [String](types/String.md)
 * [NodeMove➞change_description](NodeMove_change_description.md)  <sub>0..1</sub>
     * Description: A string serialization of the change. This should be both human-readable, and parseable.
     * Range: [String](types/String.md)
     * Example: rename UBERON:0002398 from 'manus' to 'hand' None
     * Example: move 'hand' from 'part of' 'hindlimb' to 'part of' 'forelimb' None
     * Example: merge 'cellular metabolic process' into 'metabolic process' None
     * Example: search and replace 'metabolic process' with 'metabolism' in all labels under 'biological process' None
     * Example: search and replace 'metabolic process' with 'metabolism' in all labels under 'biological process' retaining as 'exact synonym' None

### Inherited from EdgeChange:

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
 * [about_edge](about_edge.md)  <sub>0..1</sub>
     * Range: [Edge](Edge.md)
 * [object_type](object_type.md)  <sub>0..1</sub>
     * Description: The type (IRI or Literal) of an object
     * Range: [String](types/String.md)
 * [language](language.md)  <sub>0..1</sub>
     * Description: The language tag of a literal
     * Range: [LanguageTag](types/LanguageTag.md)
 * [datatype](datatype.md)  <sub>0..1</sub>
     * Description: The datatype of a literal
     * Range: [String](types/String.md)
 * [EdgeChange➞subject](EdgeChange_subject.md)  <sub>0..1</sub>
     * Range: [Node](Node.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Examples:** | | Example(value='changing a is-a b to a is-a c', description=None) |

