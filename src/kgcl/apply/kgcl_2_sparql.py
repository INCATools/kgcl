"""KGCL SPARQL implementation."""
import logging
import re
from typing import Optional, List

from kgcl.datamodel.kgcl import (ClassCreation, EdgeCreation, EdgeDeletion,
                                 NewSynonym, NodeAnnotationChange, NodeCreation,
                                 NodeDeepening, NodeDeletion, NodeMove,
                                 NodeObsoletion, NodeRename, NodeShallowing,
                                 NodeUnobsoletion, PlaceUnder, PredicateChange,
                                 RemovedNodeFromSubset, RemoveUnder, Change)


CURIE_PATTERN = re.compile(r"^(\w+):(\S+)$")


def get_prefix(curie):
    """Get prefix."""
    return curie.split(":")[0]


# TODO; JSON LD obo context look at robot
prefix_2_uri = {
    "obo": "<http://purl.obolibrary.org/obo/>",
    "ex": "<http://example.org/>",
    "oboInOwl": "<http://www.geneontology.org/formats/oboInOwl#>",
    "rdfs": "<http://www.w3.org/2000/01/rdf-schema#>",
    "xsd": "<http://www.w3.org/2001/XMLSchema#>",
    "rdf": "<http://www.w3.org/1999/02/22-rdf-syntax-ns#>",
    "owl": "<http://www.w3.org/2002/07/owl#>",
    "swrl": "<http://www.w3.org/2003/11/swrl#>",
    "oio": "<http://www.geneontology.org/formats/oboInOwl#>",
    "dce": "<http://purl.org/dc/elements/1.1/>",
    "dct": "<http://purl.org/dc/terms/>",
    "foaf": "<http://xmlns.com/foaf/0.1/>",
    "protege": "<http://protege.stanford.edu/plugins/owl/protege#>",
    "BFO": "<http://purl.obolibrary.org/obo/BFO_>",
    "CHEBI": "<http://purl.obolibrary.org/obo/CHEBI_>",
    "CL": "<http://purl.obolibrary.org/obo/CL_>",
    "IAO": "<http://purl.obolibrary.org/obo/IAO_>",
    "NCBITaxon": "<http://purl.obolibrary.org/obo/NCBITaxon_>",
    "GO": "<http://purl.obolibrary.org/obo/GO_>",
    "OBI": "<http://purl.obolibrary.org/obo/OBI_>",
    "PR": "<http://purl.obolibrary.org/obo/PR_>",
    "UP": "<http://purl.uniprot.org/uniprot/>",
    "UC": "<http://purl.uniprot.org/core/>",
    "PRO": "<http://www.uniprot.org/annotation/PRO_>",
    "faldo": "<http://biohackathon.org/resource/faldo#>",
    # TODO add more prefixes
}


def get_sparql_prefix_header(prefixes: List[str]) -> str:
    if prefixes is None:
        prefixes = ['rdfs', 'rdf']
    return "\n".join([f"PREFIX {prefix}: {prefix_2_uri[prefix]}" for prefix in prefixes])


def get_representation(node_term: str) -> Optional[str]:
    if node_term is None:
        logging.warning(f"None value for representation")
        return None
    elif node_term.startswith('<http'):
        return 'uri'
    elif ':' in node_term and CURIE_PATTERN.match(node_term):
        return 'curie'
    else:
        return 'label'


def is_label(input):
    """Check if text is label."""
    return re.match(r"\'[^ \s\'].*\'", input)


def is_id(input):
    """Check if text is id."""
    return re.match(r"<\S+>", input)


def build_curie_prefix(entity):
    """Build CURIE prefix."""
    curie_prefix = get_prefix(entity)
    curie_uri = prefix_2_uri[curie_prefix]
    return "PREFIX " + curie_prefix + ": " + curie_uri + " "


# TODO proper escape handling
def escape_literal(literal):
    """Handle escape characters."""
    return literal.replace("\\", "\\\\").replace('"', '\\"')
    # .replace("\\'", "\\\\'")


def convert(kgcl_instance: Change) -> str:
    """
    Given a KGCL dataclass, return a SPARQL UPDATE _query.

    This corresponding to the encoded change.
    """
    # label renaming
    if type(kgcl_instance) is NodeRename:
        return rename(kgcl_instance)

    # node obsoletion
    if type(kgcl_instance) is NodeObsoletion:
        representation = get_representation(kgcl_instance.about_node)
        # TODO: abstract into a single function
        if representation == "uri":
            return obsolete_by_id(kgcl_instance)
        if representation == "label":
            return obsolete_by_label(kgcl_instance)
        if representation == "curie":
            return obsolete_curie(kgcl_instance)

    # node obsoletion
    if type(kgcl_instance) is NodeUnobsoletion:
        representation = get_representation(kgcl_instance.about_node)
        # TODO: abstract into a single function
        if representation == "uri":
            return unobsolete_by_id(kgcl_instance)
        if representation == "label":
            return unobsolete_by_label(kgcl_instance)
        if representation == "curie":
            return unobsolete_curie(kgcl_instance)

    # node deletion
    if type(kgcl_instance) is NodeDeletion:
        representation = get_representation(kgcl_instance.about_node)
        # TODO: abstract into a single function
        if representation == "uri":
            return delete_by_id(kgcl_instance)
        if representation == "label":
            return delete_by_label(kgcl_instance)
        if representation == "curie":
            return delete_curie(kgcl_instance)

    # node creation
    if type(kgcl_instance) is NodeCreation:
        return create_node(kgcl_instance)

    # class creation
    if type(kgcl_instance) is ClassCreation:
        return create_class(kgcl_instance)

    # node deepending
    if type(kgcl_instance) is NodeDeepening:
        return node_deepening(kgcl_instance)

    # node shallowing
    if type(kgcl_instance) is NodeShallowing:
        return node_shallowing(kgcl_instance)

    if type(kgcl_instance) is NodeAnnotationChange:
        return node_annotation_change(kgcl_instance)

    # node move
    if type(kgcl_instance) is NodeMove:
        return node_move(kgcl_instance)

    if type(kgcl_instance) is NewSynonym:
        representation = get_representation(kgcl_instance.about_node)
        # TODO: abstract into a single function
        if representation == "uri":
            return new_synonym_for_uri(kgcl_instance)
        if representation == "label":
            return new_synonym_for_label(kgcl_instance)
        if representation == "curie":
            return new_synonym_for_curie(kgcl_instance)

    if type(kgcl_instance) is PredicateChange:
        return change_predicate(kgcl_instance)

    if type(kgcl_instance) is RemovedNodeFromSubset:
        if is_id(kgcl_instance.about_node) and is_id(kgcl_instance.subset):
            return remove_node_from_subset(kgcl_instance)

    if type(kgcl_instance) is PlaceUnder:
        return triple_creation(kgcl_instance)

    if type(kgcl_instance) is RemoveUnder:
        return triple_deletion(kgcl_instance)

    if type(kgcl_instance) is EdgeCreation:
        return create_existential_restriction(kgcl_instance)

    if type(kgcl_instance) is EdgeDeletion:
        return delete_existential_restriction(kgcl_instance)


