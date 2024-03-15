from .truck_base import TruckBase

class Volvo(TruckBase):
    def __init__(self):
        super().__init__("Volvo", 30, 2.5, 0.05, 100, 100)  # Added mental_health value

    def display_truck_info(self):
        print(f"Volvo Truck - Max Fuel: {self.fuel}, KM/L: {self.km_per_liter}, Wheel Repair Cost/KM: {self.wheel_repair_cost_per_km}, Wheel Condition: {self.wheel_condition}, Mental Health: {self.mental_health}")
