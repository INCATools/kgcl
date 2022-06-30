"""Test delete entity."""
from util import run_test


def test_delete_annotated_edge_with_ids():
    """Test delete annotated edge with IDs."""
    input_graph = "<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> ."
    kgcl_patch = "delete <http://purl.obolibrary.org/obo/NCBITaxon_2>"
    expected_graph = ""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_delete_annotated_edge_with_curies():
    """Test delete annotated edge with CURIEs."""
    input_graph = "<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> ."
    kgcl_patch = "delete obo:NCBITaxon_2"
    expected_graph = ""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_delete_annotated_edge_with_label():
    """Test delete annotated edge with label."""
    input_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
                     <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" ."""
    kgcl_patch = "delete 'Bacteria'"
    expected_graph = ""

    run_test(input_graph, kgcl_patch, expected_graph)
