"""KGCL parser."""
import logging
import re
import sys
from pathlib import Path
from typing import List

import click
from bioregistry import parse_iri, get_preferred_prefix, curie_to_str
from kgcl_schema.datamodel.kgcl import (
    Change,
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
    NodeShallowing,
    NodeTextDefinitionChange,
    NodeUnobsoletion,
    PlaceUnder,
    PredicateChange,
    RemoveSynonym,
    RemovedNodeFromSubset,
    RemoveUnder,
    Session,
)
from kgcl_schema.datamodel.ontology_model import Edge
from kgcl_schema.utils import to_json, to_rdf, to_yaml
from lark import Lark, Token


def id_generator():
    """Return a new ID for KGCL change operations."""
    id = 0
    while True:
        yield id
        id += 1


# initialise ID generator
id_gen = id_generator()


# initialise parser
path = Path(__file__).parent
kgcl_parser = Lark.open(str(path) + "/kgcl.lark", start="expression")


def parse(input: str) -> List[Change]:
    """
    Parse a set of KGCL command separated by next-line operator.

    Returns instantiated dataclass objects from model.kgcl_schema.
    """
    statements = input.splitlines()
    parsed = []

    for s in statements:
        parsed.append(parse_statement(s))
    return parsed


def parse_statement(input: str) -> Change:
    """
    Parse a KGCL command.

    Return an instantiated dataclass object from model.kgcl_schema.
    """
    # regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    # uri_list = re.findall(regex, input)
    # if uri_list:
    #     # curie = curie_from_iri(uri[0].replace("<", "").replace(">",""))
    #     for _, uri in enumerate(uri_list):
    #         pref, i = parse_iri(uri)
    #         pref = get_preferred_prefix(pref)
    #         curie = curie_to_str(pref, i)
    #         input = input.replace(uri, curie)

    tree = kgcl_parser.parse(input)
    id = "kgcl_change_id_" + str(next(id_gen))

    command = tree.data

    if command == "rename":
        return parse_rename(tree, id)
    elif command == "obsolete":
        return parse_obsolete(tree, id)
    elif command == "unobsolete":
        return parse_unobsolete(tree, id)
    elif command == "delete":
        return parse_delete(tree, id)
    elif command == "move":
        return parse_move(tree, id)
    elif command == "deepen":
        return parse_deepen(tree, id)
    elif command == "shallow":
        return parse_shallow(tree, id)
    elif command == "create_edge":
        return parse_create_edge(tree, id)
    elif command == "delete_edge":
        return parse_delete_edge(tree, id)
    elif command == "change_relationship":
        return parse_change_relationship(tree, id)
    elif command == "change_annotation":
        return parse_change_annotation(tree, id)
    elif command == "create":
        return parse_create(tree, id)
    elif command == "create_class":
        return parse_create_class(tree, id)
    elif command == "create_synonym":
        return parse_create_synonym(tree, id)
    elif command == "remove_from_subset":
        return parse_remove_from_subset(tree, id)
    elif command == "remove_synonym":
        return parse_remove_synonym(tree, id)
    elif command == "add_definition":
        return parse_add_definition(tree, id)
    elif command == "change_definition":
        return parse_change_definition(tree, id)
    else:
        raise NotImplementedError("No implementation for KGCL command: " + command)

    # TODO: does not have a field for subsets
    # if(command == "add_to_subset"):

    #    term_id = next(tree.find_data('id'))
    #    term_id_token = next(get_tokens(term_id))

    #    subset_id = next(tree.find_data('subset'))
    #    subset_id_token = next(get_tokens(subset_id))

    #    return AddNodeToSubset(
    #        id=id, in_subset=subset_id_token, about_node=term_id_token
    #     )

    # TODO: more commands
    # if(command == "merge"):
    # if(command == "add"):
    # if(command == "add_parent"):
    # if(command == "add_annotation"):
    # if(command == "add_axiom"): (in Manchester Syntax?)
    # if(command == "add_class"):
    # if(command == "add_text_definition"):
    # if(command == "merge"):


def parse_remove_from_subset(tree, id):
    """Remove node from subset."""
    term_id_token = extract(tree, "id")
    subset_id_token = extract(tree, "subset")

    return RemovedNodeFromSubset(
        id=id, subset=subset_id_token, about_node=term_id_token
    )


