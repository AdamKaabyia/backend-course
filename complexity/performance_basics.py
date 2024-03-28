import time
from typing import List, Tuple, Callable, Dict
import matplotlib.pyplot as plt

from search_in_list import *


def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int) -> List[int]:
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence[:n]


def time_function(func: Callable, arg: int) -> Tuple[float, List[int]]:
    start_time = time.time()
    result = func(arg)
    end_time = time.time()
    return end_time - start_time, result


def measure_performance(func: Callable, magnitudes: List[int]) -> Dict[int, float]:
    times = {}
    for magnitude in magnitudes:
        time_taken, _ = time_function(func, magnitude)
        times[magnitude] = time_taken
    return times


input_sizes = [1, 10, 20, 30]  # Define the input sizes we will test

recursive_times = measure_performance(fibonacci_recursive, input_sizes)
iterative_times = measure_performance(fibonacci_iterative, input_sizes)

with open('fibonacci_performance.txt', 'w') as f:  # Write the results to a file
    f.write("Fibonacci Performance\n")
    f.write("Input Size,Recursive Time,Iterative Time\n")
    for n in input_sizes:
        f.write(f"{n},{recursive_times.get(n, 'N/A')},{iterative_times[n]}\n")

plt.figure(figsize=(10, 5))  # Now we'll generate a plot of the results
plt.plot(list(recursive_times.keys()), list(recursive_times.values()), marker='o', label='Recursive')
plt.plot(list(iterative_times.keys()), list(iterative_times.values()), marker='o', label='Iterative')
plt.xlabel('Input Size')
plt.ylabel('Time in seconds')
plt.title('Fibonacci Performance Comparison')
plt.legend()
plt.grid(True)
plt.savefig('fibonacci_performance.png')  # Ensure this path is accessible
