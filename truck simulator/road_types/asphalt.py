from road_type_base import RoadTypeBase


class Asphalt(RoadTypeBase):
    def __init__(self):
        super().__init__("Asphalt", terrain_hardness=1, mental_effect=0.1, wheel_damage_effect=0.01)
