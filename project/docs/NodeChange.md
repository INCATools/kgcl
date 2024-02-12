
# Class: NodeChange


A simple change where the change is about a node

URI: [kgcl:NodeChange](http://w3id.org/kgcl/NodeChange)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SimpleChange],[SetLanguageForName],[RemoveNodeFromSubset],[NodeUnobsoletion],[NodeTextDefinitionChange],[NodeSynonymChange],[NodeRename],[NodeObsoletion],[NodeMetadataAssertionChange],[NodeMappingChange],[NodeDeletion],[NodeCreation],[Node]<about_node%200..1-%20[NodeChange&#124;about_node_representation:string%20%3F;language:LanguageTag%20%3F;old_value(i):string%20%3F;new_value(i):string%20%3F;old_value_type(i):string%20%3F;new_value_type(i):string%20%3F;new_language(i):string%20%3F;old_language(i):string%20%3F;new_datatype(i):string%20%3F;old_datatype(i):string%20%3F;id(i):string;type(i):string%20%3F;see_also(i):string%20%3F;pull_request(i):string%20%3F;creator(i):string%20%3F;change_date(i):string%20%3F;contributor(i):string%20%3F;term_tracker_issue(i):string%20%3F],[NodeChange]^-[SetLanguageForName],[NodeChange]^-[RemoveNodeFromSubset],[NodeChange]^-[NodeUnobsoletion],[NodeChange]^-[NodeTextDefinitionChange],[NodeChange]^-[NodeSynonymChange],[NodeChange]^-[NodeRename],[NodeChange]^-[NodeObsoletion],[NodeChange]^-[NodeMetadataAssertionChange],[NodeChange]^-[NodeMappingChange],[NodeChange]^-[NodeDeletion],[NodeChange]^-[NodeCreation],[NodeChange]^-[NodeAnnotationChange],[NodeChange]^-[AddNodeToSubset],[SimpleChange]^-[NodeChange],[NodeAnnotationChange],[Node],[Change],[AddNodeToSubset],[Activity])](https://yuml.me/diagram/nofunky;dir:TB/class/[SimpleChange],[SetLanguageForName],[RemoveNodeFromSubset],[NodeUnobsoletion],[NodeTextDefinitionChange],[NodeSynonymChange],[NodeRename],[NodeObsoletion],[NodeMetadataAssertionChange],[NodeMappingChange],[NodeDeletion],[NodeCreation],[Node]<about_node%200..1-%20[NodeChange&#124;about_node_representation:string%20%3F;language:LanguageTag%20%3F;old_value(i):string%20%3F;new_value(i):string%20%3F;old_value_type(i):string%20%3F;new_value_type(i):string%20%3F;new_language(i):string%20%3F;old_language(i):string%20%3F;new_datatype(i):string%20%3F;old_datatype(i):string%20%3F;id(i):string;type(i):string%20%3F;see_also(i):string%20%3F;pull_request(i):string%20%3F;creator(i):string%20%3F;change_date(i):string%20%3F;contributor(i):string%20%3F;term_tracker_issue(i):string%20%3F],[NodeChange]^-[SetLanguageForName],[NodeChange]^-[RemoveNodeFromSubset],[NodeChange]^-[NodeUnobsoletion],[NodeChange]^-[NodeTextDefinitionChange],[NodeChange]^-[NodeSynonymChange],[NodeChange]^-[NodeRename],[NodeChange]^-[NodeObsoletion],[NodeChange]^-[NodeMetadataAssertionChange],[NodeChange]^-[NodeMappingChange],[NodeChange]^-[NodeDeletion],[NodeChange]^-[NodeCreation],[NodeChange]^-[NodeAnnotationChange],[NodeChange]^-[AddNodeToSubset],[SimpleChange]^-[NodeChange],[NodeAnnotationChange],[Node],[Change],[AddNodeToSubset],[Activity])

## Parents

 *  is_a: [SimpleChange](SimpleChange.md) - A change that is about a single ontology element

## Children

 * [AddNodeToSubset](AddNodeToSubset.md) - Places a node inside a subset, by annotating that node
 * [NodeAnnotationChange](NodeAnnotationChange.md) - A node change where the change alters node properties/annotations. TODO
 * [NodeCreation](NodeCreation.md) - a node change in which a new node is created
 * [NodeDeletion](NodeDeletion.md) - Deletion of a node from the graph. Note it is recommended nodes are obsoleted and never merged, but this operation exists to represent deletions in ontologies, accidental or otherwise
 * [NodeMappingChange](NodeMappingChange.md) - A node change where the mappings for that node are altered
 * [NodeMetadataAssertionChange](NodeMetadataAssertionChange.md) - A node change where the metadata assertion (OWL annotations) for that node are altered
 * [NodeObsoletion](NodeObsoletion.md) - Obsoletion of a node deprecates usage of that node, but does not delete it.
 * [NodeRename](NodeRename.md) - A node change where the name (aka rdfs:label) of the node changes
 * [NodeSynonymChange](NodeSynonymChange.md)
 * [NodeTextDefinitionChange](NodeTextDefinitionChange.md) - A node change where the text definition is changed
 * [NodeUnobsoletion](NodeUnobsoletion.md) - unobsoletion of a node deprecates usage of that node. Rarely applied.
 * [RemoveNodeFromSubset](RemoveNodeFromSubset.md) - Removes a node from a subset, by removing an annotation
 * [SetLanguageForName](SetLanguageForName.md) - A node change where the string value for the name is unchanged but the language tag is set

## Referenced by Class


## Attributes


### Own

 * [about_node](about_node.md)  <sub>0..1</sub>
     * Range: [Node](Node.md)
 * [about_node_representation](about_node_representation.md)  <sub>0..1</sub>
     * Description: The representation of a node (URI, CURIE, label) 
     * Range: [String](types/String.md)
 * [language](language.md)  <sub>0..1</sub>
     * Description: The language tag of a literal
     * Range: [LanguageTag](types/LanguageTag.md)

### Inherited from SimpleChange:

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
