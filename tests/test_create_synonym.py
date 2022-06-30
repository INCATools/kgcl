"""Test create synonym."""
from .util import run_test


def test_create_synonym_with_ids():
    """Test create synonym with IDs."""
    input_graph = '<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .'
    kgcl_patch = (
        "create synonym 'Virus' for <http://purl.obolibrary.org/obo/NCBITaxon_2>"
    )
    expected_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .
                        <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.geneontology.org/formats/oboInOwl#hasSynonym> "Virus" ."""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_create_synonym_with_language_tag():
    """Test create synonym with language tag."""
    input_graph = '<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .'
    kgcl_patch = (
        "create synonym 'Virus'@en for <http://purl.obolibrary.org/obo/NCBITaxon_2>"
    )
    expected_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .
                        <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.geneontology.org/formats/oboInOwl#hasSynonym> "Virus"@en ."""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_create_broad_synonym_with_ids():
    """Test create broad synonym with IDs."""
    input_graph = '<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .'
    kgcl_patch = (
        "create broad synonym 'Virus' for <http://purl.obolibrary.org/obo/NCBITaxon_2>"
    )
    expected_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .
                    <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.geneontology.org/formats/oboInOwl#hasBroadSynonym> "Virus" ."""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_create_broad_synonym_with_curies():
    """Test create broad synonym with CURIEs."""
    input_graph = '<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .'
    kgcl_patch = "create broad synonym 'Virus' for obo:NCBITaxon_2"
    expected_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .
                        <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.geneontology.org/formats/oboInOwl#hasBroadSynonym> "Virus" ."""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_create_broad_synonym_with_labels():
    """Test create broad synonym with label."""
    input_graph = '<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .'
    kgcl_patch = "create broad synonym 'Virus' for 'Bacteria'"
    expected_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .
                        <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.geneontology.org/formats/oboInOwl#hasBroadSynonym> "Virus" ."""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_create_exact_synonym_with_ids():
    """Test create exact synonym with IDs."""
    input_graph = '<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .'
    kgcl_patch = (
        "create exact synonym 'Virus' for <http://purl.obolibrary.org/obo/NCBITaxon_2>"
    )
    expected_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .
                        <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.geneontology.org/formats/oboInOwl#hasExactSynonym> "Virus" ."""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_create_narrow_synonym_with_ids():
    """Test create narrow synonym with IDs."""
    input_graph = '<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .'
    kgcl_patch = (
        "create narrow synonym 'Virus' for <http://purl.obolibrary.org/obo/NCBITaxon_2>"
    )
    expected_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .
                        <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.geneontology.org/formats/oboInOwl#hasNarrowSynonym> "Virus" ."""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_create_related_synonym_with_ids():
    """Test create related synonym with IDs."""
    input_graph = '<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .'
    kgcl_patch = "create related synonym 'Virus' for <http://purl.obolibrary.org/obo/NCBITaxon_2>"
    expected_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .
                        <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym> "Virus" ."""

    run_test(input_graph, kgcl_patch, expected_graph)


def test_create_related_synonym_with_language_tags_and_labels():
    """Test create related synonym with language tags and labels."""
    input_graph = '<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .'
    kgcl_patch = "create related synonym 'Virus'@en for 'Bacteria'"
    expected_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .
                        <http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym> "Virus"@en ."""

    run_test(input_graph, kgcl_patch, expected_graph)
