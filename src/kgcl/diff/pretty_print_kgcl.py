"""Print KGCL in user-friendly format."""
from rdflib.namespace import RDFS

import kgcl.grammar.parser
from kgcl.datamodel.kgcl import (ClassCreation, EdgeCreation, EdgeDeletion,
                             NewSynonym, NodeAnnotationChange, NodeCreation,
                             NodeDeletion, NodeMove, NodeObsoletion,
                             NodeRename, NodeUnobsoletion, PlaceUnder,
                             PredicateChange, RemoveUnder)

# TODO: maintain this dictionary in a file
prefix_2_uri = {
    "obo": "http://purl.obolibrary.org/obo/",
    "ex": "http://example.org/",
    "oboInOwl": "http://www.geneontology.org/formats/oboInOwl#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "swrl": "http://www.w3.org/2003/11/swrl#",
    "oio": "http://www.geneontology.org/formats/oboInOwl#",
    "dce": "http://purl.org/dc/elements/1.1/",
    "dct": "http://purl.org/dc/terms/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "protege": "http://protege.stanford.edu/plugins/owl/protege#",
    "BFO": "http://purl.obolibrary.org/obo/BFO_",
    "CHEBI": "http://purl.obolibrary.org/obo/CHEBI_",
    "CL": "http://purl.obolibrary.org/obo/CL_",
    "IAO": "http://purl.obolibrary.org/obo/IAO_",
    "NCBITaxon": "http://purl.obolibrary.org/obo/NCBITaxon_",
    "OBI": "http://purl.obolibrary.org/obo/OBI_",
    "PR": "http://purl.obolibrary.org/obo/PR_",
    "obo": "http://purl.obolibrary.org/obo/",
    "UP": "http://purl.uniprot.org/uniprot/",
    "UC": "http://purl.uniprot.org/core/",
    "PRO": "http://www.uniprot.org/annotation/PRO_",
    "faldo": "http://biohackathon.org/resource/faldo#",
}


def get_labels(graph):
    """Return a map from IRIs in a graph to (a set of) labels."""
    entity_2_label = {}
    for s, _, o in graph.triples((None, RDFS.label, None)):
        ss = str(s)
        os = str(o)
        if "'" not in os:
            if ss not in entity_2_label:
                entity_2_label[ss] = []
            entity_2_label[ss].append(os)

    return entity_2_label


def render_instances(kgcl_patch, graph):
    """
    Return patch with IRIs replaced by CURIEs.

    Takes a KGCL patch for a graph and
    returns a more readable patch
    in which IRI's are replaced by CURIEs and labels where possible.
    """
    labelling = get_labels(graph)

    pretty_print_kgcl_patch = []
    for k in kgcl_patch:
        kgcl_instance = kgcl.grammar.parser.parse_statement(k)
        # render_instance(kgcl_instance, labelling)
        pretty_print_kgcl_patch.append(render_instance(kgcl_instance, labelling))

    return pretty_print_kgcl_patch


def has_label(entity, labelling):
    """Return the label for an entity if it exists and the entity itself otherwise."""
    if entity in labelling:
        return "'" + labelling[entity][0] + "'"
    else:
        return entity


def curie_entity(entity):
    """Return the CURIE for an entity if it exists and the entity itself otherwise."""
    for prefix, curie in prefix_2_uri.items():
        if curie in entity:
            return entity.replace(curie, prefix + ":")[1:-1]
    return entity


def render_entity(entity, type, labelling):
    """Return an encoding of the given entity using either a CURIE, a label, a literal, or a URI."""
    entity = str(entity)
    entity = repr(entity)[1:-1]
    if type == "uri":
        labelling = has_label(entity[1:-1], labelling)
        if entity[1:-1] != labelling:
            return labelling

        curing = curie_entity(entity)
        if entity != curing:
            return curing
        # return "<" + entity + ">"
        return entity

    elif type == "label":
        if "'" not in entity:
            return "'" + entity + "'"

    elif type == "literal":
        if '"' not in entity:
            return '"' + entity + '"'
        elif "'''" not in entity and entity[-1] != "'":
            return "'''" + entity + "'''"
        elif '"""' not in entity and entity[-1] != '"':
            return '"""' + entity + '"""'
        else:
            # return "Error  " + entity
            print("Rendering error: " + entity)
            raise
    else:
        # return "Error  " + entity
        print("Rendering error: " + entity)
        raise


