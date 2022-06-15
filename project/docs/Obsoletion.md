
# Class: obsoletion


Obsoletion of an element deprecates usage of that element, but does not delete that element.

URI: [kgcl:Obsoletion](http://w3id.org/kgcl/Obsoletion)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Unobsoletion],[OntologyElement],[Obsoletion]<has%20undo%200..1-++[Obsoletion],[OntologyElement]<about%200..1-++[Obsoletion],[Unobsoletion]++-%20has%20undo%200..1>[Obsoletion],[NodeObsoletion]uses%20-.->[Obsoletion],[EdgeObsoletion]uses%20-.->[Obsoletion],[Obsoletion]^-[AllowsAutomaticReplacementOfEdges],[ChangeMixin]^-[Obsoletion],[NodeObsoletion],[EdgeObsoletion],[ChangeMixin],[AllowsAutomaticReplacementOfEdges])](https://yuml.me/diagram/nofunky;dir:TB/class/[Unobsoletion],[OntologyElement],[Obsoletion]<has%20undo%200..1-++[Obsoletion],[OntologyElement]<about%200..1-++[Obsoletion],[Unobsoletion]++-%20has%20undo%200..1>[Obsoletion],[NodeObsoletion]uses%20-.->[Obsoletion],[EdgeObsoletion]uses%20-.->[Obsoletion],[Obsoletion]^-[AllowsAutomaticReplacementOfEdges],[ChangeMixin]^-[Obsoletion],[NodeObsoletion],[EdgeObsoletion],[ChangeMixin],[AllowsAutomaticReplacementOfEdges])

## Parents

 *  is_a: [ChangeMixin](ChangeMixin.md) - root class for all change mixins

## Children

 * [AllowsAutomaticReplacementOfEdges](AllowsAutomaticReplacementOfEdges.md) - Applies to an obsoletion in which annotations or edges pointing at the obsoleted node can be automatically rewired to point to a target

## Mixin for

 * [EdgeObsoletion](EdgeObsoletion.md) (mixin)  - An edge change in which an edge is obsoleted.
 * [NodeObsoletion](NodeObsoletion.md) (mixin)  - Obsoletion of a node deprecates usage of that node, but does not delete it.

## Referenced by Class

 *  **[Obsoletion](Obsoletion.md)** *[obsoletion➞has undo](obsoletion_has_undo.md)*  <sub>0..1</sub>  **[Obsoletion](Obsoletion.md)**
 *  **[Unobsoletion](Unobsoletion.md)** *[unobsoletion➞has undo](unobsoletion_has_undo.md)*  <sub>0..1</sub>  **[Obsoletion](Obsoletion.md)**

## Attributes


### Own

 * [obsoletion➞about](obsoletion_about.md)  <sub>0..1</sub>
     * Description: The element that is obsoleted by this change.
     * Range: [OntologyElement](OntologyElement.md)
 * [obsoletion➞has undo](obsoletion_has_undo.md)  <sub>0..1</sub>
     * Description: A change that reverses this change
     * Range: [Obsoletion](Obsoletion.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | deprecation |
|  | | retiring |
| **Comments:** | | In OWL, deprecation is handled by the deprecation axiom. In OBO, we use this, but place additional requirements and expectations on obsolete elements |
| **See also:** | | [http://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term](http://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term) |
|  | | [https://mondo.readthedocs.io/en/latest/editors-guide/merging-and-obsoleting/](https://mondo.readthedocs.io/en/latest/editors-guide/merging-and-obsoleting/) |

