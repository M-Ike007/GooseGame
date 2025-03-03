"""
READ ME:
    game_runner

DESCRIPTION:
    game_runner is a Python script that initializes and runs the initial state of a Goose game.
    The script integrates various classes and functions, including the graphical user interface (GUI) and game logic.
    The GUI is responsible for gathering player names and their preferred colors.
    Once the setup is complete, the main game loop is initiated.
    The game features 2 background music tracks: relaxed.mp3 for the main gameplay, setup_menu.mp3 for the setup screen.

PARAMETERS:
    log_name(.log): name of the log_file which is used for logging
    name_p1 (str): name of player 1
    name_p2 (str): name of player 2
    color_p1 (list of int): color of player 1
    color_p2 (list of int) = color of player 2
    player1, player2 are Goose classes
    handle_turn(current_p, gui_board, board, log_name)  This calls the handle_turn function and it passes all
     information needed for a turn.

LIMITATIONS:
Fixed Files: The music files, Python files, images need to be in working directory.
Single Device: The game is designed to run on a single device, with both players interacting through the same interface.


STRUCTURES:
    The game logic includes several key structures:
    While True Loop: This loop handles the main event processing using Pygame. 
    It includes several if and elif structures to create on-screen buttons, 
    such as throw_button, stats_button, and stats_ok_button.
    Event Handling: The game captures various events like mouse clicks and quit events. 
    Clicking the Quit button exits the game.

OUTPUT:
  This really fun Goosegame!

"""

import Load_modules
from Board import Board
from Gui_board import GUIBoardGame
from Goose import Goose
from Turn_Handler import handle_turn
import Logging
from Gui_Setup import Gui_setup
import pygame as pygame

# check if all modules present on device
Load_modules.load_modules()

# load and start music
pygame.init()
pygame.mixer.music.load('setup_menu.mp3')
pygame.mixer.music.play(-1)

log_name = 'GooseGames.log'
Logging.clear_log(log_name)

# create and show a GUI setup
start_game = Gui_setup()
start_game.mainloop()

# store the information from the setup
colors_RGB ={'Red': (255,0,0), 'Blue':(0,0,255), 'Green': (0,255,0)}

# create 2 gooses with correct color and name
name_p1, name_p2, color_p1, color_p2 = start_game.start()
color_p1 = colors_RGB[color_p1]
color_p2 = colors_RGB[color_p2]
player1 = Goose(0, color_p1, name_p1, log_name)
player2 = Goose(0, color_p2, name_p2, log_name)

# Music in game is updated
pygame.mixer.music.load('relaxed.mp3')
pygame.mixer.music.play(-1)

board = Board()
gui_board = GUIBoardGame()

current_p = player1
players = [player1, player2]
gui_board.add_player(player1)
gui_board.add_player(player2)
gui_board.add_color(color_p1)
gui_board.add_color(color_p2)

# Eventhandeler for Pygame, which is basically for the buttons on screen to click on.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if not gui_board.draw_popup and not gui_board.draw_stats:
            if event.type == pygame.MOUSEBUTTONDOWN and gui_board.throw_button.collidepoint(event.pos):
                if current_p == player1:
                    current_p = player2
                elif current_p == player2:
                    current_p = player1
                handle_turn(current_p, gui_board, board, log_name)  # Pass game and board and log_name
            if event.type == pygame.MOUSEBUTTONDOWN and gui_board.stats_button.collidepoint(event.pos):
                gui_board.draw_stats = True
        if gui_board.draw_popup:
            if event.type == pygame.MOUSEBUTTONDOWN and gui_board.popup_ok_btn.collidepoint(event.pos):
                gui_board.popup_height = 200
                gui_board.draw_popup = False
        if gui_board.draw_stats:
            if event.type == pygame.MOUSEBUTTONDOWN and gui_board.stats_ok_btn.collidepoint(event.pos):
                gui_board.draw_stats = False

    gui_board.draw()
