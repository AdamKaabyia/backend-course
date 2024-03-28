

keys=[4, 93, 52, 12, 41, 23, 9, 1, 34, 2, 11, 111, 6, 13, 24, 99, 100,
30, 10, 26, 16, 29, 155, 32, 37, 61, 15, 42, 3, 633, 27, 70, 77,
45, 55, 43, 35, 108, 103, 56, 159, 166, 7, 8, 174, 36]


declaration_text = "When in the Course of human events..."

def decode_message(text, cipher):
    words = text.split()
    decoded_message = ''
    for number in cipher:
        word = words[number - 1] if number <= len(words) else ''
        decoded_message += word[0] if word else ''
    return decoded_message


# Decode the message
message = decode_message(declaration_text, keys)
print(f"Decoded message: {message}")
