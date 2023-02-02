
# Class: Configuration


The meaning of operations can be configured

URI: [kgcl:Configuration](http://w3id.org/kgcl/Configuration)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ChangeLanguageElement]^-[Configuration&#124;name_predicate:string%20%3F;definition_predicate:string%20%3F;main_synonym_predicate:string%20%3F;synonym_predicates:string%20%3F;creator_predicate:string%20%3F;contributor_predicate:string%20%3F;obsolete_node_label_prefix:string%20%3F;obsoletion_workflow:string%20%3F;obsoletion_policies:ObsoletionPolicyEnum%20*;obsolete_subclass_of_shadow_property:uriorcurie%20%3F],[ChangeLanguageElement])](https://yuml.me/diagram/nofunky;dir:TB/class/[ChangeLanguageElement]^-[Configuration&#124;name_predicate:string%20%3F;definition_predicate:string%20%3F;main_synonym_predicate:string%20%3F;synonym_predicates:string%20%3F;creator_predicate:string%20%3F;contributor_predicate:string%20%3F;obsolete_node_label_prefix:string%20%3F;obsoletion_workflow:string%20%3F;obsoletion_policies:ObsoletionPolicyEnum%20*;obsolete_subclass_of_shadow_property:uriorcurie%20%3F],[ChangeLanguageElement])

## Parents

 *  is_a: [ChangeLanguageElement](ChangeLanguageElement.md) - A broad grouping for all elements of the change language

## Attributes


### Own

 * [➞name_predicate](configuration__name_predicate.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞definition_predicate](configuration__definition_predicate.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞main_synonym_predicate](configuration__main_synonym_predicate.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞synonym_predicates](configuration__synonym_predicates.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞creator_predicate](configuration__creator_predicate.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞contributor_predicate](configuration__contributor_predicate.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞obsolete_node_label_prefix](configuration__obsolete_node_label_prefix.md)  <sub>0..1</sub>
     * Description: A prefix to add to the label of an obsolete node. This may include a space at the end.
     * Range: [String](types/String.md)
 * [➞obsoletion_workflow](configuration__obsoletion_workflow.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞obsoletion_policies](configuration__obsoletion_policies.md)  <sub>0..\*</sub>
     * Range: [ObsoletionPolicyEnum](ObsoletionPolicyEnum.md)
 * [➞obsolete_subclass_of_shadow_property](configuration__obsolete_subclass_of_shadow_property.md)  <sub>0..1</sub>
     * Description: specifies the annotation property to be used to create a shadow annotation assertion triple when a subclass edge is deleted.
     * Range: [Uriorcurie](types/Uriorcurie.md)
