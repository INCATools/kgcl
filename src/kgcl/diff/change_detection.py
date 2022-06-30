"""Detect changes."""
import rdflib
from rdflib import Literal, URIRef
from rdflib.namespace import RDFS

from kgcl.model.kgcl import (NodeAnnotationChange, NodeMove, NodeRename,
                             PredicateChange)
from kgcl.model.ontology_model import Edge


def id_generator():
    """Return a new ID for KGCL change operations."""
    id = 0
    while True:
        yield id
        id += 1


# initialise ID generator
id_gen = id_generator()

# TODO:
# obsoletion
# unobsoletion


def get_type(rdf_entity):
    """Return type of rdf entity."""
    if isinstance(rdf_entity, URIRef):
        return "uri"
    elif isinstance(rdf_entity, Literal):
        return "literal"
    else:
        return "Error"


def detect_renamings(added, deleted):
    """Detect NodeRename instances and associated triples.

    Given a diff represented by 'added' and 'deleted' triples,
    return an encoding in terms of
    (i) NodeRename instances,
    (ii) triples involved in (i), and
    (iii) nondeterministic choices.
    """
    covered = rdflib.Graph()

    # get labeling information
    added_labels = {}
    deleted_labels = {}

    for s, _, o in added.triples((None, RDFS.label, None)):
        if s not in added_labels:
            added_labels[s] = set()
        added_labels[s].add(o)

    for s, _, o in deleted.triples((None, RDFS.label, None)):
        if s not in deleted_labels:
            deleted_labels[s] = set()
        deleted_labels[s].add(o)

    # collect renamings
    non_deterministic = []  # list of non-deterministic choices
    kgcl = []
    for subject in deleted_labels:
        if subject in added_labels:

            moved_from = deleted_labels[subject]
            moved_to = added_labels[subject]

            if len(moved_to) > 1 or len(moved_from) > 1:
                non_deterministic.append((set(moved_from), set(moved_to)))

            shared = min(len(moved_to), len(moved_from))

            for _ in range(shared):
                id = "test_id_" + str(next(id_gen))

                new = moved_to.pop()
                old = moved_from.pop()

                old_label = str(old)
                new_label = str(new)
                # get language tags
                old_language = old.language
                new_language = new.language

                node = NodeRename(
                    id=id,
                    about_node=subject,
                    old_value=old_label,
                    new_value=new_label,
                    old_language=old_language,
                    new_language=new_language,
                )
                kgcl.append(node)

                covered.add((subject, RDFS.label, new))
                covered.add((subject, RDFS.label, old))

    return kgcl, covered, non_deterministic


def detect_annotation_changes(added, deleted, new_annotations, old_annotations):
    """
    Detect annotation changes.

    :param added: Added node.
    :param deleted: Deleted node.
    :param new_annotations: new annotations.
    :param old_annotations: old annotations.
    :return: Tuple(kgcl, covered, non_deterministic)
    """
    covered = rdflib.Graph()

    # maps from subjects to lists of annotation properties
    s_2_aps_deleted = {}
    s_2_aps_added = {}

    kgcl = []
    for s, p, _ in added:
        if p in new_annotations:
            if s not in s_2_aps_added:
                s_2_aps_added[s] = []
            s_2_aps_added[s].append(p)

    for s, p, _ in deleted:
        if p in old_annotations:
            if s not in s_2_aps_deleted:
                s_2_aps_deleted[s] = []
            s_2_aps_deleted[s].append(p)

    kgcl = []
    non_deterministic = []  # list of non-deterministic choices
    for s in s_2_aps_added:
        if s in s_2_aps_deleted:

            # get properties as sets
            added_properties = set(s_2_aps_added[s])
            deleted_properties = set(s_2_aps_deleted[s])

            # get intersection of relevant objects
            shared_properties = added_properties & deleted_properties

            for i in shared_properties:
                # get corresponding predicates
                changed_to = set()
                changed_from = set()
                for s, p, o in added.triples((s, i, None)):
                    changed_to.add((s, p, o))
                for s, p, o in deleted.triples((s, i, None)):
                    changed_from.add((s, p, o))

                if len(changed_to) > 1 or len(changed_from) > 1:
                    non_deterministic.append((set(changed_from), set(changed_to)))

                # match potential annotation changes
                m = min(len(changed_to), len(changed_from))

                for _ in range(m):
                    id = "test_id_" + str(next(id_gen))
                    old = (changed_from.pop())[2]
                    new = (changed_to.pop())[2]

                    old_language = None
                    old_datatype = None
                    if isinstance(old, Literal):
                        old_language = old.language
                        old_datatype = old.datatype
                        if old_datatype is not None:
                            old_datatype = (
                                "<" + old_datatype + ">"
                            )  # expect data types without curies

                    new_language = None
                    new_datatype = None
                    if isinstance(new, Literal):
                        new_language = new.language
                        new_datatype = new.datatype
                        if new_datatype is not None:
                            new_datatype = (
                                "<" + new_datatype + ">"
                            )  # expect data types without curies

                    change = NodeAnnotationChange(
                        id=id,
                        about_node=str(s),
                        about_node_representation=get_type(s),
                        annotation_property=str(i),
                        annotation_property_type=get_type(i),
                        old_value=str(old),
                        new_value=str(new),
                        old_value_type=get_type(old),
                        new_value_type=get_type(new),
                        old_language=old_language,
                        new_language=new_language,
                        old_datatype=old_datatype,
                        new_datatype=new_datatype,
                    )
                    kgcl.append(change)
                    covered.add((s, i, old))
                    covered.add((s, i, new))

    return kgcl, covered, non_deterministic


