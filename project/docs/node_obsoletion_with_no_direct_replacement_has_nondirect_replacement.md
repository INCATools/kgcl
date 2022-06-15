
# Slot: has nondirect replacement


An obsoletion replacement where it is NOT valid to automatically update annotations/edges pointing at the node with its direct replacement

URI: [kgcl:node_obsoletion_with_no_direct_replacement_has_nondirect_replacement](http://w3id.org/kgcl/node_obsoletion_with_no_direct_replacement_has_nondirect_replacement)


## Domain and Range

[NodeObsoletionWithNoDirectReplacement](NodeObsoletionWithNoDirectReplacement.md) &#8594;  <sub>1..\*</sub> [Node](Node.md)

## Parents

 *  is_a: [has nondirect replacement](has_nondirect_replacement.md)

## Children


## Used by

 * [NodeObsoletionWithNoDirectReplacement](NodeObsoletionWithNoDirectReplacement.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | if a node obsoletion C, C about N1, and C has direct replacement N2, and there exists an edge with an edge property referencing N1, it is possible to replace with N2 |
|  | | if a node obsoletion C C about N1, and Chas direct replacement N2, then N1 oio:consider N2 |
| **Close Mappings:** | | oio:consider |

