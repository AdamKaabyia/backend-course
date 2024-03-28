import random


def create_board(size=5):
    return [[None for _ in range(size)] for _ in range(size)]


def place_ships(board, num_ships=5):
    ships = {}
    for ship_id in range(1, num_ships + 1):
        while True:
            x, y = random.randint(0, len(board) - 1), random.randint(0, len(board) - 1)
            if not board[x][y]:
                board[x][y] = ship_id
                ships[ship_id] = {'sunk': False, 'location': (x, y)}
                break
    return ships


def print_board(board, reveal=False):
    for row in board:
        print(" ".join(str(cell) if reveal and cell is not None else 'X' for cell in row))


def fire_missile(board, ships, x, y):
    if board[x][y]:
        ship_id = board[x][y]
        ships[ship_id]['sunk'] = True
        return True, ship_id
    else:
        return False, None


def get_user_input():
    try:
        x, y = map(int, input("Enter coordinates (row col): ").split())
        return x, y
    except ValueError:
        print("Invalid input. Please enter valid coordinates.")
        return None, None


def print_game_results(ships, missiles, hits):
    num_ships = len(ships)
    sunk_ships = sum(1 for ship in ships.values() if ship['sunk'])
    print("\nGame Over!")
    print(f"Ships sunk: {sunk_ships}/{num_ships}")
    accuracy = hits / float(missiles + hits) if missiles + hits > 0 else 0
    print(f"Accuracy: {accuracy:.2%}")
    print(f"Ships ID that sunk: {[ship_id for ship_id, ship in ships.items() if ship['sunk']]}")
    if sunk_ships == num_ships:
        print("Congratulations, you won!")
    else:
        print("Computer wins. Better luck next time!")


def game():
    board_size = 5
    num_ships = 5
    missiles = 15  # Decide how many missiles the player has
    hits = 0

    board = create_board(board_size)
    ships = place_ships(board, num_ships)

    while missiles > 0 and not all(ship['sunk'] for ship in ships.values()):
        print(f"\nMissiles remaining: {missiles}")
        print_board(board)
        x, y = get_user_input()
        if x is None or y is None or y >= board_size or y >= board_size: continue
        hit, ship_id = fire_missile(board, ships, x, y)
        if hit:
            hits += 1
            print(f"Hit! You've sunk ship ID {ship_id}.")
        else:
            print("Miss!")
        missiles -= 1

    print_game_results(ships, missiles, hits)


if __name__ == "__main__":
    game()
