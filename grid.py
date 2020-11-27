from math import floor
import numpy as np
from tabulate import tabulate


class Grid:
    def __init__(self):
        self.grid = np.full((3, 3), -1, dtype=np.int8)

    def __str__(self):
        return tabulate(self._str_arr(self.grid), tablefmt="fancy_grid")

    def draw(self):
        print(self)

    def enter_input(self, player_input, symbol):
        coords = (player_input-1) % 3, floor((9-player_input) / 3)
        self.grid[coords[1]][coords[0]] = symbol

    def check_for_winner(self, turn):
        for row in self.grid:
            if np.all(row == turn):
                return turn

        for col in self.grid.T:
            if np.all(col == turn):
                return turn

        if self.grid[0, 0] == self.grid[1, 1] == self.grid[2, 2] == turn:
            return turn

        if self.grid[0, 2] == self.grid[1, 1] == self.grid[2, 0] == turn:
            return turn

        return None

    _str_arr = np.vectorize(lambda cell: "O" if cell == 0 else "X" if cell == 1 else ".")