def node_move(kgcl_instance: NodeMove) -> str:
    """Return SPARQL query to move node."""
    # NB: object and old_value are (necessarily) the same
    subject = kgcl_instance.about_edge.subject
    predicate = kgcl_instance.about_edge.predicate
    object = kgcl_instance.about_edge.object

    subject_type = get_representation(kgcl_instance.about_edge.subject)
    predicate_type = get_representation(kgcl_instance.about_edge.predicate)
    object_type = get_representation(kgcl_instance.about_edge.object)

    old_value = kgcl_instance.old_value
    new_value = kgcl_instance.new_value

    old_type = kgcl_instance.old_object_type
    new_type = kgcl_instance.new_object_type

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "
    prefix += "PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#> "

    # set up prefixes  for curies as needed
    if subject_type == "curie":
        prefix += build_curie_prefix(subject)

    if predicate_type == "curie":
        prefix += build_curie_prefix(predicate)

    if object_type == "curie":
        prefix += build_curie_prefix(object)

    if old_type == "curie":
        prefix += build_curie_prefix(old_value)

    if new_type == "curie":
        prefix += build_curie_prefix(new_value)

    delete__query = "?subject ?predicate ?old . "

    delete = "DELETE {" + delete__query + "}"

    insert__query = "?subject ?predicate ?new . "

    insert = "INSERT {" + insert__query + "}"

    where__query = ""

    if old_type == "label":
        where__query += "?old rdfs:label ?old_label . "
        where__query += ' FILTER(STR(?old_label)="' + old_value + '") '
    else:
        where__query += " BIND(" + old_value + " AS ?old) "

    if new_type == "label":
        where__query += "?new rdfs:label ?new_label . "
        where__query += ' FILTER(STR(?new_label)="' + new_value + '") '
    else:
        where__query += " BIND(" + new_value + " AS ?new) "

    if subject_type == "label":
        where__query += "?subject rdfs:label ?entity_label . "
        where__query += ' FILTER(STR(?entity_label)="' + subject + '") '
    else:
        where__query += " BIND(" + subject + " AS ?subject) "

    if predicate_type == "label":
        where__query += "?predicate rdfs:label ?predicate_label . "
        where__query += ' FILTER(STR(?predicate_label)="' + predicate + '") '
    else:
        where__query += " BIND(" + predicate + " AS ?predicate) "

    where__query += "?subject ?predicate ?old . "

    where = "WHERE {" + where__query + "}"

    update__query = prefix + " " + delete + " " + insert + " " + where

    return update__query


def remove_node_from_subset(kgcl_instance) -> str:
    """Return SPARQL query to remove node from subset."""
    about = kgcl_instance.about_node
    subset = kgcl_instance.subset

    update__query = (
        f"PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
        f"PREFIX obo: <http://purl.obolibrary.org/obo/>"
        f"DELETE {{ {about} obo:inSubset {subset} }}"
        f"WHERE {{ {about} obo:inSubset {subset} }}"
    )

    # prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  "
    # prefix += "PREFIX obo: <http://purl.obolibrary.org/obo/> "

    # delete_query = about + " obo:inSubset " + subset + " . "

    # delete = "DELETE {" + delete_query + "}"

    # where_query = about + " obo:inSubset " + subset + " . "

    # where = "WHERE { " + where_query + " }"

    # update_query = prefix + " " + delete + " " + where

    return update__query


def change_predicate(kgcl_instance) -> str:
    """Return SPARQL query to change predicate."""
    subject = kgcl_instance.about_edge.subject
    object = kgcl_instance.about_edge.object

    old_value = kgcl_instance.old_value
    new_value = kgcl_instance.new_value

    language = kgcl_instance.language
    datatype = kgcl_instance.datatype

    subject_type = get_representation(kgcl_instance.about_edge.subject)
    object_type = get_representation(kgcl_instance.about_edge.object)

    old_value_type = kgcl_instance.old_value_type
    new_value_type = kgcl_instance.new_value_type

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  "

    if subject_type == "curie":
        prefix += build_curie_prefix(subject)

    if object_type == "curie":
        prefix += build_curie_prefix(object)

    if old_value_type == "curie":
        prefix += build_curie_prefix(old_value)

    if new_value_type == "curie":
        prefix += build_curie_prefix(new_value)

    delete__query = "?subject ?old ?object . "

    delete = "DELETE {" + delete__query + "}"

    insert__query = "?subject ?new ?object . "

    insert = "INSERT {" + insert__query + "}"

    where__query = delete__query

    if subject_type == "label":
        where__query += "?subject rdfs:label ?subject_label . "
        where__query += ' FILTER(STR(?subject_label)="' + subject + '") '

    if subject_type == "uri" or subject_type == "curie":
        where__query += " BIND(" + subject + " AS ?subject) "

    if object_type == "label":
        where__query += "?object rdfs:label ?object_label . "
        where__query += ' FILTER(STR(?object_label)="' + object + '") '

    if object_type == "uri" or object_type == "curie":
        where__query += " BIND(" + object + " AS ?object) "

    if object_type == "literal":
        object = escape_literal(object)
        if datatype is not None:
            # TODO: accept CURIES for data types
            where__query += (
                ' BIND( STRDT("' + object + '",' + datatype + ") AS ?object) "
            )
        elif language is not None:
            where__query += (
                'BIND( STRLANG("' + object + '","' + language + '") AS ?object) '
            )
        else:
            where__query += 'BIND("' + object + '" AS ?object)'

    if new_value_type == "label":
        where__query += "?new rdfs:label ?new_label . "
        where__query += ' FILTER(STR(?new_label)="' + new_value + '") '
    else:
        where__query += " BIND(" + new_value + " AS ?new) "

    if old_value_type == "label":
        where__query += "?old rdfs:label ?old_label . "
        where__query += ' FILTER(STR(?old_label)="' + old_value + '") '
    else:
        where__query += " BIND(" + old_value + " AS ?old) "

    where = "WHERE {" + where__query + "}"

    update__query = prefix + " " + delete + " " + insert + " " + where

    return update__query


def node_deepening(kgcl_instance) -> str:
    """Return SPARQL query to deepen node."""
    entity = kgcl_instance.about_edge.subject
    old_value = kgcl_instance.old_value
    new_value = kgcl_instance.new_value

    entity_type = get_representation(kgcl_instance.about_edge.subject)
    old_type = kgcl_instance.old_object_type
    new_type = kgcl_instance.new_object_type

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "
    prefix += "PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#> "

    # set up prefixes  for curies as needed
    if entity_type == "curie":
        prefix += build_curie_prefix(entity)

    if old_type == "curie":
        prefix += build_curie_prefix(old_value)

    if new_type == "curie":
        prefix += build_curie_prefix(new_value)

    delete__query = "?entity ?relation ?old . "

    delete = "DELETE {" + delete__query + "}"

    insert__query = "?entity ?relation ?new . "

    insert = "INSERT {" + insert__query + "}"

    where__query = ""

    if old_type == "label":
        where__query += "?old rdfs:label ?old_label . "
        where__query += ' FILTER(STR(?old_label)="' + old_value + '") '
    else:
        where__query += " BIND(" + old_value + " AS ?old) "

    if new_type == "label":
        where__query += "?new rdfs:label ?new_label . "
        where__query += ' FILTER(STR(?new_label)="' + new_value + '") '
    else:
        where__query += " BIND(" + new_value + " AS ?new) "

    if entity_type == "label":
        where__query += "?entity rdfs:label ?entity_label . "
        where__query += ' FILTER(STR(?entity_label)="' + entity + '") '
    else:
        where__query += " BIND(" + entity + " AS ?entity) "

    where__query += "?entity ?relation ?old . "
    where__query += "?new ?relation ?old . "

    where = "WHERE {" + where__query + "}"

    update__query = prefix + " " + delete + " " + insert + " " + where

    return update__query


