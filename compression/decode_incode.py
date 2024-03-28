def run_length_encode(input_bytes, unit_size):
    unit_size = int(unit_size)
    encoded_bytes = bytearray()
    i = 0
    while i < len(input_bytes):
        current_unit = input_bytes[i:i + unit_size]
        count = 1
        while i + unit_size < len(input_bytes) and input_bytes[i:i + unit_size] == input_bytes[
                                                                                   i + unit_size:i + 2 * unit_size]:
            i += unit_size
            count += 1

        # Append count and unit
        encoded_bytes.extend(count.to_bytes(1, byteorder='big'))
        encoded_bytes.extend(current_unit)
        i += unit_size

    return bytes(encoded_bytes)


def run_length_decode(encoded_bytes, unit_size):
    unit_size = int(unit_size)  # Ensure unit_size is an integer
    decoded_bytes = bytearray()
    i = 0
    while i < len(encoded_bytes):
        count = encoded_bytes[i]
        i += 1
        current_unit = encoded_bytes[i:i + unit_size]
        decoded_bytes.extend(current_unit * count)
        i += unit_size

    return bytes(decoded_bytes)
