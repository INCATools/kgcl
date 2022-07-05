"""Existential restriction change information."""

import rdflib

from kgcl.diff.graph_diff import (get_added_existentials,
                                  get_deleted_existentials)
from kgcl.diff.render_operations import render
from kgcl.datamodel.kgcl import EdgeCreation, EdgeDeletion


def id_generator():
    """Return generated id."""
    id = 0
    while True:
        yield id
        id += 1


id_gen = id_generator()


class ExistentialChangeSummary:
    """Dataclass holding information about (atomic) existential restriction changes."""

    def __init__(self):

        self.existential_additions = []
        self.existential_deletions = []
        self.covered_triples_triple_existential_additions = []
        self.covered_triples_triple_existential_deletions = []

    def get_commands(self):
        """Get commands.

        :return: None
        """
        kgcl_commands = []
        for k in self.existential_additions:
            kgcl_commands.append(k)
        for k in self.existential_deletions:
            kgcl_commands.append(k)
        return kgcl_commands

    def get_existential_additions(self):
        """Get existential additions..

        :return: None
        """
        return self.existential_additions

    def get_existential_deletions(self):
        """Get existential deletions.

        :return: None
        """
        return self.existential_deletions

    def get_summary_kgcl_commands(self) -> str:
        """Get summary commands.

        :return: None
        """
        out = (
            "EdgeCreation (existential): " + str(len(self.existential_additions)) + "\n"
            "EdgeDeletion (existential): " + str(len(self.existential_deletions)) + "\n"
        )
        return out

    def get_summary_rdf_triples(self) -> str:
        """Get summary RDF triples.

        :return: None
        """
        out = (
            "EdgeCreation (existential)"
            + str(len(self.covered_triples_triple_existential_additions))
            + "\n"
            "EdgeDeletion (existential)"
            + str(len(self.covered_triples_triple_existential_deletions))
            + "\n"
        )
        return out

    # RDF data

    def get_covered_triples_existential_additions(self):
        """Get covered triples existential additions.

        :return: None
        """
        return self.covered_triples_triple_existential_additions

    def get_covered_triples_existential_deletions(self):
        """Get covered triples existential deletions.

        :return: None
        """
        return self.covered_triples_triple_existential_deletions

    def add_covered_triples_existential_additions(self, triples):
        """
        Add covered triples existential additions.

        :param triples: Graph triples provided to add.
        :type triples: Graph
        """
        for t in triples:
            self.covered_triples_triple_existential_additions.append(t)

    def add_covered_triples_existential_deletions(self, triples):
        """Add covered triples existential deletions.

        :param triples: Graph triples provided to delete.
        :type triples: Graph
        """
        for t in triples:
            self.covered_triples_triple_existential_deletions.append(t)

    # KGCL data

    def add_existential_addition(self, i):
        """Add existential additions.

        :param i: Information to be added.
        :type i: str
        """
        self.existential_additions.append(i)

    def add_existential_deletion(self, i):
        """Add existential deletions.

        :param i: Information to be deleted.
        :type i: str
        """
        self.existential_deletions.append(i)


def generate_atomic_existential_commands(g1, g2):
    """
    Given two graphs g1 and g2.

    return all edge creations and edge deletions.
    """
    summary = ExistentialChangeSummary()

    added = get_added_existentials(g1, g2)
    deleted = get_deleted_existentials(g1, g2)

    existential_additions, covered = generate_existential_additions(added)
    summary.add_covered_triples_existential_additions(covered)

    existential_deletions, covered = generate_existential_deletions(deleted)
    summary.add_covered_triples_existential_deletions(covered)

    for a in existential_additions:
        summary.add_existential_addition(render(a))
    for d in existential_deletions:
        summary.add_existential_deletion(render(d))

    return summary


def generate_existential_deletions(deleted):
    """Return EdgeDeletion instances for given (deleted) triples."""
    covered = rdflib.Graph()
    kgcl = []

    for a in deleted:
        subclass = str(a.subclass)
        property = str(a.property)
        filler = str(a.filler)

        id = "test_id_" + str(next(id_gen))

        node = EdgeDeletion(
            id=id,
            subject=subclass,
            predicate=property,
            object=filler,
            subject_type="uri",
            predicate_type="uri",
            object_type="uri",
        )

        kgcl.append(node)
        for t in a.triples:
            covered.add(t)

    return kgcl, covered


def generate_existential_additions(added):
    """Return EdgeCreation instances for given (added) triples."""
    covered = rdflib.Graph()
    kgcl = []

    for a in added:
        subclass = str(a.subclass)
        property = str(a.property)
        filler = str(a.filler)

        id = "test_id_" + str(next(id_gen))

        node = EdgeCreation(
            id=id,
            subject=subclass,
            predicate=property,
            object=filler,
            subject_type="uri",
            predicate_type="uri",
            object_type="uri",
        )

        kgcl.append(node)
        for t in a.triples:
            covered.add(t)

    return kgcl, covered
