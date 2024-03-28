import threading
#from sensor import sensor_simulation

import analyzer
import sensor_seperate as S
import analyzer as A

from backend import backend_simulation
from db import write_json

json_file_path = 'rabbit_records.json'


def initialize_json_file():
    try:
        write_json([], json_file_path)  # Create an empty list in the JSON file
    except Exception as exc:
        print(f"Initialization Error: {exc}")


def main():
    initialize_json_file()

    # Start sensor and backend simulations in separate threads
    sensor_thread = threading.Thread(target=S.sensor_simulation)
    backend_thread = threading.Thread(target=A.backend_simulation)

    sensor_thread.start()
    backend_thread.start()

    sensor_thread.join()
    backend_thread.join()


if __name__ == "__main__":
    main()
