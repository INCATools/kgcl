
# Class: add to subset


placing an element inside a subset

URI: [kgcl:AddToSubset](http://w3id.org/kgcl/AddToSubset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SubsetMembershipChange],[RemoveFromSubset],[OntologySubset],[OntologySubset]<in%20subset%200..1-++[AddToSubset],[RemoveFromSubset]++-%20has%20undo%200..1>[AddToSubset],[AddNodeToSubset]uses%20-.->[AddToSubset],[SubsetMembershipChange]^-[AddToSubset],[AddNodeToSubset])](https://yuml.me/diagram/nofunky;dir:TB/class/[SubsetMembershipChange],[RemoveFromSubset],[OntologySubset],[OntologySubset]<in%20subset%200..1-++[AddToSubset],[RemoveFromSubset]++-%20has%20undo%200..1>[AddToSubset],[AddNodeToSubset]uses%20-.->[AddToSubset],[SubsetMembershipChange]^-[AddToSubset],[AddNodeToSubset])

## Parents

 *  is_a: [SubsetMembershipChange](SubsetMembershipChange.md) - A change in the membership status of a node with respect to a subset (view)

## Mixin for

 * [AddNodeToSubset](AddNodeToSubset.md) (mixin)  - Places a node inside a subset, by annotating that node

## Referenced by Class

 *  **[RemoveFromSubset](RemoveFromSubset.md)** *[remove from subset➞has undo](remove_from_subset_has_undo.md)*  <sub>0..1</sub>  **[AddToSubset](AddToSubset.md)**

## Attributes


### Own

 * [add to subset➞in subset](add_to_subset_in_subset.md)  <sub>0..1</sub>
     * Description: subset that the element is being placed inside.
     * Range: [OntologySubset](OntologySubset.md)