def detect_node_moves(added, deleted):
    """
    Detect NodeMove and associated triples.

    Given a diff represented by 'added' and 'deleted' triples,
    return an encoding in terms of
    (i) NodeMove instances,
    (ii) triples involved in (i), and
    (iii) nondeterministic choices.
    """
    covered = rdflib.Graph()

    # map from subject 2 property (in added)
    s2p_added = {}
    for s, p, _ in added:
        if s not in s2p_added:
            s2p_added[s] = set()
        s2p_added[s].add(p)

    # map from subject 2 property (in deleted)
    s2p_deleted = {}
    for s, p, _ in deleted:
        if s not in s2p_deleted:
            s2p_deleted[s] = set()
        s2p_deleted[s].add(p)

    # identify triples that only differ wrt their object
    s2p_shared = {}
    for s in s2p_added:
        if s in s2p_deleted:
            s2p_shared[s] = s2p_added[s] & s2p_deleted[s]

    kgcl = []  # list of detected KGCL node modes
    non_deterministic = []  # list of non-deterministic choices
    for subject in s2p_shared:
        for predicate in s2p_shared[subject]:

            # triples with the same subject and predicate
            moved_to = set()
            moved_from = set()
            for s, p, o in added.triples((subject, predicate, None)):
                if isinstance(o, URIRef):  # node move operates only on nodes
                    moved_to.add((s, p, o))
            for s, p, o in deleted.triples((subject, predicate, None)):
                if isinstance(o, URIRef):
                    moved_from.add((s, p, o))

            if len(moved_to) > 1 or len(moved_from) > 1:
                non_deterministic.append((set(moved_from), set(moved_to)))

            # TODO: impose an order to make this deterministic
            shared = min(len(moved_to), len(moved_from))
            # TODO: What is x doing here?
            for _ in range(shared):
                id = "test_id_" + str(next(id_gen))

                new = moved_to.pop()
                old = moved_from.pop()

                covered.add(new)
                covered.add(old)

                old_subject = str(old[0])
                old_predicate = str(old[1])
                old_object = str(old[2])
                new_object = str(new[2])

                edge = Edge(
                    subject=old_subject, predicate=old_predicate, object=old_object
                )

                # record entity type for KGCL rendering purposes
                old_object_type = get_type(old[2])
                new_object_type = get_type(new[2])

                node = NodeMove(
                    id=id,
                    about_edge=edge,
                    old_value=old_object,
                    new_value=new_object,
                    old_object_type=old_object_type,
                    new_object_type=new_object_type,
                )

                kgcl.append(node)

    return kgcl, covered, non_deterministic


def detect_predicate_changes(added, deleted):
    """Detect PredicateChange and associated triples.

    Given a diff represented by 'added' and 'deleted' triples,
    return an encoding in terms of
    (i) PredicateChange instances,
    (ii) triples involved in (i), and
    (iii) nondeterministic choices.
    """
    covered = rdflib.Graph()

    # maps from subjects to lists of objects
    s_2_os_deleted = {}
    s_2_os_added = {}

    for s, _, o in added:
        if s not in s_2_os_added:
            s_2_os_added[s] = []
        s_2_os_added[s].append(o)

    for s, _, o in deleted:
        if s not in s_2_os_deleted:
            s_2_os_deleted[s] = []
        s_2_os_deleted[s].append(o)

    # encode renamings wrt KGCL model
    kgcl = []
    non_deterministic = []  # list of non-deterministic choices
    for s in s_2_os_added:
        if s in s_2_os_deleted:

            # get the objects as sets
            added_objects = set(s_2_os_added[s])
            deleted_objects = set(s_2_os_deleted[s])

            # get intersection of relevant objects
            shared_objects = added_objects & deleted_objects

            for i in shared_objects:
                # get corresponding predicates
                changed_to = set()
                changed_from = set()
                for s, p, o in added.triples((s, None, i)):
                    changed_to.add((s, p, o))
                for s, p, o in deleted.triples((s, None, i)):
                    changed_from.add((s, p, o))

                # create KGCL edge object
                edge = Edge(subject=str(s), object=str(i))

                language = None
                datatype = None
                if isinstance(i, Literal):
                    language = i.language
                    datatype = i.datatype
                    if datatype is not None:
                        datatype = (
                            "<" + datatype + ">"
                        )  # expect data types without curies

                # if i.language is not None:
                #    language = str(i.language)
                # else:
                #    language = None
                # if i.datatype is not None:
                #    datatype = str(i.datatype)
                # else:
                #    datatype = None

                object_type = get_type(i)

                if len(changed_to) > 1 or len(changed_from) > 1:
                    non_deterministic.append((set(changed_from), set(changed_to)))

                # match potential predicate changes
                m = min(len(changed_to), len(changed_from))

                for _ in range(m):
                    id = "test_id_" + str(next(id_gen))
                    old = (changed_from.pop())[1]
                    new = (changed_to.pop())[1]

                    # KGCL change object
                    change = PredicateChange(
                        id=id,
                        about_edge=edge,
                        old_value=str(old),
                        new_value=str(new),
                        object_type=object_type,
                        language=language,
                        datatype=datatype,
                    )

                    kgcl.append(change)
                    covered.add((s, old, i))
                    covered.add((s, new, i))

    return kgcl, covered, non_deterministic
