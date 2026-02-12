# KGCL: Knowledge Graph Change Language

KGCL is a standard data model for describing changes to knowledge graphs and ontologies at a high level, and an accompanying human-readable Controlled Natural Language (CNL).
A curator can use KGCL to request desired changes, and it can also be used to describe changes that have already happened, corresponding to the concepts of “apply patch” and “diff” commonly used for managing changes in text documents and computer programs. 

This repository houses:

- The KGCL schema/standard
- The Python implementation of the standard (LinkML model, LARK grammar)

The following URIs will resolve to the KGCL standard:

- OWL: https://w3id.org/kgcl/kgcl.owl.ttl
- JSONLD: https://w3id.org/kgcl/kgcl.context.jsonld
- SHACL: https://w3id.org/kgcl/kgcl.shacl.ttl
- YAML: https://w3id.org/kgcl/kgcl.yaml

## More information

- [Documentation](https://incatools.github.io/kgcl/)
- [Publication](https://academic.oup.com/database/article/doi/10.1093/database/baae133/7972659): Hegde H, Vendetti J, Goutte-Gattat D, Caufield JH, Graybeal JB, Harris NL, Karam N, Kindermann C, Matentzoglu N, Overton JA, Musen MA, Mungall CJ. A change language for ontologies and knowledge graphs. Database (Oxford). Oxford University Press (OUP); 2025 Jan 22;2025(baae133). https://doi.org/10.1093/database/baae133 PMCID: PMC11753292 

## How to run project locally
install python 3.9, using mise (optional), get mise from [here](https://mise.jdx.dev/)
```bash
mise install python 3.9
```
install poetry
```bash
pip install poetry
```
install dependencies
```bash
poetry install
```
run tests
```bash
poetry run pytest
```
