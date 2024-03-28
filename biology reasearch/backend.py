import time
from db import read_json, write_json

json_file_path = 'rabbit_records.json'
alive_rabbits = 100


def process_records(records):
    global alive_rabbits
    for record in records[-10:]:
        if record['deaths'] > alive_rabbits:
            continue
        alive_rabbits += (record['births'] - record['deaths'])
    return records[-10:]


def backend_simulation():
    while True:
        try:
            records = read_json(json_file_path)
            if len(records) >= 10:
                processed_records = process_records(records)
                write_json(processed_records, json_file_path)
        except Exception as exc:
            print(f"Backend Error: {exc}")
        time.sleep(1)