import logging


def calculate_fuel_consumption(truck, road):
    # Simplified example: fuel consumption might increase based on terrain hardness
    fuel_consumption = road.length / truck.km_per_liter * road.terrain_hardness
    return fuel_consumption


def calculate_wheel_wear(truck, road):
    # Example: wheel wear could increase based on the road's wheel damage effect
    wheel_wear = road.length * road.wheel_damage_effect
    return wheel_wear


def calculate_mental_health_effect(truck, road):
    mental_health_effect = road.length * road.mental_effect
    return mental_health_effect


def simulate_journey(truck, road):
    fuel_consumed = calculate_fuel_consumption(truck, road)
    wheel_wear = calculate_wheel_wear(truck, road)
    mental_health_effect = calculate_mental_health_effect(truck, road)

    truck.fuel -= fuel_consumed
    truck.wheel_condition -= wheel_wear
    truck.mental_health += mental_health_effect  # Assuming mental_effect is negative for difficult roads

    logging.info(f"Journey on {road.name}: {road.length}km")
    logging.info(
        f"Fuel consumed: {fuel_consumed:.2f}, Wheel condition: {truck.wheel_condition}, Driver's mental health: {truck.mental_health}")

    return truck.fuel > 0 and truck.wheel_condition > 0 and truck.mental_health > 0