def node_shallowing(kgcl_instance: NodeShallowing) -> str:
    """Return SPARQL query to make node shallow."""
    entity = kgcl_instance.about_edge.subject
    old_value = kgcl_instance.old_value
    new_value = kgcl_instance.new_value

    entity_type = get_representation(kgcl_instance.about_edge.subject)
    old_type = kgcl_instance.old_object_type
    new_type = kgcl_instance.new_object_type

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "
    prefix += "PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#> "

    if entity_type == "curie":
        prefix += build_curie_prefix(entity)

    if old_type == "curie":
        prefix += build_curie_prefix(old_value)

    if new_type == "curie":
        prefix += build_curie_prefix(new_value)

    delete__query = "?entity ?relation ?old . "

    delete = "DELETE {" + delete__query + "}"

    insert__query = "?entity ?relation ?new . "

    insert = "INSERT {" + insert__query + "}"

    where__query = ""

    if old_type == "label":
        where__query += "?old rdfs:label ?old_label . "
        where__query += ' FILTER(STR(?old_label)="' + old_value + '") '
    else:
        where__query += " BIND(" + old_value + " AS ?old) "

    if new_type == "label":
        where__query += "?new rdfs:label ?new_label . "
        where__query += ' FILTER(STR(?new_label)="' + new_value + '") '
    else:
        where__query += " BIND(" + new_value + " AS ?new) "

    if entity_type == "label":
        where__query += "?entity rdfs:label ?entity_label . "
        where__query += ' FILTER(STR(?entity_label)="' + entity + '") '
    else:
        where__query += " BIND(" + entity + " AS ?entity) "

    where__query += "?entity ?relation ?old . "
    where__query += "?old ?relation ?new . "

    where = "WHERE {" + where__query + "}"

    update__query = prefix + " " + delete + " " + insert + " " + where

    return update__query


# TODO: handling of language tags
# look things up at https://www.ebi.ac.uk/ols/ontologies/iao
def unobsolete_by_id(kgcl_instance) -> str:
    """Return SPARQL query to unobsolete by id."""
    about = kgcl_instance.about_node
    # http://wiki.geneontology.org/index.php/Restoring_an_Obsolete_Ontology_Term
    # 1. remove 'obsolete' from label
    # 2. remove 'OBSOLETE' from definition
    # 3. update comment to "Note that this term was reinstated from obsolete"
    #   TODO: no we remove the previous comment?  (all comments?)
    # 4. Remove any replaced_by and consider tags
    # 5. Remove the owl:deprecated: true tag

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "
    prefix += "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> "
    prefix += "PREFIX obo: <http://purl.obolibrary.org/obo/> "
    prefix += "PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#> "

    delete__query = about + " rdfs:label ?label . "
    delete__query += about + ' owl:deprecated "true"^^xsd:boolean . '
    delete__query += about + " obo:IAO_0000115 ?unobsolete_definition . "
    delete__query += about + " obo:IAO_0100001 ?replacedBy .  "
    delete__query += about + " oboInOwl:consider ?consider . "
    delete__query += about + " rdfs:subClassOf oboInOwl:ObsoleteClass . "

    delete = "DELETE {" + delete__query + "}"

    insert__query = about + " rdfs:label ?unobsolete_label . "
    insert__query += about + " obo:IAO_0000115 ?unobsolete_definition . "
    insert__query += (
        '?entity rdfs:comment "Note that this term was reinstated from obsolete." . '
    )

    insert = "INSERT {" + insert__query + "}"

    where__query = "{ " + about + " rdfs:label ?label . "
    where__query += 'BIND(IF(STRSTARTS(?label, "obsolete "),'
    where__query += "SUBSTR(?label,10),?label) AS ?unobsolete_label ) } "
    where__query += " UNION "
    where__query += "{ " + about + " rdfs:label ?label . "
    where__query += about + " obo:IAO_0000115 ?definition . "
    where__query += 'BIND(IF(STRSTARTS(?definition, "OBSOLETE "),'
    where__query += "SUBSTR(?definition,10),?definition) AS ?unobsolete_definition ) } "
    where__query += " UNION "
    where__query += "{ " + about + " rdfs:label ?label . "
    where__query += about + " obo:IAO_0100001 ?replacedBy . } "
    where__query += " UNION "
    where__query += "{ " + about + " rdfs:label ?label . "
    where__query += about + " oboInOwl:consider ?consider . } "

    where = "WHERE {" + where__query + "}"

    update__query = prefix + " " + delete + " " + insert + " " + where

    return update__query


def unobsolete_by_label(kgcl_instance) -> str:
    """Return SPARQL query to unobsolete by label."""
    about = kgcl_instance.about_node
    # http://wiki.geneontology.org/index.php/Restoring_an_Obsolete_Ontology_Term
    # 1. remove 'obsolete' from label
    # 2. remove 'OBSOLETE' from definition
    # 3. update comment to "Note that this term was reinstated from obsolete"
    #   TODO: no we remove the previous comment?  (all comments?)
    # 4. Remove any replaced_by and consider tags
    # 5. Remove the owl:deprecated: true tag

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "
    prefix += "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> "
    prefix += "PREFIX obo: <http://purl.obolibrary.org/obo/> "
    prefix += "PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#> "

    delete__query = " ?about rdfs:label ?label . "
    delete__query += ' ?about owl:deprecated "true"^^xsd:boolean . '
    delete__query += " ?about obo:IAO_0000115 ?unobsolete_definition . "
    delete__query += " ?about obo:IAO_0100001 ?replacedBy .  "
    delete__query += " ?about oboInOwl:consider ?consider . "
    delete__query += " ?about rdfs:subClassOf oboInOwl:ObsoleteClass . "

    delete = "DELETE {" + delete__query + "}"

    insert__query = "?about rdfs:label ?unobsolete_label . "
    insert__query += "?about obo:IAO_0000115 ?unobsolete_definition . "
    insert__query += (
        '?entity rdfs:comment "Note that this term was reinstated from obsolete." . '
    )

    insert = "INSERT {" + insert__query + "}"

    where__query = "{ ?about rdfs:label ?label . "
    where__query += ' FILTER(STR(?label)="' + about + '") '
    where__query += 'BIND(IF(STRSTARTS(?label, "obsolete "),'
    where__query += "SUBSTR(?label,10),?label) AS ?unobsolete_label ) } "
    where__query += " UNION "
    where__query += "{ ?about rdfs:label ?label . "
    where__query += ' FILTER(STR(?label)="' + about + '") '
    where__query += "?about obo:IAO_0000115 ?definition . "
    where__query += 'BIND(IF(STRSTARTS(?definition, "OBSOLETE "),'
    where__query += "SUBSTR(?definition,10),?definition) AS ?unobsolete_definition ) } "
    where__query += " UNION "
    where__query += "{ ?about rdfs:label ?label . "
    where__query += ' FILTER(STR(?label)="' + about + '") '
    where__query += "?about obo:IAO_0100001 ?replacedBy . } "
    where__query += " UNION "
    where__query += "{ ?about rdfs:label ?label . "
    where__query += ' FILTER(STR(?label)="' + about + '") '
    where__query += "?about oboInOwl:consider ?consider . } "

    where = "WHERE {" + where__query + "}"

    update__query = prefix + " " + delete + " " + insert + " " + where

    return update__query


def unobsolete_curie(kgcl_instance) -> str:
    """Return SPARQL query to unobsolete a CURIE."""
    about = kgcl_instance.about_node
    # http://wiki.geneontology.org/index.php/Restoring_an_Obsolete_Ontology_Term
    # 1. remove 'obsolete' from label
    # 2. remove 'OBSOLETE' from definition
    # 3. update comment to "Note that this term was reinstated from obsolete"
    #   TODO: no we remove the previous comment?  (all comments?)
    # 4. Remove any replaced_by and consider tags
    # 5. Remove the owl:deprecated: true tag

    curie_prefix = get_prefix(about)
    curie_uri = prefix_2_uri[curie_prefix]

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "
    prefix += "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> "
    prefix += "PREFIX obo: <http://purl.obolibrary.org/obo/> "
    prefix += "PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#> "
    prefix += "PREFIX " + curie_prefix + ": " + curie_uri + " "

    delete__query = about + " rdfs:label ?label . "
    delete__query += about + ' owl:deprecated "true"^^xsd:boolean . '
    delete__query += about + " obo:IAO_0000115 ?unobsolete_definition . "
    delete__query += about + " obo:IAO_0100001 ?replacedBy .  "
    delete__query += about + " oboInOwl:consider ?consider . "
    delete__query += about + " rdfs:subClassOf oboInOwl:ObsoleteClass . "

    delete = "DELETE {" + delete__query + "}"

    insert__query = about + " rdfs:label ?unobsolete_label . "
    insert__query += about + " obo:IAO_0000115 ?unobsolete_definition . "
    insert__query += (
        '?entity rdfs:comment "Note that this term was reinstated from obsolete." . '
    )

    insert = "INSERT {" + insert__query + "}"

    where__query = "{ " + about + " rdfs:label ?label . "
    where__query += 'BIND(IF(STRSTARTS(?label, "obsolete "),'
    where__query += "SUBSTR(?label,10),?label) AS ?unobsolete_label ) } "
    where__query += " UNION "
    where__query += "{ " + about + " rdfs:label ?label . "
    where__query += about + " obo:IAO_0000115 ?definition . "
    where__query += 'BIND(IF(STRSTARTS(?definition, "OBSOLETE "),'
    where__query += "SUBSTR(?definition,10),?definition) AS ?unobsolete_definition ) } "
    where__query += " UNION "
    where__query += "{ " + about + " rdfs:label ?label . "
    where__query += about + " obo:IAO_0100001 ?replacedBy . } "
    where__query += " UNION "
    where__query += "{ " + about + " rdfs:label ?label . "
    where__query += about + " oboInOwl:consider ?consider . } "

    where = "WHERE {" + where__query + "}"

    update__query = prefix + " " + delete + " " + insert + " " + where

    return update__query


