
# Class: ChangeSetSummaryStatistic


A summary statistic for a set of changes of the same type, grouped by zero or more node properties

URI: [kgcl:ChangeSetSummaryStatistic](http://w3id.org/kgcl/ChangeSetSummaryStatistic)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PropertyValue],[PropertyValue]<property_value_set%200..*-++[ChangeSetSummaryStatistic&#124;change_type:ChangeClassType%20%3F;count:integer%20%3F],[ChangeLanguageElement]^-[ChangeSetSummaryStatistic],[ChangeLanguageElement])](https://yuml.me/diagram/nofunky;dir:TB/class/[PropertyValue],[PropertyValue]<property_value_set%200..*-++[ChangeSetSummaryStatistic&#124;change_type:ChangeClassType%20%3F;count:integer%20%3F],[ChangeLanguageElement]^-[ChangeSetSummaryStatistic],[ChangeLanguageElement])

## Parents

 *  is_a: [ChangeLanguageElement](ChangeLanguageElement.md) - A broad grouping for all elements of the change language

## Referenced by Class


## Attributes


### Own

 * [ChangeSetSummaryStatistic➞change type](ChangeSetSummaryStatistic_change_type.md)  <sub>0..1</sub>
     * Range: [ChangeClassType](types/ChangeClassType.md)
 * [ChangeSetSummaryStatistic➞count](ChangeSetSummaryStatistic_count.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [ChangeSetSummaryStatistic➞property_value_set](ChangeSetSummaryStatistic_property_value_set.md)  <sub>0..\*</sub>
     * Description: Summary statistic is grouped by these constraints
     * Range: [PropertyValue](PropertyValue.md)