def render_instance(kgcl_instance, labelling):
    """Render instance."""
    if type(kgcl_instance) is NodeRename:
        # TODO: subject could be 'None'? (not in KGCL Diff)
        # passing an empty labelling because we do not want to repeat labels
        subject = render_entity(kgcl_instance.about_node, "uri", {})
        old = kgcl_instance.old_value
        new = kgcl_instance.new_value

        new_language = kgcl_instance.new_language
        old_language = kgcl_instance.old_language

        if old_language is not None:
            old = old + "@" + old_language

        if new_language is not None:
            new = new + "@" + new_language

        return "rename " + subject + " from " + old + " to " + new

    if type(kgcl_instance) is NodeObsoletion:
        subject = render_entity(kgcl_instance.about_node, "uri", labelling)
        replacement = render_entity(
            kgcl_instance.has_direct_replacement, "uri", labelling
        )
        if kgcl_instance.has_direct_replacement is not None:
            return "obsolete " + subject + " with replacement " + replacement
        else:
            return "obsolete " + subject

    if type(kgcl_instance) is NodeUnobsoletion:
        subject = render_entity(kgcl_instance.about_node, "uri", labelling)
        return "unobsolete " + subject

    if type(kgcl_instance) is NodeDeletion:
        subject = render_entity(kgcl_instance.about_node, "uri", labelling)
        return "delete " + subject

    if type(kgcl_instance) is NodeMove:
        subject = render_entity(kgcl_instance.about_edge.subject, "uri", labelling)
        predicate = render_entity(kgcl_instance.about_edge.predicate, "uri", labelling)
        new = render_entity(
            kgcl_instance.new_value, kgcl_instance.new_object_type, labelling
        )
        old = render_entity(
            kgcl_instance.old_value, kgcl_instance.old_object_type, labelling
        )

        return (
            "move "
            + subject
            + " "
            + predicate
            + " "
            + old
            + " "
            + "from"
            + " "
            + old
            + " "
            + "to"
            + " "
            + new
        )

    if type(kgcl_instance) is EdgeCreation:
        return render_edge_creation(kgcl_instance, labelling)

    if type(kgcl_instance) is EdgeDeletion:
        return render_edge_deletion(kgcl_instance, labelling)

    if type(kgcl_instance) is PredicateChange:
        subject = render_entity(kgcl_instance.about_edge.subject, "uri", labelling)
        object = render_entity(
            kgcl_instance.about_edge.object,
            kgcl_instance.about_edge.object_representation,
            labelling,
        )

        new = render_entity(
            kgcl_instance.new_value,
            "uri",
            labelling,
        )
        old = render_entity(kgcl_instance.old_value, "uri", labelling)

        if kgcl_instance.language is not None:
            object += "@" + kgcl_instance.language

        if kgcl_instance.datatype is not None:
            object += "^^" + kgcl_instance.datatype

        return (
            "change relationship between "
            + subject
            + " and "
            + object
            + " from "
            + old
            + " to "
            + new
        )

    if type(kgcl_instance) is NodeCreation:
        subject = render_entity(kgcl_instance.about_node, "uri", labelling)
        label = render_entity(kgcl_instance.name, "label", labelling)
        if kgcl_instance.name is not None:
            return "create node " + subject + " " + label
        else:
            return "create " + subject

    if type(kgcl_instance) is ClassCreation:
        subject = render_entity(kgcl_instance.node_id, "uri", labelling)
        return "create " + subject

    if type(kgcl_instance) is NewSynonym:
        subject = render_entity(kgcl_instance.about_node, "uri", labelling)
        synonym = render_entity(kgcl_instance.new_value, "label", labelling)
        qualifier = kgcl_instance.qualifier
        language = kgcl_instance.language

        if language is not None:
            synonym = synonym + "@" + language

        if qualifier is not None:
            return (
                "create " + qualifier + " synonym" + " " + synonym + " for " + subject
            )
        else:
            return "create synonym " + synonym + " for " + subject

    if type(kgcl_instance) is PlaceUnder:
        subclass = render_entity(kgcl_instance.subject, "uri", labelling)
        superclass = render_entity(kgcl_instance.object, "uri", labelling)
        return "create edge " + subclass + " rdfs:subClassOf " + superclass

    if type(kgcl_instance) is RemoveUnder:
        subclass = render_entity(kgcl_instance.subject, "uri", labelling)
        superclass = render_entity(kgcl_instance.object, "uri", labelling)
        return "delete edge " + subclass + " rdfs:subClassOf " + superclass

    if type(kgcl_instance) is NodeAnnotationChange:
        subject = render_entity(
            kgcl_instance.about_node, kgcl_instance.about_node_representation, labelling
        )
        predicate = render_entity(
            kgcl_instance.annotation_property,
            kgcl_instance.annotation_property_type,
            labelling,
        )
        old_object = render_entity(
            kgcl_instance.old_value,
            kgcl_instance.old_value_type,
            labelling,
        )
        new_object = render_entity(
            kgcl_instance.new_value,
            kgcl_instance.new_value_type,
            labelling,
        )

        if kgcl_instance.old_language is not None:
            old_object += "@" + kgcl_instance.old_language

        if kgcl_instance.new_language is not None:
            new_object += "@" + kgcl_instance.new_language

        if kgcl_instance.old_datatype is not None:
            old_object += "^^" + kgcl_instance.old_datatype

        if kgcl_instance.new_datatype is not None:
            new_object += "^^" + kgcl_instance.new_datatype

        return (
            "change annotation of "
            + subject
            + " with "
            + predicate
            + " from "
            + old_object
            + " to "
            + new_object
        )


def render_edge_deletion(kgcl_instance, labelling):
    """Render edge deletion."""
    subject = render_entity(kgcl_instance.subject, "uri", labelling)
    predicate = render_entity(kgcl_instance.predicate, "uri", labelling)
    object = render_entity(kgcl_instance.object, kgcl_instance.object_type, labelling)

    language = kgcl_instance.language
    datatype = kgcl_instance.datatype

    base = "delete edge " + subject + " " + predicate + " " + object

    if language is not None:
        return base + "@" + language
    elif datatype is not None:
        return base + "^^" + datatype
    else:
        return base


def render_edge_creation(kgcl_instance, labelling):
    """Render edge creation."""
    subject = render_entity(kgcl_instance.subject, "uri", labelling)
    predicate = render_entity(kgcl_instance.predicate, "uri", labelling)
    object = render_entity(kgcl_instance.object, kgcl_instance.object_type, labelling)

    language = kgcl_instance.language
    datatype = kgcl_instance.datatype

    base = "create edge " + subject + " " + predicate + " " + object

    if language is not None:
        return base + "@" + language
    elif datatype is not None:
        return base + "^^" + datatype
    else:
        return base
