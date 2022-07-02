"""Test creat edge."""
from tests.util import run_test


def test_create_edge_with_ids():
    """Test create edge with IDs."""
    input_graph = ""
    kgcl_patch = "create edge <http://example.org/subject> <http://example.org/predicate> <http://example.org/object>"
    expected_graph = """_:Nfb1ff91c88fe4e328efb4ceea0a11730 <http://www.w3.org/2002/07/owl#onProperty> <http://example.org/predicate> .
                        _:Nfb1ff91c88fe4e328efb4ceea0a11730 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Restriction> .
                        <http://example.org/subject> <http://www.w3.org/2000/01/rdf-schema#subClassOf> _:Nfb1ff91c88fe4e328efb4ceea0a11730 .
                        _:Nfb1ff91c88fe4e328efb4ceea0a11730 <http://www.w3.org/2002/07/owl#someValuesFrom> <http://example.org/object> ."""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_create_edge_with_curies():
    """Test create edge with CURIEs."""
    input_graph = ""
    kgcl_patch = "create edge ex:subject ex:predicate ex:object"
    expected_graph = """_:Nfb1ff91c88fe4e328efb4ceea0a11730 <http://www.w3.org/2002/07/owl#onProperty> <http://example.org/predicate> .
                        _:Nfb1ff91c88fe4e328efb4ceea0a11730 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Restriction> .
                        <http://example.org/subject> <http://www.w3.org/2000/01/rdf-schema#subClassOf> _:Nfb1ff91c88fe4e328efb4ceea0a11730 .
                        _:Nfb1ff91c88fe4e328efb4ceea0a11730 <http://www.w3.org/2002/07/owl#someValuesFrom> <http://example.org/object> ."""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_create_edge_with_labels():
    """Test create edge with labels."""
    input_graph = """<http://example.org/subject> <http://www.w3.org/2000/01/rdf-schema#label> "subject" .
                     <http://example.org/predicate> <http://www.w3.org/2000/01/rdf-schema#label> "predicate" .
                     <http://example.org/object> <http://www.w3.org/2000/01/rdf-schema#label> "object" ."""
    kgcl_patch = "create edge 'subject' 'predicate' 'object'"
    expected_graph = """_:Nfb1ff91c88fe4e328efb4ceea0a11730 <http://www.w3.org/2002/07/owl#onProperty> <http://example.org/predicate> .
                        _:Nfb1ff91c88fe4e328efb4ceea0a11730 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Restriction> .
                        <http://example.org/subject> <http://www.w3.org/2000/01/rdf-schema#subClassOf> _:Nfb1ff91c88fe4e328efb4ceea0a11730 .
                        _:Nfb1ff91c88fe4e328efb4ceea0a11730 <http://www.w3.org/2002/07/owl#someValuesFrom> <http://example.org/object> .
                        <http://example.org/subject> <http://www.w3.org/2000/01/rdf-schema#label> "subject" .
                        <http://example.org/predicate> <http://www.w3.org/2000/01/rdf-schema#label> "predicate" .
                        <http://example.org/object> <http://www.w3.org/2000/01/rdf-schema#label> "object" ."""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_create_subsumption_with_ids():
    """Test create subsumption with IDs."""
    input_graph = ""
    kgcl_patch = "create edge <http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/superclass>"
    expected_graph = "<http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/superclass> ."

    run_test(input_graph, kgcl_patch, expected_graph)


def test_create_subsumption_with_curies():
    """Test create subsumptions with CURIEs."""
    input_graph = ""
    kgcl_patch = "create edge ex:subclass rdfs:subClassOf ex:superclass"
    expected_graph = "<http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/superclass> ."

    run_test(input_graph, kgcl_patch, expected_graph)


def test_create_subsumption_with_labels():
    """Test create subsumptions with labels."""
    input_graph = """<http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#label> "subclass" .
                     <http://example.org/superclass> <http://www.w3.org/2000/01/rdf-schema#label> "superclass" ."""
    kgcl_patch = "create edge 'subclass' rdfs:subClassOf 'superclass'"
    expected_graph = """<http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/superclass> .
                        <http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#label> "subclass" .
                        <http://example.org/superclass> <http://www.w3.org/2000/01/rdf-schema#label> "superclass" ."""

    run_test(input_graph, kgcl_patch, expected_graph)
