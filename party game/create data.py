import json


def create_places_json():
    places = [
        "Ancient Castle", "Mysterious Forest", "Abandoned Warehouse",
        "Luxurious Mansion", "Secluded Beach", "Bustling City Square",
        "Quiet Suburban Home", "Creepy Carnival", "Secret Underground Lab",
        "High-Tech Space Station", "Old Lighthouse", "Haunted Graveyard",
        "Snowy Mountain Cabin", "Deserted Island", "Royal Palace",
        "Downtown Rooftop", "Medieval Village", "Underwater Bunker",
        "Enchanted Garden", "Majestic Library"
    ]
    with open('places.json', 'w') as f:
        json.dump(places, f, indent=4)


def create_weapons_json():
    weapons = [
        "Candlestick", "Dagger", "Lead Pipe", "Revolver", "Rope",
        "Wrench", "Poison", "Crossbow", "Trophy", "Fire Poker"
    ]
    with open('weapons.json', 'w') as f:
        json.dump(weapons, f, indent=4)


if __name__ == "__main__":
    create_places_json()
    create_weapons_json()
    print("places.json and weapons.json have been created successfully.")
