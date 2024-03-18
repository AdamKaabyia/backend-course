import random


class Player:
    def __init__(self, name, favorite_weapons):
        self.name = name
        self.favorite_weapons = favorite_weapons
        self.visited_places = []
        self.is_assassin = False

    def visit_places(self, places):
        self.visited_places = random.sample(places, random.randint(1, 3))

    def suspect_players(self, players):
        suspects = random.sample(players, 2)
        print(f"{self.name} suspects: {[p.name for p in suspects]}")
        for suspect in suspects:
            print(f" - {suspect.name}'s Visited Places: {suspect.visited_places}")
            print(f" - {suspect.name}'s Favorite Weapon: {random.choice(suspect.favorite_weapons)}")

    def accuse_player(self, players):
        accused = random.choice(players)
        print(f"{self.name} accuses {accused.name}")
        return accused
