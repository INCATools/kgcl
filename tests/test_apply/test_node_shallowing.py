"""Test node shallowing."""
from tests.util import run_test


def test_node_shallowing_with_ids():
    """Test for node shallowing with ids."""
    input_graph = """<http://example.org/targetClass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/subclass> .
                     <http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/superclass> ."""
    kgcl_patch = "shallow <http://example.org/targetClass> from <http://example.org/subclass> to <http://example.org/superclass>"
    expected_graph = """<http://example.org/targetClass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/superclass> .
                        <http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/superclass> ."""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_node_shallowing_with_curies():
    """Test for node shallowing with CURIEs."""
    input_graph = """<http://example.org/targetClass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/subclass> .
                     <http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/superclass> ."""
    kgcl_patch = "shallow ex:targetClass from ex:subclass to ex:superclass"
    expected_graph = """<http://example.org/targetClass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/superclass> .
                        <http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/superclass> ."""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_node_shallowing_with_labels():
    """Test for node shallowing with labels."""
    input_graph = """<http://example.org/targetClass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/subclass> .
                     <http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/superclass> .
                     <http://example.org/targetClass> <http://www.w3.org/2000/01/rdf-schema#label> "targetClass" .
                     <http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#label> "subclass" .
                     <http://example.org/superclass> <http://www.w3.org/2000/01/rdf-schema#label> "superclass" .
                     """
    kgcl_patch = "shallow 'targetClass' from 'subclass' to 'superclass'"
    expected_graph = """<http://example.org/targetClass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/superclass> .
                        <http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://example.org/superclass> .
                        <http://example.org/targetClass> <http://www.w3.org/2000/01/rdf-schema#label> "targetClass" .
                        <http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#label> "subclass" .
                        <http://example.org/superclass> <http://www.w3.org/2000/01/rdf-schema#label> "superclass" ."""

    run_test(input_graph, kgcl_patch, expected_graph)
