"""Test delete edge."""
from tests.util import run_test


def test_delete_edge_with_ids():
    """Test delete edge with IDs."""
    input_graph = """_:Ndb451c3aad3841c88d7042f29b20bea8 <http://www.w3.org/2002/07/owl#onProperty> <http://example.org/predicate> .
                     _:Ndb451c3aad3841c88d7042f29b20bea8 <http://www.w3.org/2002/07/owl#someValuesFrom> <http://example.org/object> .
                     _:Ndb451c3aad3841c88d7042f29b20bea8 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Restriction> .
                     <http://example.org/subject> <http://www.w3.org/2000/01/rdf-schema#subClassOf> _:Ndb451c3aad3841c88d7042f29b20bea8 ."""
    kgcl_patch = "delete edge <http://example.org/subject> <http://example.org/predicate> <http://example.org/object>"
    expected_graph = ""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_delete_edge_with_curies():
    """Test delete edge with CURIEs."""
    input_graph = """_:Ndb451c3aad3841c88d7042f29b20bea8 <http://www.w3.org/2002/07/owl#onProperty> <http://example.org/predicate> .
                     _:Ndb451c3aad3841c88d7042f29b20bea8 <http://www.w3.org/2002/07/owl#someValuesFrom> <http://example.org/object> .
                     _:Ndb451c3aad3841c88d7042f29b20bea8 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Restriction> .
                     <http://example.org/subject> <http://www.w3.org/2000/01/rdf-schema#subClassOf> _:Ndb451c3aad3841c88d7042f29b20bea8 ."""
    kgcl_patch = "delete edge ex:subject ex:predicate ex:object"
    expected_graph = ""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_delete_edge_with_labels():
    """Test delete edge with labels."""
    input_graph = """_:Ndb451c3aad3841c88d7042f29b20bea8 <http://www.w3.org/2002/07/owl#onProperty> <http://example.org/predicate> .
                     _:Ndb451c3aad3841c88d7042f29b20bea8 <http://www.w3.org/2002/07/owl#someValuesFrom> <http://example.org/object> .
                     _:Ndb451c3aad3841c88d7042f29b20bea8 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Restriction> .
                     <http://example.org/subject> <http://www.w3.org/2000/01/rdf-schema#subClassOf> _:Ndb451c3aad3841c88d7042f29b20bea8 .
                     <http://example.org/subject> <http://www.w3.org/2000/01/rdf-schema#label> "subject" .
                     <http://example.org/predicate> <http://www.w3.org/2000/01/rdf-schema#label> "predicate" .
                     <http://example.org/object> <http://www.w3.org/2000/01/rdf-schema#label> "object" ."""
    kgcl_patch = "delete edge 'subject' 'predicate' 'object'"
    expected_graph = """<http://example.org/subject> <http://www.w3.org/2000/01/rdf-schema#label> "subject" .
                        <http://example.org/predicate> <http://www.w3.org/2000/01/rdf-schema#label> "predicate" .
                        <http://example.org/object> <http://www.w3.org/2000/01/rdf-schema#label> "object" ."""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_delete_subsumption_with_ids():
    """Test delete subsumption with IDs."""
    input_graph = "<http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/superclass> ."
    kgcl_patch = "delete edge <http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/superclass>"
    expected_graph = ""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_delete_subsumption_with_curies():
    """Test delete subsumption with CURIEs."""
    input_graph = "<http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/superclass> ."
    kgcl_patch = "delete edge ex:subclass rdfs:subClassOf ex:superclass"
    expected_graph = ""

    run_test(input_graph, kgcl_patch, expected_graph)
