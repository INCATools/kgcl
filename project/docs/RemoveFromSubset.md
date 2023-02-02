
# Class: RemoveFromSubset


removing an element from a subset

URI: [kgcl:RemoveFromSubset](http://w3id.org/kgcl/RemoveFromSubset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SubsetMembershipChange],[AddToSubset]<has_undo%200..1-++[RemoveFromSubset],[OntologySubset]<in_subset%200..1-++[RemoveFromSubset],[RemoveNodeFromSubset]uses%20-.->[RemoveFromSubset],[SubsetMembershipChange]^-[RemoveFromSubset],[RemoveNodeFromSubset],[OntologySubset],[AddToSubset])](https://yuml.me/diagram/nofunky;dir:TB/class/[SubsetMembershipChange],[AddToSubset]<has_undo%200..1-++[RemoveFromSubset],[OntologySubset]<in_subset%200..1-++[RemoveFromSubset],[RemoveNodeFromSubset]uses%20-.->[RemoveFromSubset],[SubsetMembershipChange]^-[RemoveFromSubset],[RemoveNodeFromSubset],[OntologySubset],[AddToSubset])

## Parents

 *  is_a: [SubsetMembershipChange](SubsetMembershipChange.md) - A change in the membership status of a node with respect to a subset (view)

## Mixin for

 * [RemoveNodeFromSubset](RemoveNodeFromSubset.md) (mixin)  - Removes a node from a subset, by removing an annotation

## Referenced by Class


## Attributes


### Own

 * [RemoveFromSubset➞in_subset](RemoveFromSubset_in_subset.md)  <sub>0..1</sub>
     * Description: subset that the element is being removed from
     * Range: [OntologySubset](OntologySubset.md)
 * [RemoveFromSubset➞has_undo](RemoveFromSubset_has_undo.md)  <sub>0..1</sub>
     * Description: A change that reverses this change
     * Range: [AddToSubset](AddToSubset.md)
