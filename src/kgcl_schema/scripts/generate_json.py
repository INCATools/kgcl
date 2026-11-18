"""
Generate the class-hierarchy JSON used by the visualization on the docs site.

Adapted from code developed for biolink-model.
Run from the repository root (`make gendoc` does this).
"""

import json
from collections import defaultdict
from typing import Dict, List, Set

from kgcl_schema.schema import get_schemaview

ROOT_NODE = "ChangeLanguageElement"
OUTPUT_PATH = "src/docs/categories.json"


def get_tree_class_recursive(root_node: dict, parent_to_child_map: Dict[str, Set[str]]) -> dict:
    """
    Recursively attach children to a tree node.

    :param root_node: The node to expand, as a dict with "name" and "parent".
    :param parent_to_child_map: A dictionary mapping parent class names to child class names.
    :return: The node, with a sorted "children" list if it has any.
    """
    root_name = root_node["name"]
    children_names = parent_to_child_map.get(root_name, [])
    if children_names:
        children = []
        for child_name in children_names:
            child_node = {"name": child_name, "parent": root_name}
            children.append(get_tree_class_recursive(child_node, parent_to_child_map))
        root_node["children"] = sorted(children, key=lambda x: x["name"])
    return root_node


def load_category_tree_data() -> List[dict]:
    """
    Build the class tree from the schema, rooted at ROOT_NODE.

    Deprecated classes are left out.

    :return: A one-element list holding the root of the tree.
    """
    sv = get_schemaview()
    parent_to_child_dict = defaultdict(set)
    for class_name in sv.all_classes(imports=True):
        cls = sv.get_class(class_name)
        if cls.deprecated:
            continue
        if cls.is_a:
            parent_to_child_dict[cls.is_a].add(class_name)
    root_node = {"name": ROOT_NODE, "parent": None}
    return [get_tree_class_recursive(root_node, parent_to_child_dict)]


def generate_viz_json():
    """Write the class tree to OUTPUT_PATH."""
    cat_data = load_category_tree_data()
    with open(OUTPUT_PATH, "w", encoding="utf-8") as json_file:
        json.dump(cat_data, json_file, indent=4)


if __name__ == "__main__":
    generate_viz_json()
