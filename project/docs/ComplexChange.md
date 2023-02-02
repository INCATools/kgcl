
# Class: ComplexChange


A change that is is a composition of other changes

URI: [kgcl:ComplexChange](http://w3id.org/kgcl/ComplexChange)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MultiNodeObsoletion],[Change]<change_set%200..*-++[ComplexChange&#124;id(i):string;type(i):string%20%3F;see_also(i):string%20%3F;pull_request(i):string%20%3F;creator(i):string%20%3F;change_date(i):string%20%3F;contributor(i):string%20%3F;term_tracker_issue(i):string%20%3F],[ComplexChange]^-[MultiNodeObsoletion],[Change]^-[ComplexChange],[Change],[Activity])](https://yuml.me/diagram/nofunky;dir:TB/class/[MultiNodeObsoletion],[Change]<change_set%200..*-++[ComplexChange&#124;id(i):string;type(i):string%20%3F;see_also(i):string%20%3F;pull_request(i):string%20%3F;creator(i):string%20%3F;change_date(i):string%20%3F;contributor(i):string%20%3F;term_tracker_issue(i):string%20%3F],[ComplexChange]^-[MultiNodeObsoletion],[Change]^-[ComplexChange],[Change],[Activity])

## Parents

 *  is_a: [Change](Change.md) - Any change perform on an ontology or knowledge graph

## Children

 * [MultiNodeObsoletion](MultiNodeObsoletion.md) - A complex change consisting of multiple obsoletions.

## Referenced by Class


## Attributes


### Own

 * [change_set](change_set.md)  <sub>0..\*</sub>
     * Description: A collection of changes
     * Range: [Change](Change.md)

### Inherited from Change:

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