def parse_create_synonym(tree, id):
    """Create new synonym."""
    entity_token = extract(tree, "entity")
    entity, representation = get_entity_representation(entity_token)

    synonym_string_token = extract(tree, "synonym")
    synonym, representation2 = get_entity_representation(synonym_string_token)

    language_token = extract(tree, "language")
    qualifier_token = extract(tree, "synonym_qualifier")

    return NewSynonym(
        id=id,
        about_node=entity,
        about_node_representation=representation,
        new_value=synonym,
        qualifier=qualifier_token,
        language=language_token,
    )


def parse_remove_synonym(tree, id):
    """Remove a synonym."""
    entity_token = extract(tree, "entity")
    entity, representation = get_entity_representation(entity_token)

    synonym_string_token = extract(tree, "synonym")
    synonym, _ = get_entity_representation(synonym_string_token)

    language_token = extract(tree, "language")
    # qualifier_token = extract(tree, "synonym_qualifier")

    return RemoveSynonym(
        id=id,
        old_value=synonym,
        about_node=entity,
        about_node_representation=representation,
        # qualifier=qualifier_token,
        language=language_token,
    )


def parse_create_class(tree, id):
    """Create new class."""
    term_id_token = extract(tree, "id")
    entity, representation = get_entity_representation(term_id_token)

    return ClassCreation(
        id=id, node_id=entity, about_node_representation=representation
    )


def parse_add_definition(tree, id):
    """Add definition to class."""
    entity_token = extract(tree, "entity")
    new_value = extract(tree, "new_definition")
    entity, representation = get_entity_representation(entity_token)
    return NewTextDefinition(
        id=id,
        about_node=entity,
        about_node_representation=representation,
        new_value=new_value,
    )


def parse_change_definition(tree, id):
    """Change the definition of a class."""
    entity_token = extract(tree, "entity")
    old_value = extract(tree, "old_definition")
    new_value = extract(tree, "new_definition")
    entity, representation = get_entity_representation(entity_token)
    return NodeTextDefinitionChange(
        id=id,
        about_node=entity,
        about_node_representation=representation,
        new_value=new_value,
        old_value=old_value
    )


# the KGCL model suggests the command
# 'create node {id} {label} with {annotation set}'
# TODO: handling of {annotation set}
def parse_create(tree, id):
    """Create a node."""
    term_id_token = extract(tree, "id")
    label_token = extract(tree, "label")
    language_token = extract(tree, "language")

    entity, representation = get_entity_representation(term_id_token)

    return NodeCreation(
        id=id,
        about_node=entity,
        about_node_representation=representation,
        node_id=entity,  # was term_id_token
        name=label_token,
        language=language_token,
    )


def parse_change_annotation(tree, id):
    """Change node annotation."""
    subject_token = extract(tree, "entity_subject")
    predicate_token = extract(tree, "entity_predicate")

    subject, s_representation = get_entity_representation(subject_token)
    predicate, p_representation = get_entity_representation(predicate_token)

    old_token = extract(tree, "old_entity_object")
    new_token = extract(tree, "new_entity_object")

    old, old_representation = get_entity_representation(old_token)
    new, new_representation = get_entity_representation(new_token)

    old_language_token = extract(tree, "old_language")
    new_language_token = extract(tree, "new_language")

    old_datatype_token = extract(tree, "old_datatype")
    new_datatype_token = extract(tree, "new_datatype")

    return NodeAnnotationChange(
        id=id,
        about_node=subject,
        about_node_representation=s_representation,
        annotation_property=predicate,
        annotation_property_type=p_representation,
        old_value=old,
        new_value=new,
        old_value_type=old_representation,
        new_value_type=new_representation,
        old_language=old_language_token,
        new_language=new_language_token,
        old_datatype=old_datatype_token,
        new_datatype=new_datatype_token,
    )


def parse_change_relationship(tree, id):
    """Change predicate."""
    subject_token = extract(tree, "entity_subject")
    object_token = extract(tree, "entity_object")

    subject, s_representation = get_entity_representation(subject_token)
    object, o_representation = get_entity_representation(object_token)

    old_token = extract(tree, "old_entity")
    new_token = extract(tree, "new_entity")

    old, old_representation = get_entity_representation(old_token)
    new, new_representation = get_entity_representation(new_token)

    edge = Edge(
        subject=subject,
        predicate=old,
        object=object,
        subject_representation=s_representation,
        predicate_representation=old_representation,
        object_representation=o_representation,
    )

    language_token = extract(tree, "language")
    datatype_token = extract(tree, "datatype")

    return PredicateChange(
        id=id,
        about_edge=edge,
        old_value=old,
        new_value=new,
        old_value_type=old_representation,
        new_value_type=new_representation,
        language=language_token,
        datatype=datatype_token,
    )


