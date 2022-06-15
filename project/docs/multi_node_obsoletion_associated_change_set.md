
# Slot: associated change set


All changes associated with a set of obsoletions. This change set is the composed change set rather than the set of individual changes. For example, if previous state is:
  `A subClassOf B subClassOf C subClassOf D`
and we obsolete {B,C}, then the individual changes are `A moves from B to C` and `B moves from C to D`, but the composed change set is `A moves from B to D`

URI: [kgcl:multi_node_obsoletion_associated_change_set](http://w3id.org/kgcl/multi_node_obsoletion_associated_change_set)


## Domain and Range

[MultiNodeObsoletion](MultiNodeObsoletion.md) &#8594;  <sub>0..\*</sub> [Change](Change.md)

## Parents

 *  is_a: [change set](change_set.md)

## Children


## Used by

 * [MultiNodeObsoletion](MultiNodeObsoletion.md)
