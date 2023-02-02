
# Class: InstanceNode


A node that is an individual

URI: [kgcl:InstanceNode](http://w3id.org/kgcl/InstanceNode)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Node],[Node]^-[InstanceNode&#124;id(i):string;name(i):string%20%3F;owl_type(i):OwlTypeEnum%20%3F],[Annotation])](https://yuml.me/diagram/nofunky;dir:TB/class/[Node],[Node]^-[InstanceNode&#124;id(i):string;name(i):string%20%3F;owl_type(i):OwlTypeEnum%20%3F],[Annotation])

## Parents

 *  is_a: [Node](Node.md) - Any named entity in an ontology. May be a class, individual, property

## Attributes


### Inherited from Node:

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
| **Aliases:** | | named individual |
| **Mappings:** | | owl:NamedIndividual |

