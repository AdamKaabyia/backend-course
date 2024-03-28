
from space_explorations import *

import tkinter as tk
from tkinter import ttk

class SpaceGameGUI:
    def __init__(self, master, player):
        self.master = master
        self.player = player
        master.title("Space Exploration Game")

        self.status_label = ttk.Label(master, text="SpaceShip Status")
        self.status_label.pack()

        ttk.Button(master, text="Explore", command=self.explore_space).pack()

        self.update_status()

    def explore_space(self):
        self.player.explore()
        self.update_status()

    def update_status(self):
        ship = self.player.ship
        status_text = f"Name: {ship.name}, Fuel: {ship.fuel}, Health: {ship.health}, Location: X={ship.location.coordinatesXYZ.X}, Y={ship.location.coordinatesXYZ.Y}, Z={ship.location.coordinatesXYZ.Z}"
        self.status_label.config(text=status_text)


def main():
    root = tk.Tk()
    ship = SpaceShip("Explorer", 100, 100)
    player = Player("Astronaut John", ship)
    gui = SpaceGameGUI(root, player)
    root.mainloop()


if __name__ == "__main__":
    main()
