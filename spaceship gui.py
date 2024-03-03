import tkinter as tk
from tkinter import ttk

from space_explorations import *


class SpaceShipGUI:
    def __init__(self, master, spaceship):
        self.master = master
        self.spaceship = spaceship

        master.title("SpaceShip Thruster Control")

        self.status_label = ttk.Label(master, text="Use the mouse and arrow keys to control the spaceship")
        self.status_label.pack()

        self.update_status()

        master.bind("<Left>", lambda e: self.move_ship('W'))
        master.bind("<Right>", lambda e: self.move_ship('E'))
        master.bind("<Button-1>", lambda e: self.move_ship('F'))
        master.bind("<Button-3>", lambda e: self.move_ship('B'))

        master.focus_set()  # Focus on the window to capture key events

    def move_ship(self, direction):
        # Simplified movement logic for demonstration
        if direction == 'N':  # Not used in this setup
            self.spaceship.location.coordinatesXYZ.Y += 10
        elif direction == 'S':  # Not used in this setup
            self.spaceship.location.coordinatesXYZ.Y -= 10
        elif direction == 'E':
            self.spaceship.location.coordinatesXYZ.X += 10
        elif direction == 'W':
            self.spaceship.location.coordinatesXYZ.X -= 10
        elif direction == 'F':  # Forward movement
            self.spaceship.location.coordinatesXYZ.Z += 10
        elif direction == 'B':  # Backward movement
            self.spaceship.location.coordinatesXYZ.Z -= 10

        self.update_status()

    def update_status(self):
        self.status_label[
            'text'] = f"Location: X={self.spaceship.location.coordinatesXYZ.X}, Y={self.spaceship.location.coordinatesXYZ.Y}, Z={self.spaceship.location.coordinatesXYZ.Z}"


# Setup and run the GUI
def run_gui(spaceship):
    root = tk.Tk()
    gui = SpaceShipGUI(root, spaceship)
    root.mainloop()


"""
if __name__ == "__main__":
    spaceship = SpaceShip("Explorer", 100, 100)  # Assuming a spaceship instance
    spaceship.location = Location("Space", CoordinationXYZ(0, 0, 0))  # Setting an initial location
    run_gui(spaceship)
"""

"""
import pygame
import sys

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Simulator GUI")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw GUI elements here
    # For example, a simple rectangle as a button
    pygame.draw.rect(screen, (255, 0, 0), (350, 275, 100, 50))

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()
"""
import tkinter as tk
from tkinter import ttk


# Assuming the SpaceShip, Player, CoordinationXYZ, and Location classes are defined as provided above

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
