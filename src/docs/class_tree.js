// Render the KGCL change-type hierarchy as a collapsible tree.
// Data comes from categories.json, which `make gendoc` regenerates from the
// schema (via the generate_viz_json script). Each class links to its page in
// the schema reference.
(function () {
  var script = document.currentScript;
  var siteRoot = new URL(".", script.src);
  var OPEN_DEPTH = 4; // levels expanded on load (through NodeChange/EdgeChange)

  function build(node, depth) {
    var li = document.createElement("li");
    var link = document.createElement("a");
    link.href = new URL(node.name + "/", siteRoot).href;
    link.textContent = node.name;
    var children = node.children || [];
    if (children.length === 0) {
      li.appendChild(link);
      return li;
    }
    var details = document.createElement("details");
    details.open = depth < OPEN_DEPTH;
    var summary = document.createElement("summary");
    summary.appendChild(link);
    var count = document.createElement("span");
    count.className = "kgcl-tree-count";
    count.textContent = " (" + children.length + ")";
    summary.appendChild(count);
    details.appendChild(summary);
    var ul = document.createElement("ul");
    children.forEach(function (child) {
      ul.appendChild(build(child, depth + 1));
    });
    details.appendChild(ul);
    li.appendChild(details);
    return li;
  }

  function render() {
    var container = document.getElementById("kgcl-class-tree");
    if (!container) return;
    fetch(new URL("categories.json", siteRoot))
      .then(function (response) { return response.json(); })
      .then(function (roots) {
        var ul = document.createElement("ul");
        ul.className = "kgcl-tree";
        roots.forEach(function (root) { ul.appendChild(build(root, 0)); });
        container.replaceChildren(ul);
      })
      .catch(function (error) {
        container.textContent = "Could not load the class hierarchy: " + error;
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", render);
  } else {
    render();
  }
})();