# NB this does not preserve language tags
def rename(kgcl_instance: NodeRename) -> str:
    """Return SPARQL query to rename node."""
    old_value = kgcl_instance.old_value
    new_value = kgcl_instance.new_value

    # strip label's single quotes
    old_value = old_value[1:-1]
    new_value = new_value[1:-1]

    old_language = kgcl_instance.old_language
    new_language = kgcl_instance.new_language

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"

    if kgcl_instance.about_node is None:
        subject = "?entity"
    else:
        subject = kgcl_instance.about_node
        if get_representation(kgcl_instance.about_node) == "curie":
            prefix += build_curie_prefix(subject)

    delete__query = subject + " rdfs:label ?oldlabel ."
    delete = "DELETE {" + delete__query + "}"

    insert_query = subject + " rdfs:label ?newlabel ."
    insert = "INSERT {" + insert_query + "}"

    where_query = subject + " rdfs:label ?label .  "
    where_query += ' FILTER(STR(?label)="' + old_value + '") '

    if old_language is None:
        where_query += ' BIND("' + old_value + '" AS ?oldlabel) '
    else:
        where_query += ' FILTER(LANG(?label) ="' + old_language + '")'
        where_query += (
            ' BIND( STRLANG("' + old_value + '","' + old_language + '") AS ?oldlabel) '
        )

    if new_language is None:
        where_query += ' BIND("' + new_value + '" AS ?newlabel) '
    else:
        where_query += (
            ' BIND( STRLANG("' + new_value + '","' + new_language + '") AS ?newlabel) '
        )

    where = "WHERE {" + where_query + "}"

    update_query = prefix + " " + delete + " " + insert + " " + where

    return update_query


# TODO: this implementation is buggy
# this implementation should preserve language tags
# note that this cannot be used for diffing
def rename_preserve(kgcl_instance) -> str:
    """Return SPARQL query to rename node but preserve language tags."""
    old_value = kgcl_instance.old_value
    new_value = kgcl_instance.new_value
    old_value = old_value.replace("'", "")
    old_language = kgcl_instance.old_language
    new_language = kgcl_instance.new_language

    # initialise subject
    if kgcl_instance.about_node is None:
        subject = "?entity"
    else:
        subject = kgcl_instance.about_node

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
    delete_query = subject + " rdfs:label ?tag ."
    delete = "DELETE {" + delete_query + "}"

    insert_query = subject + " rdfs:label ?tag ."
    insert = "INSERT {" + insert_query + "}"

    where_query = subject + " rdfs:label ?label .  "
    where_query += " BIND( LANG(?label) AS ?language)  "
    where_query += ' FILTER(STR(?label)="' + old_value + '") '

    # if old_Language tag is specified
    # then, we need to filter results according to the specified language tag
    if old_language is not None:
        where_query += ' FILTER(LANG(?label) ="' + old_language + '")'

    # if new_language tag is specifed, then
    # we need to add this tag to insert _query
    if new_language is None:
        where_query += " BIND( STRLANG(" + new_value + ",?language) AS ?tag) "
    else:
        where_query += (
            " BIND( STRLANG(" + new_value + ',"' + new_language + '") AS ?tag) '
        )

    where = "WHERE {" + where_query + "}"

    update_query = prefix + " " + delete + " " + insert + " " + where

    return update_query


def delete_by_id(kgcl_instance) -> str:
    """Return SPARQL query to delete node by id."""
    about = kgcl_instance.about_node  # this needs to be an ID - not a label

    delete_query = (
        "?s1 ?p1 " + about + " . "
    )  # this does not delete triples with blank nodes
    delete_query += "?s2 " + about + " ?o1 . "
    delete_query += "?s2 " + about + " ?o1 . "
    delete_query += about + " ?p2 ?o2 . "

    delete = "DELETE {" + delete_query + "}"

    where_query = "{ ?s1 ?p1 " + about + " . } "
    where_query += " UNION "
    where_query = "{ ?s2 " + about + " ?o1 . } "
    where_query += " UNION "
    where_query += "{ " + about + " ?p2 ?o2 . } "

    where = "WHERE {" + where_query + "}"

    update_query = delete + " " + where

    return update_query


def delete_curie(kgcl_instance) -> str:
    """Return SPARQL query to delete CURIE."""
    about = kgcl_instance.about_node

    prefix = build_curie_prefix(about)

    # this does not delete triples with blank nodes
    delete_query = "?s1 ?p1 " + about + " . "
    delete_query += "?s2 " + about + " ?o1 . "
    delete_query += about + " ?p2 ?o2 . "

    delete = "DELETE {" + delete_query + "}"

    where_query = "{ ?s1 ?p1 " + about + " . } "
    where_query += " UNION "
    where_query = "{ ?s2 " + about + " ?o1 . } "
    where_query += " UNION "
    where_query += "{ " + about + " ?p2 ?o2 . } "

    where = "WHERE {" + where_query + "}"

    update_query = prefix + " " + delete + " " + where

    return update_query


def delete_by_label(kgcl_instance) -> str:
    """Return SPARQL query to delete by label."""
    about = kgcl_instance.about_node

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"

    delete_query = "?s1 rdfs:label ?label . "
    delete_query += "?s1 ?p2 ?o1 . "

    delete = "DELETE {" + delete_query + "}"

    where_query = "?s1 rdfs:label ?label . "
    where_query += "?s1 ?p2 ?o1 . "
    where_query += ' FILTER(STR(?label)="' + about + '") '  # ignore language tags

    where = "WHERE {" + where_query + "}"

    update_query = prefix + " " + delete + " " + where

    return update_query


def create_class(kgcl_instance: ClassCreation) -> str:
    """Return SPARQL query to create a class."""
    term_id = kgcl_instance.node_id
    id_type = get_representation(kgcl_instance.node_id)

    prefix = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "

    if id_type == "curie":
        prefix += build_curie_prefix(term_id)

    insert_query = term_id + " rdf:type owl:Class  . "
    insert = "INSERT {" + insert_query + "}"
    where = "WHERE {}"

    update_query = prefix + " " + insert + " " + where

    return update_query


def create_node(kgcl_instance) -> str:
    """Return SPARQL query to create a node."""
    term_id = kgcl_instance.node_id
    label = kgcl_instance.name
    language = kgcl_instance.language
    id_type = get_representation(kgcl_instance.about_node)

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  "

    if id_type == "curie":
        prefix += build_curie_prefix(term_id)

    if language is None:
        insert_query = term_id + " rdfs:label " + label + "  . "
    else:
        insert_query = term_id + " rdfs:label ?tag  . "

    insert = "INSERT {" + insert_query + "}"

    if language is None:
        where = "WHERE {}"
    else:
        where_query = " BIND( STRLANG(" + label + ',"' + language + '") AS ?tag) '
        where = "WHERE {" + where_query + "}"

    update_query = prefix + " " + insert + " " + where

    return update_query


