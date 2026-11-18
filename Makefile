MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

RUN = poetry run
# get values from about.yaml file
SCHEMA_NAME = $(shell bash ./utils/get-value.sh name)
SOURCE_SCHEMA_PATH = $(shell bash ./utils/get-value.sh source_schema_path)
SRC = src
DEST = project
PYMODEL = $(SRC)/$(SCHEMA_NAME)_schema/datamodel
DOCDIR = docs
TEMPLATEDIR = doc-templates

.PHONY: all clean

help: status
	@echo ""
	@echo "make all -- makes site locally"
	@echo "make install -- install dependencies"
	@echo "make gen-project -- regenerates project files and the Python datamodel from the schema"
	@echo "make test -- runs tests"
	@echo "make docs-check -- builds docs and fails on warnings"
	@echo "make testdoc -- builds docs and runs local test server"
	@echo "make deploy -- deploys site"
	@echo "make upgrade -- updates linkml version"
	@echo "make help -- show this help"
	@echo ""

status:
	@echo "Project: $(SCHEMA_NAME)"
	@echo "Source: $(SOURCE_SCHEMA_PATH)"

install:
	poetry install
.PHONY: install

all: gen-project gendoc
%.yaml: gen-project
deploy: all mkd-gh-deploy

# generates all project files; the JSON-LD context is also copied into the
# package, where kgcl_schema.utils.to_jsonld reads it
gen-project: $(PYMODEL)
	$(RUN) gen-project -d $(DEST) $(SOURCE_SCHEMA_PATH) --config-file project_config.yaml  && mv $(DEST)/*.py $(PYMODEL)
	cp $(DEST)/jsonld/$(SCHEMA_NAME).context.jsonld $(SRC)/$(SCHEMA_NAME)_schema/schema/

src/kgcl_schema/datamodel/%.py: src/kgcl_schema/schema/%.yaml
	$(RUN) gen-python $< > $@.tmp && mv $@.tmp $@

test:
	$(RUN) pytest

upgrade:
	poetry add -D linkml@latest

# Test documentation locally
serve: mkd-serve

# Python datamodel
$(PYMODEL):
	mkdir -p $@


$(DOCDIR):
	mkdir -p $@

# Copy hand-written pages and their assets (images, the class-hierarchy
# script and its data), regenerate the hierarchy data from the schema, then build
# the schema reference pages.
gendoc: $(DOCDIR)
	$(RUN) generate_viz_json
	cp -r $(SRC)/docs/*.md $(SRC)/docs/*.js $(SRC)/docs/*.json $(DOCDIR)
	cp -r $(SRC)/docs/images $(DOCDIR)
	$(RUN) gen-doc -d $(DOCDIR) --template-directory $(SRC)/$(TEMPLATEDIR) --index-name schema-reference $(SOURCE_SCHEMA_PATH)

# Build the site without deploying; fails on broken links and other warnings
docs-check: gendoc
	$(MKDOCS) build --strict

testdoc: gendoc serve

MKDOCS = $(RUN) mkdocs
mkd-%:
	$(MKDOCS) $*

clean:
	rm -rf $(DEST)
	rm -rf tmp

include project.Makefile
