
# Class: Change


Any change perform on an ontology or knowledge graph

URI: [kgcl:Change](http://w3id.org/kgcl/Change)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Transaction],[SimpleChange],[NodeObsoletion],[MultiNodeObsoletion],[ComplexChange],[ChangeLanguageElement],[Change]<has_undo%200..1-%20[Change&#124;id:string;type:string%20%3F;see_also:string%20%3F;pull_request:string%20%3F;creator:string%20%3F;change_date:string%20%3F;contributor:string%20%3F;term_tracker_issue:string%20%3F],[Activity]<was_generated_by%200..1-%20[Change],[MultiNodeObsoletion]++-%20associated%20change%20set%200..*>[Change],[NodeObsoletion]++-%20associated%20change%20set%200..*>[Change],[ComplexChange]++-%20change_set%200..*>[Change],[Transaction]++-%20change_set%200..*>[Change],[Session]++-%20change_set%200..*>[Change],[Change]^-[Transaction],[Change]^-[SimpleChange],[Change]^-[ComplexChange],[ChangeLanguageElement]^-[Change],[Session],[Activity])](https://yuml.me/diagram/nofunky;dir:TB/class/[Transaction],[SimpleChange],[NodeObsoletion],[MultiNodeObsoletion],[ComplexChange],[ChangeLanguageElement],[Change]<has_undo%200..1-%20[Change&#124;id:string;type:string%20%3F;see_also:string%20%3F;pull_request:string%20%3F;creator:string%20%3F;change_date:string%20%3F;contributor:string%20%3F;term_tracker_issue:string%20%3F],[Activity]<was_generated_by%200..1-%20[Change],[MultiNodeObsoletion]++-%20associated%20change%20set%200..*>[Change],[NodeObsoletion]++-%20associated%20change%20set%200..*>[Change],[ComplexChange]++-%20change_set%200..*>[Change],[Transaction]++-%20change_set%200..*>[Change],[Session]++-%20change_set%200..*>[Change],[Change]^-[Transaction],[Change]^-[SimpleChange],[Change]^-[ComplexChange],[ChangeLanguageElement]^-[Change],[Session],[Activity])

## Parents

 *  is_a: [ChangeLanguageElement](ChangeLanguageElement.md) - A broad grouping for all elements of the change language

## Children

 * [ComplexChange](ComplexChange.md) - A change that is is a composition of other changes
 * [SimpleChange](SimpleChange.md) - A change that is about a single ontology element
 * [Transaction](Transaction.md) - A change that is a composition of a set of changes, where those changes are treated as a single unit. Could be a single change, or the results of an ontology diff

## Referenced by Class

 *  **[MultiNodeObsoletion](MultiNodeObsoletion.md)** *[MultiNodeObsoletion➞associated change set](MultiNodeObsoletion_associated_change_set.md)*  <sub>0..\*</sub>  **[Change](Change.md)**
 *  **[NodeObsoletion](NodeObsoletion.md)** *[NodeObsoletion➞associated change set](NodeObsoletion_associated_change_set.md)*  <sub>0..\*</sub>  **[Change](Change.md)**
 *  **None** *[associated change set](associated_change_set.md)*  <sub>0..\*</sub>  **[Change](Change.md)**
 *  **None** *[change_set](change_set.md)*  <sub>0..\*</sub>  **[Change](Change.md)**
 *  **[Change](Change.md)** *[has_undo](has_undo.md)*  <sub>0..1</sub>  **[Change](Change.md)**

## Attributes


### Own

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
