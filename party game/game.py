#from config_loader import load_places, load_weapons
from loader_json import *
from player import Player
import random

min_players = 3
max_players = 10
max_rounds = 10


class Game:
    def __init__(self, num_players):
        if not min_players <= num_players <= max_players:
            raise ValueError("Number of players must be between {min_players} and {max_players}.")
        self.places = load_places()
        self.weapons = load_weapons()
        self.players = [Player(f"Player{i}", random.sample(self.weapons, 3)) for i in range(num_players)]
        self.assassin = random.choice(self.players)
        self.assassin.is_assassin = True

    def start_game(self):
        print("Game started with the following players:")
        for player in self.players:
            print(f" - {player.name}")
        print(f"Assassin is: {self.assassin.name} (Secret)")

    def play_round(self):
        murder_weapon = random.choice(self.assassin.favorite_weapons)
        murder_place = random.choice(self.places)
        print(f"Murder happened at {murder_place} with {murder_weapon}")

        for player in self.players:
            player.visit_places(self.places)
            if player.is_assassin:
                player.visited_places.append(murder_place)  # Ensure assassin visits the murder place

        for player in self.players:
            player.suspect_players(self.players)
            accused = player.accuse_player(self.players)
            if accused.is_assassin:
                print(f"{player.name} correctly accused {accused.name}! Game Over.")
                return True
        return False


def main():
    try:
        num_players = int(input("Enter the number of players: "))
        game = Game(num_players)
    except ValueError as e:
        print(f"Error: {e}")
        return

    game.start_game()
    round_number = 1
    while True:
        print(f"\nRound {round_number}")
        if game.play_round():
            break
        round_number += 1
        if round_number > max_rounds:  # Optional: limit the number of rounds
            print(f"Reached maximum number of rounds {max_rounds}. Game Over.")
            break


if __name__ == "__main__":
    main()
