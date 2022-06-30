"""Test Unobsolete."""
from util import run_test


def test_unobsolete_with_id():
    """Test unobsolete with ID."""
    input_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2002/07/owl#deprecated> "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
                    <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
                    <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "obsolete Bacteria" ."""
    kgcl_patch = "unobsolete <http://purl.obolibrary.org/obo/NCBITaxon_2>"
    expected_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .
                        <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> ."""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_unobsolete_with_curies():
    """Test unobsolete with CURIEs."""
    input_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2002/07/owl#deprecated> "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
                    <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
                    <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "obsolete Bacteria" ."""
    kgcl_patch = "unobsolete obo:NCBITaxon_2"
    expected_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .
                        <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> ."""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_unobsolete_with_label():
    """Test unobsolete with label."""
    input_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2002/07/owl#deprecated> "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
                    <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
                    <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "obsolete Bacteria" ."""
    kgcl_patch = "unobsolete 'obsolete Bacteria'"
    expected_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .
                        <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> ."""

    run_test(input_graph, kgcl_patch, expected_graph)
