""" 
Functions for generating JSON files for visualizations. 
Adapted from code developed for biolink-model. 
"""

from collections import defaultdict
import json
from typing import Any, List, Union

from linkml_runtime.utils.schemaview import SchemaView

file_path = "src/kgcl_schema/schema/kgcl.yaml"

# Read the file content
with open(file_path, "r") as file:
    file_content_str = file.read()

# Parse the YAML content
sv = SchemaView(file_content_str)


def get_tree_class_recursive(root_node: dict, parent_to_child_map: dict) -> dict:
    """
    Recursively get the tree node.

    :param root_node: The root node of the tree.
    :type root_node: dict
    :param parent_to_child_map: A dictionary mapping parent nodes to child nodes.
    :type parent_to_child_map: dict
    :return: The tree node.
    :rtype: dict

    """
    root_name = root_node["name"]
    children_names = parent_to_child_map.get(root_name, [])
    if children_names:
        children = []
        for child_name in children_names:
            child_node = {"name": child_name, "parent": root_name}
            child_node = get_tree_class_recursive(child_node, parent_to_child_map)
            children.append(child_node)
        root_node["children"] = sorted(children, key=lambda x: x["name"])
        # test

    return root_node


def load_predicate_tree_data(
    return_parent_to_child_dict: bool = False,
) -> Union[List[List[Any]], dict]:
    """
    Load the predicate tree data from the model.

    :return: The predicate tree data.
    """
    parent_to_child_dict = defaultdict(set)
    predicate_tree = []
    for slot_name in sv.all_slots(imports=True):
        slot = sv.get_slot(slot_name)
        if slot.deprecated:
            continue
        slot_name = convert_predicate_to_trapi_format(slot_name)
        parent_name_english = slot.is_a
        if parent_name_english:
            parent_name = convert_predicate_to_trapi_format(parent_name_english)
            parent_to_child_dict[parent_name].add(slot_name)
            root_node = {"name": "related_to"}
            predicate_tree = get_tree_slot_recursive(root_node, parent_to_child_dict)
        if slot.mixins:
            for mixin in slot.mixins:
                parent_name_english = mixin
                parent_name = convert_predicate_to_trapi_format(parent_name_english)
                parent_to_child_dict[parent_name].add(slot_name)
                root_node = {"name": "related_to_at_instance_level"}
                predicate_tree = get_tree_slot_recursive(
                    root_node, parent_to_child_dict
                )
    return (
        ([predicate_tree], parent_to_child_dict)
        if return_parent_to_child_dict
        else ([predicate_tree])
    )


def load_qualifier_tree_data(
    return_parent_to_child_dict: bool = False,
) -> Union[List[List[Any]], dict]:
    """
    Load the qualifier tree data from the model.

    :return: The qualifier tree data.
    """
    parent_to_child_dict = defaultdict(set)
    predicate_tree = []
    for slot_name in sv.all_slots(imports=True):
        slot = sv.get_slot(slot_name)
        if slot.deprecated:
            continue
        slot_name = convert_predicate_to_trapi_format(slot_name)
        parent_name_english = slot.is_a
        if parent_name_english:
            parent_name = convert_predicate_to_trapi_format(parent_name_english)
            parent_to_child_dict[parent_name].add(slot_name)
            root_node = {"name": "qualifier"}
            predicate_tree = get_tree_slot_recursive(root_node, parent_to_child_dict)
    return (
        ([predicate_tree], parent_to_child_dict)
        if return_parent_to_child_dict
        else ([predicate_tree])
    )


def load_category_tree_data(return_parent_to_child_dict: bool = False) -> tuple:
    """
    Load the category tree data from the model.

    :param return_parent_to_child_dict: Whether to return the parent to child dictionary.
    :type return_parent_to_child_dict: bool
    :return: The category tree data.
    :rtype: tuple
    """
    parent_to_child_dict = defaultdict(set)
    category_tree = {}
    for class_name in sv.all_classes(imports=True):
        cls = sv.get_class(class_name)
        if cls.deprecated:
            continue
        class_name = convert_predicate_to_trapi_format(class_name)
        if cls.is_a:
            parent_name_english = cls.is_a
            if parent_name_english:
                parent_name = convert_predicate_to_trapi_format(parent_name_english)
                parent_to_child_dict[parent_name].add(class_name)
                root_node = {"name": "NamedThing", "parent": None}
                category_tree = get_tree_class_recursive(
                    root_node, parent_to_child_dict
                )
                parent_name = convert_category_to_trapi_format(parent_name_english)
                parent_to_child_dict[parent_name].add(class_name)

    return (
        ([category_tree], parent_to_child_dict)
        if return_parent_to_child_dict
        else ([category_tree])
    )


