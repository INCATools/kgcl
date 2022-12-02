
# Class: annotation


owl annotations. Not to be confused with annotations sensu GO

URI: [kgcl:Annotation](http://w3id.org/kgcl/Annotation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PropertyValue],[Node],[Node]<property(i)%200..1-%20[Annotation&#124;property_type:string%20%3F;filler_type:string%20%3F;filler(i):string%20%3F],[Annotation]<annotation%20set%200..1-++[Annotation],[PropertyValue]^-[Annotation])](https://yuml.me/diagram/nofunky;dir:TB/class/[PropertyValue],[Node],[Node]<property(i)%200..1-%20[Annotation&#124;property_type:string%20%3F;filler_type:string%20%3F;filler(i):string%20%3F],[Annotation]<annotation%20set%200..1-++[Annotation],[PropertyValue]^-[Annotation])

## Parents

 *  is_a: [PropertyValue](PropertyValue.md) - a property-value pair

## Referenced by Class

 *  **None** *[annotation set](annotation_set.md)*  <sub>0..1</sub>  **[Annotation](Annotation.md)**

## Attributes


### Own

 * [property](property.md)  <sub>0..1</sub>
     * Range: [Node](Node.md)
 * [filler](filler.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [annotation set](annotation_set.md)  <sub>0..1</sub>
     * Range: [Annotation](Annotation.md)
 * [property type](property_type.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [filler type](filler_type.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | owl:Annotation |

