#!/usr/bin/env python3
"""
Dice roller will return a random integer  between 1 and the upper maximum set by the user
"""

__author__ = "Chris Watt [chris@teknetia.com]"
__version__ = "0.1.0"
__license__ = "MIT"

import random


def main(dice_size):
    """ Main entry point of the app """
    roll = roll_dice(int(dice_size))
    print("You rolled a {} on a {} sided die!".format(roll, dice_size))
    current_size = input("What size dice are we rolling? [{}] ".format(dice_size))

    if not current_size:
        current_size = dice_size

    main(current_size)


def roll_dice(sides):
    """ Roll the dice between 1 and the provided maximum """
    return random.randint(1, sides)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    dice_size = input("What size dice are we rolling? [6] ")

    if not dice_size:
        dice_size = 6

    main(dice_size)