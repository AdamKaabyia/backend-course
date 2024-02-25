import copy
import random

def split_list(input_list, chunk_size):
    return [
        input_list[i: i + chunk_size] for i in range(0, len(input_list), chunk_size)
    ]

points = {"win": 1, "lose": 0, "draw": 0.5}

class player:
    def __init__(self, name, total_points):
        self.name = name
        self.rank = random.randrange(1500, 2000)
        self.total_points = total_points

    def print(self):
        print(self.name, self.rank, self.total_points,'\n')


# returns the elo probability of the player with higher score to win
def probability_calculation(player1, player2):
    if player1.rank <= player2.rank:
        ratio = player1.rank / player2.rank
        reverse_ratio = 1 - ratio
        return 0.4 + reverse_ratio
    return probability_calculation(player2, player1)


def update_player_score(player, result):
    player.total_points += points[result]


def update_round_robin(array):
    size = (len(array[0]))
    new_array = copy.deepcopy(array)
    for i in range(0, size-1):
        new_array[0][i + 1] = array[0][i]
        new_array[1][i] = array[1][i + 1]
    # now edge cases
    new_array[0][0] = array[0][0]
    new_array[0][1] = array[1][0]
    new_array[1][size - 1] = array[0][size - 1]
    return new_array


"""
def elo_calculate(playerA,playerB):
    Ea=1/(1+10**((playerB.rank-playerA.rank)/400))
    Eb=1/(1+10**((playerA.rank-playerB.rank)/400))
    R_a=Ra+K*(Sa-Ea)
    R_b=Rb+K*(Sb-Eb)
"""


# game updates total points -V
# game updates elo rating
def game(player1, player2):
    if (random.randrange(1, 10) < 3):
        # draw
        update_player_score(player2, "draw")
        update_player_score(player1, "draw")
    else:
        if player1.rank <= player2.rank:
            tmp = player2
            player2 = player1
            player1 = tmp
        winner_probability_score = probability_calculation(player1, player2)

        # if player1.total_points>player2.total_points:
        if random.uniform(0, 0.8) < winner_probability_score:
            update_player_score(player1, "win")
            update_player_score(player2, "lose")
        else:
            update_player_score(player2, "win")
            update_player_score(player1, "lose")

players = []
number_of_players = 14

for i in range(1, number_of_players + 1):
    players.append(player("player" + str(i), 0))



round_robin_array = split_list(players, int(len(players) / 2))
round_robin_array[1].reverse()
for round in range(number_of_players - 1):  # n rounds
    # single round:
    for index, playerA in enumerate(round_robin_array[0]):
            playerB = round_robin_array[1][index]
            game(playerA, playerB)
    round_robin_array = update_round_robin(round_robin_array)
players = sorted(players,key=lambda x:x.total_points)

print("after the tornament:")
for val in players:
    print(val.print())

