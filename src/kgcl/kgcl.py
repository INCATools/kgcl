"""KGCL."""
import sys

import click
import rdflib
from rdflib.util import guess_format

from kgcl.apply import graph_transformer
from kgcl.grammar import parser

# TODO: remove this
sys.path.append("../")


class Config(object):
    """Configuration class."""

    def __init__(self):
        self.verbose = False


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.command()
@click.option("--graph", type=click.Path(), required=True)
@click.option("--kgcl", type=click.File("r"), required=True)
@click.option("--output",
              "-o",
              type=click.Path(), required=True)
# @click.option("--verbose", "-v", is_flag=True, help="Print more output.")
@pass_config
def cli(config, graph, kgcl, output):
    """
    Modify graph based on KGCL commands.
    """
    # read kgcl commands from file
    kgcl_patch = kgcl.read()

    # parser kgcl commands
    parsed_patch = parser.parse(kgcl_patch)

    # apply kgcl commands as SPARQL UPDATE queries to graph
    g = rdflib.Graph()
    g.load(graph, format=guess_format(graph))
    # g.parse(graph)  # , format="nt") #TODO: this doesn't always work
    graph_transformer.apply_patch(parsed_patch, g)

    # save updated graph
    g.serialize(destination=output, format="ttl")


if __name__ == "__main__":
    cli()
