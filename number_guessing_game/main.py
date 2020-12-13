from number_guessing_game.game import NumberGuessingGame


def start_game():
    print("Starting Game...")
    game = NumberGuessingGame()
    game.run()

if __name__ == '__main__':
    start_game()