def node_annotation_change(kgcl_instance) -> str:
    """Return SPARQL query to change node annotation."""
    subject = kgcl_instance.about_node
    predicate = kgcl_instance.annotation_property
    old_object = kgcl_instance.old_value
    new_object = kgcl_instance.new_value

    subject_type = get_representation(kgcl_instance.about_node)
    predicate_type = kgcl_instance.annotation_property_type
    old_type = kgcl_instance.old_value_type
    new_type = kgcl_instance.new_value_type

    # TODO: allow language tags and datattypes for
    # both the old and new annotation value
    old_language = kgcl_instance.old_language
    new_language = kgcl_instance.new_language
    old_datatype = kgcl_instance.old_datatype
    new_datatype = kgcl_instance.new_datatype

    prefix = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "

    if subject_type == "curie":
        prefix += build_curie_prefix(subject)

    if predicate_type == "curie":
        prefix += build_curie_prefix(predicate)

    if old_type == "curie":
        prefix += build_curie_prefix(old_object)

    if new_type == "curie":
        prefix += build_curie_prefix(new_object)

        # todo: delete _query
    delete_query = "?subject ?predicate ?old_object . "

    delete = "DELETE {" + delete_query + "}"

    insert_query = "?subject ?predicate ?new_object . "

    insert = "INSERT {" + insert_query + "}"

    where_query = ""
    if subject_type == "label":
        where_query += "?subject rdfs:label ?subject_label . "
        where_query += ' FILTER(STR(?subject_label)="' + subject + '") '
    else:
        where_query += " BIND(" + subject + " AS ?subject)"

    if predicate_type == "label":
        where_query += "?predicate rdfs:label ?predicate_label . "
        where_query += ' FILTER(STR(?predicate_label)="' + predicate + '") '
    else:
        where_query += "?predicate rdf:type owl:AnnotationProperty . "
        where_query += " BIND(" + predicate + " AS ?predicate)"

    if old_type == "label":
        where_query += "?old_object rdfs:label ?old_object_label . "
        where_query += ' FILTER(STR(?old_object_label)="' + old_object + '") '

    if old_type == "uri" or old_type == "curie":
        where_query += " BIND(" + old_object + " AS ?old_object) "

    if old_type == "literal":
        old_object = escape_literal(old_object)
        if old_datatype is not None:
            where_query += (
                ' BIND(STRDT("'
                + old_object
                + '",'
                + old_datatype
                + ") AS ?old_object) "
            )
        elif old_language is not None:
            where_query += (
                ' BIND(STRLANG("'
                + old_object
                + '","'
                + old_language
                + '") AS ?old_object) '
            )
        else:
            where_query += ' BIND("' + old_object + '" AS ?old_object)'

    if new_type == "label":
        where_query += "?new_object rdfs:label ?new_object_label . "
        where_query += ' FILTER(STR(?new_object_label)="' + new_object + '") '

    if new_type == "uri" or old_type == "curie":
        where_query += " BIND(" + new_object + " AS ?new_object) "

    if new_type == "literal":
        new_object = escape_literal(new_object)
        if new_datatype is not None:
            where_query += (
                ' BIND(STRDT("'
                + new_object
                + '",'
                + new_datatype
                + ") AS ?new_object) "
            )
        elif new_language is not None:
            where_query += (
                ' BIND(STRLANG("'
                + new_object
                + '","'
                + new_language
                + '") AS ?new_object) '
            )
        else:
            where_query += ' BIND("' + new_object + '" AS ?new_object)'

    where = "WHERE { " + where_query + " }"

    update_query = prefix + " " + delete + " " + insert + " " + where

    return update_query


def edge_annotation_creation(kgcl_instance) -> str:
    """Return SPARQL query to change edge annotation."""
    subject = kgcl_instance.subject
    predicate = kgcl_instance.predicate
    object = kgcl_instance.object

    subject_type = kgcl_instance.subject_type
    predicate_type = kgcl_instance.predicate_type
    object_type = kgcl_instance.object_type

    annotation = kgcl_instance.annotation_set

    # annotation.property_type
    # annotation.filler_type

    prefix = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "

    if subject_type == "curie":
        prefix += build_curie_prefix(subject)

    if predicate_type == "curie":
        prefix += build_curie_prefix(predicate)

    if object_type == "curie":
        prefix += build_curie_prefix(object)

    if annotation.property_type == "curie":
        prefix += build_curie_prefix(annotation.property)

    if annotation.filler_type == "curie":
        prefix += build_curie_prefix(annotation.filler)

    insert_query = "?bnode owl:annotatedSource ?subject . "
    insert_query += "?bnode owl:annotatedProperty ?predicate . "
    insert_query += "?bnode owl:annotatedTarget ?object . "
    insert_query += "?bnode ?annotation_property ?filler . "
    insert_query += "?bnode rdf:type owl:Axiom ."
    insert = "INSERT {" + insert_query + "}"

    where_query = ' BIND(BNODE("reification") AS ?bnode) '
    if subject_type == "label":
        where_query += "?subject rdfs:label ?subject_label . "
        where_query += ' FILTER(STR(?subject_label)="' + subject + '") '
    else:
        where_query += "BIND(" + subject + " AS ?subject) "

    if predicate_type == "label":
        where_query += "?predicate rdfs:label ?predicate_label . "
        where_query += ' FILTER(STR(?predicate_label)="' + predicate + '") '
    else:
        where_query += "BIND(" + predicate + " AS ?predicate) "

    if annotation.property_type == "label":
        where_query += "?annotation_property rdfs:label ?ap_label . "
        where_query += ' FILTER(STR(?ap_label)="' + annotation.property + '") '
    else:
        where_query += "BIND(" + annotation.property + " AS ?annotation_property) "

    if annotation.filler_type == "label":
        where_query += "?filler rdfs:label ?filler_label . "
        where_query += ' FILTER(STR(?filler_label)="' + annotation.filler + '") '

    if annotation.filler_type == "literal":
        where_query += 'BIND("' + escape_literal(annotation.filler) + '" AS ?filler) '

    if annotation.filler_type == "uri" or annotation.filler_type == "curie":
        where_query += "BIND(" + annotation.filler + " AS ?filler) "

    if object_type == "label":
        where_query += "?object rdfs:label ?object_label . "
        where_query += ' FILTER(STR(?object_label)="' + object + '") '

    if object_type == "literal":
        where_query += 'BIND("' + escape_literal(object) + '" AS ?object) '

    if object_type == "uri" or object_type == "curie":
        where_query += "BIND(" + object + " AS ?object) "

    where = "WHERE {" + where_query + "}"

    update_query = prefix + " " + insert + " " + where

    return update_query


