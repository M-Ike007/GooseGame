'''
READ ME
    Square class

DESCRIPTION:
    The Square class creates a square object (tile on the board) which include the position, the name of the action
    on that specific tile and the action value (number of the tile) and its occupation (if a player is present on that
    tile)
    Functions:
        - get_position: returns the position of a square on the board
        - get_occ_count: returns the occupation of a square
        - set_occ_count: sets the occupation of a square according to the count value given

PARAMETERS:
    - position (int): Position of the square.
    - action_name (str): Name of the action associated with the square.
    - action_value (str): Value associated with the action.
    - occupation (int, optional): Number of geese on the square (default is 0).

LIMITATIONS:
    - The occupation of a square can never be above 1, but the set_occupation function asks for a count value, but this
     should always be 0 or 1 except for tile 0. This is because when a player ends up on a tile where there is another
     player present, the player returns to tile 0.
    - there is no check within the class to check if the parameters given are of the correct type.

STRUCTURES:
    None

OUTPUTS:
    Returns position and occupation of a square
'''


class Square:
    def __init__(self, position, action_name, action_value, occupation=0):
        self.position = position
        self.action_name = action_name
        self.action_value = action_value
        self.occupation = occupation

    def get_position(self):
        return self.position

    def get_occ_count(self):
        return self.occupation

    def set_occ_count(self, count):
        self.occupation = count

    def __repr__(self):
        return f'Square object with position {self.position}, occupation: {self.occupation}, action: {self.action_name}'
