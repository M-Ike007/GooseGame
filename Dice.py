"""
READ ME:
    Dice module

DESCRIPTION:
    this module returns a random integer between 1 and 6 to simulate a dice roll.

PARAMETERS:
    none

LIMITATIONS:
    can only be used for six-sided dice situations

STRUCTURES:
    none

OUTPUT:
    single integer value between 1 and 6

"""

import random


def throw():
    value = random.randint(1, 6)
    print(value)
    return value

