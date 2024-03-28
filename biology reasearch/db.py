import json
import random

import threading

failure_probability = 0


def raise_random_exception_with_probability():
    global failure_probability
    if random.random() < failure_probability:
        random_exception = random.choice([
            FileNotFoundError,
            PermissionError,
            IsADirectoryError,
            FileExistsError,
            NotADirectoryError,
            IOError
        ])
        raise random_exception("Random exception raised")
    else:
        if failure_probability < 1.0:
            failure_probability += 0.05
        print('Failure probability after: ', failure_probability)


def reset_failure_probability():
    global failure_probability
    failure_probability = 0


def read_json(file_path):
    try:
        raise_random_exception_with_probability()
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        reset_failure_probability()
        raise e


def write_json(data, file_path):
    try:
        raise_random_exception_with_probability()
        with open(file_path, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        reset_failure_probability()
        raise e
