"""Convenience wrappers around linkml runtime.

Needed for doing basic conversion between objects and serialization formats.
The top level class is a Session object
Some of this will become unnecessary in the future
"""

import json
import logging
import re
from typing import Any, Dict, Iterator, Optional
from uuid import uuid1

import yaml
from rdflib import RDF, Graph, Literal, URIRef
from kgcl_schema.schema import PATH as SCHEMA_DIR, get_schemaview
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import json_dumper, yaml_dumper, rdflib_dumper
from linkml_runtime.loaders.yaml_loader import YAMLLoader
from linkml_runtime.utils.formatutils import camelcase
from linkml_runtime.utils.yamlutils import YAMLRoot

import kgcl_schema.datamodel as model
from kgcl_schema.datamodel.kgcl import Session, Change
from kgcl_schema.datamodel.kgcl import Activity

# JSON-LD context generated from the schema by `make gen-project`
LD = SCHEMA_DIR / "kgcl.context.jsonld"


def get_context() -> str:
    """Get JSON-LD context."""
    with open(LD, encoding="utf-8") as stream:
        context = json.load(stream)
        context["@context"]["ANAT"] = {
            "@id": "https://example.org/anatomy/",
            "@prefix": True,
        }
        context["@context"]["uuid"] = {
            "@id": "https://example.org/uuid/",
            "@prefix": True,
        }
        context["@context"]["type"] = {"@type": "@id"}
        return json.dumps(context)


def to_json(session: Session) -> str:
    """Convert a session object to plain json."""
    assign_types(session)
    return json_dumper.dumps(session)


def to_yaml(session: Session) -> str:
    """Convert a session object to plain json."""
    assign_types(session)
    return yaml_dumper.dumps(session)


def to_jsonld(session: Session) -> str:
    """Convert a session object to JSON-LD."""
    assign_types(session)
    return json_dumper.dumps(session, get_context())


# Base IRI for change IDs without a prefix, such as the parser's
KGCL_BASE = "http://w3id.org/kgcl/"

# Temporary base for unprefixed values during RDF export; see to_rdf
_UNPREFIXED = "urn:x-kgcl-unprefixed:"

# Prefixes needed for RDF output that the schema does not declare
RDF_EXTRA_PREFIXES = {
    # from_dict() assigns change IDs of the form uuid:...
    "uuid": "https://example.org/uuid/",
}

# A CURIE prefix: an XML NCName (no colon), as required by the RDF dumper
NCNAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_.\-]*$")


def _iter_strings(obj: Any) -> Iterator[str]:
    """Yield every string value in a (possibly nested) model object."""
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from _iter_strings(v)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            yield from _iter_strings(v)
    elif isinstance(obj, YAMLRoot):
        for k, v in vars(obj).items():
            if not k.startswith("_"):
                yield from _iter_strings(v)


def _rdf_prefix_map(
    session: Session, schemaview: SchemaView, prefix_map: Optional[Dict[str, str]]
) -> Dict[str, str]:
    """
    Build the prefix map for RDF output.

    Starts from the prefixes the session uses that the default CURIE converter
    knows, then adds RDF_EXTRA_PREFIXES and a temporary @base for unprefixed
    values, then the caller's prefix_map, which wins over all of these. Prefixes the schema already
    declares are never overridden by the fallback (prefix lookup in the dumper
    is case-insensitive, so e.g. a converter's "OM" would replace the schema's
    "om").
    """
    from kgcl_schema.grammar.parser import get_curie_converter

    converter = get_curie_converter()
    schema_prefixes = {p.lower() for p in schemaview.namespaces()}
    pm: Dict[str, str] = {}
    for value in _iter_strings(session):
        if ":" not in value:
            continue
        prefix = value.split(":", 1)[0]
        if (
            prefix in pm
            or prefix.lower() in schema_prefixes
            or not NCNAME.match(prefix)
        ):
            continue
        uri_prefix = converter.bimap.get(prefix)
        if uri_prefix:
            pm[prefix] = uri_prefix
    for k, v in RDF_EXTRA_PREFIXES.items():
        if k.lower() not in schema_prefixes:
            pm[k] = v
    if prefix_map:
        pm.update(prefix_map)
    # The dumper always uses the temporary base; to_rdf applies the caller's
    # "@base" (if any) to change IDs only.
    pm["@base"] = _UNPREFIXED
    return pm


