
# Class: AddToSubset


placing an element inside a subset

URI: [kgcl:AddToSubset](http://w3id.org/kgcl/AddToSubset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SubsetMembershipChange],[RemoveFromSubset],[OntologySubset],[OntologySubset]<in_subset%200..1-++[AddToSubset],[RemoveFromSubset]++-%20has_undo%200..1>[AddToSubset],[AddNodeToSubset]uses%20-.->[AddToSubset],[SubsetMembershipChange]^-[AddToSubset],[AddNodeToSubset])](https://yuml.me/diagram/nofunky;dir:TB/class/[SubsetMembershipChange],[RemoveFromSubset],[OntologySubset],[OntologySubset]<in_subset%200..1-++[AddToSubset],[RemoveFromSubset]++-%20has_undo%200..1>[AddToSubset],[AddNodeToSubset]uses%20-.->[AddToSubset],[SubsetMembershipChange]^-[AddToSubset],[AddNodeToSubset])

## Parents

 *  is_a: [SubsetMembershipChange](SubsetMembershipChange.md) - A change in the membership status of a node with respect to a subset (view)

## Mixin for

 * [AddNodeToSubset](AddNodeToSubset.md) (mixin)  - Places a node inside a subset, by annotating that node

## Referenced by Class

 *  **[RemoveFromSubset](RemoveFromSubset.md)** *[RemoveFromSubset➞has_undo](RemoveFromSubset_has_undo.md)*  <sub>0..1</sub>  **[AddToSubset](AddToSubset.md)**

## Attributes


### Own

 * [AddToSubset➞in_subset](AddToSubset_in_subset.md)  <sub>0..1</sub>
     * Description: subset that the element is being placed inside.
     * Range: [OntologySubset](OntologySubset.md)
