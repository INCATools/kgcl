
# Slot: change description


A string serialization of the change. This should be both human-readable, and parseable.

URI: [kgcl:change_description](http://w3id.org/kgcl/change_description)


## Domain and Range

None &#8594;  <sub>0..1</sub> [String](types/String.md)

## Parents


## Children

 *  [edge creation➞change description](edge_creation_change_description.md)
 *  [edge deletion➞change description](edge_deletion_change_description.md)
 *  [edge obsoletion➞change description](edge_obsoletion_change_description.md)
 *  [multi node obsoletion➞change description](multi_node_obsoletion_change_description.md)
 *  [name becomes synonym➞change description](name_becomes_synonym_change_description.md)
 *  [node creation➞change description](node_creation_change_description.md)
 *  [node deletion➞change description](node_deletion_change_description.md)
 *  [node move➞change description](node_move_change_description.md)
 *  [node obsoletion➞change description](node_obsoletion_change_description.md)
 *  [node rename➞change description](node_rename_change_description.md)
 *  [node unobsoletion➞change description](node_unobsoletion_change_description.md)
 *  [predicate change➞change description](predicate_change_change_description.md)
 *  [removed node from subset➞change description](removed_node_from_subset_change_description.md)
 *  [set language for name➞change description](set_language_for_name_change_description.md)

## Used by


## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | {'Form 1': 'IRIs are denoted by CURIEs, optionally followed by label in parenthesis'} |
|  | | {'Form 2': "IRIs are denoted by the rdfs:label in single quotes, e.g. 'nervous system'"} |
| **Examples:** | | Example(value="rename UBERON:0002398 from 'manus' to 'hand'", description=None) |
|  | | Example(value="move 'hand' from 'part of' 'hindlimb' to 'part of' 'forelimb'", description=None) |
|  | | Example(value="merge 'cellular metabolic process' into 'metabolic process'", description=None) |
|  | | Example(value="search and replace 'metabolic process' with 'metabolism' in all labels under 'biological process'", description=None) |
|  | | Example(value="search and replace 'metabolic process' with 'metabolism' in all labels under 'biological process' retaining as 'exact synonym'", description=None) |

