"""
Read Me:
    Function handle_turn to control the turns in the game. Function collision_check to check for collisions.

DESCRIPTION:
    The turn handler makes sure that every turn is done properly. Starting with throwing the dice.
    Checking for collision on the new position, using collision_check function.
    After this, a check for an action is done. If there is an action name, the proper action is done.
    At last position is checked for tile 39, the finish line.

PARAMETERS:
    - goose_p (Goose class): The current player taking the turn.
    - game (GUI board): The GUI from the board containing game state.
    - board (Board class): The board class, which keeps track of squares and their actions.
    - file_name_log (str): The name of the log file where game events are recorded.

LIMITATIONS:
    - When a player has to skip a turn, the next player's turn will proceed
        automatically without needing to press the dice button.
    - we use None as a string in our dictionary, byt it is also a python term, which
        could cause confustion or unwanted errors.

STRUCTURES:
    In handle_turn:
    if-statement: to check if there is an action that needs to be done
    if-elif-statement: to check for specific actions
    for-loop and if-statement: looping through list of players to check which player is not the current player
    if-statement: check if new position is tile 39
    if-statement: to check if new position of the current player is the same as the position of the player which is not the current player



OUTPUTS:
    Sets the goose to the new position after taking its turn.

"""


import logging
from Logging import game_logging
from Logging import read_log
game_logging('GooseGames.log')
logger = logging.getLogger()


def handle_turn(goose_p, game, board, file_name_log):
    game_logging(file_name_log)
    logger = logging.getLogger(f'Turn handler')

    # 1. Throw dice
    new_position = goose_p.take_step()
    board.update_square(new_position)
    game.Number = goose_p.number
    game.Owner = goose_p.owner
    print(f"{goose_p.owner} and on position {new_position}")

    # 3. Check for conditions
    # Same position as other goose (except for tile 0)?
    collision_check(goose_p, game, board, file_name_log, new_position)

    # Action on current tile?
    current_tile = board.squares[new_position]
    if current_tile.action_name != 'None':
        action_name = current_tile.action_name
        poetic_text = board.poetic_actions[new_position]
        print_text = f'{goose_p} {poetic_text}'
        game.popup_text = print_text
        if action_name == 'move':
            game.draw_popup = True
            logger.info(f"{goose_p.owner} is moved to another place")
            action_value = int(current_tile.action_value)
            new_position = action_value
            goose_p.move_to(new_position)
            collision_check(goose_p, game, board, file_name_log, new_position)

        elif action_name == 'wait':
            game.draw_popup = True
            logger.info(f"{goose_p.owner} has to wait this turn")
            for other_goose_p in game.players:
                if other_goose_p.owner != goose_p.owner:
                    logger.info(f"{other_goose_p} has now two turns")
                    handle_turn(other_goose_p, game, board, file_name_log)

        elif action_name == 'dice again':
            game.draw_popup = True
            logger.info(f"{goose_p.owner} is allowed to dice again")
            handle_turn(goose_p, game, board, file_name_log)


        line1, line2, line3, line4, line5, line6 = \
        (read_log('GooseGames.log', game.players[0], game.players[1]))
        game.sText1 = line1
        game.sText2 = line2
        game.sText3 = line3
        game.sText4 = line4
        game.sText5 = line5
        game.sText6 = line6

    # Did someone win the game?
    if new_position == 39:
        game.draw_popup = True
        print(f"{goose_p.owner} has won the game!")


def collision_check(current_p, game, board, file_name_log, new_position):
    logger = logging.getLogger(f'Turn handler')
    game_logging(file_name_log)
    for other_goose_p in game.players:
        if other_goose_p != current_p:
            if other_goose_p.get_position() == new_position:
                logger.info(f"{current_p.owner}'s goose bumped {other_goose_p.owner}'s goose off the board")
                logger.info(f"{other_goose_p.owner}'s goose has been set back to start")
                other_goose_p.move_to(0)
                board.update_square(0)
