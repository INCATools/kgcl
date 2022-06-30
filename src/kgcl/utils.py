"""Convenience wrappers around linkml runtime.

Needed for doing basic conversion between objects and serialization formats.
The top level class is a Session object
Some of this will become unnecessary in the future
"""

import json
import logging
import os
from typing import List
from uuid import uuid1

import click
import yaml
from linkml_runtime.dumpers.json_dumper import JSONDumper
from linkml_runtime.dumpers.rdf_dumper import RDFDumper
from linkml_runtime.loaders.yaml_loader import YAMLLoader
from rdflib import Graph

import kgcl.datamodel as model
from kgcl.datamodel.kgcl import Session
from kgcl.datamodel.prov import Activity

THIS_DIR = os.path.abspath(os.path.dirname(__file__))
LD = os.path.join(THIS_DIR, "../ldcontext/kgcl.context.jsonld")


def get_context() -> str:
    """Get JSON-LD context."""
    with open(LD) as stream:
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


def to_json(session: Session) -> Graph:
    """Convert a session object to plain json."""
    dumper = JSONDumper()
    jsons = dumper.dumps(session)
    return jsons


def to_jsonld(session: Session) -> str:
    """Convert a session object to JSON-LD."""
    dumper = JSONDumper()
    jsons = dumper.dumps(session, get_context())
    return jsons


def to_rdf(session: Session) -> Graph:
    """Convert a session object to an rdflib Graph."""
    dumper = RDFDumper()
    g = dumper.as_rdf_graph(element=session, contexts=get_context())
    return g


def from_yaml(filename: str) -> Session:
    """
    Parse a slight variant of the standard serialization of the model into YAML.

    See de-novo.yaml as an example

    In particular, until linkml supports a polymorphic discriminator we need ad-hoc
    code for instantiating to the correct class
    """
    logging.info(f"Converting {filename}")
    session = Session()
    loader = YAMLLoader()
    with open(filename, "r") as stream:
        obj = yaml.safe_load(stream)
        for a in obj["activity_set"]:
            activity = loader.load(source=a, target_class=Activity)
            session.activity_set.append(activity)
        for c in obj["change_set"]:
            # auto-create an ID
            c["id"] = f"uuid:{uuid1()}"
            tc = c["type"]
            del c["type"]
            print(f"Converting type {tc} // {c}")
            chg = loader.load(source=c, target_class=getattr(model.kgcl, tc))
            chg.type = f"kgcl:{tc}"
            session.change_set.append(chg)
    return session


@click.command()
@click.argument("files", nargs=-1)
def cli(files: List[str]):
    """CLI."""
    pass
    # for f in files:
    #     session = from_yaml(f)


# USED FOR TESTING:
# https://github.com/cmungall/knowledge-graph-change-language/pull/30#discussion_r832205466


if __name__ == "__main__":
    cli()
