
# Class: LanguageTagChange




URI: [kgcl:LanguageTagChange](http://w3id.org/kgcl/LanguageTagChange)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SetLanguageForName]uses%20-.->[LanguageTagChange&#124;old_value:LanguageTag%20%3F;new_value:LanguageTag%20%3F],[DatatypeOrLanguageTagChange]^-[LanguageTagChange],[SetLanguageForName],[DatatypeOrLanguageTagChange])](https://yuml.me/diagram/nofunky;dir:TB/class/[SetLanguageForName]uses%20-.->[LanguageTagChange&#124;old_value:LanguageTag%20%3F;new_value:LanguageTag%20%3F],[DatatypeOrLanguageTagChange]^-[LanguageTagChange],[SetLanguageForName],[DatatypeOrLanguageTagChange])

## Parents

 *  is_a: [DatatypeOrLanguageTagChange](DatatypeOrLanguageTagChange.md) - A change in a value assertion where the value remain unchanged but either the datatype or language changes

## Mixin for

 * [SetLanguageForName](SetLanguageForName.md) (mixin)  - A node change where the string value for the name is unchanged but the language tag is set

## Referenced by Class


## Attributes


### Own

 * [LanguageTagChange➞old_value](LanguageTagChange_old_value.md)  <sub>0..1</sub>
     * Description: The value of a property held in the old instance of the ontology
     * Range: [LanguageTag](types/LanguageTag.md)
 * [LanguageTagChange➞new_value](LanguageTagChange_new_value.md)  <sub>0..1</sub>
     * Description: The value of a property held in the new instance of the ontology
     * Range: [LanguageTag](types/LanguageTag.md)
