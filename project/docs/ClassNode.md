
# Class: ClassNode


A node that is a class

URI: [kgcl:ClassNode](http://w3id.org/kgcl/ClassNode)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Node],[Node]^-[ClassNode&#124;id(i):string;name(i):string%20%3F;owl_type(i):OwlTypeEnum%20%3F],[Annotation])](https://yuml.me/diagram/nofunky;dir:TB/class/[Node],[Node]^-[ClassNode&#124;id(i):string;name(i):string%20%3F;owl_type(i):OwlTypeEnum%20%3F],[Annotation])

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
| **Aliases:** | | concept |
| **Mappings:** | | owl:Class |

