import os

import matplotlib
import matplotlib.pyplot as plt
import random
import time

from complexity.feb import fib, fibonacci
from complexity.search_in_list import search, binary_search
import two_sum


def calculate_execution_time(func, *args):
    start_time = time.perf_counter()
    func(*args)
    end_time = time.perf_counter()
    return round(end_time - start_time, 5)


def generate_unique_numbers(num):
    return random.sample(range(1, num * 2), num)


def test_functions():
    nums = [2 ** x for x in range(1, 2)]
    results = {
        'optimized_two_sum': [],
        'brute_two_sum': [],
        'fib': [],
        'binary_search': [],
        'iterative_search': [],
        'fibonacci': []
    }

    for num in nums:
        rand_num = random.randint(2, num)
        unique_numbers = generate_unique_numbers(num)
        target_sum = random.choice(unique_numbers) + random.choice(unique_numbers)

        results['optimized_two_sum'].append(
            (num, calculate_execution_time(two_sum.optimized_two_sum, target_sum, unique_numbers)))
        results['brute_two_sum'].append(
            (num, calculate_execution_time(two_sum.brute_two_sum, target_sum, unique_numbers)))

        results['fib'].append((num, calculate_execution_time(fib, num)))
        results['fibonacci'].append((num, calculate_execution_time(fibonacci, num)))

        sorted_numbers = sorted(unique_numbers)
        results['iterative_search'].append((num, calculate_execution_time(search, sorted_numbers, target_sum)))
        results['binary_search'].append((num, calculate_execution_time(binary_search, sorted_numbers, target_sum)))

    return results


def draw_results(results):
    try:
        # Debug: Print the current backend and working directory
        print(f"Current Matplotlib backend: {matplotlib.get_backend()}")
        print(f"Current working directory: {os.getcwd()}")

        plt.figure(figsize=(10, 6))
        with open('performance.txt', 'w') as f:
            f.write("Algorithm Performance Comparison\n")
            f.write("Function, Input Size, Time (seconds)\n")
            for func_name, data in results.items():
                for size, time in data:
                    f.write(f"{func_name}, {size}, {time}\n")

        plt.figure(figsize=(10, 6))  # Create a new figure with a specified size
        for func_name, data in results.items():
            list_size = [val[0] for val in data]
            times = [val[1] for val in data]
            plt.plot(list_size, times, marker='o', label=func_name)  # Added markers for clarity

        plt.xlabel('Input Size')
        plt.ylabel('Time (seconds)')
        plt.title('Algorithm Performance Comparison')
        plt.legend()
        plt.grid(True)

        plt.savefig('plot.png', bbox_inches='tight')  # Save the plot as a PNG file
        print("Plot saved.")  # Debug: Confirm the plot is saved

        plt.show()
        print("Plot shown.")  # Debug: Confirm the plot is shown

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    results = test_functions()
    draw_results(results)
