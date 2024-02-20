import random


class Pokemon:
    def __init__(self, name, level, strength, speed, pokemon_type, life):
        self.name = name
        self.level = level
        self.strenght = strength
        self.speed = speed
        self.pokemon_type = pokemon_type
        self.life = life


def damage(modifier, strength):
    return int(modifier) * (random.randint(1, 20) + int(strength))


def modifier_calculator(attacker, defender):
    match defender.pokemon_type:
        case "fire":
            if attacker.pokemon_type == "earth":
                return 2
            return 1
        case "water":
            if attacker.pokemon_type == "wind":
                return 2
            return 1
        case "earth":
            if attacker.pokemon_type == "water":
                return 2
            return 1
        case "wind":
            match attacker.pokemon_type:
                case "fire":
                    return 2
                case "earth":
                    return 2
            return 1

def CalculateSpeed(pokemon):
    return pokemon.speed + random.randint(1, 20)

def WhoAttacks(pokemon1, pokemon2):
    if (CalculateSpeed(pokemon1) > CalculateSpeed(pokemon2)):
        return pokemon1
    else:
        return pokemon2

class player:
    def __init__(self, pokemons=None):
        self.pokemons = pokemons

    def pickPokemon(self):
        if self.pokemons is not None and len(self.pokemons) > 0 :
            return self.pokemons[random.randint(0, len(self.pokemons) - 1)]
        #return None


def isAlive(x):
    if x is not None:
        return x.life > 0 and x.life <= 120
    #return None


FireDragon = Pokemon("FireDragon", 34, 7, 3, "fire", 70)
WindDragon = Pokemon("WindDragon", 63, 5, 5, "wind", 120)
WaterDragon = Pokemon("WaterDragon", 50, 6, 4, "water", 50)
EarthDragon = Pokemon("EarthDragon", 90, 9, 1, "earth", 100)

FireTurtle = Pokemon("FireTurtle", 34, 7, 3, "fire", 70)
WindTurtle = Pokemon("WindTurtle", 63, 5, 5, "wind", 120)
WaterTurtle = Pokemon("WaterTurtle", 50, 6, 4, "water", 50)
EarthTurtle = Pokemon("EarthTurtle", 90, 9, 1, "earth", 100)

WaterBird = Pokemon("WaterBird", 70, 4, 5, "water", 38)
FireBird = Pokemon("FireBird", 64, 10, 1, "fire", 20)

### the plan we need to have a loop
player1 = player([FireTurtle, FireDragon, WaterTurtle, WindTurtle])
player2 = player([WindDragon, WaterDragon, EarthDragon, EarthTurtle])

# pokemon1=pokemon2=None
"""
if player1.pokemons is not None and player2.pokemons is not None:

"""
pokemon1 = player1.pickPokemon()
pokemon2 = player2.pickPokemon()
while player1.pokemons is not None and player2.pokemons is not None:

    while pokemon1 is not None and isAlive(pokemon1) and pokemon2 is not None and isAlive(pokemon2):
        # pokemon1 attacks pokemon
        if WhoAttacks(pokemon1, pokemon2) == pokemon1:
            dam = damage(modifier_calculator(pokemon1, pokemon2), pokemon1.strenght)
            print(pokemon1.name + " attacks " + pokemon2.name + " and deals: " + str(dam) + '\n')
            pokemon2.life -= int(dam)
        else:
            # pokemon2 attacks pokemon1
            dam = damage(modifier_calculator(pokemon2, pokemon1), pokemon2.strenght)
            print(pokemon2.name + " attacks " + pokemon1.name + " and deals: " + str(dam) + '\n')
            pokemon1.life -= int(dam)

    if isAlive(pokemon1):
        # we need to remove pokemon 2 from player2 arsenal
        if pokemon2 in player2.pokemons:
            player2.pokemons.remove(pokemon2)
            if pokemon2 in player2.pokemons:
                pokemon2 = player2.pickPokemon()
        else:
            break

    else:
        # we need to remove pokemon 1 from player 1 arsenal
        if pokemon1 in player1.pokemons:
            player1.pokemons.remove(pokemon1)
            if player1.pokemons is not None:
                pokemon1 = player1.pickPokemon()
        else:
            break

if player1.pokemons is None and player2.pokemons is None:
    print("Its a tie")
elif player1.pokemons is None:
    print("player 2 won!!!!!!!!!!")
else:
    print("player 1 won!!!!!!!!!!")
