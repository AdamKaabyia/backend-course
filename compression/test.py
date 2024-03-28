from compression import *
from compression.files_handeing import *
from compression.folder_handeling import *


def main():
    folder_path = r"/compression\recursion"
    archive_path = r"C:\Users\akaab\Downloads\recursion_test"  # Specify the name of the archive file as well
    unit_size = 1  # Size of units in bytes for run length encoding
    compress_directory(folder_path, archive_path, unit_size)
    output_folder = r'C:\Users\akaab\PycharmProjects\backend-course\Jerusalem\recursion_test'  # Specify where to extract the files
    decompress_directory(archive_path, output_folder, unit_size)


if __name__ == "__main__":
    main()
