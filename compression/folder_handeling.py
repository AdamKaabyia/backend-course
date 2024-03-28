import os
from files_handeing import *
import time


def compress_folder(folder_path, archive_path, unit_size):
    if not os.path.isdir(folder_path):
        raise ValueError(f"Provided path is not a directory: {folder_path}")

    start_time = time.time()
    file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if
                  os.path.isfile(os.path.join(folder_path, f))]
    compress_files_with_stats(file_paths, archive_path, unit_size)
    duration = time.time() - start_time
    print(f"Compression completed in {duration:.2f} seconds.")


def extract_files_to_folder(archive_path, target_folder, unit_size):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    extract_files(archive_path, unit_size, target_folder)


def compress_directory(folder_path, archive_path, unit_size):
    start_time = time.time()
    file_paths = []

    # Traverse directory recursively
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Construct the full file path
            file_path = os.path.join(root, file)
            # Add file path to list
            file_paths.append(file_path)

    # Compress all collected file paths
    compress_files_with_stats(file_paths, archive_path, unit_size)

    # Calculate and print the duration of the compression process
    duration = time.time() - start_time
    print(f"Compression completed in {duration:.2f} seconds.")


def decompress_directory(archive_path, output_folder, unit_size):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # Extract files from the archive to the target folder
    extract_files(archive_path, unit_size, output_folder)