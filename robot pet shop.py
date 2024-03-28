class Robot:
    def __init__(self, name, robot_id, battery_type):
        self.name = name
        self.robot_id = robot_id
        self.battery_type = battery_type

    def update_state(self, new_state):
        self.state = new_state


"""
    def __str__(self):
        return f"Robot Name: {self.name}, ID: {self.robot_id}, Battery: {self.battery_type}"

"""


class pet(Robot):
    def __init__(self, name, robot_id, price, main_material, battery_type):
        super().__init__(name, robot_id, battery_type)
        self.price = price
        self.main_material = main_material
        self.state = "for sale"

    def update_state(self, new_state):
        self.state = new_state

    def __str__(self):
        return f"Robot Name: {self.name}, ID: {self.robot_id}, Price: {self.price}, Material: {self.main_material}, Battery: {self.battery_type}, State: {self.state}"


class Employee(Robot):
    def __init__(self, name, employee_id, salary, battery_type):
        super().__init__(name, employee_id, battery_type)
        self.salary = salary

    def __str__(self):
        return f"Robot Name: {self.name}, ID: {self.robot_id}, salary: {self.salary}, Battery: {self.battery_type}"


class PetShop:
    def __init__(self):
        self.pets = []
        self.employees = []
        self.balance = 0.0

    def add_pet(self, robot):
        self.pets.append(robot)

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_pets_for_sale(self):
        return [pet for pet in self.pets if pet.state == "for sale"]

    def update_balance(self, amount):
        self.balance += amount

    def display_balance(self):
        print(f"Current Store Balance: ${self.balance}")

    def repair_pet_robot(self, robot_id, repair_cost):
        robot_pet = next((pet for pet in self.pets if pet.robot_id == robot_id), None)
        if robot_pet:
            robot_pet.update_state("in repair")
            self.update_balance(-repair_cost)  # Deduct repair cost from balance

    def robots_by_price_range(self, min_price, max_price):
        return [pet for pet in self.pets if min_price <= pet.price <= max_price]

    def robots_by_state(self, state):
        return [pet for pet in self.pets if pet.state == state]

    def print_all_employees_salary(self):
        for x in self.employees:
            print(x)

    def return_robot_by_id_or_name(self, id=None, name=None):
        pets_id_match = [pet for pet in self.pets if pet.robot_id == id]
        pets_name_match = [pet for pet in self.pets if pet.name == name]
        employees_id_match = [employee for employee in self.employees if employee.robot_id == id]
        employees_name_match = [employee for employee in self.employees if employee.name == name]
        return pets_id_match+ pets_name_match+employees_id_match+employees_name_match


pet_shop = PetShop()
pet_shop.add_pet(pet("RoboDog", "001", 1500, "Metal", "Lithium-ion"))
pet_shop.add_pet(pet("JimCat", "012", 600, "aluminium", "hydroelectric"))

pet_shop.add_employee(Employee("Jane Doe", "E001", 50000, "solar"))
pet_shop.add_employee(Employee("kim", "7563", 900000, "nuclear"))
for pets in pet_shop.list_pets_for_sale():
    print(pets)
print("\n")
pet_shop.print_all_employees_salary()
print("\n")

for x in pet_shop.return_robot_by_id_or_name(name="kim"):
    print(x)
