from random import random


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

