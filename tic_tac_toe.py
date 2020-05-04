from game import Game


def check_play_again():
    while True:
        try:
            do_new_game = input("Play again? (y/n)\n")
            if (r := do_new_game.strip().lower()) != "y" and r != "n" and r != "":
                raise ValueError
        except ValueError:
            print("Please enter 'y', 'n' or nothing.")
        else:
            if r == "y":
                return True
            return False


def main():
    while True:
        game = Game()
        game.main_loop()
        if not check_play_again():
            break


if __name__ == '__main__':
    main()