def parse_delete_edge(tree, id):
    """Delete edge."""
    subject_token = extract(tree, "entity_subject")
    predicate_token = extract(tree, "entity_predicate")
    object_token = extract(tree, "entity_object_id")

    subject, s_representation = get_entity_representation(subject_token)
    predicate, p_representation = get_entity_representation(predicate_token)
    object, o_representation = get_entity_representation(object_token)

    if (
        predicate == "rdfs:subClassOf"
        or predicate == "<http://www.w3.org/2000/01/rdf-schema#subClassOf>"
    ):
        return RemoveUnder(
            id=id,
            subject=subject,
            predicate=predicate,
            object=object,
            subject_type=s_representation,
            predicate_type=p_representation,
            object_type=o_representation,
        )
    else:
        return EdgeDeletion(
            id=id,
            subject=subject,
            predicate=predicate,
            object=object,
            subject_type=s_representation,
            predicate_type=p_representation,
            object_type=o_representation,
        )


def parse_create_edge(tree, id):
    """Create new edge."""
    subject_token = extract(tree, "entity_subject")
    predicate_token = extract(tree, "entity_predicate")
    object_token = extract(tree, "entity_object_id")

    subject, s_representation = get_entity_representation(subject_token)
    predicate, p_representation = get_entity_representation(predicate_token)
    object, o_representation = get_entity_representation(object_token)

    if (
        predicate == "rdfs:subClassOf"
        or predicate == "<http://www.w3.org/2000/01/rdf-schema#subClassOf>"
    ):
        return PlaceUnder(
            id=id,
            subject=subject,
            predicate=predicate,
            object=object,
            subject_type=s_representation,
            predicate_type=p_representation,
            object_type=o_representation,
        )
    else:
        return EdgeCreation(
            id=id,
            subject=subject,
            predicate=predicate,
            object=object,
            subject_type=s_representation,
            predicate_type=p_representation,
            object_type=o_representation,
        )


def parse_shallow(tree, id):
    """Perform node shallowing."""
    entity_token = extract(tree, "entity")
    old_token = extract(tree, "old_entity")
    new_token = extract(tree, "new_entity")

    entity, e_representation = get_entity_representation(entity_token)
    old_entity, o_representation = get_entity_representation(old_token)
    new_entity, n_representation = get_entity_representation(new_token)

    edge = Edge(
        subject=entity,
        object=old_entity,
        subject_representation=e_representation,
        object_representation=o_representation,
    )

    return NodeShallowing(
        id=id,
        about_edge=edge,
        old_value=old_entity,
        new_value=new_entity,
        old_object_type=o_representation,
        new_object_type=n_representation,
    )


def parse_deepen(tree, id):
    """Perform node deepening."""
    entity_token = extract(tree, "entity")
    old_token = extract(tree, "old_entity")
    new_token = extract(tree, "new_entity")

    entity, e_representation = get_entity_representation(entity_token)
    old_entity, o_representation = get_entity_representation(old_token)
    new_entity, n_representation = get_entity_representation(new_token)

    edge = Edge(
        subject=entity,
        object=old_entity,
        subject_representation=e_representation,
        object_representation=o_representation,
    )

    return NodeDeepening(
        id=id,
        about_edge=edge,
        old_value=old_entity,
        new_value=new_entity,
        old_object_type=o_representation,
        new_object_type=n_representation,
    )


def parse_move(tree, id):
    """Move a node."""
    subject_token = extract(tree, "entity_subject")
    predicate_token = extract(tree, "entity_predicate")
    object_token = extract(tree, "entity_object")

    subject, s_representation = get_entity_representation(subject_token)
    predicate, p_representation = get_entity_representation(predicate_token)
    object, o_representation = get_entity_representation(object_token)

    old_token = extract(tree, "old_entity")
    new_token = extract(tree, "new_entity")

    old, old_representation = get_entity_representation(old_token)
    new, new_representation = get_entity_representation(new_token)

    edge = Edge(
        subject=subject,
        predicate=predicate,
        object=object,
        subject_representation=s_representation,
        predicate_representation=p_representation,
        object_representation=o_representation,
    )

    return NodeMove(
        id=id,
        about_edge=edge,
        old_value=old,
        new_value=new,
        old_object_type=old_representation,
        new_object_type=new_representation,
    )


