from typing import Tuple, Optional, List, Union

from kgcl_schema.datamodel.kgcl import (
    NodeObsoletionWithDirectReplacement,
    NodeRename,
    NodeObsoletion,
    NewSynonym,
    ClassCreation,
    PredicateChange,
    Change,
    NodeCreation,
    EdgeCreation,
    PlaceUnder,
    RemoveSynonym,
    RemoveUnder,
    EdgeDeletion,
    NodeDeepening,
)
from kgcl_schema.datamodel.ontology_model import Edge

TODO_TOKEN = "TODO"
PART_OF = "BFO:0000050"
PART_OF_URI = "http://purl.obolibrary.org/obo/BFO_0000050"
IS_A = "rdfs:subClassOf"
IS_A_URI = "http://www.w3.org/2000/01/rdf-schema#subClassOf"
NUCLEUS = "GO:0005634"
NUCLEUS_URI = "http://purl.obolibrary.org/obo/GO_0005634"
MITOCHONDRION = "GO:0005739"
MITOCHONDRION_URI = "http://purl.obolibrary.org/obo/GO_0005739"
IMBO = "GO:0043231"
IMBO_URI = "http://purl.obolibrary.org/obo/GO_0043231"
NUCLEAR_ENVELOPE = "GO:0005635"
NUCLEAR_ENVELOPE_URI = "http://purl.obolibrary.org/obo/GO_0005635"
NEW_TERM = "GO:9999999"
NEW_TERM_URI = "http://purl.obolibrary.org/obo/GO_9999999"
RESPONSE_TO_UV = "GO:0009411"
RESPONSE_TO_UV_URI = "http://purl.obolibrary.org/obo/GO_0009411"

UID = "CHANGE:001"
TERM = "GO:123"
TERM2 = "GO:999"

KGCL_COMMAND = str

CASE = Tuple[
    KGCL_COMMAND, Optional[KGCL_COMMAND], Change, Optional[Union[List[Change], Change]]
]
"""
Each case is a tuple of:

- Input command
- Output command after round-tripping through apply-diff
- Expected change object corresponding to command
- Expected change object(s) after round-tripping through apply-diff
"""

