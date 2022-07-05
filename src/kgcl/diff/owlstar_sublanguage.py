"""Owlstar related stuff."""
import time

import rdflib
from rdflib import BNode
from rdflib.namespace import OWL, RDF, RDFS


class TripleAnnotation:
    """Annotate triples."""

    # TODO: store blank node associated with the annotation
    def __init__(self, s, p, t, ap, a):
        self.source = s
        self.property = p
        self.target = t
        self.annotation_property = ap
        self.annotation = a
        self.triples = set()

    # TODO check that all triples have the same blank node
    def add_triple(self, t):
        """
        Add triple.

        :param t: Triple to be added.
        :type t: Any
        """
        self.triples.add(t)

    def add_triples(self, ts):
        """
        Add mutiple triples.

        :param ts: Triples to be added.
        :type ts: Any
        """
        self.triples.update(ts)

    def __repr__(self):
        return (
            "<<"
            + str(self.source)
            + " "
            + str(self.property)
            + " "
            + str(self.target)
            + ">> "
            + str(self.annotation_property)
            + " "
            + str(self.annotation)
        )

    def __eq__(self, other):
        if isinstance(other, TripleAnnotation):
            return (
                self.source == other.source
                and self.property == other.property
                and self.target == other.target
                and self.annotation_property == other.annotation_property
                and self.annotation == other.annotation
            )
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __key(self):
        return (
            self.source,
            self.property,
            self.target,
            self.annotation_property,
            self.annotation,
        )

    def __hash__(self):
        return hash(self.__key())


class ExistentialRestriction:
    """Existential restiction."""

    # TODO: store blank node associated with the existential restriction
    def __init__(self, sub, prop, fil):
        self.subclass = sub
        self.property = prop
        self.filler = fil
        self.triples = set()

    def add_triple(self, t):
        """
        Add triple.

        :param t: Triple to be added.
        :type t: Any
        """
        self.triples.add(t)

    def add_triples(self, ts):
        """
        Add multiple triples.

        :param ts: Triple to be added.
        :type ts: Any
        """
        self.triples.update(ts)

    def __repr__(self):
        return (
            self.subclass
            + " "
            + "SubClassOf"
            + " "
            + self.property
            + " "
            + "some"
            + " "
            + self.filler
        )

    def __eq__(self, other):
        if isinstance(other, ExistentialRestriction):
            return (
                self.subclass == other.subclass
                and self.property == other.property
                and self.filler == other.filler
            )
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __key(self):
        return (
            self.subclass,
            self.property,
            self.filler,
        )

    def __hash__(self):
        return hash(self.__key())


def get_thin_triples(g):
    """Get thin triples."""
    res = rdflib.Graph()
    for s, p, o in g.triples((None, None, None)):
        if (
            not isinstance(s, BNode)
            and not isinstance(o, BNode)
            # and p != RDFS.subClassOf
        ):
            res.add((s, p, o))

    return res


def get_atomic_subsumptions(g):
    """Get atomic subsumptions."""
    res = rdflib.Graph()
    for s, p, o in g.triples((None, RDFS.subClassOf, None)):
        if not isinstance(s, BNode) and not isinstance(o, BNode):
            res.add((s, p, o))

    return res


def get_atomic_existentials(g):
    """Get atomic existentials."""
    some_values_from = set(g.subjects(predicate=OWL.someValuesFrom))
    on_property = set(g.subjects(predicate=OWL.onProperty))

    intersection = some_values_from & on_property

    existential_2_classes = {}  # map from blank node to (named) subclasses
    for i in intersection:
        existential_2_classes[i] = []
        if isinstance(i, BNode):  # this check should be unnecessary
            for s, _, _ in g.triples((None, RDFS.subClassOf, i)):
                if not isinstance(s, BNode):
                    existential_2_classes[i].append(str(s))

    owlstar_axiom = []
    bnodes_2_existentials = get_bnodes_2_atomic_existentials(g)
    for i, subclasses in existential_2_classes.items():
        # bnode = str(i)  # don't really need the bnode
        filler = ""
        bnode_filler = True
        property = ""
        bnode_property = True

        # get property
        for _, _, o in g.triples((i, OWL.onProperty, None)):
            if not isinstance(o, BNode):  # this test is unnecessary
                property = str(o)
                bnode_property = False

        # get filler
        for _, _, o in g.triples((i, OWL.someValuesFrom, None)):
            if not isinstance(o, BNode):
                filler = str(o)
                bnode_filler = False

        if not bnode_property and not bnode_filler:
            for subclass in subclasses:
                ex = ExistentialRestriction(subclass, property, filler)
                ex.add_triples(bnodes_2_existentials[i])
                owlstar_axiom.append(ex)
                # owlstar_axiom.append((subclass, property, filler))

    return owlstar_axiom


