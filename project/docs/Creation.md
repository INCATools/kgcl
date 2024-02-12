
# Class: Creation


Creation of an element.

URI: [kgcl:Creation](http://w3id.org/kgcl/Creation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Deletion],[Deletion]<has_undo%200..1-++[Creation],[NodeCreation]uses%20-.->[Creation],[MappingCreation]uses%20-.->[Creation],[EdgeCreation]uses%20-.->[Creation],[ChangeMixin]^-[Creation],[NodeCreation],[MappingCreation],[EdgeCreation],[ChangeMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Deletion],[Deletion]<has_undo%200..1-++[Creation],[NodeCreation]uses%20-.->[Creation],[MappingCreation]uses%20-.->[Creation],[EdgeCreation]uses%20-.->[Creation],[ChangeMixin]^-[Creation],[NodeCreation],[MappingCreation],[EdgeCreation],[ChangeMixin])

## Parents

 *  is_a: [ChangeMixin](ChangeMixin.md) - root class for all change mixins

## Mixin for

 * [EdgeCreation](EdgeCreation.md) (mixin)  - An edge change in which a de-novo edge is created. The edge is potentially annotated in the same action.
 * [MappingCreation](MappingCreation.md) (mixin)  - A specific kind of edge creation in which the created edge is a mapping.
 * [NodeCreation](NodeCreation.md) (mixin)  - a node change in which a new node is created

## Referenced by Class


## Attributes


### Own

 * [Creation➞has_undo](Creation_has_undo.md)  <sub>0..1</sub>
     * Description: A change that reverses this change
     * Range: [Deletion](Deletion.md)
