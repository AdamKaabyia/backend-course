
import numpy as np
import hashlib

# 1 means alive
# 0 means dead
class Grid:
    def __init__(self, size, Values=None):
        self.size = size
        if Values is None:
            # randomly initialize the grid with random 0/1
            self.array = np.random.randint(0, 2, size=(size, size))
        else:
            self.array = Values

    def __str__(self):
        grid_str = ''
        for row in self.array:
            # Join the string representation of each number in the row, separated by a space
            grid_str += ' '.join(str(cell) for cell in row) + '\n'
        return grid_str

    def print(self):
        print(str(self.array))


    #checks if everyone died
    def are_all_zeros(self):
        return np.all(self.array==0)

    #updates the matrix based on the rules
    def update(self):
        newGrid = np.zeros((self.size, self.size), dtype=int)
        for row in range(self.size):
            for col in range(self.size):
                total = np.sum(self.array[max(row - 1, 0):min(row + 2, self.size), max(col - 1, 0):min(col + 2, self.size)]) - \
                        self.array[row, col]
                if self.array[row, col] == 1 and total in (2, 3):
                    newGrid[row, col] = 1
                elif self.array[row, col] == 0 and total == 3:
                    newGrid[row, col] = 1
        self.array = newGrid

    def set_cell(self, row, col, value):
        if 0 <= row < self.size and 0 <= col < self.size:
            self.array[row, col] = value
        else:
            print("Warning: Attempt to access cell out of bounds.")



"""
grid_obj = Grid(8)
print(grid_obj)
grid_obj.print()
"""