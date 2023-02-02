
# Class: Node


Any named entity in an ontology. May be a class, individual, property

URI: [kgcl:Node](http://w3id.org/kgcl/Node)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[RemoveNodeFromSubset],[OntologyElement],[NodeUnobsoletion],[NodeObsoletionWithNoDirectReplacement],[NodeObsoletionWithDirectReplacement],[NodeObsoletion],[NodeDirectMerge],[Annotation]<annotation_set%200..1-++[Node&#124;id:string;name:string%20%3F;owl_type:OwlTypeEnum%20%3F],[EdgeChange]-%20subject%200..1>[Node],[MappingCreation]-%20object%200..1>[Node],[MappingCreation]-%20predicate%200..1>[Node],[MappingCreation]-%20subject%200..1>[Node],[NodeDirectMerge]-%20about_node%200..1>[Node],[NodeDirectMerge]-%20has_direct_replacement%201..1>[Node],[NodeObsoletionWithDirectReplacement]-%20has_direct_replacement%201..1>[Node],[NodeObsoletionWithNoDirectReplacement]-%20has_nondirect_replacement%201..*>[Node],[NodeUnobsoletion]-%20consider%200..1>[Node],[NodeUnobsoletion]-%20replaced%20by%200..1>[Node],[RemoveNodeFromSubset]-%20about_node%200..1>[Node],[NodeChange]-%20about_node%200..1>[Node],[NodeObsoletion]-%20has_direct_replacement%200..1>[Node],[NodeObsoletion]-%20has_nondirect_replacement%200..*>[Node],[NodeCreation]-%20node_id%200..1>[Node],[EdgeCreation]-%20object%200..1>[Node],[EdgeDeletion]-%20object%200..1>[Node],[EdgeObsoletion]-%20object%200..1>[Node],[MappingCreation]-%20object(i)%200..1>[Node],[NewMapping]-%20object%200..1>[Node],[RemoveMapping]-%20object%200..1>[Node],[NewMetadataAssertion]-%20object%200..1>[Node],[RemoveMetadataAssertion]-%20object%200..1>[Node],[Edge]-%20object%200..1>[Node],[EdgeCreation]-%20predicate%200..1>[Node],[EdgeDeletion]-%20predicate%200..1>[Node],[EdgeObsoletion]-%20predicate%200..1>[Node],[MappingCreation]-%20predicate(i)%200..1>[Node],[NewMapping]-%20predicate%200..1>[Node],[RemoveMapping]-%20predicate%200..1>[Node],[NewMetadataAssertion]-%20predicate%200..1>[Node],[RemoveMetadataAssertion]-%20predicate%200..1>[Node],[Edge]-%20predicate%200..1>[Node],[PropertyValue]-%20property%200..1>[Node],[Annotation]-%20property(i)%200..1>[Node],[EdgeCreation]-%20subject%200..1>[Node],[EdgeDeletion]-%20subject%200..1>[Node],[EdgeObsoletion]-%20subject%200..1>[Node],[MappingCreation]-%20subject(i)%200..1>[Node],[Edge]-%20subject%200..1>[Node],[ClassCreation]-%20superclass%200..1>[Node],[Node]^-[InstanceNode],[Node]^-[ClassNode],[OntologyElement]^-[Node],[RemoveMetadataAssertion],[RemoveMapping],[PropertyValue],[NodeCreation],[NodeChange],[NewMetadataAssertion],[NewMapping],[MappingCreation],[InstanceNode],[EdgeObsoletion],[EdgeDeletion],[EdgeCreation],[EdgeChange],[Edge],[ClassNode],[ClassCreation],[Annotation])](https://yuml.me/diagram/nofunky;dir:TB/class/[RemoveNodeFromSubset],[OntologyElement],[NodeUnobsoletion],[NodeObsoletionWithNoDirectReplacement],[NodeObsoletionWithDirectReplacement],[NodeObsoletion],[NodeDirectMerge],[Annotation]<annotation_set%200..1-++[Node&#124;id:string;name:string%20%3F;owl_type:OwlTypeEnum%20%3F],[EdgeChange]-%20subject%200..1>[Node],[MappingCreation]-%20object%200..1>[Node],[MappingCreation]-%20predicate%200..1>[Node],[MappingCreation]-%20subject%200..1>[Node],[NodeDirectMerge]-%20about_node%200..1>[Node],[NodeDirectMerge]-%20has_direct_replacement%201..1>[Node],[NodeObsoletionWithDirectReplacement]-%20has_direct_replacement%201..1>[Node],[NodeObsoletionWithNoDirectReplacement]-%20has_nondirect_replacement%201..*>[Node],[NodeUnobsoletion]-%20consider%200..1>[Node],[NodeUnobsoletion]-%20replaced%20by%200..1>[Node],[RemoveNodeFromSubset]-%20about_node%200..1>[Node],[NodeChange]-%20about_node%200..1>[Node],[NodeObsoletion]-%20has_direct_replacement%200..1>[Node],[NodeObsoletion]-%20has_nondirect_replacement%200..*>[Node],[NodeCreation]-%20node_id%200..1>[Node],[EdgeCreation]-%20object%200..1>[Node],[EdgeDeletion]-%20object%200..1>[Node],[EdgeObsoletion]-%20object%200..1>[Node],[MappingCreation]-%20object(i)%200..1>[Node],[NewMapping]-%20object%200..1>[Node],[RemoveMapping]-%20object%200..1>[Node],[NewMetadataAssertion]-%20object%200..1>[Node],[RemoveMetadataAssertion]-%20object%200..1>[Node],[Edge]-%20object%200..1>[Node],[EdgeCreation]-%20predicate%200..1>[Node],[EdgeDeletion]-%20predicate%200..1>[Node],[EdgeObsoletion]-%20predicate%200..1>[Node],[MappingCreation]-%20predicate(i)%200..1>[Node],[NewMapping]-%20predicate%200..1>[Node],[RemoveMapping]-%20predicate%200..1>[Node],[NewMetadataAssertion]-%20predicate%200..1>[Node],[RemoveMetadataAssertion]-%20predicate%200..1>[Node],[Edge]-%20predicate%200..1>[Node],[PropertyValue]-%20property%200..1>[Node],[Annotation]-%20property(i)%200..1>[Node],[EdgeCreation]-%20subject%200..1>[Node],[EdgeDeletion]-%20subject%200..1>[Node],[EdgeObsoletion]-%20subject%200..1>[Node],[MappingCreation]-%20subject(i)%200..1>[Node],[Edge]-%20subject%200..1>[Node],[ClassCreation]-%20superclass%200..1>[Node],[Node]^-[InstanceNode],[Node]^-[ClassNode],[OntologyElement]^-[Node],[RemoveMetadataAssertion],[RemoveMapping],[PropertyValue],[NodeCreation],[NodeChange],[NewMetadataAssertion],[NewMapping],[MappingCreation],[InstanceNode],[EdgeObsoletion],[EdgeDeletion],[EdgeCreation],[EdgeChange],[Edge],[ClassNode],[ClassCreation],[Annotation])

## Parents

 *  is_a: [OntologyElement](OntologyElement.md) - Any component of an ontology or knowledge graph

## Children

 * [ClassNode](ClassNode.md) - A node that is a class
 * [InstanceNode](InstanceNode.md) - A node that is an individual

## Referenced by Class

 *  **[EdgeChange](EdgeChange.md)** *[EdgeChange➞subject](EdgeChange_subject.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **[MappingCreation](MappingCreation.md)** *[MappingCreation➞object](MappingCreation_object.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **[MappingCreation](MappingCreation.md)** *[MappingCreation➞predicate](MappingCreation_predicate.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **[MappingCreation](MappingCreation.md)** *[MappingCreation➞subject](MappingCreation_subject.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **[NodeDirectMerge](NodeDirectMerge.md)** *[NodeDirectMerge➞about_node](NodeDirectMerge_about_node.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **[NodeDirectMerge](NodeDirectMerge.md)** *[NodeDirectMerge➞has_direct_replacement](NodeDirectMerge_has_direct_replacement.md)*  <sub>1..1</sub>  **[Node](Node.md)**
 *  **[NodeObsoletionWithDirectReplacement](NodeObsoletionWithDirectReplacement.md)** *[NodeObsoletionWithDirectReplacement➞has_direct_replacement](NodeObsoletionWithDirectReplacement_has_direct_replacement.md)*  <sub>1..1</sub>  **[Node](Node.md)**
 *  **[NodeObsoletionWithNoDirectReplacement](NodeObsoletionWithNoDirectReplacement.md)** *[NodeObsoletionWithNoDirectReplacement➞has_nondirect_replacement](NodeObsoletionWithNoDirectReplacement_has_nondirect_replacement.md)*  <sub>1..\*</sub>  **[Node](Node.md)**
 *  **[NodeUnobsoletion](NodeUnobsoletion.md)** *[NodeUnobsoletion➞consider](NodeUnobsoletion_consider.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **[NodeUnobsoletion](NodeUnobsoletion.md)** *[NodeUnobsoletion➞replaced by](NodeUnobsoletion_replaced_by.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **[RemoveNodeFromSubset](RemoveNodeFromSubset.md)** *[RemoveNodeFromSubset➞about_node](RemoveNodeFromSubset_about_node.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[about_node](about_node.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[consider](consider.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[has_direct_replacement](has_direct_replacement.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[has_nondirect_replacement](has_nondirect_replacement.md)*  <sub>0..\*</sub>  **[Node](Node.md)**
 *  **[NodeObsoletion](NodeObsoletion.md)** *[has_replacement](has_replacement.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[node_id](node_id.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[object](object.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[predicate](predicate.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[property](property.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[replaced by](replaced_by.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[subject](subject.md)*  <sub>0..1</sub>  **[Node](Node.md)**
 *  **None** *[superclass](superclass.md)*  <sub>0..1</sub>  **[Node](Node.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [name](name.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [annotation_set](annotation_set.md)  <sub>0..1</sub>
     * Range: [Annotation](Annotation.md)
 * [owl_type](owl_type.md)  <sub>0..1</sub>
     * Range: [OwlTypeEnum](OwlTypeEnum.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | entity |
|  | | term |