def get_bnodes_2_atomic_existentials(g):
    """Get blank nodes to atomic existentials."""
    some_values_from = set(g.subjects(predicate=OWL.someValuesFrom))
    on_property = set(g.subjects(predicate=OWL.onProperty))
    # restriction = set(g.subjects(predicate=rdf.type)) # Restriction

    intersection = some_values_from & on_property

    existential_2_classes = {}  # map from blank node to (named) subclass
    for i in intersection:
        existential_2_classes[i] = []
        if isinstance(i, BNode):  # this check should be unnecessary
            for s, _, _ in g.triples((None, RDFS.subClassOf, i)):
                if not isinstance(s, BNode):
                    existential_2_classes[i].append(s)

    bnode_triples = {}
    for i, subclasses in existential_2_classes.items():
        bnode_triples[i] = []

        filler = i
        bnode_filler = True
        property = i
        bnode_property = True

        # get property
        for _, _, o in g.triples((i, OWL.onProperty, None)):
            if not isinstance(o, BNode):
                property = o
                bnode_property = False

        # get filler
        for _, _, o in g.triples((i, OWL.someValuesFrom, None)):
            if not isinstance(o, BNode):
                filler = o
                bnode_filler = False

        if not bnode_property and not bnode_filler:
            for subclass in subclasses:
                bnode_triples[i].append((i, OWL.someValuesFrom, filler))
                bnode_triples[i].append((i, OWL.onProperty, property))
                bnode_triples[i].append((subclass, RDFS.subClassOf, i))

    return bnode_triples


def get_triple_annotations(g):
    """Get triple annotations."""
    source = set(g.subjects(predicate=OWL.annotatedSource))
    property = set(g.subjects(predicate=OWL.annotatedProperty))
    target = set(g.subjects(predicate=OWL.annotatedTarget))

    intersection = source & property & target

    exclude = {
        OWL.annotatedSource,
        OWL.annotatedProperty,
        OWL.annotatedTarget,
        RDF.type,
    }

    bnodes_2_triple_annotations = get_bnodes_2_triple_annotations(g)
    annotations = []
    for i in intersection:
        if isinstance(i, BNode):  # this check should be unnecessary
            # NB these generators are singletons
            source = next(g.objects(subject=i, predicate=OWL.annotatedSource))
            property = next(g.objects(subject=i, predicate=OWL.annotatedProperty))
            target = next(g.objects(subject=i, predicate=OWL.annotatedTarget))
            for s, p, o in g.triples((i, None, None)):
                if (
                    p not in exclude
                    and not isinstance(o, BNode)
                    and not isinstance(p, BNode)
                    and not isinstance(source, BNode)
                    and not isinstance(property, BNode)
                    and not isinstance(target, BNode)
                ):
                    ta = TripleAnnotation(source, property, target, p, o)
                    ta.add_triples(bnodes_2_triple_annotations[s])
                    annotations.append(ta)

                    # annotations.append((source, property, target, p, o))
                    # (str(source), str(property), str(target), str(p), str(o))

    return annotations


def get_bnodes_2_triple_annotations(g):
    """Get blank nodes to triple annotations."""
    source = set(g.subjects(predicate=OWL.annotatedSource))
    property = set(g.subjects(predicate=OWL.annotatedProperty))
    target = set(g.subjects(predicate=OWL.annotatedTarget))

    # get blank nodes that have all three required predicates
    intersection = source & property & target

    exclude = {
        OWL.annotatedSource,
        OWL.annotatedProperty,
        OWL.annotatedTarget,
        # RDF.type,
    }

    annotations = {}
    for i in intersection:
        annotations[i] = []
        if isinstance(i, BNode):  # this check should be unnecessary
            # NB these generators are singletons
            source = next(g.objects(subject=i, predicate=OWL.annotatedSource))
            property = next(g.objects(subject=i, predicate=OWL.annotatedProperty))
            target = next(g.objects(subject=i, predicate=OWL.annotatedTarget))

            annotations[i].append((i, OWL.annotatedSource, source))
            annotations[i].append((i, OWL.annotatedProperty, property))
            annotations[i].append((i, OWL.annotatedTarget, target))

            for s, p, o in g.triples((i, None, None)):
                if (
                    p not in exclude
                    and not isinstance(o, BNode)
                    and not isinstance(p, BNode)
                    and not isinstance(source, BNode)
                    and not isinstance(property, BNode)
                    and not isinstance(target, BNode)
                ):
                    annotations[i].append((s, p, o))

    return annotations


def render_triple_annotation(a):
    """Render triple annotations."""
    return (
        "<<"
        # + a[0].n3()
        + a[0]
        + " "
        # + a[1].n3()
        + a[1]
        + " "
        # + a[2].n3()
        + a[2]
        + ">> "
        # + a[3].n3()
        + a[3]
        + " "
        # + a[4].n3()
        + a[4]
    )


def render_atomic_existential(a):
    """Render atomic annotations."""
    return (
        "<<"
        + a[0]
        + " "
        + a[1]
        + " "
        + a[2]
        + ">> "
        + "os:interpretation"
        + " "
        + "os:AllSomeInterpretation"
    )


if __name__ == "__main__":
    g = rdflib.Graph()

    start = time.time()
    g.load("n3/obi/obi_1.nt", format="nt")
    # g.load("n3/uberon/uberon_1.nt", format="nt")
    end = time.time()
    print(end - start)

    start = time.time()
    thin = get_thin_triples(g)
    end = time.time()
    print(end - start)

    start = time.time()
    axioms = get_atomic_existentials(g)
    end = time.time()
    print(end - start)

    print(len(axioms))

    annotations = get_triple_annotations(g)
    print(len(annotations))
    # for a in annotations:
    #    print(str(a[0]) + " " + str(a[1]))
    # for a in axioms:
    # print(a)
