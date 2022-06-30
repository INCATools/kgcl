# KGCL Tooling
This folder contains tooling for handling change operations in ontologies according to the [Knowledge-Graph-Change-Language](https://cmungall.github.io/knowledge-graph-change-language/).

**The code is in active development and subject to frequent changes.**

**Feedback and PRs are welcome! There is always more to do and things to improve.**

## tl;dr

Example code for applying a KGCL patch to a graph.
The examples make use of relative paths.
So, they need to be located in the root folder of this project (i.e., knowledge-graph-change-language - the parent folder of this folder).

```
import rdflib
from rdflib.util import guess_format
import kgcl.grammar.parser
import kgcl.apply.graph_transformer

#graph: path to an RDF graph
#patch_file: file containing a set of KGCL commands
#output: path to an output destination

# read kgcl commands from file
patch_file = open("examples/kgcl/demo/example_patch.kgcl", "r")
patch = patch_file.read()

# parse kgcl commands
parsed_patch = kgcl.grammar.parser.parse(patch)

#load RDF graph
path_to_graph = "examples/kgcl/demo/example_graph.nt"
g = rdflib.Graph()
g.load(path_to_graph, format=guess_format(path_to_graph))

# apply kgcl commands as SPARQL UPDATE queries to graph
kgcl.apply.graph_transformer.apply_patch(parsed_patch, g)

# save updated graph
output = "output.nt"
g.serialize(destination=output, format="nt") 
```

Example code for generating a KGCL Diff between two graphs:

```
from kgcl.diff.summary_generation import run

#graph_1: path to an RDF graph
#graph_2: path to an RDF graph
#output: path to an output destination (which must not exist as a folder)

graph_1 = "examples/kgcl/demo/example_graph.nt"
graph_2 = "examples/kgcl/demo/example_graph_version_2.nt"
output = "output"

run(graph_1, graph_2, output)
```

Example code for generating a KGCL Diff between two graphs (without writing a summary to an output folder): 

```
import rdflib

import kgcl.diff.diff_2_kgcl_single as single
import kgcl.diff.diff_2_kgcl_existential as existential

#graph_1: path to an RDF graph
#graph_2: path to an RDF graph
#output: path to an output destination (which must not exist as a folder)

graph_1 = "examples/kgcl/demo/example_graph.nt"
graph_2 = "examples/kgcl/demo/example_graph_version_2.nt"

#load RDF graphs
g_1 = rdflib.Graph()
g_1.load(graph_1, format=guess_format(graph_1))
g_2 = rdflib.Graph()
g_2.load(graph_2, format=guess_format(graph_2))

#generate diff
single_triple_summary = single.generate_thin_triple_commands(g1, g2)
existential_summary = existential.generate_atomic_existential_commands(g1, g2) 

# get KGCL commands
kgcl_commands = existential_summary.get_commands()
kgcl_commands += single_triple_summary.get_commands()
``` 

Example code for converting a KGCL patch into RDF:
```
from kgcl.grammar.kgcl_2_rdf import kgcl_2_yaml
from kgcl.utils import from_yaml, to_rdf
from rdflib import Graph

patch_file = open("examples/kgcl/demo/example_patch_2.kgcl", "r")
patch = patch_file.read() 
output = "output"

#this parses a KGCL into KGCL instances of the KGCL data model
#encodes them in YAML,
#and writes them to output
kgcl_2_yaml(patch, output)

#this loads the YAML encoding
#and translates it into RDF
session = from_yaml("output")
G: Graph
G = to_rdf(session)
G.serialize("kgcl_patch.rdf", format="turtle") 
```

## What are KGCL change operations?

A KGCL change operation is a statement that specifies a change for a knowledge graph (or ontology). 
For example, the statment `add A SubClassOf B` specifies the addition of a subsumption axiom between two (named) classes `A` and `B`.
The current prototype supports the following KGCL change operations (according to this [grammar](https://github.com/ckindermann/knowledge-graph-change-language/blob/parser/kgcl_tool/grammar/kgcl.lark)):
- renaming labels
- creating nodes
- deleting nodes
- obsoleting entities
- unobsoleting entities
- deepening nodes
- shallowing nodes
- creating synonyms
- moving nodes
- changing relationships 
- creating (annotated) edges
- deleting (annotated) edges
- adding subsumption axioms
- deleting subsumption axioms
- adding atomic existential restriction axioms
- deleting atomic existential restriction axioms 

## How do I use KGCL operations?

A (text) file containing KGCL operations in each line is called a _patch_. A patch can be applied to an `input.nt` knowledge graph (serialised as N-triples) by calling `python kgcl.py input.nt patch output.nt` to generate the `output.n` knowledge graph.
 
## How can I specify test cases for KGCL?

A _test_ for KGCL can be specified by creating a folder containing three files:
1. `inputGraph.nt` (the input knowledge graph)
2. `kgcl` (the KGCL patch)
3. `outputGraph.nt` (the expected output knowledge graph).  

Calling `python custom_kgcl_tests.py` executes all tests in the folder [`tests/data/kgcl`](https://github.com/ckindermann/knowledge-graph-change-language/tree/parser/kgcl_tool/tests/data/kgcl).

## What is a KGCL Diff?

A KGCL Diff of two knowledge graphs `g1.nt` and `g2.nt` is a KGCL patch `p` such that `p` applied to `g1.nt` yields `g2.nt`.

## How do I generate a KGCL Diff?

**Note: the current implementation does not generate a KGCL Diff as defined above. KGCL Diff does not support all change operations that are already available in KGCL. In particular, most OWL axioms involving blank nodes are currently ignored.**

A KGLC Diff can be generated by calling `python kgcl_diff.py g1.nt g2.nt output` where `output` is a path to the desired output directory (note that this directory will be created and must not already exist). Besides the KGCL patch, the `output` folder will contain supplementary information about the generated patch.

## What is an incomplete KGCL Diff useful for?

Even an incomplete KGCL Diff, i.e. a KGCL patch that doesn't account for all changes between two knowledge graphes, can provide useful information about how to versions of a knowledge graph differ.
For example, consider an update for a knowledge graph in which only a language tag, say `en`, to labels have been added. In this case, a KGCL Diff is generated that only consists of KGCL change operations
of the form `rename node from x to x@en`. The current implementation provides a summary report about the number of different change operations involved in a KGCL Diff (keeping in mind that KGCL Diff does not yet support all operations from KGCL).

# Installation

This project uses [pipenv](https://pipenv-fork.readthedocs.io/en/latest/) for installation.

 `pipenv install kgcl`

# How to contribute?

There are many things left to do. 
- testing both KGCL and KGCL Diff (beyond simple unit testing)
- extending the grammar (there are many missing KGCL operations)
- making KGCL commands more user-friendly and forgiving (i.e. by allowing the use of labels instead of IRIs)
- building a GUI (start with a Jupyter Notebook?)
- building a (proper) CLI (that integrates KGCL and KGCL Diff with proper subgroups)
- extending KGCL data model to handle general OWL axioms (or at least OWL EL)
- package the project for easy installation
- handling of non-deterministic diffs
- robust handling of complex KGCL change operations (consider the case of obsoletions - when can a class be considerd 'obsoleted'? If it's label chaged "obsolete X"? If there is a triple with `oboInOwl:deprecated` set to `true`? Are both conditions sufficient by themselves?)
- (proper) parsing of URIs and CURIES 
- validating constraints on KGCL operations
- setting up Github Actions
- change ontologies via GitHub tickets (using KGCL commands)
- cleaning up the code base (many things are not yet pythonic - if something seems off to you, it's because it probably is)
