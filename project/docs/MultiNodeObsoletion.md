
# Class: MultiNodeObsoletion


A complex change consisting of multiple obsoletions.

URI: [kgcl:MultiNodeObsoletion](http://w3id.org/kgcl/MultiNodeObsoletion)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NodeObsoletion],[Change]<associated%20change%20set%200..*-++[MultiNodeObsoletion&#124;change_description:string%20%3F;id(i):string;type(i):string%20%3F;see_also(i):string%20%3F;pull_request(i):string%20%3F;creator(i):string%20%3F;change_date(i):string%20%3F;contributor(i):string%20%3F;term_tracker_issue(i):string%20%3F],[NodeObsoletion]<change_set%200..*-++[MultiNodeObsoletion],[ComplexChange]^-[MultiNodeObsoletion],[ComplexChange],[Change],[Activity])](https://yuml.me/diagram/nofunky;dir:TB/class/[NodeObsoletion],[Change]<associated%20change%20set%200..*-++[MultiNodeObsoletion&#124;change_description:string%20%3F;id(i):string;type(i):string%20%3F;see_also(i):string%20%3F;pull_request(i):string%20%3F;creator(i):string%20%3F;change_date(i):string%20%3F;contributor(i):string%20%3F;term_tracker_issue(i):string%20%3F],[NodeObsoletion]<change_set%200..*-++[MultiNodeObsoletion],[ComplexChange]^-[MultiNodeObsoletion],[ComplexChange],[Change],[Activity])

## Parents

 *  is_a: [ComplexChange](ComplexChange.md) - A change that is is a composition of other changes

## Referenced by Class


## Attributes


### Own

 * [MultiNodeObsoletion➞change_set](MultiNodeObsoletion_change_set.md)  <sub>0..\*</sub>
     * Description: A collection of changes
     * Range: [NodeObsoletion](NodeObsoletion.md)
 * [MultiNodeObsoletion➞change_description](MultiNodeObsoletion_change_description.md)  <sub>0..1</sub>
     * Description: A string serialization of the change. This should be both human-readable, and parseable.
     * Range: [String](types/String.md)
     * Example: rename UBERON:0002398 from 'manus' to 'hand' None
     * Example: move 'hand' from 'part of' 'hindlimb' to 'part of' 'forelimb' None
     * Example: merge 'cellular metabolic process' into 'metabolic process' None
     * Example: search and replace 'metabolic process' with 'metabolism' in all labels under 'biological process' None
     * Example: search and replace 'metabolic process' with 'metabolism' in all labels under 'biological process' retaining as 'exact synonym' None
 * [MultiNodeObsoletion➞associated change set](MultiNodeObsoletion_associated_change_set.md)  <sub>0..\*</sub>
     * Description: All changes associated with a set of obsoletions. This change set is the composed change set rather than the set of individual changes. For example, if previous state is:\n  `A subClassOf B subClassOf C subClassOf D` and we obsolete {B,C}, then the individual changes are `A moves from B to C` and `B moves from C to D`, but the composed change set is `A moves from B to D`"
     * Range: [Change](Change.md)

### Inherited from ComplexChange:

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | multi node deprecation |
|  | | multi class obsoletion |
|  | | multi term obsoletion |
|  | | multi concept obsoletion |
| **See also:** | | [https://github.com/cmungall/obo-scripts/blob/master/obo-obsoletify.pl](https://github.com/cmungall/obo-scripts/blob/master/obo-obsoletify.pl) |

