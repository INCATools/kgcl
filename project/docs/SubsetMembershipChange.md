
# Class: subset membership change


A change in the membership status of a node with respect to a subset (view)

URI: [kgcl:SubsetMembershipChange](http://w3id.org/kgcl/SubsetMembershipChange)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologySubset]<in%20subset%200..1-++[SubsetMembershipChange],[SubsetMembershipChange]^-[RemoveFromSubset],[SubsetMembershipChange]^-[AddToSubset],[ChangeMixin]^-[SubsetMembershipChange],[RemoveFromSubset],[OntologySubset],[ChangeMixin],[AddToSubset])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologySubset]<in%20subset%200..1-++[SubsetMembershipChange],[SubsetMembershipChange]^-[RemoveFromSubset],[SubsetMembershipChange]^-[AddToSubset],[ChangeMixin]^-[SubsetMembershipChange],[RemoveFromSubset],[OntologySubset],[ChangeMixin],[AddToSubset])

## Parents

 *  is_a: [ChangeMixin](ChangeMixin.md) - root class for all change mixins

## Children

 * [AddToSubset](AddToSubset.md) - placing an element inside a subset
 * [RemoveFromSubset](RemoveFromSubset.md) - removing an element from a subset

## Referenced by Class


## Attributes


### Own

 * [in subset](in_subset.md)  <sub>0..1</sub>
     * Description: The subset that pertains to this change
     * Range: [OntologySubset](OntologySubset.md)
