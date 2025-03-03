"""
READ ME:
    Gui_setup is the start of the game.

DESCRIPTION:
    Gui-setup is a tkinter GUI that will show at the start of the game. Two players have to fill in their name and choose their color.
    The GUI also includes a rules button, start button and a nice goose image.
    Functions:
            -define_widget
            -start
            -rules

PARAMETERS:
    - self.master.title(str): variable, setting the name for the GUI
    - self.master.geometry(str): variable setting the size of the GUI
    - self.dpdn_p1(str) and self.dpdn_p2(str): variable to assign the dropdown menu for the players color
    - self.p1_name(str) and self.p2_name(str): variable to assign the two players names to player 1 and 2
    - self.color_value1(str) and self.color_value2(str): variable to assign the color of the players to player 1 and 2
    - self.colors1(list) and self.colors2(list): list of strings of the color
    - self.meme: variable containing the image of in the GUI
    - self.define_widget(): function which includes all the elements of the GUI
    - self.grid(): grid to place all the elements of the GUI in the right position

LIMITATIONS:
    - the GUI setup does not close after pressing start.
    - when players play with the same name, you can only differentiate them by the color of their goose.

STRUCTURES:
    If-else statement in start:
    In the start function there are different if statements to make sure the two players insert a name and do not have
    the same color. If one of those two things happen, there is a label that appears. The GUI therefore only closes
    when the two players have a name and two different colors

OUTPUT:
    Players names and colors

"""


import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk


class Gui_setup(tk.Frame):
    def __init__(self, width=900, height=700):
        tk.Frame.__init__(self)
        self.master.title('Goose Game setup')
        self.master.geometry(f"{width}x{height}")

        self.dpdn_p1 = tk.StringVar()
        self.dpdn_p2 = tk.StringVar()

        self.p1_name = tk.StringVar()
        self.p2_name = tk.StringVar()

        self.color_value1 = tk.StringVar()
        self.colors1 = ['Red', 'Blue', 'Green']
        self.color_value1.set(self.colors1[0])
        self.color_value2 = tk.StringVar()
        self.colors2 = ['Blue', 'Green', 'Red']
        self.color_value2.set(self.colors2[0])

        self.meme = ImageTk.PhotoImage(Image.open('3.jpeg'))

        self.define_widget()
        self.grid()

    def define_widget(self):
        lbl_p1 = tk.Label(self, bg="#ffb175")
        lbl_p1['text'] = "Player 1:"
        lbl_p1.grid(row=0, column=0, sticky='E')

        txt_name_p1 = tk.Entry(self)
        txt_name_p1['textvariable'] = self.p1_name
        txt_name_p1.grid(row=0, column=1)

        lbl_color_p1= tk.Label(self, bg="#ffb175")
        lbl_color_p1['text'] = "Color:"
        lbl_color_p1.grid(row=1, column=0, sticky='E')

        self.dpdn_p1 = tk.OptionMenu(self, self.color_value1, *self.colors1)
        self.dpdn_p1.grid(row=1, column=1, sticky='W')

        lbl_p2 = tk.Label(self, bg="#8be9e9")
        lbl_p2['text'] = "Player 2:"
        lbl_p2.grid(row=3, column=0, sticky='E')

        txt_name_p2 = tk.Entry(self)
        txt_name_p2['textvariable'] = self.p2_name
        txt_name_p2.grid(row=3, column=1)

        lbl_color_p2 = tk.Label(self, bg="#8be9e9")
        lbl_color_p2['text'] = "Color:"
        lbl_color_p2.grid(row=4, column=0, sticky='E')

        self.dpdn_p2 = tk.OptionMenu(self, self.color_value2, *self.colors2)
        self.dpdn_p2.grid(row=4, column=1, sticky='W')

        self.btn_start = tk.Button(self, bg="#ffe88a")
        self.btn_start['text'] = 'Start Goose Game'
        self.btn_start['command'] = self.start
        self.btn_start.grid(row=10, column=2)

        self.btn_rules= tk.Button(self)
        self.btn_rules['text'] = 'Game rules'
        self.btn_rules['command'] = self.rules
        self.btn_rules.grid(row = 1, column = 3)

        self.lbl_meme = tk.Label(self)
        self.lbl_meme['image'] = self.meme
        self.lbl_meme.grid(row = 6, column = 3)

    def start(self):
        if self.p1_name.get() != '' and self.p2_name.get() != '':
            if self.color_value1.get() != self.color_value2.get():
                self.quit()
                return self.p1_name.get(), self.p2_name.get(), self.color_value1.get(), self.color_value2.get()
            else:
                lbl_start = tk.Label(self, fg='red')
                lbl_start['text'] = 'Players cannot have the same color'
                lbl_start.grid(row=9, column=2)
        else:
            lbl_start = tk.Label(self, fg='red')
            lbl_start['text'] = 'Please enter a name for both players'
            lbl_start.grid(row=8, column=2)

    def rules(self):
        tk.messagebox.showinfo('Gamerules Ganzenbord:', 'The ganzenbord game is played with: \n'
                                                        '- 1 dice\n'
                                                        '- 2 players with a goose pawn \n'
                                                        '- a board\n\n'
                                                        'Each player take turns and throws the dice, then the goose \n'
                                                        'moves to the right tile and carries out the action linked to \n'
                                                        'that tile. The goose which ends up first exactly on the last \n'
                                                        'tile (39), wins \n\n'
                                                        'Tiles with action:\n'                                                    
                                                        '- 3: Fly (move to tile 5)\n- 4: Bridge (move to tile 11)\n'
                                                        '- 8: Fly (move to tile 14)\n- 11: Thirsty (skip turn)\n'
                                                        '- 12: Stuck (move to tile 14)\n- 14: Dice again\n'
                                                        '- 17: Thirsty (skip turn)\n- 18: Fly (move to tile 22)\n'
                                                        '- 22: Stuck (skip turn)\n- 25: Nighty night (skip turn)\n'
                                                        '- 28: Looked up (skip turn)\n- 30: Dice again\n'
                                                        '- 31: Fly (move to tile 34)\n- 34: Sick (skip turn)\n'
                                                        '- 35: Tired (skip turn)\n- 37: Picnic (skip turn)\n- 39: Win!!')
