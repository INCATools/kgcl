
# Class: Session


A session consists of a set of change sets bundled with the activities that generated those change sets

URI: [kgcl:Session](http://w3id.org/kgcl/Session)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Activity]<activity_set%200..*-++[Session],[Change]<change_set%200..*-++[Session],[ChangeLanguageElement]^-[Session],[ChangeLanguageElement],[Change],[Activity])](https://yuml.me/diagram/nofunky;dir:TB/class/[Activity]<activity_set%200..*-++[Session],[Change]<change_set%200..*-++[Session],[ChangeLanguageElement]^-[Session],[ChangeLanguageElement],[Change],[Activity])

## Parents

 *  is_a: [ChangeLanguageElement](ChangeLanguageElement.md) - A broad grouping for all elements of the change language

## Attributes


### Own

 * [change_set](change_set.md)  <sub>0..\*</sub>
     * Description: A collection of changes
     * Range: [Change](Change.md)
 * [activity_set](activity_set.md)  <sub>0..\*</sub>
     * Range: [Activity](Activity.md)
