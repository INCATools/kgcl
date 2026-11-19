# Governance

> **Work in progress.** This is a proposal for discussion and has not been agreed by the community yet. Comments welcome on the issue tracker.

KGCL is used by several downstream tools and ontology pipelines, so changes to the data model affect people beyond this repository. This document describes how changes are reviewed and approved.

## Steering committee

KGCL is overseen by a steering committee made up of volunteers from the community.

- Anyone who uses or contributes to KGCL can volunteer by opening an issue on this repository.
- New members are added when the existing committee agrees by a simple majority. Until a first committee exists, the initial members are agreed in a single issue open for at least two weeks.
- Members can step down at any time by opening a PR that removes them from the list below.
- The committee aims to include people from more than one organisation and more than one downstream project.

Current members:

- _To be decided._

## What counts as a data model change

A data model change is any change that alters what KGCL can express or how it is interpreted. This includes changes to:

- the LinkML schema (`src/kgcl_schema/schema/*.yaml`, including `kgcl.yaml`, `prov.yaml`, `basics.yaml` and `ontology_model.yaml`): adding, removing or renaming classes, slots, enums or prefixes, and changing ranges, cardinality, URIs, mappings or descriptions that change meaning
- the KGCL grammar (`src/kgcl_schema/grammar/kgcl.lark`) and the parsing or rendering behaviour that defines the KGCL syntax

Regenerated artifacts (`project/`, `src/kgcl_schema/datamodel/`, the JSON-LD context) follow the change they were generated from and need no separate approval.

Everything else counts as tooling and documentation: CI, packaging, release workflows, Python code that does not change the language, tests, examples and the documentation site. Typo fixes and wording changes in schema descriptions that do not change meaning also fall here.

When it is unclear which category a change belongs to, treat it as a data model change.

## Approval rules

All changes go through a pull request. Authors do not approve their own PRs.

| Change type | Approvals required |
|---|---|
| Data model | 2 approving reviews from steering committee members, not counting the author |
| Tooling and documentation | 1 approving review from a maintainer other than the author |

In addition, for data model changes:

- The change should start as an issue that describes the use case, so the proposal can be discussed before code is written.
- The PR stays open for at least 5 working days before merging, so people in other time zones and projects can comment.
- Removing or renaming anything in the schema or grammar is a breaking change and needs to be called out in the PR title and the release notes.

## Releases

Releases are cut by a maintainer. A release that contains data model changes lists them in the release notes, with links to the approving PRs.

## Disagreements

If reviewers cannot agree, the steering committee decides by simple majority of its members.

## Changing this document

Changes to this document follow the rules for data model changes.