def to_rdf(session: Session, prefix_map: Optional[Dict[str, str]] = None) -> str:
    """
    Convert a session object to RDF (Turtle).

    :param session: the session to convert
    :param prefix_map: optional prefix map (prefix -> URI prefix). Prefixes used
        in the session that are missing here are looked up in the default CURIE
        converter (OBO, Bioregistry, linked data).

    Unprefixed change IDs (such as the parser's "kgcl_change_id_0") are placed
    under KGCL_BASE, unless the caller's prefix_map sets "@base". Other values
    without a prefix, such as nodes given by label ('nucleus'), are not IRIs
    and are written as plain literals.
    """
    assign_types(session)
    # A fresh SchemaView each call: the dumper adds the prefix map to its
    # namespaces, which would otherwise leak into later calls.
    schemaview = get_schemaview()
    pm = _rdf_prefix_map(session, schemaview, prefix_map)
    # Unprefixed labels may contain spaces; rdflib warns about such IRIs, but
    # they are replaced with literals below before serialization.
    term_logger = logging.getLogger("rdflib.term")
    level = term_logger.level
    term_logger.setLevel(logging.ERROR)
    try:
        graph = rdflib_dumper.as_rdf_graph(session, schemaview, prefix_map=pm)
    finally:
        term_logger.setLevel(level)
    # Copy into a clean graph: the dumper binds "@base" as if it were a prefix,
    # which is not valid Turtle, and sets a base that makes IRIs relative.
    base = (prefix_map or {}).get("@base", KGCL_BASE)
    change_ids = {
        str(c.id) for c in session.change_set if c.id and ":" not in str(c.id)
    }

    def fix(node):
        if isinstance(node, URIRef) and str(node).startswith(_UNPREFIXED):
            local = str(node)[len(_UNPREFIXED) :]
            return URIRef(base + local) if local in change_ids else Literal(local)
        return node

    out = Graph()
    for prefix, ns in {**dict(schemaview.namespaces()), **pm}.items():
        if NCNAME.match(prefix) and str(ns) != _UNPREFIXED:
            out.bind(prefix, URIRef(str(ns)), override=True, replace=True)
    for s, p, o in graph:
        # The type slot holds a class name; write it as rdf:type <class IRI>.
        if p == RDF.type and isinstance(o, Literal):
            o = URIRef(schemaview.get_uri(str(o), expand=True))
        out.add((fix(s), p, fix(o)))
    return out.serialize(format="turtle")


def from_json(filename: str) -> Session:
    """
    As from_yaml, but with json
    """
    logging.info(f"Converting {filename}")
    with open(filename, "r") as stream:
        obj = json.load(stream)
        return from_dict(obj)


def from_yaml(filename: str) -> Session:
    """
    Parse a slight variant of the standard serialization of the model into YAML.

    See de-novo.yaml as an example

    In particular, until linkml supports a polymorphic discriminator we need ad-hoc
    code for instantiating to the correct class
    """
    logging.info(f"Converting {filename}")
    with open(filename, "r", encoding="utf-8") as stream:
        obj = yaml.safe_load(stream)
        return from_dict(obj)


def from_dict(obj: Dict[str, Any]) -> Session:
    # TODO: move this to LinkML runtime
    # at this time we need wrapper code to introspect type fields
    # and use this to determine which type to instantiate;
    # we also auto-populate identifier fields
    session = Session()
    loader = YAMLLoader()
    for a in obj.get("activity_set", []):
        session.activity_set.append(Activity(**a))
    for c in obj.get("change_set", []):
        # auto-create an ID
        c["id"] = f"uuid:{uuid1()}"
        tc = c["type"]
        del c["type"]
        typ = getattr(model.kgcl, tc)
        logging.info(f"Converting type {tc} // {c}")
        chg = typ(**c)
        chg.type = f"kgcl_schema:{tc}"
        session.change_set.append(chg)
    return session


def assign_types(obj: YAMLRoot):
    if isinstance(obj, Session):
        for ch in obj.change_set:
            assign_types(ch)
    elif isinstance(obj, Change):
        tc = type(obj).class_name
        obj.type = camelcase(tc)

