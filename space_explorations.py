import random
import time
import math
import json
from datetime import datetime


class CoordinationXYZ:
    def __init__(self, X, Y, Z):
        self.X = X
        self.Y = Y
        self.Z = Z


class Location:
    def __init__(self, object, coordinatesXYZ, time=None):
        self.object = object
        self.coordinatesXYZ = coordinatesXYZ
        self.time = time if time is not None else datetime.now()


class SpaceShip:
    def __init__(self, name, fuel, health):
        self.name = name
        self.fuel = fuel
        self.health = health
        self.location = Location("Space", CoordinationXYZ(0, 0, 0))  # Initial location not set

    def move_to(self, new_coordinatesXYZ):
        if self.fuel <= 0:
            print("Not enough fuel to move.")
            return
        self.fuel -= 10
        self.location = Location("Space", new_coordinatesXYZ)
        print(
            f"{self.name} moved to new location: X={new_coordinatesXYZ.X}, Y={new_coordinatesXYZ.Y}, Z={new_coordinatesXYZ.Z}. Remaining fuel: {self.fuel}")

    def __str__(self):
        location_str = f"Location: X={self.location.coordinatesXYZ.X}, Y={self.location.coordinatesXYZ.Y}, Z={self.location.coordinatesXYZ.Z}" if self.location else "Unknown Location"
        return f'Name: {self.name}, Fuel: {self.fuel}, Health: {self.health}, {location_str}'


class Player:
    def __init__(self, name, ship):
        self.name = name
        self.ship = ship

    def explore(self, new_location):
        self.ship.move_to(new_location)


def asteroid_field(player, intensity=23):
    player.ship.health -= intensity


def space_pirates(player, intensity=10):
    player.ship.health -= intensity
    player.ship.fuel -= intensity


def alien_diplomacy(player):
    player.ship.fuel += 1000
    player.ship.health += 1000


def black_hole(player):
    x, y, z = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)
    player.explore(CoordinationXYZ(x, y, z))


import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import json
from datetime import datetime


def simulate_external_data():
    weather_conditions = ['sunny', 'stormy', 'meteor shower', 'peaceful']
    return random.choice(weather_conditions)


def save_game_state(player):
    state = {
        'name': player.name,
        'ship': {
            'name': player.ship.name,
            'fuel': player.ship.fuel,
            'health': player.ship.health,
            'location': {
                'X': player.ship.location.coordinatesXYZ.X,
                'Y': player.ship.location.coordinatesXYZ.Y,
                'Z': player.ship.location.coordinatesXYZ.Z
            }
        }
    }
    with open('game_state.json', 'w') as file:
        json.dump(state, file)


def load_game_state():
    with open('game_state.json', 'r') as file:
        state = json.load(file)
    ship_location = CoordinationXYZ(**state['ship']['location'])
    ship = SpaceShip(state['ship']['name'], state['ship']['fuel'], state['ship']['health'])
    ship.location = Location("Space", ship_location)
    player = Player(state['name'], ship)
    return player


def handle_space_event(player):
    events = [asteroid_field, space_pirates, alien_diplomacy, black_hole]
    event = random.choice(events)
    event(player)


def update_status():
    status_var.set(
        f"Status: Name={player.ship.name}, Fuel={player.ship.fuel}, Health={player.ship.health}, Location=({player.ship.location.coordinatesXYZ.X}, {player.ship.location.coordinatesXYZ.Y}, {player.ship.location.coordinatesXYZ.Z})"
    )
    weather = simulate_external_data()
    messagebox.showinfo("Galactic Weather Update", f"Current weather: {weather}")


def move_spaceship():
    x = simpledialog.askinteger("Input", "Enter X coordinate:")
    y = simpledialog.askinteger("Input", "Enter Y coordinate:")
    z = simpledialog.askinteger("Input", "Enter Z coordinate:")
    player.explore(CoordinationXYZ(x, y, z))
    handle_space_event(player)
    update_status()


def main_gui(player):
    global status_var
    root = tk.Tk()
    root.title("Space Exploration Game")

    tk.Button(root, text="Move Spaceship", command=move_spaceship).pack()
    tk.Button(root, text="Save Game", command=lambda: save_game_state(player)).pack()
    tk.Button(root, text="Load Game", command=lambda: load_game_state()).pack()

    status_var = tk.StringVar(root)
    tk.Label(root, textvariable=status_var).pack()

    update_status()
    root.mainloop()


try:
    player = load_game_state()
except FileNotFoundError:
    ship = SpaceShip("Explorer", 100, 100)
    player = Player("Astronaut John", ship)

main_gui(player)
