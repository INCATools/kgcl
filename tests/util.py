"""Compare graph test."""
from linkml_runtime.dumpers import json_dumper
from linkml_runtime.loaders import json_loader
from linkml_runtime.utils.yamlutils import YAMLRoot
from rdflib import Graph
from rdflib.compare import graph_diff, to_isomorphic

from kgcl_schema.apply.graph_transformer import apply_patch
from kgcl_schema.grammar.parser import parse


def compare_graphs(actual, expected):
    """Compare actual and expected graphs."""
    actual_iso = to_isomorphic(actual)
    expected_iso = to_isomorphic(expected)

    if actual_iso != expected_iso:
        _, in_first, in_second = graph_diff(actual_iso, expected_iso)
        print("The actual and expected graphs differ")
        print("----- Contents of actual graph not in expected graph -----")
        print(in_first.serialize(format="nt").decode("utf-8"))
        # dump_ttl_sorted(in_first)
        print("----- Contents of expected graph not in actual graph -----")
        print(in_second.serialize(format="nt").decode("utf-8"))
        # dump_ttl_sorted(in_second)

    assert actual_iso == expected_iso # commented by H2.


def run_test(input_graph, kgcl_patch, expected_graph):
    """Run tests."""
    # load input graph
    g = Graph().parse(data=input_graph, format="nt")

    # load expected output graph
    expected = Graph().parse(data=expected_graph, format="nt")

    parsed_patch = parse(kgcl_patch)
    apply_patch(parsed_patch, g)

    compare_graphs(g, expected)


def roundtrip(obj: YAMLRoot, format='json'):
    dumper = json_dumper
    loader = json_loader
    serialization = dumper.dumps(obj)
    obj2 = json_loader.loads(serialization, target_class=type(obj))
    return obj2