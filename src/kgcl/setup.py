"""Setup config."""
from setuptools import setup

setup(
    name="kgcl",  # this is what we pip install
    version="0.0.1",
    description="Knowledge Graph Change Language",
    py_modules=[
        "kgcl"
    ],  # list of python code modules - this is the code I want to distribute (this is what people import - not what they pip-install)
    package_dir={"": "kgcl"},
),
