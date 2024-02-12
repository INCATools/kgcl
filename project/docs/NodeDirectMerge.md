
# Class: NodeDirectMerge


An obsoletion change in which all metadata (including name/label) from the source node is deleted and added to the target node, and edges can automatically be rewired to point to the target node

URI: [kgcl:NodeDirectMerge](http://w3id.org/kgcl/NodeDirectMerge)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyElement],[NodeObsoletion],[Node]<about_node%200..1-%20[NodeDirectMerge&#124;change_description:string%20%3F;about_node_representation(i):string%20%3F;language(i):LanguageTag%20%3F;old_value(i):string%20%3F;new_value(i):string%20%3F;old_value_type(i):string%20%3F;new_value_type(i):string%20%3F;new_language(i):string%20%3F;old_language(i):string%20%3F;new_datatype(i):string%20%3F;old_datatype(i):string%20%3F;id(i):string;type(i):string%20%3F;see_also(i):string%20%3F;pull_request(i):string%20%3F;creator(i):string%20%3F;change_date(i):string%20%3F;contributor(i):string%20%3F;term_tracker_issue(i):string%20%3F],[Node]<has_direct_replacement%201..1-%20[NodeDirectMerge],[NodeDirectMerge]uses%20-.->[AllowsAutomaticReplacementOfEdges],[NodeObsoletion]^-[NodeDirectMerge],[Node],[Change],[AllowsAutomaticReplacementOfEdges],[Activity])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyElement],[NodeObsoletion],[Node]<about_node%200..1-%20[NodeDirectMerge&#124;change_description:string%20%3F;about_node_representation(i):string%20%3F;language(i):LanguageTag%20%3F;old_value(i):string%20%3F;new_value(i):string%20%3F;old_value_type(i):string%20%3F;new_value_type(i):string%20%3F;new_language(i):string%20%3F;old_language(i):string%20%3F;new_datatype(i):string%20%3F;old_datatype(i):string%20%3F;id(i):string;type(i):string%20%3F;see_also(i):string%20%3F;pull_request(i):string%20%3F;creator(i):string%20%3F;change_date(i):string%20%3F;contributor(i):string%20%3F;term_tracker_issue(i):string%20%3F],[Node]<has_direct_replacement%201..1-%20[NodeDirectMerge],[NodeDirectMerge]uses%20-.->[AllowsAutomaticReplacementOfEdges],[NodeObsoletion]^-[NodeDirectMerge],[Node],[Change],[AllowsAutomaticReplacementOfEdges],[Activity])

## Parents

 *  is_a: [NodeObsoletion](NodeObsoletion.md) - Obsoletion of a node deprecates usage of that node, but does not delete it.

## Uses Mixin

 *  mixin: [AllowsAutomaticReplacementOfEdges](AllowsAutomaticReplacementOfEdges.md) - Applies to an obsoletion in which annotations or edges pointing at the obsoleted node can be automatically rewired to point to a target

## Referenced by Class


## Attributes


### Own

 * [NodeDirectMerge➞has_direct_replacement](NodeDirectMerge_has_direct_replacement.md)  <sub>1..1</sub>
     * Description: An obsoletion replacement where it IS valid to automatically update annotations/edges pointing at the node with its direct replacement
     * Range: [Node](Node.md)
 * [NodeDirectMerge➞about_node](NodeDirectMerge_about_node.md)  <sub>0..1</sub>
     * Range: [Node](Node.md)
 * [NodeDirectMerge➞change_description](NodeDirectMerge_change_description.md)  <sub>0..1</sub>
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
 * [about_node_representation](about_node_representation.md)  <sub>0..1</sub>
     * Description: The representation of a node (URI, CURIE, label) 
     * Range: [String](types/String.md)
 * [language](language.md)  <sub>0..1</sub>
     * Description: The language tag of a literal
     * Range: [LanguageTag](types/LanguageTag.md)
 * [has_nondirect_replacement](has_nondirect_replacement.md)  <sub>0..\*</sub>
     * Description: An obsoletion replacement where it is NOT valid to automatically update annotations/edges pointing at the node with its direct replacement
     * Range: [Node](Node.md)
 * [NodeObsoletion➞associated change set](NodeObsoletion_associated_change_set.md)  <sub>0..\*</sub>
     * Description: All changes forced as a result of this obsoletion. For example, starting with `A subClassOf B subClassOf C`, if we obsolete node B, then we may decide to bundle in a node move change of A from B to C. Note: this change set is not considered a part of the obsoletion, as obsoletion is considered atomic/simple. Instead this is a reference to a change set that may exist elsewhere
     * Range: [Change](Change.md)

### Mixed in from Obsoletion:

 * [Obsoletion➞about](Obsoletion_about.md)  <sub>0..1</sub>
     * Description: The element that is obsoleted by this change.
     * Range: [OntologyElement](OntologyElement.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | In the OBO format serialization of the graph, the source node vanishes from the file as a distinct entry and is retained only as an alt_id |
| **See also:** | | [http://wiki.geneontology.org/index.php/Merging_Ontology_Terms](http://wiki.geneontology.org/index.php/Merging_Ontology_Terms) |
|  | | [http://wiki.geneontology.org/index.php/Principles_for_merging_terms](http://wiki.geneontology.org/index.php/Principles_for_merging_terms) |

