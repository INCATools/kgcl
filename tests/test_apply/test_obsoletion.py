"""Tesr obsoeltion."""
from tests.util import run_test

# TODO: extend tests to ensure not over-obsoleting
# TODO: test for proper obsoletion model
def test_obsoletion_with_ids():
    """Test obsoletion with IDs."""
    input_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .
                     <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> ."""
    kgcl_patch = "obsolete <http://purl.obolibrary.org/obo/NCBITaxon_2>"
    expected_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "obsolete Bacteria" .
                       <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2002/07/owl#deprecated> "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
                       <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
                       <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.geneontology.org/formats/oboInOwl#ObsoleteClass> ."""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_obsoletion_with_curies():
    """Test obsoletion with CURIEs."""
    input_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .
                     <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> ."""
    kgcl_patch = "obsolete obo:NCBITaxon_2"
    expected_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "obsolete Bacteria" .
                       <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2002/07/owl#deprecated> "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
                       <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
                       <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.geneontology.org/formats/oboInOwl#ObsoleteClass> ."""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_obsoletion_with_labels():
    """Test obsoletion with labels."""
    input_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .
                     <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> ."""
    kgcl_patch = "obsolete 'Bacteria'"
    expected_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "obsolete Bacteria" .
                       <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2002/07/owl#deprecated> "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
                       <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
                       <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.geneontology.org/formats/oboInOwl#ObsoleteClass> ."""

    run_test(input_graph, kgcl_patch, expected_graph)
