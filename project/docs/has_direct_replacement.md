
# Slot: has direct replacement


An obsoletion replacement where it IS valid to automatically update annotations/edges pointing at the node with its direct replacement

URI: [kgcl:has_direct_replacement](http://w3id.org/kgcl_schema/has_direct_replacement)


## Domain and Range

None &#8594;  <sub>0..1</sub> [Node](Node.md)

## Parents


## Children

 *  [node direct merge➞has direct replacement](node_direct_merge_has_direct_replacement.md)
 *  [node obsoletion with direct replacement➞has direct replacement](node_obsoletion_with_direct_replacement_has_direct_replacement.md)

## Used by

 * [NodeObsoletion](NodeObsoletion.md)
 * [NodeObsoletionWithNoDirectReplacement](NodeObsoletionWithNoDirectReplacement.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | if a node obsoletion C, C about N1, and C has direct replacement N2, and there exists an edge with an edge property referencing N1, it is possible to replace with N2 |
|  | | if a node obsoletion C C about N1, and Chas direct replacement N2, then N1 IAO:0100001 N2 |
| **Close Mappings:** | | IAO:0100001 |