def triple_creation(kgcl_instance) -> str:
    """Return SPARQL query to create a triple."""
    subject = kgcl_instance.subject
    predicate = kgcl_instance.predicate
    object = kgcl_instance.object

    subject_type = kgcl_instance.subject_type
    predicate_type = kgcl_instance.predicate_type
    object_type = kgcl_instance.object_type

    language = kgcl_instance.language
    datatype = kgcl_instance.datatype  # TODO: currently only accepting full IRIs

    prefix = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "

    if subject_type == "curie":
        prefix += build_curie_prefix(subject)

    if predicate_type == "curie":
        prefix += build_curie_prefix(predicate)

    if object_type == "curie":
        prefix += build_curie_prefix(object)

    insert_query = "?subject ?predicate ?object . "

    insert = "INSERT {" + insert_query + "}"

    where_query = ""
    if subject_type == "label":
        where_query += "?subject rdfs:label ?subject_label . "
        where_query += ' FILTER(STR(?subject_label)="' + subject + '") '
    else:
        where_query += " BIND(" + subject + " AS ?subject)"

    if predicate_type == "label":
        where_query += "?predicate rdfs:label ?predicate_label . "
        where_query += ' FILTER(STR(?predicate_label)="' + predicate + '") '
    else:
        where_query += " BIND(" + predicate + " AS ?predicate)"

    if object_type == "label":
        where_query += "?object rdfs:label ?object_label . "
        where_query += ' FILTER(STR(?object_label)="' + object + '") '

    if object_type == "uri" or object_type == "curie":
        where_query += " BIND(" + object + " AS ?object) "

    if object_type == "literal":
        object = escape_literal(object)
        if datatype is not None:
            where_query += ' BIND(STRDT("' + object + '",' + datatype + ") AS ?object) "
        elif language is not None:
            where_query += (
                ' BIND(STRLANG("' + object + '","' + language + '") AS ?object) '
            )
        else:
            where_query += ' BIND("' + object + '" AS ?object)'

    where = "WHERE { " + where_query + " }"

    update_query = prefix + " " + insert + " " + where

    return update_query


# TODO: language tags + data types
def edge_annotation_deletion(kgcl_instance) -> str:
    """Return SPARQL query to annotate an edge deletion."""
    subject = kgcl_instance.subject
    predicate = kgcl_instance.predicate
    object = kgcl_instance.object

    subject_type = kgcl_instance.subject_type
    predicate_type = kgcl_instance.predicate_type
    object_type = kgcl_instance.object_type

    annotation = kgcl_instance.annotation_set

    # NB: we need to distinguish between two cases
    # (a) the entire reification needs to be deleted
    # (b) only one annotation triple is deleted
    #     while the reification is not because it's
    #     needed for other annotations

    # TODO: example

    # _query for (a)
    # A reification for a single annotations will consist of 5 triples.
    # So, we use this size bound to determine whether we need to
    # delete the entire reification or not
    prefix = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "

    if subject_type == "curie":
        prefix += build_curie_prefix(subject)

    if predicate_type == "curie":
        prefix += build_curie_prefix(predicate)

    if object_type == "curie":
        prefix += build_curie_prefix(object)

    if annotation.property_type == "curie":
        prefix += build_curie_prefix(annotation.property)

    if annotation.filler_type == "curie":
        prefix += build_curie_prefix(annotation.filler)

    insert = "INSERT { }"

    delete_query = "?bnode owl:annotatedSource ?subject  . "
    delete_query += "?bnode owl:annotatedProperty ?predicate . "
    delete_query += "?bnode owl:annotatedTarget ?object . "
    delete_query += "?bnode ?annotation_property ?filler . "
    delete_query += "?bnode rdf:type owl:Axiom ."

    delete = "DELETE {" + delete_query + "}"

    where_query = "SELECT ?bnode ?subject ?predicate ?object ?filler ?annotation_property WHERE { "
    where_query += "?bnode ?ap ?p . "
    where_query += "?bnode owl:annotatedSource ?subject .  "

    if subject_type == "label":
        where_query += "?subject rdfs:label ?subject_label . "
        where_query += ' FILTER(STR(?subject_label)="' + subject + '") '
    else:
        where_query += "BIND(" + subject + " AS ?subject) "

    if annotation.property_type == "label":
        where_query += "?annotation_property rdfs:label ?ap_label . "
        where_query += ' FILTER(STR(?ap_label)="' + annotation.property + '") '
    else:
        where_query += "BIND(" + annotation.property + " AS ?annotation_property) "

    if predicate_type == "label":
        where_query += "?predicate rdfs:label ?predicate_label . "
        where_query += ' FILTER(STR(?predicate_label)="' + predicate + '") '
    else:
        where_query += "BIND(" + predicate + " AS ?predicate) "

    if annotation.filler_type == "label":
        where_query += "?filler rdfs:label ?filler_label . "
        where_query += ' FILTER(STR(?filler_label)="' + annotation.filler + '") '

    if annotation.filler_type == "uri" or annotation.filler_type == "curie":
        where_query += "BIND(" + annotation.filler + " AS ?filler) "

    if annotation.filler_type == "literal":
        where_query += 'BIND("' + escape_literal(annotation.filler) + '" AS ?filler) '

    if object_type == "label":
        where_query += "?object rdfs:label ?object_label . "
        where_query += ' FILTER(STR(?object_label)="' + object + '") '

    if object_type == "literal":
        where_query += 'BIND("' + escape_literal(object) + '" AS ?object) '

    if object_type == "uri" or object_type == "curie":
        where_query += "BIND(" + object + " AS ?object)  "

    where_query += "} "
    where_query += "HAVING((COUNT(?ap) <= 5) && (COUNT(?p) <= 5)) "

    where = "WHERE {" + where_query + "}"

    sub_query1 = prefix + " " + delete + " " + insert + " " + where

    # _query for (b)
    delete_query = "?bnode ?annotation_property ?filler . "
    delete = "DELETE {" + delete_query + "}"

    where_query = "SELECT ?bnode ?subject ?object ?annotation_property ?filler WHERE {"
    where_query += "?bnode ?ap ?p . "
    where_query += "?bnode owl:annotatedSource ?subject .  "

    if subject_type == "label":
        where_query += "?subject rdfs:label ?subject_label . "
        where_query += ' FILTER(STR(?subject_label)="' + subject + '") '
    else:
        where_query += "BIND(" + subject + " AS ?subject) "

    if annotation.property_type == "label":
        where_query += "?annotation_property rdfs:label ?ap_label . "
        where_query += ' FILTER(STR(?ap_label)="' + annotation.property + '") '
    else:
        where_query += "BIND(" + annotation.property + " AS ?annotation_property) "

    if annotation.filler_type == "label":
        where_query += "?filler rdfs:label ?filler_label . "
        where_query += ' FILTER(STR(?filler_label)="' + annotation.filler + '") '

    if annotation.filler_type == "uri" or annotation.filler_type == "curie":
        where_query += "BIND(" + annotation.filler + " AS ?filler) "
    if annotation.filler_type == "literal":
        where_query += 'BIND("' + escape_literal(annotation.filler) + '" AS ?filler) '

    if object_type == "label":
        where_query += "?object rdfs:label ?object_label . "
        where_query += ' FILTER(STR(?object_label)="' + object + '") '

    if object_type == "literal":
        where_query += 'BIND("' + escape_literal(object) + '" AS ?object) '

    if object_type == "uri" or object_type == "curie":
        where_query += "BIND(" + object + " AS ?object)  "

    where_query += "} "
    where_query += "HAVING((COUNT(?ap) > 5) || (COUNT(?ap) > 5)) "

    where = "WHERE {" + where_query + "}"

    sub_query2 = prefix + " " + delete + " " + insert + " " + where

    # putting (a) and (b) together
    update_query = sub_query1 + " ; " + sub_query2

    return update_query


