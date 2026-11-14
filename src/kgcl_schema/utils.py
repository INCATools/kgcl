"""Convenience wrappers around linkml runtime.

Needed for doing basic conversion between objects and serialization formats.
The top level class is a Session object
Some of this will become unnecessary in the future
"""

import json
import logging
from typing import Dict, Any
from uuid import uuid1

import yaml
from kgcl_schema.schema import PATH as SCHEMA_DIR, get_schemaview
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


# TODO: allow passing of prefix maps
def to_rdf(session: Session, prefix_map: Dict[str, str] = None) -> str:
    """Convert a session object to an rdflib Graph string."""
    assign_types(session)
    return rdflib_dumper.dumps(
        session, prefix_map=prefix_map, schemaview=get_schemaview()
    )


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

