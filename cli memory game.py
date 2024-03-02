import random
import argparse


class MemoryGame:
    def __init__(self, size=6):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]
        self.populate_board()

    def populate_board(self):
        values = list(range(1, 19)) * 2
        random.shuffle(values)
        for row in self.board:
            for i in range(self.size):
                row[i] = values.pop()

    def display_board(self, revealed=None):
        if revealed is None:
            revealed = []
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if (i, j) in revealed:
                    print(f"{cell:2}", end=" ")
                else:
                    print("X ", end="")
            print()

    def play(self):
        revealed = []
        while len(revealed) < self.size ** 2:
            guess1 = tuple(map(int, input("Guess 1 (row col): ").split()))
            guess2 = tuple(map(int, input("Guess 2 (row col): ").split()))
            if self.board[guess1[0]][guess1[1]] == self.board[guess2[0]][guess2[1]]:
                print("Match found!")
                revealed.extend([guess1, guess2])
            else:
                print("No match.")
            self.display_board(revealed)

        print("Game over! You've found all matches.")


def main():
    parser = argparse.ArgumentParser(description="Play a CLI-based memory game.")
    parser.add_argument("--size", type=int, default=6, help="Board size (default: 6x6)")
    args = parser.parse_args()

    game = MemoryGame(size=args.size)
    game.play()


if __name__ == "__main__":
    main()
