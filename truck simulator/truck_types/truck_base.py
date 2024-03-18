from abc import ABC, abstractmethod

class TruckBase(ABC):
    def __init__(self, brand, max_fuel, km_per_liter, wheel_repair_cost_per_km, wheel_condition, mental_health):
        self.brand = brand
        self.fuel = max_fuel
        self.km_per_liter = km_per_liter
        self.wheel_repair_cost_per_km = wheel_repair_cost_per_km
        self.wheel_condition = wheel_condition
        self.mental_health = mental_health  # Add this line

    @abstractmethod
    def display_truck_info(self):
        pass

    def can_complete_journey(self, road):
        max_distance = self.fuel * self.km_per_liter
        return max_distance >= road.length  # Simplified check
