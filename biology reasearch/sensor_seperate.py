import time
import random
from datetime import datetime
from db import write_json, read_json

json_file_path = 'rabbit_records.json'


def generate_record():
    return {
        'timestamp': datetime.now().isoformat(),
        'deaths': random.randint(0, 50),  # Simulate number of deaths
        'births': random.randint(0, 50)  # Simulate number of births
    }


def sensor_simulation():
    while True:
        record = generate_record()
        try:
            records = read_json(json_file_path)
        except FileNotFoundError:
            records = []
        except Exception as e:
            print(f"Error reading from JSON: {e}")
            time.sleep(10)  # Wait before retrying
            continue

        records.append(record)
        try:
            write_json(records, json_file_path)
        except Exception as e:
            print(f"Error writing to JSON: {e}")

        time.sleep(random.randint(5, 10))  # Wait between 5-10 seconds before generating the next record
