# Class hierarchy

Every KGCL change type sits in one classification hierarchy. Changes to terms
(`NodeChange`) and changes to relationships (`EdgeChange`) are the two main branches
under `SimpleChange`. Click a triangle to expand or collapse a branch, and click a
class name to open its page in the schema reference. The numbers in parentheses count
each class's direct subclasses. The tree is regenerated from the schema each time the
documentation is built.

<div id="kgcl-class-tree" markdown="0">Loading the class hierarchy…</div>

The same hierarchy, with a description of each class, is in the
[schema reference](schema-reference.md#classes). It is also browsable as an ontology on
[BioPortal](https://bioportal.bioontology.org/ontologies/KGCL).

<style>
  /* A plain indented tree: undo Material's list and collapsible-callout styles. */
  .md-typeset .kgcl-tree, .md-typeset .kgcl-tree ul {
    list-style: none; margin: 0; padding-left: 1.4em;
  }
  .md-typeset .kgcl-tree { padding-left: 0; }
  .md-typeset .kgcl-tree li { margin: 0.2em 0; }
  .md-typeset .kgcl-tree details {
    border: none; box-shadow: none; background: none; margin: 0; padding: 0;
    font-size: inherit; overflow: visible;
  }
  .md-typeset .kgcl-tree summary {
    background: none; border: none; margin: 0; padding: 0 0 0 1.2em;
    font-weight: normal; cursor: pointer; position: relative;
  }
  .md-typeset .kgcl-tree summary::after { display: none; }
  .md-typeset .kgcl-tree summary::before {
    content: "▸"; position: absolute; left: 0; top: 0;
    width: auto; height: auto; background: none; transform: none;
    -webkit-mask: none; mask: none; color: var(--md-default-fg-color--light);
  }
  .md-typeset .kgcl-tree details[open] > summary::before { content: "▾"; }
  .md-typeset .kgcl-tree li:not(:has(> details)) { padding-left: 1.2em; }
  .md-typeset .kgcl-tree a { font-family: var(--md-code-font-family, monospace); font-size: 0.95em; }
  .kgcl-tree-count { color: var(--md-default-fg-color--light); font-size: 0.85em; }
</style>
