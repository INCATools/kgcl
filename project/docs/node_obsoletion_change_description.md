
# Slot: change description


A string serialization of the change. This should be both human-readable, and parseable.

URI: [kgcl:node_obsoletion_change_description](http://w3id.org/kgcl/node_obsoletion_change_description)


## Domain and Range

[NodeObsoletion](NodeObsoletion.md) &#8594;  <sub>0..1</sub> [String](types/String.md)

## Parents

 *  is_a: [change description](change_description.md)

## Children

 *  [node direct merge➞change description](node_direct_merge_change_description.md)
 *  [node obsoletion with direct replacement➞change description](node_obsoletion_with_direct_replacement_change_description.md)
 *  [node obsoletion with no direct replacement➞change description](node_obsoletion_with_no_direct_replacement_change_description.md)

## Used by

 * [NodeObsoletion](NodeObsoletion.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | {'Form 1': 'IRIs are denoted by CURIEs, optionally followed by label in parenthesis'} |
|  | | {'Form 2': "IRIs are denoted by the rdfs:label in single quotes, e.g. 'nervous system'"} |
| **Examples:** | | Example(value="rename UBERON:0002398 from 'manus' to 'hand'", description=None, object=None) |
|  | | Example(value="move 'hand' from 'part of' 'hindlimb' to 'part of' 'forelimb'", description=None, object=None) |
|  | | Example(value="merge 'cellular metabolic process' into 'metabolic process'", description=None, object=None) |
|  | | Example(value="search and replace 'metabolic process' with 'metabolism' in all labels under 'biological process'", description=None, object=None) |
|  | | Example(value="search and replace 'metabolic process' with 'metabolism' in all labels under 'biological process' retaining as 'exact synonym'", description=None, object=None) |

