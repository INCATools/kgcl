
# Class: remove from subset


removing an element from a subset

URI: [kgcl:RemoveFromSubset](http://w3id.org/kgcl/RemoveFromSubset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SubsetMembershipChange],[AddToSubset]<has%20undo%200..1-++[RemoveFromSubset],[OntologySubset]<in%20subset%200..1-++[RemoveFromSubset],[RemoveNodeFromSubset]uses%20-.->[RemoveFromSubset],[SubsetMembershipChange]^-[RemoveFromSubset],[RemoveNodeFromSubset],[OntologySubset],[AddToSubset])](https://yuml.me/diagram/nofunky;dir:TB/class/[SubsetMembershipChange],[AddToSubset]<has%20undo%200..1-++[RemoveFromSubset],[OntologySubset]<in%20subset%200..1-++[RemoveFromSubset],[RemoveNodeFromSubset]uses%20-.->[RemoveFromSubset],[SubsetMembershipChange]^-[RemoveFromSubset],[RemoveNodeFromSubset],[OntologySubset],[AddToSubset])

## Parents

 *  is_a: [SubsetMembershipChange](SubsetMembershipChange.md) - A change in the membership status of a node with respect to a subset (view)

## Mixin for

 * [RemoveNodeFromSubset](RemoveNodeFromSubset.md) (mixin)  - Removes a node from a subset, by removing an annotation

## Referenced by Class


## Attributes


### Own

 * [remove from subset➞in subset](remove_from_subset_in_subset.md)  <sub>0..1</sub>
     * Description: subset that the element is being removed from
     * Range: [OntologySubset](OntologySubset.md)
 * [remove from subset➞has undo](remove_from_subset_has_undo.md)  <sub>0..1</sub>
     * Description: A change that reverses this change
     * Range: [AddToSubset](AddToSubset.md)
