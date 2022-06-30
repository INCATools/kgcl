"""Render KGCL."""
from kgcl.datamodel.kgcl import (ClassCreation, EdgeCreation, EdgeDeletion,
                             NewSynonym, NodeCreation, NodeDeepening,
                             NodeDeletion, NodeMove, NodeObsoletion,
                             NodeRename, NodeShallowing, NodeUnobsoletion,
                             PredicateChange, RemovedNodeFromSubset)


def render(kgcl_instance):
    """Render kGCL based on instance type."""
    render = ""
    if type(kgcl_instance) is NodeRename:
        render = (
            render
            + "NodeRename("
            + "ID="
            + kgcl_instance.id
            + ", "
            + "Old Value="
            + kgcl_instance.old_value
            + ", "
            + "New Value="
            + kgcl_instance.new_value
            + ")"
        )

    if type(kgcl_instance) is NodeObsoletion:
        render = (
            render
            + "NodeObsoletion("
            + "ID="
            + kgcl_instance.id
            + ", "
            + "Repacelement="
            + str(kgcl_instance.has_direct_replacement)
            + ", "
            + "About="
            + kgcl_instance.about_node
            + ")"
        )

    if type(kgcl_instance) is NodeDeletion:
        render = (
            render
            + "NodeDeletion("
            + "ID="
            + kgcl_instance.id
            + ", "
            + "About="
            + kgcl_instance.about_node
            + ")"
        )

    if type(kgcl_instance) is ClassCreation:
        render = (
            render
            + "ClassCreation("
            + "ID="
            + kgcl_instance.id
            + ", "
            + "Term_ID"
            + kgcl_instance.node_id
            + ")"
        )

    if type(kgcl_instance) is NodeCreation:
        render = (
            render
            + "NodeCreation("
            + "ID="
            + kgcl_instance.id
            + ", "
            + "Term ID="
            + kgcl_instance.node_id
            + ", "
            + "Label="
            + kgcl_instance.name
            + ")"
        )

    if type(kgcl_instance) is NodeMove:
        render = (
            render
            + "NodeMove("
            + "ID="
            + kgcl_instance.id
            + ", "
            + "Old Value="
            + kgcl_instance.old_value
            + ", "
            + "New Value="
            + kgcl_instance.new_value
            + ")"
        )

    if type(kgcl_instance) is NodeUnobsoletion:
        render = (
            render
            + "NodeUnobsoletion("
            + "ID="
            + kgcl_instance.id
            + ", "
            + "Term id="
            + kgcl_instance.about_node
            + ")"
        )

    if type(kgcl_instance) is NodeDeepening:
        render = (
            render
            + "NodeDeepening("
            + "ID="
            + kgcl_instance.id
            + ", "
            + "Term ID="
            + kgcl_instance.about_edge.subject
            + ", "
            + "Old Value="
            + kgcl_instance.old_value
            + ", "
            + "New Value="
            + kgcl_instance.new_value
            + ")"
        )

    if type(kgcl_instance) is NodeShallowing:
        render = (
            render
            + "NodeShallowing("
            + "ID="
            + kgcl_instance.id
            + ", "
            + "Term ID="
            + kgcl_instance.about_edge.subject
            + ", "
            + "Old Value="
            + kgcl_instance.old_value
            + ", "
            + "New Value="
            + kgcl_instance.new_value
            + ")"
        )

    if type(kgcl_instance) is EdgeCreation:
        render = (
            render
            + "EdgeCreation("
            + "ID="
            + kgcl_instance.id
            + ", "
            + "Subject="
            + kgcl_instance.subject
            + ", "
            + "Predicate="
            + kgcl_instance.predicate
            + ", "
            + "Object="
            + kgcl_instance.object
            + ")"
        )

    if type(kgcl_instance) is EdgeDeletion:
        render = (
            render
            + "EdgeDeletion("
            + "ID="
            + kgcl_instance.id
            + ", "
            + "Subject="
            + kgcl_instance.subject
            + ", "
            + "Predicate="
            + kgcl_instance.predicate
            + ", "
            + "Object="
            + kgcl_instance.object
            + ")"
        )

    if type(kgcl_instance) is NewSynonym:
        render = (
            render
            + "NewSynonym("
            + "ID="
            + kgcl_instance.id
            + ", "
            + "About Node="
            + kgcl_instance.about_node
            + ", "
            + "Synonym="
            + kgcl_instance.new_value
            + ")"
        )

    if type(kgcl_instance) is PredicateChange:
        render = (
            render
            + "PredicateChange("
            + "ID="
            + kgcl_instance.id
            + ", "
            + "Subject="
            + kgcl_instance.about_edge.subject
            + ", "
            + "Subject="
            + kgcl_instance.about_edge.object
            + ", "
            + "Old Value="
            + kgcl_instance.old_value
            + ", "
            + "New Value"
            + kgcl_instance.new_value
            + ")"
        )

    # if(type(kgclInstance) is AddNodeToSubset):
    #    render = render + "AddNodeToSubset(" \
    #            + "ID=" + kgclInstance.id + ", " \
    #            + "Subset=" + kgclInstance.in_subset + ", " \
    #            + "About Node" + kgclInstance.about_node + ")"

    if type(kgcl_instance) is RemovedNodeFromSubset:
        render = (
            render
            + "RemovedNodeFromSubset("
            + "ID="
            + kgcl_instance.id
            + ", "
            + "Subset="
            + kgcl_instance.subset
            + ", "
            + "About Node"
            + kgcl_instance.about_node
            + ")"
        )

    return render
