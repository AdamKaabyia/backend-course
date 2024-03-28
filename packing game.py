class Item:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.category} - {self.name} (Weight: {self.weight})'


class Electronics(Item):
    def __init__(self, name, weight, brand, connectivity, **extra_properties):
        super().__init__(name, weight, 'Electronics')
        self.brand = brand
        self.connectivity = connectivity
        self.extra_properties = extra_properties

    def __str__(self):
        extra = ', '.join(f"{key}: {value}" for key, value in self.extra_properties.items())
        return f"{super().__str__()}, Brand: {self.brand}, Connectivity: {self.connectivity}, {extra}"


class TravelItem(Item):
    def __init__(self, name, weight, color, cost, bought_from):
        super().__init__(name, weight, 'Travel')
        self.color = color
        self.cost = cost
        self.bought_from = bought_from

    def __str__(self):
        return f"{super().__str__()}, Color: {self.color}, Cost: {self.cost}, Bought from: {self.bought_from}"


class Wearable(Item):
    def __init__(self, name, weight, brand, has_case=None, **extra_properties):
        super().__init__(name, weight, 'Wearable')
        self.brand = brand
        self.has_case = has_case
        self.extra_properties = extra_properties

    def __str__(self):
        extra = ', '.join(f"{key}: {value}" for key, value in self.extra_properties.items())
        case_str = f", Has case: {self.has_case}" if self.has_case is not None else ""
        return f"{super().__str__()}, Brand: {self.brand}{case_str}, {extra}"


class Bag:
    MAX_WEIGHT = 80
    MAX_ITEMS = 6

    def __init__(self):
        self.items = []

    def add_item(self, item):
        if sum(i.weight for i in self.items) + item.weight > Bag.MAX_WEIGHT:
            return "Cannot add item, weight limit exceeded."
        if len(self.items) >= Bag.MAX_ITEMS:
            return "Cannot add item, item limit exceeded."
        self.items.append(item)
        return f"Added {item.name} to the bag."

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return f"Removed {item.name} from the bag."
        return f"Item {item_name} not found in the bag."

    def print_items(self):
        for item in self.items:
            print(item)

    def print_items_by_category(self, category_name):
        category_map = {
            'Electronics': Electronics,
            'Travel': TravelItem,
            'Wearable': Wearable
        }
        category_class = category_map.get(category_name)
        if category_class:
            for item in self.items:
                if isinstance(item, category_class):
                    print(item)
        else:
            print("Invalid category.")


def main():
    bag = Bag()
    while True:
        command = input("Enter command (add_electronics, add_travel, add_wearable, remove, list, list by category, or quit): ").lower()
        match command:
        ### in general - no input validation. what if the user puts in something wrong?
            case "add_electronics":
                ### DRY with many properties below
                name = input("Enter electronics name: ")
                weight = int(input("Enter weight: "))
                brand = input("Enter brand: ")
                connectivity = input("Enter connectivity: ")
                extra_properties = {}
                while True:
                    property_name = input("Enter extra property name (or leave blank to finish): ").strip()
                    if not property_name:
                        break
                    property_value = input(f"Enter value for {property_name}: ")
                    extra_properties[property_name] = property_value
                ### if putting the item inside the bag is impossible, is there a reason to create the item? same for all the rest of item craetions
                item = Electronics(name, weight, brand, connectivity, **extra_properties)
                print(bag.add_item(item))

            case "add_travel":
                name = input("Enter travel item name: ")
                weight = int(input("Enter weight: "))
                color = input("Enter color: ")
                cost = int(input("Enter cost: "))
                bought_from = input("Enter bought from: ")
                extra_properties = {}
                while True:
                    property_name = input("Enter extra property name (or leave blank to finish): ").strip()
                    if not property_name:
                        break
                    property_value = input(f"Enter value for {property_name}: ")
                    extra_properties[property_name] = property_value
                item = TravelItem(name, weight, color, cost, bought_from, **extra_properties)
                print(bag.add_item(item))

            case "add_wearable":
                name = input("Enter wearable name: ")
                weight = int(input("Enter weight: "))
                brand = input("Enter brand: ")
                has_case = input("Has case? (yes/no): ").lower() == 'yes'
                extra_properties = {}
                while True:
                    property_name = input("Enter extra property name (or leave blank to finish): ").strip()
                    if not property_name:
                        break
                    property_value = input(f"Enter value for {property_name}: ")
                    extra_properties[property_name] = property_value
                    ### nice usage of kwargs
                item = Wearable(name, weight, brand, has_case, **extra_properties)
                print(bag.add_item(item))

            case "remove":
                name = input("Enter item name to remove: ")
                print(bag.remove_item(name))

            case "list":
                bag.print_items()

            case "list by category":
                category_name = input("Enter category (Electronics, Travel, Wearable): ")
                bag.print_items_by_category(category_name)

            case "quit":
                print("Exiting the packing game.")
                break

            case _:
                print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