def load_association_tree_data(return_parent_to_child_dict: bool = False) -> tuple:
    """
    Load the category tree data from the model.

    :param return_parent_to_child_dict: Whether to return the parent to child dictionary.
    :type return_parent_to_child_dict: bool
    :return: The category tree data.
    :rtype: tuple
    """
    parent_to_child_dict = defaultdict(set)
    category_tree = {}
    for class_name in sv.all_classes(imports=True):
        cls = sv.get_class(class_name)
        if cls.deprecated:
            continue
        class_name = convert_predicate_to_trapi_format(class_name)
        if cls.is_a:
            parent_name_english = cls.is_a
            if parent_name_english:
                parent_name = convert_predicate_to_trapi_format(parent_name_english)
                parent_to_child_dict[parent_name].add(class_name)
                root_node = {"name": "Association", "parent": None}
                category_tree = get_tree_class_recursive(
                    root_node, parent_to_child_dict
                )
                parent_name = convert_category_to_trapi_format(parent_name_english)
                parent_to_child_dict[parent_name].add(class_name)

    return (
        ([category_tree], parent_to_child_dict)
        if return_parent_to_child_dict
        else ([category_tree])
    )


def convert_predicate_to_trapi_format(english_predicate: str) -> str:
    # Converts a string like "treated by" to "treated_by"
    return english_predicate.replace(" ", "_")


def convert_category_to_trapi_format(english_category: str) -> str:
    # Converts a string like "named thing" to "NamedThing"
    return "".join(
        [f"{word[0].upper()}{word[1:]}" for word in english_category.split(" ")]
    )


def get_tree_slot_recursive(root_node: dict, parent_to_child_map: dict) -> dict:
    """
    Recursively get the tree node.

    :param root_node: The root node of the tree.
    :type root_node: dict
    :param parent_to_child_map: A dictionary mapping parent nodes to child nodes.
    :type parent_to_child_map: dict
    :return: The tree node.
    :rtype: dict

    """
    root_name = root_node["name"]
    children_names = parent_to_child_map.get(root_name, [])
    if children_names:
        children = []
        for child_name in children_names:
            child_node = {"name": child_name, "parent": root_name}
            child_node = get_tree_slot_recursive(child_node, parent_to_child_map)
            children.append(child_node)
        root_node["children"] = sorted(children, key=lambda x: x["name"])
        # test

    return root_node


"""
            elements: {
                nodes: [
                    {data: {id: 'a', label: 'treats', mdFile: "treats", mixin: "true"}},
                    {data: {id: 'b', label: 'contraindicated in', mdFile: "contraindicated in", mixin: "false"}},
                    {data: {id: 'c', label: 'studied_to_treat', mdFile: "studied to treat", mixin: "false"}},
                    {data: {id: 'd', label: 'taken_or_studied_or_treats', mdFile: "studied to treat", mixin: "false"}}

                ],
                edges: [
                    {data: {id: 'ab', source: 'a', target: 'b'}},
                    {data: {id: 'bc', source: 'a', target: 'c'}},
                    {data: {id: 'ca', source: 'd', target: 'a'}},
                    {data: {id: 'ca', source: 'b', target: 'a'}}
                ]
            },
"""

def generate_viz_json():

    # Generate the d3 viz data
    pred_data = load_predicate_tree_data()
    qualifier_data = load_qualifier_tree_data()
    cat_data = load_category_tree_data()
    association_data = load_association_tree_data()

    with open("src/docs/predicates.json", "w") as json_file:
        json.dump(pred_data, json_file, indent=4)

    with open("src/docs/qualifiers.json", "w") as json_file:
        json.dump(qualifier_data, json_file, indent=4)

    with open("src/docs/categories.json", "w") as json_file:
        json.dump(cat_data, json_file, indent=4)

    with open("src/docs/associations.json", "w") as json_file:
        json.dump(association_data, json_file, indent=4)


if __name__ == "__main__":
    generate_viz_json()
