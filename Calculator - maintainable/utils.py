# fn loads all sub python files from fns dir

import os
from importlib import import_module

# load file names
operation_files = [f.replace(".py", "") for f in os.listdir('fns') if f.endswith('.py') and not f.startswith("__")]


# ["add"]

def load_operations():
    operations = {}
    for name in operation_files:
        module = import_module(f"fns.{name}")
        fn = getattr(module, name)
        if callable(fn):
            operations[name] = fn
    return operations
