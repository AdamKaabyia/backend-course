import time
from db import read_json

json_file_path = 'rabbit_records.json'


def analyze_records():
    try:
        records = read_json(json_file_path)
        alive_rabbits = 100
        for record in records:
            if record['deaths'] > alive_rabbits:
                print("Error: Deaths exceed number of alive rabbits. Record ignored.")
                continue
            alive_rabbits += record['births'] - record['deaths']
        print(f"Currently alive rabbits: {alive_rabbits}")
    except Exception as e:
        print(f"Error analyzing records: {e}")


def backend_simulation():
    while True:
        analyze_records()
        time.sleep(10)
