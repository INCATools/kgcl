
# Class: property value


a property-value pair

URI: [kgcl:PropertyValue](http://w3id.org/kgcl/PropertyValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Node]<property%200..1-%20[PropertyValue&#124;filler:string%20%3F],[ChangeSetSummaryStatistic]++-%20property%20value%20set%200..*>[PropertyValue],[PropertyValue]^-[Annotation],[OntologyElement]^-[PropertyValue],[OntologyElement],[Node],[ChangeSetSummaryStatistic],[Annotation])](https://yuml.me/diagram/nofunky;dir:TB/class/[Node]<property%200..1-%20[PropertyValue&#124;filler:string%20%3F],[ChangeSetSummaryStatistic]++-%20property%20value%20set%200..*>[PropertyValue],[PropertyValue]^-[Annotation],[OntologyElement]^-[PropertyValue],[OntologyElement],[Node],[ChangeSetSummaryStatistic],[Annotation])

## Parents

 *  is_a: [OntologyElement](OntologyElement.md) - Any component of an ontology or knowledge graph

## Children

 * [Annotation](Annotation.md) - owl annotations. Not to be confused with annotations sensu GO

## Referenced by Class

 *  **[ChangeSetSummaryStatistic](ChangeSetSummaryStatistic.md)** *[change set summary statistic➞property value set](change_set_summary_statistic_property_value_set.md)*  <sub>0..\*</sub>  **[PropertyValue](PropertyValue.md)**
 *  **None** *[property value set](property_value_set.md)*  <sub>0..\*</sub>  **[PropertyValue](PropertyValue.md)**

## Attributes


### Own

 * [property](property.md)  <sub>0..1</sub>
     * Range: [Node](Node.md)
 * [filler](filler.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
