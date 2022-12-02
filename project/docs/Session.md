
# Class: session


A session consists of a set of change sets bundled with the activities that generated those change sets

URI: [kgcl:Session](http://w3id.org/kgcl_schema/Session)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Activity]<activity%20set%200..*-++[Session],[Change]<change%20set%200..*-++[Session],[Change],[Activity])](https://yuml.me/diagram/nofunky;dir:TB/class/[Activity]<activity%20set%200..*-++[Session],[Change]<change%20set%200..*-++[Session],[Change],[Activity])

## Attributes


### Own

 * [change set](change_set.md)  <sub>0..\*</sub>
     * Description: A collection of changes
     * Range: [Change](Change.md)
 * [activity set](activity_set.md)  <sub>0..\*</sub>
     * Range: [Activity](Activity.md)
