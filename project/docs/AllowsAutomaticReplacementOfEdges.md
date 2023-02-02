
# Class: AllowsAutomaticReplacementOfEdges


Applies to an obsoletion in which annotations or edges pointing at the obsoleted node can be automatically rewired to point to a target

URI: [kgcl:AllowsAutomaticReplacementOfEdges](http://w3id.org/kgcl/AllowsAutomaticReplacementOfEdges)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyElement],[Obsoletion],[NodeObsoletionWithDirectReplacement]uses%20-.->[AllowsAutomaticReplacementOfEdges],[NodeDirectMerge]uses%20-.->[AllowsAutomaticReplacementOfEdges],[Obsoletion]^-[AllowsAutomaticReplacementOfEdges],[NodeObsoletionWithDirectReplacement],[NodeDirectMerge])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyElement],[Obsoletion],[NodeObsoletionWithDirectReplacement]uses%20-.->[AllowsAutomaticReplacementOfEdges],[NodeDirectMerge]uses%20-.->[AllowsAutomaticReplacementOfEdges],[Obsoletion]^-[AllowsAutomaticReplacementOfEdges],[NodeObsoletionWithDirectReplacement],[NodeDirectMerge])

## Parents

 *  is_a: [Obsoletion](Obsoletion.md) - Obsoletion of an element deprecates usage of that element, but does not delete that element.

## Mixin for

 * [NodeDirectMerge](NodeDirectMerge.md) (mixin)  - An obsoletion change in which all metadata (including name/label) from the source node is deleted and added to the target node, and edges can automatically be rewired to point to the target node
 * [NodeObsoletionWithDirectReplacement](NodeObsoletionWithDirectReplacement.md) (mixin)  - An obsoletion change in which information from the obsoleted node is selectively copied to a single target, and edges can automatically be rewired to point to the target node

## Referenced by Class


## Attributes


### Inherited from Obsoletion:

 * [Obsoletion➞about](Obsoletion_about.md)  <sub>0..1</sub>
     * Description: The element that is obsoleted by this change.
     * Range: [OntologyElement](OntologyElement.md)
 * [Obsoletion➞has_undo](Obsoletion_has_undo.md)  <sub>0..1</sub>
     * Description: A change that reverses this change
     * Range: [Obsoletion](Obsoletion.md)
