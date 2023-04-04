"""Render operations."""
# TODO: move this to grammar package

from kgcl_schema.datamodel.kgcl import (
    ClassCreation,
    EdgeCreation,
    EdgeDeletion,
    NewSynonym,
    NewTextDefinition,
    NodeAnnotationChange,
    NodeCreation,
    NodeDeepening,
    NodeDeletion,
    NodeMove,
    NodeObsoletion,
    NodeObsoletionWithDirectReplacement,
    NodeRename,
    NodeTextDefinitionChange,
    NodeUnobsoletion,
    PlaceUnder,
    PredicateChange,
    RemoveSynonym,
    RemoveUnder,
    Change,
)
from lark.lexer import Token


# TODO: replace this with rdflib methods
def render_entity(entity, rdf_type):
    """
    Render entity based on rdf type.

    :param entity: entity to be rendered.
    :param rdf_type: type of RDF ["uri", "label", "literal]
    """
    entity = repr(entity)
    if rdf_type is None:
        return entity
    elif rdf_type == "uri":
        entity = entity.replace("'", "")
        return entity
    elif rdf_type == "label":
        if type(eval(entity)) == Token:
            entity = eval(entity).value
        # elif "'" in entity:
        #     # TODO: replacing quotes with backticks
        #     # is only a temporary workaround
        #     entity = entity.replace("'", "`")
        return entity
    elif rdf_type == "literal":
        # TODO: test this
        if '"' not in entity:
            return '"' + entity + '"'
        elif "'''" not in entity and entity[-1] != "'":
            return "'''" + entity + "'''"
        elif '"""' not in entity and entity[-1] != '"':
            return '"""' + entity + '"""'
        else:
            raise ValueError("Rendering error: " + entity)
    else:
        raise ValueError(f"Rendering error: {entity} {rdf_type}")
    # return "'" + entity.replace("\\'", "`") + "'"


def render(kgcl_instance: Change) -> str:
    """Render KGCL."""
    if type(kgcl_instance) is NodeRename:
        # TODO: subject could be 'None'?
        subject = render_entity(kgcl_instance.about_node, "uri")
        old = render_entity(kgcl_instance.old_value, "label")
        new = render_entity(kgcl_instance.new_value, "label")

        new_language = kgcl_instance.new_language
        old_language = kgcl_instance.old_language

        if old_language is not None:
            old = old + "@" + old_language

        if new_language is not None:
            new = new + "@" + new_language

        return "rename " + subject + " from " + old + " to " + new

    if type(kgcl_instance) is NodeAnnotationChange:
        subject = render_entity(
            kgcl_instance.about_node, kgcl_instance.about_node_representation
        )
        predicate = render_entity(
            kgcl_instance.annotation_property, kgcl_instance.annotation_property_type
        )
        old_object = render_entity(
            kgcl_instance.old_value, kgcl_instance.old_value_type
        )
        new_object = render_entity(
            kgcl_instance.new_value, kgcl_instance.new_value_type
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

    if (
        type(kgcl_instance) is NodeObsoletion
        or type(kgcl_instance) is NodeObsoletionWithDirectReplacement
    ):
        subject = render_entity(kgcl_instance.about_node, "uri")
        # TODO: type this correctly
        replacement = render_entity(kgcl_instance.has_direct_replacement, "uri")
        if kgcl_instance.has_direct_replacement is not None:
            return "obsolete " + subject + " with replacement " + replacement
        else:
            return "obsolete " + subject

    if type(kgcl_instance) is NodeUnobsoletion:
        subject = render_entity(kgcl_instance.about_node, "uri")
        return "unobsolete " + subject

    if type(kgcl_instance) is NodeDeletion:
        subject = render_entity(kgcl_instance.about_node, "uri")
        return "delete " + subject

    if type(kgcl_instance) is NodeMove:
        subject = render_entity(kgcl_instance.about_edge.subject, "uri")
        predicate = render_entity(kgcl_instance.about_edge.predicate, "uri")
        new = render_entity(kgcl_instance.new_value, kgcl_instance.new_object_type)
        old = render_entity(kgcl_instance.old_value, kgcl_instance.old_object_type)
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

    if type(kgcl_instance) is PredicateChange:
        subject = render_entity(kgcl_instance.about_edge.subject, "uri")
        object = render_entity(kgcl_instance.about_edge.object, "uri")
        new = render_entity(kgcl_instance.new_value, "uri")
        old = render_entity(kgcl_instance.old_value, "uri")

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
        subject = render_entity(kgcl_instance.about_node, "uri")
        label = render_entity(kgcl_instance.name, "label")
        if kgcl_instance.name is not None:
            return "create node " + subject + " " + label
        else:
            return "create " + subject

    if type(kgcl_instance) is ClassCreation:
        subject = render_entity(kgcl_instance.node_id, "uri")
        return "create " + subject

    if type(kgcl_instance) is NewSynonym:
        subject = render_entity(kgcl_instance.about_node, "uri")
        synonym = render_entity(kgcl_instance.new_value, "label")
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

    if type(kgcl_instance) is RemoveSynonym:
        subject = render_entity(kgcl_instance.about_node, "uri")
        synonym = render_entity(kgcl_instance.old_value, "label")
        # qualifier = kgcl_instance.qualifier
        language = kgcl_instance.language

        if language is not None:
            synonym = synonym + "@" + language

        # if qualifier is not None:
        #     return (
        #         "remove " + qualifier + " synonym" + " " + synonym + " for " + subject
        #     )
        # else:
        return "remove synonym " + synonym + " for " + subject

    if type(kgcl_instance) is PlaceUnder:
        subclass = render_entity(kgcl_instance.subject, "uri")
        superclass = render_entity(kgcl_instance.object, "uri")
        predicate_type = render_entity(kgcl_instance.predicate, "uri")
        return "create edge " + subclass + " " + predicate_type + " " + superclass

    if type(kgcl_instance) is RemoveUnder:
        subclass = render_entity(kgcl_instance.subject, "uri")
        superclass = render_entity(kgcl_instance.object, "uri")
        predicate_type = render_entity(kgcl_instance.predicate, "uri")
        return "delete edge " + subclass + " " + predicate_type + " " + superclass

    # TODO these need to be changed
    if type(kgcl_instance) is EdgeCreation:
        subclass = render_entity(kgcl_instance.subject, "uri")
        property = render_entity(kgcl_instance.predicate, "uri")
        filler = render_entity(kgcl_instance.object, "uri")
        return "create edge " + subclass + " " + property + " " + filler

    if type(kgcl_instance) is EdgeDeletion:
        subclass = render_entity(kgcl_instance.subject, "uri")
        property = render_entity(kgcl_instance.predicate, "uri")
        filler = render_entity(kgcl_instance.object, "uri")
        return "delete edge " + subclass + " " + property + " " + filler

    if type(kgcl_instance) is NodeDeepening:
        subject = kgcl_instance.about_edge.subject
        old_value = kgcl_instance.old_value
        new_value = kgcl_instance.new_value
        return "deepen " + subject + " from " + old_value + " to " + new_value

    if type(kgcl_instance) is NewTextDefinition:
        subject = kgcl_instance.about_node
        definition = kgcl_instance.new_value
        return "add definition " + definition + " to " + subject

    if type(kgcl_instance) is NodeTextDefinitionChange:
        subject = kgcl_instance.about_node
        new_definition = kgcl_instance.new_value
        if kgcl_instance.old_value:
            old_definition = kgcl_instance.old_value
            return "change definition of " + subject + " from " + old_definition + " to " + new_definition
        else:
            return "change definition of " + subject + " to " + new_definition
