import random

# Define the moves with numbers
moves = {1: 'Jab', 2: 'Cross', 3: 'Hook', 4: 'Uppercut'}

# Define the winning logic
winning_moves = {1: 4, 2: 3, 3: 1, 4: 2}  # For example, Jab (1) beats Uppercut (4), etc.


def simulate_round():
    user_move = int(input("Choose your move (1: Jab, 2: Cross, 3: Hook, 4: Uppercut): "))
    opponent_move = random.randint(1, 4)

    print(f"Your move: {moves[user_move]}")
    print(f"Opponent's move: {moves[opponent_move]}")

    if winning_moves[user_move] == opponent_move:
        print("You win the round!")
    elif winning_moves[opponent_move] == user_move:
        print("You lose the round!")
    else:
        print("It's a draw!")


def simulate_fight(is_championship):
    rounds = 12 if is_championship else 3  # Championship fights have more rounds
    for _ in range(rounds):
        simulate_round()
        print("---")



is_championship = input("Is it a championship fight? (yes/no): ").lower() == "yes"
simulate_fight(is_championship)
