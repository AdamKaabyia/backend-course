we will simulate the game of life

user interface

# 1 means alive
# 0 means dead
lets start by explaining what each class is:

grid.py has the implementation of the class Grid:

    def __init__(self, size, Values=None):
       #holds size, and the grid of size sizeXsize now that grid is either filled randomly or with the Values the user gave us

    def print(self):
        #prints the grid

    def are_all_zeros(self):
        #returns 1 if all the values on the grid are zero
        #checks if everyone died

    #updates the matrix based on the rules
    def update(self):
        """
            updates the grid based on:
                Any live cell with fewer than two live neighbors dies, as if by underpopulation. (die is 0, alive is 1)
                Any live cell with two or three live neighbors lives on to the next generation. (die is 0, alive is 1)
                Any live cell with more than three live neighbors dies, as if by overpopulation. (die is 0, alive is 1)
                Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction. (die is 0, alive is 1)
        """

     def set_cell(self, row, col, value)
            #sets the value of array[row][col]=value

###############################################################
Game of Life.py using cli
    logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


    def create_board(size):
        """Initializes the game board."""

    def get_user_params(grid):
        """Prompts the user for initial live cells and the number of rounds."""

    def start_game(grid, rounds):
        """Simulates the game for the given number of rounds."""

    def print_results(grid):
        """Prints the current state of the grid."""
