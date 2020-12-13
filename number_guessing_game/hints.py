


class BisectionHint:
    help_statement = "Divide the range in half. Cost: up to half the range"
    def __init__(self, game):
        self.game = game

    def apply(self):
        values = [i for i in range(1, self.game.num_range[1]) if i not in self.game.guesses]

        halfway_idx = len(values) // 2
        halfway = values[halfway_idx]

        if self.game.answer < halfway:
            symbol = "<"
            guesses = values[halfway_idx:]

        elif self.game.answer >= halfway:
            symbol = ">="
            guesses = values[:halfway_idx - 1]

        hint = f"The correct answer is {symbol} {halfway}"
        cost = self.game.apply_guesses(guesses)
        return hint, cost



class WarmColdHint:
    cost = 20
    help_statement = f"Warm if last guess is +- 15% of the answer. Cold otherwise. Cost: {cost}"
    def __init__(self, game):
        self.game = game

    def apply(self):
        if not self.game.prev_guess:
            msg = print("You must make at least one guess before using this hint.")
            return msg, None

        if self.game.answer + self.game.num_range[1] * .15 >= self.game.prev_guess <= self.game.answer + self.game.num_range[1] * .15:
            temp = "Warm"
        else:
            temp = "Cold"
        msg = f"Your last guess of {self.game.prev_guess} was {temp}."
        self.game.apply_cost(self.cost)
        return msg, self.cost

