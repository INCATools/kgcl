from pathlib import Path
from linkml_runtime import SchemaView

PATH = Path(__file__).parent


def get_schemaview() -> SchemaView:
    schema_root = str(PATH / 'kgcl.yaml')
    return SchemaView(schema_root)
