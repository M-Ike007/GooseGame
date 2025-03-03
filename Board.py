"""
READ ME:
    Board class

DESCRIPTION:
    This class includes the dictionary with all the tiles and corresponding actions, it also includes the different
    functions needed to read the actions and occupation corresponding to the tiles which are needed in the game runner.
    Functions:
        - set_squares: function to create a square using the square class and putting it in a dictionary
        - get_occ: function that returns the occupation of a tile
        - set_occ: function that counts the occupation of a tile
        - update_square: function that updates a square's occupation

PARAMETERS:
    - self.squares: empty dictionary in which the squares with name and value are stored
    - self.num_squares: number of tile numbers on the board
    - self.actions: dictionary with tile numbers and corresponding actions
    - self.poetic_actions: dictionary with tile numbers and description of the tile's action

LIMITATIONS:
    - The dictionary of the actions are redundant because of all the tiles with no actions
    - Having two dictionaries works well, but it gives way to a little bit of redundancy for none-action squares

STRUCTURES:
    for loop to get the corresponding action of a specific tile

OUTPUT:
    actions, occupation of a tile
"""


from Square import Square


class Board:
    def __init__(self):
        self.squares = {}
        self.num_squares = 40
        self.actions = {
            0: 'None:None', 1: 'None:None', 2: 'None:None', 3: 'None:None', 4: "move:6", 5: "move:11",
            6: 'None:None', 7: 'None:None', 8: 'None:None', 9: "move:0", 10: 'None:None',
            11: 'None:None', 12: "wait:Skip_turn", 13: "move:14", 14: 'None:None', 15: "dice again:dice",
            16: 'None:None', 17: 'None:None', 18: "wait:stuck", 19: "move:22", 20: 'None:None',
            21: 'None:None', 22: 'None:None', 23: 'move:16', 24: 'None:None', 25: 'None:None',
            26: "wait:Skip_turn", 27: 'None:None', 28: 'None:None', 29: "wait:Skip_turn",
            30: 'None:None', 31: "dice again:dice", 32: "move:24", 33: 'None:None', 34: 'None:None',
            35: "wait:Skip_turn", 36: "wait:Skip_turn", 37: 'None:None', 38: "move:34", 39: "win:quit"
        }
        self.poetic_actions = {
            0: 'None:None', 1: 'None:None', 2: 'None:None', 3: 'None:None', 4: "moves because of love to tile 6.",
            5: "walks over a bridge to tile 11.", 6: 'None:None', 7: 'None:None', 8: 'None:None',
            9: "has bad luck, and moves back to the start.", 10: 'None:None', 11: 'None:None',
            12: "has to wait a turn.", 13: ", got lucky and moves to 14", 14: 'None:None',
            15: "throws the dice again.", 16: 'None:None', 17: 'None:None', 18: "got stuck and has to wait a turn",
            19: "got lucky and moves to tile 22", 20: 'None:None', 21: 'None:None', 22: 'None:None',
            23: 'got unlucky and moves to tile 16', 24: 'None:None', 25: 'None:None', 26: "has to wait a turn.",
            27: 'None:None', 28: 'None:None', 29: "has to wait a turn.", 30: 'None:None', 31: "throws the dice again.",
            32: "got unlucky and moves to tile 24.", 33: 'None:None', 34: 'None:None', 35: "has to wait a turn.",
            36: "has to wait a turn.", 37: 'None:None', 38: "got unlucky and moves to tile 34.", 39: " has won!!"
        }
        self.set_squares()

    def set_squares(self):
        for i in range(0, self.num_squares):
            name, value = self.actions[i].split(':')
            square = Square(i, name, value)
            self.squares[i] = square

    def get_occ(self, square: int):
        my_square = self.squares[square]
        occupation = Square.get_occ_count(my_square)
        return occupation

    def set_occ(self, square, occupation):
        my_square = self.squares[square]
        my_square.set_occ_count(occupation)
        self.squares.update({square: my_square})

    def update_square(self, square: int):
        self.set_occ(square, self.get_occ(square) + 1)

    def __repr__(self):
        return '\n'.join(str(square) for square in self.squares.values())
