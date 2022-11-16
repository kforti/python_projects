import sys
from random import randint


def roll_dice():
    value = randint(1, 6)
    return value

if __name__ == '__main__':
    try:
        args = sys.argv
        number_of_dice = int(sys.argv[1])
    except:
        number_of_dice = 2
    dice_rolls = [roll_dice() for i in range(number_of_dice)]
    print("Number of dice:", number_of_dice)
    value = sum(dice_rolls)
    print("Value:", value)
