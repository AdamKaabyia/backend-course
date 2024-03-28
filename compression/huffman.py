def build_frequency_table(data):
    frequency = {}
    for character in data:
        if character not in frequency:
            frequency[character] = 0
        frequency[character] += 1
    return frequency


import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For heap queue to compare nodes
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(frequency):
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    return priority_queue[0]  # Root of the Huffman Tree


def generate_codes(node, prefix="", code={}):
    if node is not None:
        if node.char is not None:
            code[node.char] = prefix
        generate_codes(node.left, prefix + "0", code)
        generate_codes(node.right, prefix + "1", code)
    return code


def encode(data, codes):
    encoded_data = "".join([codes[char] for char in data])
    return encoded_data


def decode(data, root):
    decoded_data = ""
    node = root
    for bit in data:
        if bit == "0":
            node = node.left
        else:
            node = node.right

        if node.char is not None:
            decoded_data += node.char
            node = root  # Reset for next character

    return decoded_data


def huffman_coding(data):
    frequency = build_frequency_table(data)
    root = build_huffman_tree(frequency)
    codes = generate_codes(root)
    encoded_data = encode(data, codes)
    decoded_data = decode(encoded_data, root)

    return encoded_data, decoded_data, codes


# Example Usage
data = "this is an example for huffman encoding"
encoded_data, decoded_data, codes = huffman_coding(data)
print(f"Original: {data}")
print(f"Encoded: {encoded_data}")
print(f"Decoded: {decoded_data}")
print(f"Codes: {codes}")
