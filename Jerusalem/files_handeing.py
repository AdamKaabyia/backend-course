import time
from wb import *
from decode_incode import *
import os


def compress_files_with_stats(file_paths, archive_path, unit_size):
    # This will create a simple archive with added functionality to display compression stats for each file.
    archive_data = bytearray()
    total_original_size = 0
    total_compressed_size = 0
    start_time = time.time()

    for file_path in file_paths:
        # Read the file in binary mode
        with open(file_path, 'rb') as f:
            file_data = f.read()

        original_size = len(file_data)
        total_original_size += original_size

        # Encode the file data
        encoded_data = run_length_encode(file_data, unit_size)
        compressed_size = len(encoded_data)
        total_compressed_size += compressed_size

        # Calculate compression ratio for each file
        compression_ratio = ((original_size - compressed_size) / original_size) * 100 if original_size > 0 else 0

        # Append the size of the file name, the file name itself, the size of the encoded content, and then the encoded content
        archive_data.extend(len(file_path).to_bytes(4, byteorder='big'))
        archive_data.extend(file_path.encode('utf-8'))
        archive_data.extend(len(encoded_data).to_bytes(4, byteorder='big'))
        archive_data.extend(encoded_data)

        # Print stats for the current file
        print(
            f"File: {file_path} - Original size: {original_size} bytes, Compressed size: {compressed_size} bytes, Compression ratio: {compression_ratio:.2f}%.")

    # Write the combined archive data to a binary file
    write_to_binary_file(archive_path, archive_data)

    # Calculate and print overall stats
    total_duration = time.time() - start_time
    overall_compression_ratio = ((
                                         total_original_size - total_compressed_size) / total_original_size) * 100 if total_original_size > 0 else 0
    print(f"\nTotal compression completed in {total_duration:.2f} seconds.")
    print(
        f"Overall original size: {total_original_size} bytes, Overall compressed size: {total_compressed_size} bytes, Overall compression ratio: {overall_compression_ratio:.2f}%.")


def extract_files(archive_path, unit_size, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(archive_path, 'rb') as f:
        archive_data = f.read()

    i = 0
    while i < len(archive_data):
        try:
            if i + 4 > len(archive_data):
                raise ValueError("Unexpected end of archive data.")
            file_name_size = int.from_bytes(archive_data[i:i + 4], byteorder='big')
            i += 4

            if i + file_name_size > len(archive_data):
                raise ValueError("File name goes beyond archive data.")
            file_name = archive_data[i:i + file_name_size].decode('utf-8')
            i += file_name_size

            if i + 4 > len(archive_data):
                raise ValueError("Unexpected end of archive data before encoded data size.")
            encoded_data_size = int.from_bytes(archive_data[i:i + 4], byteorder='big')
            i += 4

            if i + encoded_data_size > len(archive_data):
                raise ValueError("Encoded data goes beyond archive data.")
            encoded_data = archive_data[i:i + encoded_data_size]
            i += encoded_data_size

            file_data = run_length_decode(encoded_data, unit_size)

            full_path = os.path.join(output_folder, file_name)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'wb') as file:
                file.write(file_data)
        except ValueError as e:
            print(f"Error extracting archive: {e}")
            break  # or continue, based on your strategy
