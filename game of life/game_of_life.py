from grid import Grid
import logging

logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


def create_board(size):
    """Initializes the game board."""
    return Grid(size)


def get_user_params(grid):
    """Prompts the user for initial live cells and the number of rounds."""
    logging.info("Getting user parameters for initial live cells.")

    while True:
        user_input = input("Enter the row and column of a live cell, separated by a comma (or type 'done' to finish): ")
        if user_input.lower() == 'done':
            break

        try:
            row, col = map(int, user_input.split(","))
            grid.set_cell(row, col, 1)
        except ValueError:
            print("Invalid input. Please enter row and column as two numbers separated by a comma.")

    rounds = int(input("Enter the number of rounds to simulate: "))
    return rounds


def start_game(grid, rounds):
    """Simulates the game for the given number of rounds."""
    logging.info("Starting game simulation.")
    for _ in range(rounds):
        grid.update()
        print_results(grid)


def print_results(grid):
    """Prints the current state of the grid."""
    logging.info("Printing current grid state.")
    grid.print()


def main():
    logging.info("Game of Life started.")
    size = 8  # Define the grid size
    grid = create_board(size)

    # Prompt user for initial configuration and get the number of rounds to simulate
    rounds = get_user_params(grid)  # Now returns the number of rounds as well

    start_game(grid, rounds)


if __name__ == "__main__":
    main()
