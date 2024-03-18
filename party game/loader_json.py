import json


def load_config(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Could not parse the JSON in {file_path}.")
        exit(1)


def load_places():
    return load_config('places.json')


def load_weapons():
    return load_config('weapons.json')
