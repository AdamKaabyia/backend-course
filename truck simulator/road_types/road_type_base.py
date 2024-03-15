
class RoadTypeBase:
    def __init__(self, name, terrain_hardness, mental_effect, wheel_damage_effect, length=100):
        self.name = name
        self.terrain_hardness = terrain_hardness
        self.mental_effect = mental_effect
        self.wheel_damage_effect = wheel_damage_effect
        self.length = length  # Default length; can be overridden in specific road types if needed
