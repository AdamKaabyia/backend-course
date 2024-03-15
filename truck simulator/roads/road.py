class RoadType:
    def __init__(self, name, terrain_hardness, mental_effect, wheel_damage_effect):
        self.name = name
        self.terrain_hardness = terrain_hardness
        self.mental_effect = mental_effect
        self.wheel_damage_effect = wheel_damage_effect


class Road:
    def __init__(self, road_type, length):
        self.road_type = road_type
        self.length = length
