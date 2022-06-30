"""Test for creating edges."""
from .util import run_test


def test_create_edge_with_ids():
    """Test for creating edge with ids."""
    input_graph = ""
    kgcl_patch = "create <http://purl.obolibrary.org/obo/NCBITaxon_2>"
    expected_graph = "<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> ."

    run_test(input_graph, kgcl_patch, expected_graph)


def test_create_edge_with_label():
    """Test for creating edge with labels."""
    input_graph = ""
    kgcl_patch = (
        "create node <http://purl.obolibrary.org/obo/NCBITaxon_2> 'Bacteria'@en"
    )
    expected_graph = '<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria"@en .'

    run_test(input_graph, kgcl_patch, expected_graph)
