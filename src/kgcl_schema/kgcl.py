"""KGCL."""
import logging
import sys

import click
import rdflib
from rdflib.util import guess_format

from kgcl_schema.apply import graph_transformer
from kgcl_schema.grammar import parser

# TODO: remove this
sys.path.append("../")


@click.command()
@click.option("-i", "--graph", type=click.Path(), required=True)
@click.option("--kgcl-file", type=click.File("r"))
@click.option("--output",
              "-o",
              type=click.File(mode='wb'),
              default=sys.stdout)
@click.option("-v", "--verbose", count=True)
@click.argument('patch')
def cli(patch, verbose: int, graph, kgcl_file, output):
    """
    Modify graph based on KGCL commands.
    """
    if verbose >= 2:
        logging.basicConfig(level=logging.DEBUG)
    elif verbose == 1:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)
    # read kgcl_schema commands from file
    if kgcl_file:
        kgcl_patch = kgcl_file.read()
    elif patch:
        kgcl_patch = patch
    else:
        raise ValueError(f"Must pass EITHER kgcl_schema-file OR kgcl_schema")

    # parser kgcl_schema commands
    parsed_patch = parser.parse(kgcl_patch)
    logging.info(f"Patch: {patch}")

    # apply kgcl_schema commands as SPARQL UPDATE queries to graph
    g = rdflib.Graph()
    g.load(graph, format=guess_format(graph))
    # g.parse(graph)  # , format="nt") #TODO: this doesn't always work
    graph_transformer.apply_patch(parsed_patch, g)

    # save updated graph
    g.serialize(destination=output, format="ttl")


if __name__ == "__main__":
    cli()