def triple_deletion(kgcl_instance) -> str:
    """Return SPARQL query to delete a triple."""
    subject = kgcl_instance.subject
    predicate = kgcl_instance.predicate
    object = kgcl_instance.object

    subject_type = kgcl_instance.subject_type
    predicate_type = kgcl_instance.predicate_type
    object_type = kgcl_instance.object_type

    language = kgcl_instance.language
    datatype = kgcl_instance.datatype

    prefix = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "

    if subject_type == "curie":
        prefix += build_curie_prefix(subject)

    if predicate_type == "curie":
        prefix += build_curie_prefix(predicate)

    if object_type == "curie":
        prefix += build_curie_prefix(object)

    delete_query = "?subject ?predicate ?object . "
    delete = "DELETE {" + delete_query + "}"

    where_query = ""

    where_query = ""
    if subject_type == "label":
        where_query += "?subject rdfs:label ?object_label . "
        where_query += ' FILTER(STR(?object_label)="' + subject + '") '
    else:
        where_query += "BIND(" + subject + " AS ?subject)"

    if predicate_type == "label":
        where_query += "?predicate rdfs:label ?predicate_label . "
        where_query += ' FILTER(STR(?predicate_label)="' + predicate + '") '
    else:
        where_query += "BIND(" + predicate + " AS ?predicate)"

    if object_type == "label":
        where_query += "?object rdfs:label ?object_label . "
        where_query += ' FILTER(STR(?object_label)="' + object + '") '

    if object_type == "uri" or object_type == "curie":
        where_query += " BIND(" + object + " AS ?object) "

    if object_type == "literal":
        object = escape_literal(object)
        if datatype is not None:
            where_query += (
                ' BIND( STRDT("' + object + '",' + datatype + ") AS ?object) "
            )
        elif language is not None:
            where_query += (
                'BIND( STRLANG("' + object + '","' + language + '") AS ?object) '
            )
        else:
            where_query += 'BIND("' + object + '" AS ?object)'

    where = "WHERE { " + where_query + " }"

    update_query = prefix + " " + delete + " " + where

    return update_query


def obsolete_by_id(kgcl_instance) -> str:
    """Return SPARQL query to obsolete by id."""
    about = kgcl_instance.about_node
    replacement = kgcl_instance.has_direct_replacement

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "
    prefix += "PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#> "
    prefix += "PREFIX obo: <http://purl.obolibrary.org/obo/> "
    prefix += "PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#> "

    delete_query = about + "rdfs:label ?label . "
    delete_query += about + " rdfs:subClassOf ?superclass . "
    delete_query += about + " owl:equivalentClass ?rhs . "
    delete_query += "?lhs owl:equivalentClass " + about + " ."

    delete = "DELETE {" + delete_query + "}"

    insert_query = "?entity rdfs:label ?tag . "
    insert_query += about + ' owl:deprecated "true"^^xsd:boolean . '
    insert_query += "?entity rdfs:subClassOf oboInOwl:ObsoleteClass . "

    if kgcl_instance.has_direct_replacement is not None:
        insert_query += about + " obo:IAO_0100001 " + replacement + "  .  "

    insert = "INSERT {" + insert_query + "}"

    where_query = "{ " + about + " rdfs:subClassOf ?superclass . } "
    where_query += " UNION "
    where_query += "{ " + about + " owl:equivalentClass ?rhs . } "
    where_query += " UNION "
    where_query += "{ ?lhs owl:equivalentClass " + about + " . } "
    where_query += " UNION "
    where_query += "{ ?entity rdfs:label ?label . "
    where_query += ' BIND(CONCAT("obsolete ", ?label) AS ?obsolete_label )  '
    where_query += " BIND( LANG(?label) AS ?language)  "
    where_query += " BIND( STRLANG(?obsolete_label,?language) AS ?tag) }  "

    where = "WHERE {" + where_query + "}"

    update_query = prefix + " " + delete + " " + insert + " " + where
    return update_query


def obsolete_by_label(kgcl_instance) -> str:
    """Return SPARQL query to obsolete by label."""
    about = kgcl_instance.about_node

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "
    prefix += "PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#> "
    prefix += "PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#> "

    delete_query = "?entity rdfs:label ?label . "
    delete_query += "?entity rdfs:subClassOf ?superclass . "
    delete_query += "?entity owl:equivalentClass ?rhs . "
    delete_query += "?lhs owl:equivalentClass ?entity . "

    delete = "DELETE {" + delete_query + "}"

    # inner_label = about.replace("'", "")
    obsolete_label = "obsolete " + about

    insert_query = "?entity rdfs:label ?tag . "
    insert_query += '?entity owl:deprecated "true"^^xsd:boolean . '
    insert_query += "?entity rdfs:subClassOf oboInOwl:ObsoleteClass . "

    insert = "INSERT {" + insert_query + "}"

    # TODO: handle the special case where only a label is present
    # (in that case we need to _query for a single triple)
    where_query = "{ ?entity rdfs:label ?label .  "
    where_query += " ?entity rdfs:subClassOf ?superclass .  "
    where_query += " BIND( LANG(?label) AS ?language)  "
    where_query += ' BIND( STRLANG("' + obsolete_label + '",?language) AS ?tag)  '
    where_query += ' FILTER(STR(?label)="' + about + '") } '

    where_query += " UNION "

    where_query += "{ ?entity rdfs:label ?label .  "
    where_query += " ?entity owl:equivalentClass ?rhs . "
    where_query += " BIND( LANG(?label) AS ?language) "
    where_query += ' BIND( STRLANG("' + obsolete_label + '",?language) AS ?tag)  '
    where_query += ' FILTER(STR(?label)="' + about + '") } '

    where_query += " UNION "

    where_query += "{ ?entity rdfs:label ?label .  "
    where_query += " ?lhs owl:equivalentClass ?entity . "
    where_query += " BIND( LANG(?label) AS ?language) "
    where_query += ' BIND( STRLANG("' + obsolete_label + '",?language) AS ?tag)  '
    where_query += ' FILTER(STR(?label)="' + about + '") } '

    where_query += " UNION "

    where_query += "{ ?entity rdfs:label ?label .  "
    where_query += " ?entity rdf:type ?type .  "
    where_query += " BIND( LANG(?label) AS ?language) "
    where_query += ' BIND( STRLANG("' + obsolete_label + '",?language) AS ?tag)  '
    where_query += ' FILTER(STR(?label)="' + about + '") } '

    where = "WHERE {" + where_query + "}"

    update_query = prefix + " " + delete + " " + insert + " " + where

    return update_query


def obsolete_curie(kgcl_instance) -> str:
    """Return SPARQL query to obsolete a CURIE."""
    about = kgcl_instance.about_node
    replacement = kgcl_instance.has_direct_replacement

    curie_prefix = get_prefix(about)
    curie_uri = prefix_2_uri[curie_prefix]

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "
    prefix += "PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#> "
    prefix += "PREFIX obo: <http://purl.obolibrary.org/obo/> "
    prefix += "PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#> "
    prefix += "PREFIX " + curie_prefix + ": " + curie_uri + " "

    delete_query = about + " rdfs:label ?label . "
    delete_query += about + " rdfs:subClassOf ?superclass . "
    delete_query += about + " owl:equivalentClass ?rhs . "
    delete_query += "?lhs owl:equivalentClass " + about + " ."

    delete = "DELETE {" + delete_query + "}"

    insert_query = "?entity rdfs:label ?tag . "
    insert_query += about + ' owl:deprecated "true"^^xsd:boolean . '
    insert_query += "?entity rdfs:subClassOf oboInOwl:ObsoleteClass . "

    if kgcl_instance.has_direct_replacement is not None:
        insert_query += about + " obo:IAO_0100001 " + replacement + "  .  "

    insert = "INSERT {" + insert_query + "}"

    where_query = "{ " + about + " rdfs:subClassOf ?superclass . } "
    where_query += " UNION "
    where_query += "{ " + about + " owl:equivalentClass ?rhs . } "
    where_query += " UNION "
    where_query += "{ ?lhs owl:equivalentClass " + about + " . } "
    where_query += " UNION "
    where_query += "{ ?entity rdfs:label ?label . "
    where_query += ' BIND(CONCAT("obsolete ", ?label) AS ?obsolete_label )  '
    where_query += " BIND( LANG(?label) AS ?language)  "
    where_query += " BIND( STRLANG(?obsolete_label,?language) AS ?tag) }  "

    where = "WHERE {" + where_query + "}"

    update_query = prefix + " " + delete + " " + insert + " " + where

    return update_query


