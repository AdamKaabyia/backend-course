from db import write_json, read_json
import random
from datetime import datetime

json_file_path = 'rabbit_records.json'


def generate_record():
    return {
        'timestamp': datetime.now().isoformat(),
        'deaths': random.randint(0, 50),
        'births': random.randint(0, 50)
    }


def sensor_simulation():
    records = []
    for _ in range(random.randint(100, 300)):  # Generate between 100-300 records
        record = generate_record()
        records.append(record)
        try:
            existing_records = read_json(json_file_path)
        except FileNotFoundError:
            existing_records = []
        except Exception as e:
            print(f"Error reading JSON: {e}")
            continue

        existing_records.append(record)
        try:
            write_json(existing_records, json_file_path)
        except Exception as e:
            print(f"Error writing JSON: {e}")
