"""
game_logging and clear_log
READ ME:
    game_logging to log during a game and clear_log to clear the log file.

DESCRIPTION:
    Both game_logging as clear_log configures a logging file for a game.
    The function sets up logging format, filename, encoding, logging level and filemode (either append or write).

PARAMETERS:
    file_game(.log): the name of the log file

LIMITATIONS:
    As a limitation we would state that the similarity of both functions can be confusing and 'dangerous'.
    Write will clear the log everytime the function is called and append could
    possibly create very large logger files overtime.

STRUCTURES:
    No structures present.

OUTPUTS:
    No direct output, the clear_log function creates the start for a clear game log output.
    The game_logging function configures the logger file.



read_log, turns_taken, death_count, bump_count
READ ME:
    Together these functions create the statistics of the game

DESCRIPTION:
    Read_log uses turns_taken, death_count and bump_count, to create statistic of the Goosegame.

PARAMETERS:
    file_game(.log): the name of the log file used for collecting data in logger file
    player1(str): player name 1 used for collecting data in logger file
    player2(str): player name 2 used for collecting data in logger file
    lines(str): lines from the log file used for collecting data in logger file

LIMITATIONS:
    - To properly get the statistics of the game, the way the output of the logger is written, must not be changed.
    - Due to the regex being specially written to the lines in the loggerfile.
        These function can't be used any other way.

STRUCTURES:
    With open ... as ... : to make sure that the log file is readable.
    for line in lines: For-loop to loop through every line in the log file.
    if name_pat.search(line) and threw.search(line): to check if name_pat and threw regex are in the line.
        More of these if-statement but with different regex.
    if name == player1 - elif name == player 2: to check if the
        name found in the line is in the same as the input names.


OUTPUTS:
    turns_t1, turns_t2, deaths_p1, deaths_p2, bump_p1, bump_p2: gives a string format of the turns, deaths and bumps.
    turns_p1, turns_p2 : give the turns count of player 1 and player 2.
    d_count_p1, d_count_p2 : give the deaths count of player 1 and player 2
    b_count_p1, b_count_p2 : give the bump count of player 1 and player 2.

"""

import logging
import re


def game_logging(file_game):
    logging.basicConfig(filename=file_game,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    encoding='utf-8',
                    level=logging.INFO,
                    filemode='a')


def clear_log(file_game):
    file = logging.FileHandler(filename=file_game, mode='w')
    logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s %(message)s',
                        encoding='utf-8',
                        level=logging.INFO,
                        handlers=[file])


def turns_taken(lines, player1, player2):
    turns_p1 = 0
    turns_p2 = 0
    for line in lines:
        name_pat = re.compile('[a-zA-Z]+')
        threw = re.compile('threw')
        if name_pat.search(line) and threw.search(line):
            name = name_pat.search(line).group()
            if name == player1:
                turns_p1 += 1
            elif name == player2:
                turns_p2 += 1
    return turns_p1, turns_p2


def death_count(lines, player1, player2):
    d_count_p1 = 0
    d_count_p2 = 0
    for line in lines:
        name_pat = re.compile("[a-zA-Z]+'s")
        start = re.compile('start')
        if start.search(line) and name_pat.search(line):
            name = name_pat.search(line).group()[0:-2]
            if name == player1:
                d_count_p1 += 1
            elif name == player2:
                d_count_p2 += 1
    return d_count_p1, d_count_p2


def bump_count(lines, player1, player2):
    b_count_p1 = 0
    b_count_p2 = 0
    for line in lines:
        name_pat = re.compile("[a-zA-Z]+'s")
        bump = re.compile('bumped')
        if bump.search(line) and name_pat.search(line):
            name = name_pat.search(line).group()[0:-2]
            if name == player1:
                b_count_p1 += 1
            elif name == player2:
                b_count_p2 += 1
    return b_count_p1, b_count_p2


def read_log(file_game, player1, player2):
    with (open(file_game, 'r') as log_file):
        lines = log_file.readlines()
        turns_p1, turns_p2 = turns_taken(lines, player1, player2)
        turns_t1 = f"{player1} has taken {turns_p1} turns"
        turns_t2 = f"{player2} has taken {turns_p2} turns"

        d_count_p1, d_count_p2 = death_count(lines, player1, player2)
        death_p1 = f"{player1} has died {d_count_p1} time(s)"
        death_p2 = f"{player2} has died {d_count_p2} time(s)"

        b_count_p1, b_count_p2 = bump_count(lines, player1, player2)
        bump_p1 = f"{player1}'s Goose bumped {player2}'s goose {b_count_p1} time(s)"
        bump_p2 = f"{player2}'s Goose bumped {player1}'s goose {b_count_p2} time(s)"

        items = turns_t1, turns_t2, death_p1, death_p2, bump_p1, bump_p2
        return items
