import random

from number_guessing_game.hints import *


class NumberGuessingGame:
    def __init__(self, num_range=(0, 100)):
        self.num_range = num_range

        self.points = 100
        self.max_points = 100
        self.guesses = set()
        self.prev_guess = None

        self.hints = {'bisection': BisectionHint, 'warm_cold': WarmColdHint}

        self.answer = random.randint(*self.num_range)

    def run(self):
        while True:
            user_input = input(f"Guess a number between {self.num_range[0]} and {self.num_range[1]}, or Type 'h' to use a hint. ")

            if user_input == 'h':
                self.get_user_hint()
                continue

            try:
                guess = int(user_input)
                if guess < self.num_range[0] or guess > self.num_range[1]:
                    raise Exception
            except:
                print("Error. Your input was not a valid guess...")
                continue

            correct, cost = self.apply_guess(guess)
            if correct:
                print(f"Congrats! you Won! Your final score was {self.points}")
                return
            else:
                print(f"Sorry that guess was incorrect :( Your current score is {self.points}")

    def apply_guess(self, guess, prev_guess=True):
        if guess == self.answer:
            correct = True
        else:
            correct = False

        if prev_guess:
            self.prev_guess = guess

        if not guess in self.guesses:
            self.guesses.add(guess)
            cost = self.num_range[1] / self.max_points
            self.apply_cost(cost)
        else:
            cost = 0
        return correct, cost

    def apply_guesses(self, guesses):
        for guess in guesses:
            self.apply_guess(guess, False)

    def apply_cost(self, cost):
        self.points -= cost
        return self.points

    def get_user_hint(self):
        while True:
            name = input(f"Please choose a hint from the following hints {[i for i in self.hints.keys()]} or type 'help' to see what each hint does: ")
            if name == "help":
                self.get_hints_help()
            elif name == "q":
                return
            else:
                hint_cls = self.hints[name]
                hint = hint_cls(self)
                msg, cost = hint.apply()
                print(f"Hint: {msg} | Cost: {cost} | Current Score: {self.points}")
                return

    def get_hints_help(self):
        for name, cls in self.hints.items():
            print(f"Hint name: {name}")
            print(f"Hint help statement:", cls.help_statement)
            print()
        return


