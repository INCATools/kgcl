"""Test rename."""
import pytest

from tests.util import run_test


def test_rename():
    """Test rename."""
    input_graph = '<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .'
    kgcl_patch = "rename 'Bacteria' to 'Virus'"
    expected_graph = '<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Virus" .'

    run_test(input_graph, kgcl_patch, expected_graph)


@pytest.mark.skip(reason="https://github.com/INCATools/kgcl-tools/issues/36")
def test_rename_with_string():
    """Test rename."""
    input_graph = '<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria"^^xsd:string .'
    kgcl_patch = "rename 'Bacteria' to 'Virus'"
    expected_graph = '<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Virus" .'

    run_test(input_graph, kgcl_patch, expected_graph)


def test_test_rename_with_language_tag():
    """Test rename with language tag."""
    input_graph = '<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria"@en .'
    kgcl_patch = "rename 'Bacteria'@en to 'Virus'@fr"
    expected_graph = '<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Virus"@fr .'

    run_test(input_graph, kgcl_patch, expected_graph)


def test_rename_with_id():
    """Test rename with IDs."""
    input_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" .
                    <http://purl.obolibrary.org/obo/NCBITaxon_8> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" ."""
    kgcl_patch = (
        "rename <http://purl.obolibrary.org/obo/NCBITaxon_2> from 'Bacteria' to 'Virus'"
    )
    expected_graph = """<http://purl.obolibrary.org/obo/NCBITaxon_2> <http://www.w3.org/2000/01/rdf-schema#label> "Virus" .
                        <http://purl.obolibrary.org/obo/NCBITaxon_8> <http://www.w3.org/2000/01/rdf-schema#label> "Bacteria" ."""

    run_test(input_graph, kgcl_patch, expected_graph)
