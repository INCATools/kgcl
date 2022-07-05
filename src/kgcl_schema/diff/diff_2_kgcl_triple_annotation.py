"""Triple annotation change summary."""
import rdflib
from rdflib import Graph, Literal, URIRef

from kgcl_schema.diff.graph_diff import (get_added_triple_annotations,
                                         get_deleted_triple_annotations)
from kgcl_schema.diff.render_operations import render
from kgcl_schema.datamodel.kgcl import EdgeCreation, EdgeDeletion
from kgcl_schema.datamodel.ontology_model import Annotation


def id_generator():
    """Return newly generated id."""
    id = 0
    while True:
        yield id
        id += 1


id_gen = id_generator()


class TripleAnnotationChangeSummary:
    """Dataclass holding information about triple annotation axioms."""

    def __init__(self):

        self.triple_annotations_additions = []
        self.triple_annotations_deletions = []
        self.covered_triples_triple_annotations_additions = []
        self.covered_triples_triple_annotations_deletions = []

    def get_commands(self):
        """Get commands."""
        kgcl_commands = []
        for k in self.triple_annotations_additions:
            kgcl_commands.append(k)
        for k in self.triple_annotations_deletions:
            kgcl_commands.append(k)
        return kgcl_commands

    def get_triple_annotation_additions(self):
        """Get triple annotation additions."""
        return self.triple_annotations_additions

    def get_triple_annotation_deletions(self):
        """Get triple annotation deletions."""
        return self.triple_annotations_deletions

    def get_summary_kgcl_commands(self):
        """Get summary commands."""
        out = (
            # "Triple Annotation Additions: "
            "EdgeCreations (with annotation): "
            + str(len(self.triple_annotations_additions))
            + "\n"
            # "Triple Annotation Deletions: "
            + "EdgeDeletion (with annotation): "
            + str(len(self.triple_annotations_deletions))
            + "\n"
        )
        return out

    def get_summary_rdf_triples(self):
        """Get summary RDF tripless."""
        out = (
            # "Triple Annotation Additions: "
            "EdgeCreations (with annotation): "
            + str(len(self.covered_triples_triple_annotations_additions))
            + "\n"
            # + "Triple Annotation Deletions: "
            + "EdgeDeletion (with annotation): "
            + str(len(self.covered_triples_triple_annotations_deletions))
            + "\n"
        )
        return out

    # RDF data

    def get_covered_triples_annotation_additions(self):
        """Get covered triples annotation additions."""
        return self.covered_triples_triple_annotations_additions

    def get_covered_triples_annotation_deletions(self):
        """Get covered triples annotation deletions."""
        return self.covered_triples_triple_annotations_deletions

    def add_covered_triples_annotation_additions(self, triples):
        """Add covered triples annotation additions."""
        for t in triples:
            self.covered_triples_triple_annotations_additions.append(t)

    def add_covered_triples_annotation_deletions(self, triples):
        """Add covered triples annotation deletions."""
        for t in triples:
            self.covered_triples_triple_annotations_deletions.append(t)

    # KGCL data

    def add_triple_annotation_addition(self, i):
        """Add triple annotation addition."""
        self.triple_annotations_additions.append(i)

    def add_triple_annotation_deletion(self, i):
        """Add triple annotation deletion."""
        self.triple_annotations_deletions.append(i)


def generate_triple_annotation_commands(
    g1: Graph, g2: Graph
) -> TripleAnnotationChangeSummary:
    """
    Get differences.

    Given two graphs g1 and g2,
    return all (annotated) EdgeCreation and
    (annotated) EdgeDeletions to account for their diff.
    """
    summary = TripleAnnotationChangeSummary()

    added = get_added_triple_annotations(g1, g2)
    deleted = get_deleted_triple_annotations(g1, g2)

    additions, covered = generate_triple_annotation_additions(added)
    summary.add_covered_triples_annotation_additions(covered)

    deletions, covered = generate_triple_annotation_deletions(deleted)
    summary.add_covered_triples_annotation_deletions(covered)

    for a in additions:
        summary.add_triple_annotation_addition(render(a))
    for d in deletions:
        summary.add_triple_annotation_deletion(render(d))

    return summary


def generate_triple_annotation_additions(added):
    """Return EdgeCreation instances for given (added) triples."""
    covered = rdflib.Graph()
    kgcl = []

    for a in added:
        source = str(a.source)
        property = str(a.property)
        target = str(a.target)
        target_type = get_type(a.target)
        annotation_property = str(a.annotation_property)
        annotation = str(a.annotation)
        annotation_type = get_type(a.annotation)

        id = "test_id_" + str(next(id_gen))

        language = get_language_tag(a.target)
        datatype = get_datatype(a.target)
        if datatype is not None:
            datatype = "<" + datatype + ">"  # expect data types without curies

        annotation = Annotation(
            property=annotation_property, filler=annotation, filler_type=annotation_type
        )

        node = EdgeCreation(
            id=id,
            subject=source,
            predicate=property,
            object=target,
            object_type=target_type,
            annotation_set=annotation,
            language=language,
            datatype=datatype,
        )

        kgcl.append(node)
        for t in a.triples:
            covered.add(t)

    return kgcl, covered


def generate_triple_annotation_deletions(deleted):
    """Return EdgeDeletion instances for given (deleted) triples."""
    covered = rdflib.Graph()
    kgcl = []

    for a in deleted:
        source = str(a.source)
        property = str(a.property)
        target = str(a.target)
        target_type = get_type(a.target)
        annotation_property = str(a.annotation_property)
        annotation = str(a.annotation)
        annotation_type = get_type(a.annotation)

        id = "test_id_" + str(next(id_gen))

        language = get_language_tag(a.target)
        datatype = get_datatype(a.target)
        if datatype is not None:
            datatype = "<" + datatype + ">"  # expect data types without curies

        annotation = Annotation(
            property=annotation_property, filler=annotation, filler_type=annotation_type
        )

        node = EdgeDeletion(
            id=id,
            subject=source,
            predicate=property,
            object=target,
            object_type=target_type,
            annotation_set=annotation,
            language=language,
            datatype=datatype,
        )

        kgcl.append(node)
        for t in a.triples:
            covered.add(t)

    return kgcl, covered


# TODO: factor these out in some kind of utility library


def get_type(rdf_entity):
    """Get rdf_type."""
    if isinstance(rdf_entity, URIRef):
        return "uri"
    elif isinstance(rdf_entity, Literal):
        return "literal"
    else:
        return "Error"


def get_language_tag(rdf_entity):
    """Get language tag."""
    if isinstance(rdf_entity, Literal):
        return rdf_entity.language
    else:
        return None


def get_datatype(rdf_entity):
    """Get data type."""
    if isinstance(rdf_entity, Literal) and rdf_entity.datatype is not None:
        return str(rdf_entity.datatype)
    else:
        return None
