from math import floor


class Grid:
    def __init__(self):
        self.grid = [[None for _ in range(3)] for _ in range(3)]

    def __str__(self):
        rtn = ""
        for row in self.grid:
            rtn += "+---+---+---+\n"
            for symbol in row:
                rtn += "| "
                if symbol is None:
                    rtn += " "
                else:
                    rtn += symbol
                rtn += " "
            rtn += "|\n"
        rtn += "+---+---+---+\n"
        return rtn

    def draw(self):
        print(self)

    def enter_input(self, player_input, symbol):
        coords = (player_input-1) % 3, floor((9-player_input) / 3)
        self.grid[coords[1]][coords[0]] = symbol

    def win(self):
        for row in self.grid:
            if (winner := row[0]) == row[1] == row[2] and winner is not None:
                return winner
        for col in zip(*self.grid):
            if (winner := col[0]) == col[1] == col[2] and winner is not None:
                return winner
        if (winner := self.grid[0][0]) == self.grid[1][1] == self.grid[2][2] and winner is not None:
            return winner
        if (winner := self.grid[0][2]) == self.grid[1][1] == self.grid[2][0] and winner is not None:
            return winner
        return None
