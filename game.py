import random

from grid import Grid


class Game:
    player_symbols = {0: "O", 1: "X"}

    def __init__(self):
        self.grid = Grid()
        self.turn = random.choice((0, 1))
        self.player_input = None
        self.already_played = []
        self.winner = None

    def main_loop(self):
        while True:
            self.draw_grid()
            self.print_turn()
            self.get_input()
            self.apply_input()
            if self.check_game_ended():
                self.draw_grid()
                self.print_end_msg()
                break
            self.change_turn()

    def draw_grid(self):
        self.grid.draw()

    def change_turn(self):
        self.turn = (self.turn + 1) % 2

    def print_turn(self):
        print(f"It is {self.player_symbols[self.turn]}'s turn.")

    def get_input(self):
        while True:
            try:
                self.player_input = int(input())
                if self.player_input == 0 or self.player_input > 9 or self.player_input in self.already_played:
                    raise ValueError
            except ValueError:
                print("Wrong input.")
            else:
                self.already_played.append(self.player_input)
                break

    def apply_input(self):
        self.grid.enter_input(self.player_input, self.turn)

    def check_game_ended(self):
        if len(self.already_played) == 9:
            self.winner = "No one"
            return True

        winner = self.grid.check_for_winner(self.turn)
        if winner is not None:
            self.winner = self.player_symbols[winner]
            return True

        return False

    def print_end_msg(self):
        print(f"{self.winner} has won the game!")
