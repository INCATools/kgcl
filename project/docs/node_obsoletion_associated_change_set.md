
# Slot: associated change set


All changes forced as a result of this obsoletion. For example, starting with `A subClassOf B subClassOf C`, if we obsolete node B, then we may decide to bundle in a node move change of A from B to C. Note: this change set is not considered a part of the obsoletion, as obsoletion is considered atomic/simple. Instead this is a reference to a change set that may exist elsewhere

URI: [kgcl:node_obsoletion_associated_change_set](http://w3id.org/kgcl/node_obsoletion_associated_change_set)


## Domain and Range

[NodeObsoletion](NodeObsoletion.md) &#8594;  <sub>0..\*</sub> [Change](Change.md)

## Parents

 *  is_a: [change set](change_set.md)

## Children


## Used by

 * [NodeDirectMerge](NodeDirectMerge.md)
 * [NodeObsoletion](NodeObsoletion.md)
 * [NodeObsoletionWithDirectReplacement](NodeObsoletionWithDirectReplacement.md)
 * [NodeObsoletionWithNoDirectReplacement](NodeObsoletionWithNoDirectReplacement.md)
