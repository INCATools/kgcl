"""Compare graph test."""
from linkml_runtime.dumpers import json_dumper
from linkml_runtime.loaders import json_loader
from linkml_runtime.utils.yamlutils import YAMLRoot


def roundtrip(obj: YAMLRoot, format='json'):
    dumper = json_dumper
    loader = json_loader
    serialization = dumper.dumps(obj)
    obj2 = json_loader.loads(serialization, target_class=type(obj))
    return obj2