CASES: List[CASE] = [
    (
        f"rename {NUCLEAR_ENVELOPE} from 'nuclear envelope' to 'foo bar'",
        f"rename {NUCLEAR_ENVELOPE_URI} from 'nuclear envelope' to 'foo bar'",
        NodeRename(
            id=UID,
            old_value="'nuclear envelope'",
            new_value="'foo bar'",
            about_node="GO:0005635",
            about_node_representation="curie",
        ),
        None,
    ),
    (
        f"rename {NUCLEUS} from 'nucleus' to 'bar'",
        f"rename {NUCLEUS_URI} from 'nucleus' to 'bar'",
        NodeRename(
            id=UID,
            old_value="'nucleus'",
            new_value="'bar'",
            about_node=NUCLEUS,
            about_node_representation="curie",
        ),
        None,
    ),
    # TODO: this causes multiple issues, will require fixes to renderers and parsers
    # (
    #    f"""rename {NUCLEUS} from 'nucleus' to 'bobby " tables'""",
    #    f"""rename {NUCLEUS_URI} from 'nucleus' to 'bobby " tables'""",
    #    NodeRename(id=UID,
    #               old_value="'nucleus'",
    #               new_value="'bar'",
    #               about_node=NUCLEUS,
    #               about_node_representation='curie'),
    #    None
    # ),
    (
        f"obsolete {NUCLEUS}",
        None,  ### TODO - currently obsolete is not working
        NodeObsoletion(id=UID, about_node=NUCLEUS, about_node_representation="curie"),
        None,
    ),
    (
        f"obsolete {NUCLEUS} with replacement {TERM2}",
        None,
        NodeObsoletionWithDirectReplacement(
            id=UID,
            about_node=NUCLEUS,
            about_node_representation="curie",
            has_direct_replacement=TERM2,
        ),
        None,
    ),
    (
        f"create exact synonym 'foo' for {NUCLEUS}",
        f"create exact synonym 'foo' for {NUCLEUS_URI}",
        NewSynonym(
            id=UID,
            about_node=NUCLEUS,
            about_node_representation="curie",
            new_value="foo",
            qualifier="exact",
        ),
        None,
    ),
    (
        f"create broad synonym 'foo'@en for {NUCLEUS}",
        f"create broad synonym 'foo'@en for {NUCLEUS_URI}",
        NewSynonym(
            id=UID,
            about_node=NUCLEUS,
            about_node_representation="curie",
            language="en",
            new_value="foo",
            qualifier="broad",
        ),
        None,
    ),
    (
        f"remove synonym 'foo' for {NUCLEUS}",
        f"remove synonym 'foo' for {NUCLEUS_URI}",
        RemoveSynonym(
            id=UID,
            old_value="foo",
        ),
        None,
    ),
    (
        f"create {NEW_TERM}",
        f"create {NEW_TERM_URI}",
        ClassCreation(id=UID, node_id=NEW_TERM, about_node_representation="curie"),
        None,
    ),
    (
        f"create node {NEW_TERM} 'foo'",
        # TODO: diff not working here:
        # f"create node {NEW_TERM_URI} 'foo'",
        TODO_TOKEN,
        NodeCreation(
            id=UID,
            node_id=NEW_TERM,  ## TODO: remove this
            about_node=NEW_TERM,
            name="'foo'",
            about_node_representation="curie",
        ),
        None,
    ),
    #! SAME AS ABOVE
    # (
    #     f"create node {NEW_TERM} 'foo'",
    #     # TODO: diff not working here:
    #     #f"create node {NEW_TERM_URI} 'foo'",
    #     TODO_TOKEN,
    #     NodeCreation(id=UID,
    #                  node_id=NEW_TERM,   ## TODO: remove this
    #                  about_node=NEW_TERM,
    #                  name="'foo'",
    #                  about_node_representation='curie'),
    #     None
    # ),
    (
        f"create edge {NUCLEUS} {PART_OF} {RESPONSE_TO_UV}",
        f"create edge {NUCLEUS_URI} {PART_OF_URI} {RESPONSE_TO_UV_URI}",
        EdgeCreation(
            id=UID,
            subject=NUCLEUS,
            predicate=PART_OF,
            object=RESPONSE_TO_UV,
            subject_type="curie",
            predicate_type="curie",
            object_type="curie",
        ),
        None,
    ),
    (
        f"create edge {NUCLEUS} {IS_A} {RESPONSE_TO_UV}",
        f"create edge {NUCLEUS_URI} {IS_A_URI} {RESPONSE_TO_UV_URI}",
        PlaceUnder(
            id=UID,
            subject=NUCLEUS,
            predicate=IS_A,
            object=RESPONSE_TO_UV,
            subject_type="curie",
            predicate_type="curie",
            object_type="curie",
        ),
        None,
    ),
    (
        f"change relationship between {NUCLEAR_ENVELOPE} and {NUCLEUS} from {PART_OF} to {IS_A}",
        None,  ## TODO: this adds an edge but does not delete it
        PredicateChange(
            id=UID,
            old_value=PART_OF,
            new_value=IS_A,
            old_value_type="curie",
            new_value_type="curie",
            about_edge=Edge(
                subject=NUCLEAR_ENVELOPE,
                predicate=PART_OF,
                object=NUCLEUS,
                subject_representation="curie",
                predicate_representation="curie",
                object_representation="curie",
            ),
        ),
        None,
    ),
    (
        f"change relationship between {NUCLEUS} and {IMBO} from {IS_A} to {PART_OF}",
        f"change relationship between {NUCLEUS_URI} and {IMBO_URI} from {IS_A_URI} to {PART_OF_URI}",
        PredicateChange(
            id=UID,
            old_value=IS_A,
            new_value=PART_OF,
            old_value_type="curie",
            new_value_type="curie",
            about_edge=Edge(
                subject=NUCLEUS,
                predicate=IS_A,
                object=IMBO,
                subject_representation="curie",
                predicate_representation="curie",
                object_representation="curie",
            ),
        ),
        None,
    ),
    (
        f"delete edge {NUCLEUS} {IS_A} {IMBO}",
        f"delete edge {NUCLEUS_URI} {IS_A_URI} {IMBO_URI}",
        # TODO: this should preferentially be delete edge
        RemoveUnder(
            id=UID,
            subject=NUCLEUS,
            predicate=IS_A,
            object=IMBO,
            subject_type="curie",
            predicate_type="curie",
            object_type="curie",
        ),
        None,
    ),
    (
        f"delete edge {NUCLEAR_ENVELOPE} {PART_OF} {NUCLEUS}",
        # f"delete edge {NUCLEAR_ENVELOPE_URI} {PART_OF_URI} {NUCLEUS_URI}",
        TODO_TOKEN,
        EdgeDeletion(
            id=UID,
            subject=NUCLEAR_ENVELOPE,
            predicate=PART_OF,
            object=NUCLEUS,
            subject_type="curie",
            predicate_type="curie",
            object_type="curie",
        ),
        None,
    ),
    (
        f"deepen {MITOCHONDRION} from {IMBO} to {NUCLEUS}",
        # f"deepen {MITOCHONDRION_URI} from {IMBO_URI} to {NUCLEUS_URI}",
        TODO_TOKEN,
        NodeDeepening(
            id=UID,
            old_value=IMBO,
            new_value=NUCLEUS,
            old_object_type="curie",
            new_object_type="curie",
            about_edge=Edge(
                subject=MITOCHONDRION,
                object=IMBO,
                subject_representation="curie",
                object_representation="curie",
            ),
        ),
        None,
    ),
]
