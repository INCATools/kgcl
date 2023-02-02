
# Class: Agent


a provence-generating agent

URI: [kgcl:Agent](http://w3id.org/kgcl/Agent)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ProvElement],[Activity]<was_informed_by%200..1-%20[Agent&#124;id:string],[Agent]<acted_on_behalf_of%200..1-%20[Agent],[Activity]-%20was_associated_with%200..1>[Agent],[ProvElement]^-[Agent],[Activity])](https://yuml.me/diagram/nofunky;dir:TB/class/[ProvElement],[Activity]<was_informed_by%200..1-%20[Agent&#124;id:string],[Agent]<acted_on_behalf_of%200..1-%20[Agent],[Activity]-%20was_associated_with%200..1>[Agent],[ProvElement]^-[Agent],[Activity])

## Parents

 *  is_a: [ProvElement](ProvElement.md) - A grouping for prov elements

## Referenced by Class

 *  **None** *[acted_on_behalf_of](acted_on_behalf_of.md)*  <sub>0..1</sub>  **[Agent](Agent.md)**
 *  **None** *[agent_set](agent_set.md)*  <sub>0..\*</sub>  **[Agent](Agent.md)**
 *  **None** *[was_associated_with](was_associated_with.md)*  <sub>0..1</sub>  **[Agent](Agent.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [acted_on_behalf_of](acted_on_behalf_of.md)  <sub>0..1</sub>
     * Range: [Agent](Agent.md)
 * [was_informed_by](was_informed_by.md)  <sub>0..1</sub>
     * Range: [Activity](Activity.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | prov:Agent |

