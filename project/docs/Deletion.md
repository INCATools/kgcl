
# Class: deletion


Removal of an element.

URI: [kgcl:Deletion](http://w3id.org/kgcl/Deletion)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Creation]++-%20has%20undo%200..1>[Deletion],[NodeDeletion]uses%20-.->[Deletion],[EdgeDeletion]uses%20-.->[Deletion],[ChangeMixin]^-[Deletion],[NodeDeletion],[EdgeDeletion],[Creation],[ChangeMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Creation]++-%20has%20undo%200..1>[Deletion],[NodeDeletion]uses%20-.->[Deletion],[EdgeDeletion]uses%20-.->[Deletion],[ChangeMixin]^-[Deletion],[NodeDeletion],[EdgeDeletion],[Creation],[ChangeMixin])

## Parents

 *  is_a: [ChangeMixin](ChangeMixin.md) - root class for all change mixins

## Mixin for

 * [EdgeDeletion](EdgeDeletion.md) (mixin)  - An edge change in which an edge is removed. All edge annotations/properies are removed in the same action.
 * [NodeDeletion](NodeDeletion.md) (mixin)  - Deletion of a node from the graph. Note it is recommended nodes are obsoleted and never merged, but this operation exists to represent deletions in ontologies, accidental or otherwise

## Referenced by Class

 *  **[Creation](Creation.md)** *[creation➞has undo](creation_has_undo.md)*  <sub>0..1</sub>  **[Deletion](Deletion.md)**

## Attributes


## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | In general, for OBO ontologies, node elements should never be deleted, always obsolete. However, edge deletion is more common. |

