"""Determine graph difference."""
import rdflib
from rdflib import Graph

from .owlstar_sublanguage import (get_atomic_existentials,
                                  get_atomic_subsumptions, get_thin_triples,
                                  get_triple_annotations)


def get_added_thin_triples(g1: Graph, g2: Graph) -> Graph:
    """
    Retuns triples present in g2 but not g1.

    Given two graphs g1 and g2,
    returns triples (without blank nodes) that are in g2 but not g1,
    i.e. 'added' triples.
    """
    thin1 = get_thin_triples(g1)
    thin2 = get_thin_triples(g2)

    return thin2 - thin1


def get_deleted_thin_triples(g1, g2):
    """
    Get triples in graph1 that aren't in Graph2.

    Given two graphs g1 and g2,
    returns triples (without blank nodes) that are in g1 but not g2,
    i.e. 'deleted' triples.
    """
    thin1 = get_thin_triples(g1)
    thin2 = get_thin_triples(g2)

    return thin1 - thin2


def get_added_subsumptions(g1, g2):
    """
    Return atomic subsumption axioms in Graph2 not in Graph1.

    Given two graphs g1 and g2,
    returns atomic subsumption axioms that are in g2 but not g1,
    i.e. 'added' subsumptions.
    """
    sub1 = get_atomic_subsumptions(g1)
    sub2 = get_atomic_subsumptions(g2)

    return sub2 - sub1


def get_deleted_subsumptions(g1, g2):
    """
    Return atomic subsumption axioms in Graph1 but not Graph2.

    Given two graphs g1 and g2,
    returns atomic subsumption axioms that are in g1 but not g2,
    i.e. 'deleted' subsumptions.
    """
    sub1 = get_atomic_subsumptions(g1)
    sub2 = get_atomic_subsumptions(g2)

    return sub1 - sub2


# NB: this returns a set of 'ExistentialRestrictions' (defined in owlstar_sublanguage)
def get_added_existentials(g1, g2):
    """
    Return ExistentialRestrictions in Graph2 but not in Graph1.

    Given two graphs g1 and g2,
    returns ExistentialRestrictions that are in g2 but not g1,
    i.e. 'added' ExistentialRestrictions.
    """
    ex1 = set(get_atomic_existentials(g1))
    ex2 = set(get_atomic_existentials(g2))

    return ex2 - ex1


def get_deleted_existentials(g1, g2):
    """
    Return ExistentialRestrictions from Graph1 not in Graph2.

    Given two graphs g1 and g2,
    returns ExistentialRestrictions that are in g1 but not g2,
    i.e. 'deleted' ExistentialRestrictions.
    """
    ex1 = set(get_atomic_existentials(g1))
    ex2 = set(get_atomic_existentials(g2))

    return ex1 - ex2


# NB this returns a set of 'TripleAnnotation's (defined in owlstar_sublanguage)
def get_added_triple_annotations(g1, g2):
    """
    Return ExistentialRestrictions in Graph1 not in Graph2.

    Given two graphs g1 and g2,
    returns ExistentialRestrictions that are in g2 but not g1,
    i.e. 'added' ExistentialRestrictions.
    """
    annotations1 = set(get_triple_annotations(g1))
    annotations2 = set(get_triple_annotations(g2))

    return annotations2 - annotations1


def get_deleted_triple_annotations(g1, g2):
    """
    Get TripleAnnotations from the two graphs provided.

    Given two graphs g1 and g2,
    returns TripleAnnotations that are in g1 but not g2,
    i.e. 'deleted' ExistentialRestrictions.
    """
    annotations1 = set(get_triple_annotations(g1))
    annotations2 = set(get_triple_annotations(g2))

    return annotations1 - annotations2


if __name__ == "__main__":
    g1 = rdflib.Graph()
    g2 = rdflib.Graph()

    g1.load("n3/obi/obi_1.nt", format="nt")
    g2.load("n3/obi/obi_2.nt", format="nt")

    # deleted = get_deleted_triples(g1, g2)
