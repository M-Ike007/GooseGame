"""
READ ME:
    Goose class

DESCRIPTION:
    The Goose class creates a goose object which includes the position, color and owner of the goose and also the
    different types of actions the goose can come across on the board (except for a "do second turn" type action).
    It also checks if the goose needs to take some steps back when it throws a number with which it
    goes past the finish.
    Functions:
        - get_position
        - set_position
        - set_n_position: set position when goose goes further than 39 and has to walk steps back again.
        -

PARAMETERS:
    - self.position: position of the player on the board
    - self.color: color of the goose's player
    - self.owner: owner of the goose
    - file_name_log: name of the log file
    - self.allow_walk: boolean to check if a player can play, set to True
    - number: number diced
    - new_position: number of the tile the goose has to move to

LIMITATIONS:
    - There is no functionality that the goose can throw the dice again when it is allowed to do this
      (due to an action on the board)
    - the goose contains dice and therefore we have no control over when we want to do a turn without throwing the dice.

STRUCTURES:
    - if statements in the check function to check whether the number thrown gets the player past tile 39 or not
    - if statement in the set_position function to check whether the player has won or not
    - if not and if statements in the take_step function to check whether the player is allowed to move and what the
    output of the check function to carry out the corresponding function

OUTPUT:
    - position
    - log events

"""


import logging
from Dice import throw
from Logging import game_logging


class Goose(object):
    def __init__(self, position, color, owner, file_name_log):
        self.pos = int(position)
        self.color = str(color)
        self.owner = str(owner)
        self.logger = logging.getLogger(f'{self.owner}.{self.__class__.__name__}')
        self.allow_walk = True
        self.number = 0
        game_logging(file_name_log)

    def get_position(self):
        return self.pos

    def set_position(self, number):
        self.pos += number
        if self.pos < 39:
            self.logger.info(f"{self.owner}'s goose is now on square {self.pos}")
            return self.pos
        else:
            self.win()

    def set_n_pos(self, number):
        steps = self.pos + number - 39
        self.pos = 39 - steps
        self.logger.info(f"{self.owner}'s goose has thrown {number}, which is {steps} steps to high to win,"
                         f" so {self.owner}'s goose is now on square {self.pos}")
        return self.pos

    def check(self, number):
        if self.pos + number > 39:
            within_board = False
        elif 1 <= self.pos + number <= 39:
            within_board = True
        else:
            raise ValueError(f'Number is not on Gooseboard')
        return within_board

    def take_step(self):
        if not self.allow_walk:
            self.allow_walk = True
            self.logger.info(f"{self.owner} has to wait this turn")
        else:
            self.number = throw()
            self.logger.info(f"{self.owner} threw {self.number}")
            if self.check(self.number):
                self.set_position(self.number)
            else:
                self.set_n_pos(self.number)
        return self.pos

    def move_to(self, new_position):
        self.pos = new_position
        self.logger.info(f"{self.owner}'s {self.color} goose is now on square {self.pos}")
        return self.pos

    def win(self):
        self.logger.info(f"{self.owner}'s {self.color} goose has made it to the finish")
        return f"{self.owner}'s {self.color} goose has made it to the finish"

    def __repr__(self):
        # return f"{self.owner}'s {self.color} goose is now on square {self.position}"
        return f"{self.owner}'s goose"
