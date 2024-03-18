def read_records_from_file(filename="records.txt"):
    records = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                name, quantity = line.strip().split(", ")
                records[name] = int(quantity)
    except FileNotFoundError:
        print("Records file not found, starting with an empty collection.")
    except ValueError:
        print("Error reading records. Please check the file format.")
    return records


def write_records_to_file(records, filename="records.txt"):
    with open(filename, "w") as file:
        for name, quantity in records.items():
            file.write(f"{name}, {quantity}\n")


def add_record():
    records = read_records_from_file()
    name = input("Enter record name: ")
    quantity = input("Enter quantity: ")

    if not quantity.isdigit() or int(quantity) <= 0:
        print("Invalid quantity. Please enter a positive integer.")
        return

    if name in records:
        print("Record already exists. Updating quantity.")
        records[name] += int(quantity)
    else:
        records[name] = int(quantity)

    write_records_to_file(records)
    print("Record added/updated successfully.")


def display_collection_sorted():
    records = read_records_from_file()
    if not records:
        print("The collection is empty.")
        return

    for name in sorted(records):
        print(f"Record Name: {name}, Quantity: {records[name]}")


def exit_program():
    print("Exiting program. Goodbye!")
    exit()


def delete_record():
    records = read_records_from_file()
    name = input("Enter the name of the record to delete: ")
    if name in records:
        del records[name]
        write_records_to_file(records)
        print(f"Record '{name}' deleted successfully.")
    else:
        print(f"Record '{name}' not found.")


def search_record():
    records = read_records_from_file()
    name = input("Enter the name of the record to search for: ")
    if name in records:
        print(f"Record found: {name}, Quantity: {records[name]}")
    else:
        print(f"Record '{name}' not found.")


def update_record_name():
    records = read_records_from_file()
    old_name = input("Enter the current name of the record: ")
    if old_name in records:
        new_name = input("Enter the new name of the record: ")
        records[new_name] = records.pop(old_name)
        write_records_to_file(records)
        print(f"Record name updated from '{old_name}' to '{new_name}'.")
    else:
        print(f"Record '{old_name}' not found.")


def update_record_quantity():
    records = read_records_from_file()
    name = input("Enter the name of the record to update: ")
    if name in records:
        quantity = input("Enter the new quantity: ")
        if not quantity.isdigit() or int(quantity) <= 0:
            print("Invalid quantity. Please enter a positive integer.")
            return
        records[name] = int(quantity)
        write_records_to_file(records)
        print(f"Record '{name}' updated successfully.")
    else:
        print(f"Record '{name}' not found.")


def print_total_quantity():
    records = read_records_from_file()
    total_quantity = sum(records.values())
    print(f"Total quantity of all records: {total_quantity}")


def main_menu():
    while True:
        print("\nRecord Collection Management:")
        print("1. Add Record")
        print("2. Delete Record")
        print("3. Search for a Record by Name")
        print("4. Update Record Name")
        print("5. Update Record Quantity")
        print("6. Print Total Quantity of Records")
        print("7. Display Collection Sorted")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_record()
        elif choice == "2":
            delete_record()
        elif choice == "3":
            search_record()
        elif choice == "4":
            update_record_name()
        elif choice == "5":
            update_record_quantity()
        elif choice == "6":
            print_total_quantity()
        elif choice == "7":
            display_collection_sorted()
        elif choice == "8":
            exit_program()
            break
        else:
            print("Invalid choice. Please enter a number between 1-8.")


if __name__ == "__main__":
    main_menu()
