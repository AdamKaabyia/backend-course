from space_exploration_classes import *
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