def new_synonym_for_uri(kgcl_instance) -> str:
    """Return SPARQL query to create a new synonym for URI."""
    about = kgcl_instance.about_node
    synonym = kgcl_instance.new_value
    language = kgcl_instance.language
    qualifier = kgcl_instance.qualifier

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "
    prefix += "PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#> "
    prefix += "PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#> "

    if qualifier is None:
        insert_query = about + " oboInOwl:hasSynonym "  # + synonym + " . "
    if qualifier == "exact":
        insert_query = about + " oboInOwl:hasExactSynonym "  # + synonym + " . "
    if qualifier == "narrow":
        insert_query = about + " oboInOwl:hasNarrowSynonym "  # + synonym + " . "
    if qualifier == "broad":
        insert_query = about + " oboInOwl:hasBroadSynonym "  # + synonym + " . "
    if qualifier == "related":
        insert_query = about + " oboInOwl:hasRelatedSynonym "  # + synonym + " . "

    where_query = ""
    if language is None:
        insert_query += '"' + synonym + '" .'
    else:
        insert_query += "?tag ."
        where_query = ' BIND( STRLANG("' + synonym + '","' + language + '") AS ?tag) '

    insert = "INSERT {" + insert_query + "}"
    where = "WHERE {" + where_query + "}"

    update_query = prefix + " " + insert + " " + where

    return update_query


def new_synonym_for_label(kgcl_instance) -> str:
    """Return SPARQL query to create a new synonym for a label."""
    about = kgcl_instance.about_node  # this is a label for a node
    synonym = kgcl_instance.new_value
    language = kgcl_instance.language
    qualifier = kgcl_instance.qualifier

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "
    prefix += "PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#> "
    prefix += "PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#> "

    if qualifier is None:
        insert_query = "?about oboInOwl:hasSynonym "  # + synonym + " . "
    if qualifier == "exact":
        insert_query = "?about oboInOwl:hasExactSynonym "  # + synonym + " . "
    if qualifier == "narrow":
        insert_query = "?about oboInOwl:hasNarrowSynonym "  # + synonym + " . "
    if qualifier == "broad":
        insert_query = "?about oboInOwl:hasBroadSynonym "  # + synonym + " . "
    if qualifier == "related":
        insert_query = "?about oboInOwl:hasRelatedSynonym "  # + synonym + " . "

    # this ignores language tags
    where_query = " ?about rdfs:label ?label . "
    where_query += ' FILTER(STR(?label)="' + about + '") '

    if language is None:
        insert_query += '"' + synonym + '" .'
    else:
        insert_query += "?tag ."
        where_query += ' BIND( STRLANG("' + synonym + '","' + language + '") AS ?tag) '

    insert = "INSERT {" + insert_query + "}"
    where = "WHERE {" + where_query + "}"

    update_query = prefix + " " + insert + " " + where

    return update_query


def new_synonym_for_curie(kgcl_instance) -> str:
    """Return SPARQL query to create a new synonym for a CURIE."""
    about = kgcl_instance.about_node  # this is a curie
    synonym = kgcl_instance.new_value
    language = kgcl_instance.language
    qualifier = kgcl_instance.qualifier

    curie_prefix = get_prefix(about)
    curie_uri = prefix_2_uri[curie_prefix]

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "
    prefix += "PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#> "
    prefix += "PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#> "
    prefix += "PREFIX " + curie_prefix + ": " + curie_uri + " "

    if qualifier is None:
        insert_query = about + " oboInOwl:hasSynonym "  # + synonym + " . "
    if qualifier == "exact":
        insert_query = about + " oboInOwl:hasExactSynonym "  # + synonym + " . "
    if qualifier == "narrow":
        insert_query = about + " oboInOwl:hasNarrowSynonym "  # + synonym + " . "
    if qualifier == "broad":
        insert_query = about + " oboInOwl:hasBroadSynonym "  # + synonym + " . "
    if qualifier == "related":
        insert_query = about + " oboInOwl:hasRelatedSynonym "  # + synonym + " . "

    where_query = ""
    if language is None:
        insert_query += '"' + synonym + '" .'
    else:
        insert_query += "?tag ."
        where_query += ' BIND( STRLANG("' + synonym + '","' + language + '") AS ?tag) '

    insert = "INSERT {" + insert_query + "}"
    where = "WHERE {" + where_query + "}"

    update_query = prefix + " " + insert + " " + where

    return update_query


def create_existential_restriction(kgcl_instance) -> str:
    """Return SPARQL query to create existential restriction."""
    subclass = kgcl_instance.subject
    property = kgcl_instance.predicate
    filler = kgcl_instance.object

    subclass_type = kgcl_instance.subject_type
    property_type = kgcl_instance.predicate_type
    filler_type = kgcl_instance.object_type

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "
    prefix += "PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#> "

    if subclass_type == "curie":
        prefix += build_curie_prefix(subclass)
    if property_type == "curie":
        prefix += build_curie_prefix(property)
    if filler_type == "curie":
        prefix += build_curie_prefix(filler)

    insert_query = "?subclass rdfs:subClassOf ?bnode . "
    insert_query += "?bnode owl:someValuesFrom ?filler . "
    insert_query += "?bnode owl:onProperty ?property . "
    insert_query += "?bnode rdf:type owl:Restriction ."

    insert = "INSERT {" + insert_query + "}"

    where_query = ""
    if subclass_type == "label":
        where_query += "?subclass rdfs:label ?subclass_label . "
        where_query += ' FILTER(STR(?subclass_label)="' + subclass + '") '
    else:
        where_query += " BIND(" + subclass + " AS ?subclass) "

    if property_type == "label":
        where_query += "?property rdfs:label ?property_label . "
        where_query += ' FILTER(STR(?property_label)="' + property + '") '
    else:
        where_query += " BIND(" + property + " AS ?property) "

    if filler_type == "label":
        where_query += "?filler rdfs:label ?filler_label . "
        where_query += ' FILTER(STR(?filler_label)="' + filler + '") '
    else:
        where_query += " BIND(" + filler + " AS ?filler) "

    where_query += ' BIND(BNODE("existential") AS ?bnode) '
    where = "WHERE {" + where_query + "}"

    update_query = prefix + " " + insert + " " + where

    return update_query


def delete_existential_restriction(kgcl_instance) -> str:
    """Return SPARQL query to delete existential restriction."""
    subclass = kgcl_instance.subject
    property = kgcl_instance.predicate
    filler = kgcl_instance.object

    subclass_type = kgcl_instance.subject_type
    property_type = kgcl_instance.predicate_type
    filler_type = kgcl_instance.object_type

    prefix = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  "
    prefix += "PREFIX owl: <http://www.w3.org/2002/07/owl#>  "
    prefix += "PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#> "
    prefix += "PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#> "

    if subclass_type == "curie":
        prefix += build_curie_prefix(subclass)
    if property_type == "curie":
        prefix += build_curie_prefix(property)
    if filler_type == "curie":
        prefix += build_curie_prefix(filler)

    delete_query = "?subclass rdfs:subClassOf ?bnode . "
    delete_query += "?bnode owl:someValuesFrom ?filler . "
    delete_query += "?bnode owl:onProperty ?property . "
    delete_query += "?bnode rdf:type owl:Restriction ."

    delete = "DELETE {" + delete_query + "}"

    where_query = delete_query

    if subclass_type == "label":
        where_query += "?subclass rdfs:label ?subclass_label . "
        where_query += ' FILTER(STR(?subclass_label)="' + subclass + '") '
    else:
        where_query += " BIND(" + subclass + " AS ?subclass) "

    if property_type == "label":
        where_query += "?property rdfs:label ?property_label . "
        where_query += ' FILTER(STR(?property_label)="' + property + '") '
    else:
        where_query += " BIND(" + property + " AS ?property) "

    if filler_type == "label":
        where_query += "?filler rdfs:label ?filler_label . "
        where_query += ' FILTER(STR(?filler_label)="' + filler + '") '
    else:
        where_query += " BIND(" + filler + " AS ?filler) "

    where = "WHERE {" + where_query + "}"

    update_query = prefix + " " + delete + " " + where

    return update_query
