
# Slot: change_description


A string serialization of the change. This should be both human-readable, and parseable.

URI: [kgcl:change_description](http://w3id.org/kgcl/change_description)


## Domain and Range

None &#8594;  <sub>0..1</sub> [String](types/String.md)

## Parents


## Children

 *  [EdgeCreation➞change_description](EdgeCreation_change_description.md)
 *  [EdgeDeletion➞change_description](EdgeDeletion_change_description.md)
 *  [EdgeObsoletion➞change_description](EdgeObsoletion_change_description.md)
 *  [MultiNodeObsoletion➞change_description](MultiNodeObsoletion_change_description.md)
 *  [NameBecomesSynonym➞change_description](NameBecomesSynonym_change_description.md)
 *  [NodeCreation➞change_description](NodeCreation_change_description.md)
 *  [NodeDeletion➞change_description](NodeDeletion_change_description.md)
 *  [NodeMove➞change_description](NodeMove_change_description.md)
 *  [NodeObsoletion➞change_description](NodeObsoletion_change_description.md)
 *  [NodeRename➞change_description](NodeRename_change_description.md)
 *  [NodeUnobsoletion➞change_description](NodeUnobsoletion_change_description.md)
 *  [PredicateChange➞change_description](PredicateChange_change_description.md)
 *  [RemoveNodeFromSubset➞change_description](RemoveNodeFromSubset_change_description.md)
 *  [SetLanguageForName➞change_description](SetLanguageForName_change_description.md)

## Used by


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

