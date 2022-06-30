"""Test change predicate."""
from util import run_test


def test_change_predicate_with_ids():
    """Test change predicate with IDs."""
    input_graph = "<http://example.org/subclass> <http://example.org/partOf> <http://example.org/superclass> ."
    kgcl_patch = "change relationship between <http://example.org/subclass> and <http://example.org/superclass> from <http://example.org/partOf> to <http://example.org/hasPart>"
    expected_graph = "<http://example.org/subclass> <http://example.org/hasPart> <http://example.org/superclass> ."

    run_test(input_graph, kgcl_patch, expected_graph)


def test_change_predicate_with_curies():
    """Test change predicate with CURIEs."""
    input_graph = "<http://example.org/subclass> <http://example.org/partOf> <http://example.org/superclass> ."
    kgcl_patch = "change relationship between ex:subclass and ex:superclass from ex:partOf to ex:hasPart"
    expected_graph = "<http://example.org/subclass> <http://example.org/hasPart> <http://example.org/superclass> ."

    run_test(input_graph, kgcl_patch, expected_graph)


def test_change_predicate_with_labels():
    """Test change predicate with labels."""
    input_graph = """<http://example.org/subclass> <http://example.org/partOf> <http://example.org/superclass> .
                     <http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#label> "subclass" .
                     <http://example.org/superclass> <http://www.w3.org/2000/01/rdf-schema#label> "superclass" .
                     <http://example.org/hasPart> <http://www.w3.org/2000/01/rdf-schema#label> "hasPart" ."""
    kgcl_patch = "change relationship between ex:subclass and ex:superclass from ex:partOf to ex:hasPart"
    expected_graph = """<http://example.org/subclass> <http://example.org/hasPart> <http://example.org/superclass> .
                        <http://example.org/subclass> <http://www.w3.org/2000/01/rdf-schema#label> "subclass" .
                        <http://example.org/superclass> <http://www.w3.org/2000/01/rdf-schema#label> "superclass" .
                        <http://example.org/hasPart> <http://www.w3.org/2000/01/rdf-schema#label> "hasPart" ."""

    run_test(input_graph, kgcl_patch, expected_graph)
