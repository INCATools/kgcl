## Add your own custom Makefile targets here

test:
	poetry run pytest

gen-viz:
	$(RUN) generate_viz_json