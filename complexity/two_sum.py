import random


def generate_unique_numbers(n):
    numbers = set()
    while len(numbers) < n:
        numbers.add(random.randint(1, 10000))  # Adjust the range as needed
    return list(numbers)


def brute_two_sum(sum, num_list):
    indices = []
    for i, num1 in enumerate(num_list):
        for j, num2 in enumerate(num_list):
            if i != j and num1 + num2 == sum:
                indices.append((i, j))
    return indices


def optimized_two_sum(target_sum, num_list):
    indices = []
    num_to_index = {}
    for i, num in enumerate(num_list):
        complement = target_sum - num
        if complement in num_to_index:
            indices.append((num_to_index[complement], i))
        num_to_index[num] = i
    return indices
