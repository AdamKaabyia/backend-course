def write_to_binary_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)
