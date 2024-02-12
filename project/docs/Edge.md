
# Class: Edge


A relationship between two nodes.
Currently the only kinds of edges supported in KGCL:

  * A subClassOf B <==> Edge(subject=A, predicate=owl:subClassOf, object=B)
  * A subClassOf P some B <==> Edge(subject=A, predicate=P, object=B)
  * P subPropertyOf Q <==> Edge(subject=P, predicate=owl:subPropertyOf, object=Q)

These represent the most common kind of pairwise relationship between classes, and classes are the dominant node type in ontologies.
In future a wider variety of OWL axiom types will be supportedn through the use of an additional edge property/slot to indicate the interpretation of the axiom, following owlstar (https://github.com/cmungall/owlstar).
For example:
 * `A subClassOf R only B <==> Edge(subject=A, predicate=P, object=B, interpretation=AllOnly)`
 * `A Annotation(P,B) <==> Edge(subject=A, predicate=P, object=B, interpretation=annotationAssertion)`

Note that not all axioms are intended to map to edges. Axioms/triples where the object is a literal would be represented as node properties. Complex OWL axioms involving nesting would have their own dedicated construct, or may be represented generically. These are out of scope for the current version of KGCL

URI: [kgcl:Edge](http://w3id.org/kgcl/Edge)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyElement],[Node],[Annotation]<annotation_set%200..1-++[Edge&#124;subject_representation:string%20%3F;predicate_representation:string%20%3F;object_representation:string%20%3F],[Node]<object%200..1-%20[Edge],[Node]<predicate%200..1-%20[Edge],[Node]<subject%200..1-%20[Edge],[EdgeChange]++-%20about_edge%200..1>[Edge],[OntologyElement]^-[Edge],[EdgeChange],[Annotation])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyElement],[Node],[Annotation]<annotation_set%200..1-++[Edge&#124;subject_representation:string%20%3F;predicate_representation:string%20%3F;object_representation:string%20%3F],[Node]<object%200..1-%20[Edge],[Node]<predicate%200..1-%20[Edge],[Node]<subject%200..1-%20[Edge],[EdgeChange]++-%20about_edge%200..1>[Edge],[OntologyElement]^-[Edge],[EdgeChange],[Annotation])

## Parents

 *  is_a: [OntologyElement](OntologyElement.md) - Any component of an ontology or knowledge graph

## Referenced by Class

 *  **None** *[about_edge](about_edge.md)*  <sub>0..1</sub>  **[Edge](Edge.md)**

## Attributes


### Own

 * [subject](subject.md)  <sub>0..1</sub>
     * Range: [Node](Node.md)
 * [predicate](predicate.md)  <sub>0..1</sub>
     * Range: [Node](Node.md)
 * [object](object.md)  <sub>0..1</sub>
     * Range: [Node](Node.md)
 * [subject_representation](subject_representation.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [predicate_representation](predicate_representation.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [object_representation](object_representation.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [annotation_set](annotation_set.md)  <sub>0..1</sub>
     * Range: [Annotation](Annotation.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | triple |
|  | | axiom |
|  | | relationship |
| **Mappings:** | | owl:Axiom |
|  | | rdf:Statement |

