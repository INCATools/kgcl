
# Slot: has_direct_replacement


An obsoletion replacement where it IS valid to automatically update annotations/edges pointing at the node with its direct replacement

URI: [kgcl:NodeDirectMerge_has_direct_replacement](http://w3id.org/kgcl/NodeDirectMerge_has_direct_replacement)


## Domain and Range

[NodeDirectMerge](NodeDirectMerge.md) &#8594;  <sub>1..1</sub> [Node](Node.md)

## Parents

 *  is_a: [has_direct_replacement](has_direct_replacement.md)

## Children


## Used by

 * [NodeDirectMerge](NodeDirectMerge.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | if a node obsoletion C, C about N1, and C has direct replacement N2, and there exists an edge with an edge property referencing N1, it is possible to replace with N2 |
|  | | if a node obsoletion C C about N1, and Chas direct replacement N2, then N1 IAO:0100001 N2 |
| **Close Mappings:** | | IAO:0100001 |