def parse_delete(tree, id):
    """Delete a node."""
    entity_token = extract(tree, "entity")
    entity, representation = get_entity_representation(entity_token)

    return NodeDeletion(
        id=id, about_node=entity, about_node_representation=representation
    )


def parse_unobsolete(tree, id):
    """Unobsolete a node."""
    entity_token = extract(tree, "entity")
    entity, representation = get_entity_representation(entity_token)

    return NodeUnobsoletion(
        id=id, about_node=entity, about_node_representation=representation
    )


def parse_obsolete(tree, id):
    """Obsolete a node."""
    entity_token = extract(tree, "entity")
    entity, representation = get_entity_representation(entity_token)

    replacement_token = extract(tree, "replacement")
    if replacement_token:
        return NodeObsoletionWithDirectReplacement(
            id=id,
            about_node=entity,
            about_node_representation=representation,
            has_direct_replacement=replacement_token,
        )
    else:
        return NodeObsoletion(
            id=id, about_node=entity, about_node_representation=representation
        )


def parse_rename(tree, id):
    """Rename a node."""
    old_token = extract(tree, "old_label")
    new_token = extract(tree, "new_label")
    old_language = extract(tree, "old_language")
    new_language = extract(tree, "new_language")

    # TODO old_token and new_token are enclosed in ''

    term_id_token = extract(tree, "id")
    if term_id_token is not None:
        entity, representation = get_entity_representation(term_id_token)
    else:
        entity = None
        representation = None

    return NodeRename(
        id=id,
        about_node=entity,
        about_node_representation=representation,
        old_value=old_token,
        new_value=new_token,
        old_language=old_language,
        new_language=new_language,
    )


def extract(tree, data):
    """Extract node."""
    node = get_next(tree.find_data(data))
    if node is not None:
        node_token = next(get_tokens(node))
        return node_token
    else:
        return None


def get_tokens(tree):
    """Get tokens."""
    return tree.scan_values(lambda v: isinstance(v, Token))


def get_next(generator):
    """Next generator."""
    try:
        res = next(generator)
        return res
    except StopIteration:
        return None


def get_entity_representation(entity):
    """Get entity representation."""
    first_character = entity[0]
    last_character = entity[-1:]
    if first_character == "<" and last_character == ">":
        return (
            contract_uri(entity.replace("<", "").replace(">", "")),
            "curie",
        )  # removing brackets
    if first_character == "'" and last_character == "'" and entity[1] != "'":
        return entity[1:-1], "label"
    if first_character == '"' and last_character == '"':
        return entity[1:-1], "literal"
    if entity[0:3] == '"""' and entity[-3:] == '"""':
        return entity[3:-3], "literal"
    if entity[0:3] == "'''" and entity[-3:] == "'''":
        return entity[3:-3], "literal"

    # TODO: use predefined set of prefixes to identify CURIEs
    return contract_uri(str(entity)), "curie"
    # return entity, "error"


def contract_uri(uri_or_curie: str):
    if uri_or_curie.startswith("http://") or uri_or_curie.startswith("https://"):
        pref, i = parse_iri(uri_or_curie)
        pref = get_preferred_prefix(pref)
        curie = curie_to_str(pref, i)
        return curie
    else:
        return uri_or_curie


@click.command()
@click.option("--output", "-o", type=click.File(mode="w"), default=sys.stdout)
@click.option("--output-type", "-O", help="format for output")
@click.option("-v", "--verbose", count=True)
@click.argument("patches", nargs=-1)
def cli(patches, verbose: int, output, output_type):
    """
    Parse a patch or patches specified in KGCL DSL
    """
    if verbose >= 2:
        logging.basicConfig(level=logging.DEBUG)
    elif verbose == 1:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)

    # parser kgcl_schema commands
    changes = []
    for patch in patches:
        logging.info(f"Patch: {patch}")
        changes += parse(patch)
    session = Session(change_set=changes)
    if output_type is None or output_type == "yaml":
        output.write(to_yaml(session))
    elif output_type == "json":
        output.write(to_json(session))
    elif output_type == "rdf":
        output.write(to_rdf(session))
    else:
        raise NotImplementedError(output_type)


if __name__ == "__main__":
    cli()
