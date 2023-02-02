
# Slot: has_nondirect_replacement


An obsoletion replacement where it is NOT valid to automatically update annotations/edges pointing at the node with its direct replacement

URI: [kgcl:has_nondirect_replacement](http://w3id.org/kgcl/has_nondirect_replacement)


## Domain and Range

None &#8594;  <sub>0..\*</sub> [Node](Node.md)

## Parents


## Children

 *  [NodeObsoletionWithNoDirectReplacement➞has_nondirect_replacement](NodeObsoletionWithNoDirectReplacement_has_nondirect_replacement.md)

## Used by

 * [NodeDirectMerge](NodeDirectMerge.md)
 * [NodeObsoletion](NodeObsoletion.md)
 * [NodeObsoletionWithDirectReplacement](NodeObsoletionWithDirectReplacement.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | if a node obsoletion C, C about N1, and C has direct replacement N2, and there exists an edge with an edge property referencing N1, it is possible to replace with N2 |
|  | | if a node obsoletion C C about N1, and Chas direct replacement N2, then N1 oio:consider N2 |
| **Close Mappings:** | | oio:consider |

