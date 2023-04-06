
# Class: node


Any named entity in an ontology. May be a class, individual, property

URI: [kgcl:Node](http://w3id.org/kgcl/Node)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[RemoveNodeFromSubset],[OntologyElement],[NodeUnobsoletion],[NodeObsoletionWithNoDirectReplacement],[NodeObsoletionWithDirectReplacement],[NodeObsoletion],[NodeDirectMerge],[Annotation]<annotation%20set%200..1-++[Node&#124;id:string;name:string%20%3F;owl_type:owl_type_enum%20%3F],[NodeChange]-%20about%20node%200..1>[Node],[EdgeChange]-%20subject%200..1>[Node],[NodeObsoletion]-%20has%20direct%20replacement%200..1>[Node],[NodeObsoletion]-%20has%20nondirect%20replacement%200..*>[Node],[MappingCreation]-%20object%200..1>[Node],[MappingCreation]-%20predicate%200..1>[Node],[MappingCreation]-%20subject%200..1>[Node],[NodeDirectMerge]-%20about%20node%200..1>[Node],[NodeDirectMerge]-%20has%20direct%20replacement%201..1>[Node],[NodeCreation]-%20node%20id%200..1>[Node],[NodeObsoletionWithDirectReplacement]-%20has%20direct%20replacement%201..1>[Node],[NodeObsoletionWithNoDirectReplacement]-%20has%20nondirect%20replacement%201..*>[Node],[NodeUnobsoletion]-%20consider%200..1>[Node],[NodeUnobsoletion]-%20replaced%20by%200..1>[Node],[EdgeCreation]-%20object%200..1>[Node],[EdgeDeletion]-%20object%200..1>[Node],[EdgeObsoletion]-%20object%200..1>[Node],[MappingCreation]-%20object(i)%200..1>[Node],[NewMapping]-%20object%200..1>[Node],[RemoveMapping]-%20object%200..1>[Node],[NewMetadataAssertion]-%20object%200..1>[Node],[RemoveMetadataAssertion]-%20object%200..1>[Node],[Edge]-%20object%200..1>[Node],[EdgeCreation]-%20predicate%200..1>[Node],[EdgeDeletion]-%20predicate%200..1>[Node],[EdgeObsoletion]-%20predicate%200..1>[Node],[MappingCreation]-%20predicate(i)%200..1>[Node],[NewMapping]-%20predicate%200..1>[Node],[RemoveMapping]-%20predicate%200..1>[Node],[NewMetadataAssertion]-%20predicate%200..1>[Node],[RemoveMetadataAssertion]-%20predicate%200..1>[Node],[Edge]-%20predicate%200..1>[Node],[PropertyValue]-%20property%200..1>[Node],[Annotation]-%20property(i)%200..1>[Node],[RemoveNodeFromSubset]-%20about%20node%200..1>[Node],[EdgeCreation]-%20subject%200..1>[Node],[EdgeDeletion]-%20subject%200..1>[Node],[EdgeObsoletion]-%20subject%200..1>[Node],[MappingCreation]-%20subject(i)%200..1>[Node],[Edge]-%20subject%200..1>[Node],[ClassCreation]-%20superclass%200..1>[Node],[Node]^-[InstanceNode],[Node]^-[ClassNode],[OntologyElement]^-[Node],[RemoveMetadataAssertion],[RemoveMapping],[PropertyValue],[NodeCreation],[NodeChange],[NewMetadataAssertion],[NewMapping],[MappingCreation],[InstanceNode],[EdgeObsoletion],[EdgeDeletion],[EdgeCreation],[EdgeChange],[Edge],[ClassNode],[ClassCreation],[Annotation])](https://yuml.me/diagram/nofunky;dir:TB/class/[RemoveNodeFromSubset],[OntologyElement],[NodeUnobsoletion],[NodeObsoletionWithNoDirectReplacement],[NodeObsoletionWithDirectReplacement],[NodeObsoletion],[NodeDirectMerge],[Annotation]<annotation%20set%200..1-++[Node&#124;id:string;name:string%20%3F;owl_type:owl_type_enum%20%3F],[NodeChange]-%20about%20node%200..1>[Node],[EdgeChange]-%20subject%200..1>[Node],[NodeObsoletion]-%20has%20direct%20replacement%200..1>[Node],[NodeObsoletion]-%20has%20nondirect%20replacement%200..*>[Node],[MappingCreation]-%20object%200..1>[Node],[MappingCreation]-%20predicate%200..1>[Node],[MappingCreation]-%20subject%200..1>[Node],[NodeDirectMerge]-%20about%20node%200..1>[Node],[NodeDirectMerge]-%20has%20direct%20replacement%201..1>[Node],[NodeCreation]-%20node%20id%200..1>[Node],[NodeObsoletionWithDirectReplacement]-%20has%20direct%20replacement%201..1>[Node],[NodeObsoletionWithNoDirectReplacement]-%20has%20nondirect%20replacement%201..*>[Node],[NodeUnobsoletion]-%20consider%200..1>[Node],[NodeUnobsoletion]-%20replaced%20by%200..1>[Node],[EdgeCreation]-%20object%200..1>[Node],[EdgeDeletion]-%20object%200..1>[Node],[EdgeObsoletion]-%20object%200..1>[Node],[MappingCreation]-%20object(i)%200..1>[Node],[NewMapping]-%20object%200..1>[Node],[RemoveMapping]-%20object%200..1>[Node],[NewMetadataAssertion]-%20object%200..1>[Node],[RemoveMetadataAssertion]-%20object%200..1>[Node],[Edge]-%20object%200..1>[Node],[EdgeCreation]-%20predicate%200..1>[Node],[EdgeDeletion]-%20predicate%200..1>[Node],[EdgeObsoletion]-%20predicate%200..1>[Node],[MappingCreation]-%20predicate(i)%200..1>[Node],[NewMapping]-%20predicate%200..1>[Node],[RemoveMapping]-%20predicate%200..1>[Node],[NewMetadataAssertion]-%20predicate%200..1>[Node],[RemoveMetadataAssertion]-%20predicate%200..1>[Node],[Edge]-%20predicate%200..1>[Node],[PropertyValue]-%20property%200..1>[Node],[Annotation]-%20property(i)%200..1>[Node],[RemoveNodeFromSubset]-%20about%20node%200..1>[Node],[EdgeCreation]-%20subject%200..1>[Node],[EdgeDeletion]-%20subject%200..1>[Node],[EdgeObsoletion]-%20subject%200..1>[Node],[MappingCreation]-%20subject(i)%200..1>[Node],[Edge]-%20subject%200..1>[Node],[ClassCreation]-%20superclass%200..1>[Node],[Node]^-[InstanceNode],[Node]^-[ClassNode],[OntologyElement]^-[Node],[RemoveMetadataAssertion],[RemoveMapping],[PropertyValue],[NodeCreation],[NodeChange],[NewMetadataAssertion],[NewMapping],[MappingCreation],[InstanceNode],[EdgeObsoletion],[EdgeDeletion],[EdgeCreation],[EdgeChange],[Edge],[ClassNode],[ClassCreation],[Annotation])

## Parents

 *  is_a: [OntologyElement](OntologyElement.md) - Any component of an ontology or knowledge graph

## Children

 * [ClassNode](ClassNode.md) - A node that is a class
 * [InstanceNode](InstanceNode.md) - A node that is an individual

## Referenced by Class

 *  **None** *[about node](about_node.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[consider](consider.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **[EdgeChange](EdgeChange.md)** *[edge change➞subject](edge_change_subject.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[has direct replacement](has_direct_replacement.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[has nondirect replacement](has_nondirect_replacement.md)*  <sub>0..\*</sub>  **[Node](Node.md)**
 *  **[NodeObsoletion](NodeObsoletion.md)** *[has replacement](has_replacement.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **[MappingCreation](MappingCreation.md)** *[mapping creation➞object](mapping_creation_object.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **[MappingCreation](MappingCreation.md)** *[mapping creation➞predicate](mapping_creation_predicate.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **[MappingCreation](MappingCreation.md)** *[mapping creation➞subject](mapping_creation_subject.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **[NodeDirectMerge](NodeDirectMerge.md)** *[node direct merge➞about node](node_direct_merge_about_node.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **[NodeDirectMerge](NodeDirectMerge.md)** *[node direct merge➞has direct replacement](node_direct_merge_has_direct_replacement.md)*  <sub>1..1</sub>  **[Node](Node.md)**
 *  **None** *[node id](node_id.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **[NodeObsoletionWithDirectReplacement](NodeObsoletionWithDirectReplacement.md)** *[node obsoletion with direct replacement➞has direct replacement](node_obsoletion_with_direct_replacement_has_direct_replacement.md)*  <sub>1..1</sub>  **[Node](Node.md)**
 *  **[NodeObsoletionWithNoDirectReplacement](NodeObsoletionWithNoDirectReplacement.md)** *[node obsoletion with no direct replacement➞has nondirect replacement](node_obsoletion_with_no_direct_replacement_has_nondirect_replacement.md)*  <sub>1..\*</sub>  **[Node](Node.md)**
 *  **[NodeUnobsoletion](NodeUnobsoletion.md)** *[node unobsoletion➞consider](node_unobsoletion_consider.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **[NodeUnobsoletion](NodeUnobsoletion.md)** *[node unobsoletion➞replaced by](node_unobsoletion_replaced_by.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[object](object.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[predicate](predicate.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[property](property.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **[RemoveNodeFromSubset](RemoveNodeFromSubset.md)** *[remove node from subset➞about node](remove_node_from_subset_about_node.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[replaced by](replaced_by.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[subject](subject.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[superclass](superclass.md)*  <sub>0..1</sub>  **[Node](Node.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [name](name.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [annotation set](annotation_set.md)  <sub>0..1</sub>
     * Range: [Annotation](Annotation.md)
 * [owl type](owl_type.md)  <sub>0..1</sub>
     * Range: [owl_type_enum](owl_type_enum.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | entity |
|  | | term |

