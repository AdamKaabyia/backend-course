import os
from multiprocessing import Process, Queue
from collections import defaultdict
import time
import unicodedata


def count_letters(file_path, start_index, end_index, result_queue):
    letter_count = defaultdict(int)
    with open(file_path, 'r') as file:
        file.seek(start_index)
        chunk = file.read(end_index - start_index)
        for char in chunk:
            if char.isalpha() and 'LATIN' in unicodedata.name(char):
                letter_count[char.lower()] += 1
    result_queue.put(letter_count)


def main():
    file_path = 'TheStory.txt'
    file_size = os.path.getsize(file_path)
    chunk_size = file_size

    start_time = time.time()

    processes = []
    result_queue = Queue()

    for i in range(3):
        start_index = i * chunk_size
        end_index = start_index + chunk_size if i < 2 else file_size
        process = Process(target=count_letters, args=(file_path, start_index, end_index, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    total_time = end_time - start_time

    final_result = defaultdict(int)
    while not result_queue.empty():
        letter_count = result_queue.get()
        for char, count in letter_count.items():
            final_result[char] += count
    final_result = sorted(final_result.items(), key=lambda k_v: k_v[1], reverse=True)
    print('final_result: ', final_result)
    print(f"Total time taken: {total_time:.2f} seconds")


if __name__ == "__main__":
    main()
