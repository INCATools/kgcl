
# Class: Activity


a provence-generating activity

URI: [kgcl:Activity](http://w3id.org/kgcl/Activity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ProvElement],[Change],[Agent],[Agent]<was_associated_with%200..1-%20[Activity&#124;id:string;started_at_time:string%20%3F;ended_at_time:string%20%3F;used:string%20%3F;description:string%20%3F],[Activity]<was_informed_by%200..1-%20[Activity],[Change]-%20was_generated_by%200..1>[Activity],[Session]++-%20activity_set%200..*>[Activity],[Change]-%20was_generated_by(i)%200..1>[Activity],[ProvElement]^-[Activity],[Session])](https://yuml.me/diagram/nofunky;dir:TB/class/[ProvElement],[Change],[Agent],[Agent]<was_associated_with%200..1-%20[Activity&#124;id:string;started_at_time:string%20%3F;ended_at_time:string%20%3F;used:string%20%3F;description:string%20%3F],[Activity]<was_informed_by%200..1-%20[Activity],[Change]-%20was_generated_by%200..1>[Activity],[Session]++-%20activity_set%200..*>[Activity],[Change]-%20was_generated_by(i)%200..1>[Activity],[ProvElement]^-[Activity],[Session])

## Parents

 *  is_a: [ProvElement](ProvElement.md) - A grouping for prov elements

## Referenced by Class

 *  **[Change](Change.md)** *[Change➞was_generated_by](Change_was_generated_by.md)*  <sub>0..1</sub>  **[Activity](Activity.md)**
 *  **None** *[activity_set](activity_set.md)*  <sub>0..\*</sub>  **[Activity](Activity.md)**
 *  **None** *[was_generated_by](was_generated_by.md)*  <sub>0..1</sub>  **[Activity](Activity.md)**
 *  **None** *[was_informed_by](was_informed_by.md)*  <sub>0..1</sub>  **[Activity](Activity.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [started_at_time](started_at_time.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [ended_at_time](ended_at_time.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [was_informed_by](was_informed_by.md)  <sub>0..1</sub>
     * Range: [Activity](Activity.md)
 * [was_associated_with](was_associated_with.md)  <sub>0..1</sub>
     * Range: [Agent](Agent.md)
 * [used](used.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | prov:Activity |

