import importlib
import os
import sys
import logging


def load_plugins(directory):
    plugins = {}
    directory_path = os.path.join(os.path.dirname(__file__), '..', directory)
    sys.path.insert(0, directory_path)

    for filename in os.listdir(directory_path):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]
            module_path = f"{directory}.{module_name}"
            module = importlib.import_module(module_path)
            logging.info(f"Loading plugin: {module_name}")

            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                if isinstance(attribute, type):
                    plugins[attribute_name.lower()] = attribute
                    logging.info(f"Registered plugin class: {attribute_name}")

    sys.path.pop(0)
    return plugins
