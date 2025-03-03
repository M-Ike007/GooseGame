"""
READ ME:
    GUIBoardGame GUI
DESCRIPTION:
    GUIBoardGame GUI is a pygame GUI which displays the Ganzenbord board in which the game is showed and played.

PARAMETERS:
    - self.screen: screen in which everything is showed, this is also where the size is set
    - self.stats_button : statistics button
    - self.throw_button : dice button
    - self.board_img : image used to show the Ganzenbord board
    - self.players: empty list to which the players get added to
    - self.positions: list of lists with the different positions on the board image
    - self.font: size and font of the text
    - self.width, self.height = 1250, 850: height and width of GUI

    - self.font_popup = font for popups
    - self.font_S_txt = font for statistics

    - self.stats_button = button object in gui
    - self.throw_button = button rectangle object
    - self.stats_ok_btn = ok button for statistics popup

    - self.popup = popup rectangle
    - self.popup_ok_btn = popup ok button
    - self.popup_text = text for in the popup
    - self.draw_popup = boolean to check if popup should be drawn or not

    - self.stat_pop = pygame.Rect(300, 270, 500, 200)  # x, y, width, height

LIMITATIONS:
    - the position of the players on the board is not precise and can be unclear
    - the statistics button works, and shows the statistics, but the statistics
        are not updated when the game has started

STRUCTURES:
    - for loop to assign positions to the players

OUTPUT:
    Ganzenbord Game
"""

import pygame


class GUIBoardGame:
    def __init__(self):
        pygame.init()
        self.width, self.height = 1250, 850
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.board_img = pygame.image.load("ganzenbord2.jpg")
        # Fonts
        self.font = pygame.font.SysFont('comic sans', 25)
        self.font_popup = pygame.font.SysFont('calibri', 20)
        self.font_S_txt = pygame.font.SysFont('calibri', 15)
        # Buttons
        self.stats_button = pygame.Rect(self.width - 150, 100, 140, 50) # x, y, width, height
        self.throw_button = pygame.Rect(self.width - 150, self.height - 100, 140, 50)
        self.stats_ok_btn = pygame.Rect(485, 425, 80, 40)
        # Popup
        self.popup = pygame.Rect(300, 270, 500, 200) # x, y, width, height
        self.popup_ok_btn = pygame.Rect(485, 425, 80, 40)
        self.popup_text = ''
        self.draw_popup = self.draw_stats = False
        # Stats
        self.stat_pop = pygame.Rect(300, 270, 500, 200)  # x, y, width, height
        self.stats_text = 'no stats yet'
        self.sText1 = ''
        self.sText2 = ''
        self.sText3 = ''
        self.sText4 = ''
        self.sText5 = ''
        self.sText6 = ''
        # Dice
        self.Owner, self.Number = 0, 0
        self.players, self.colors = [], []
        self.dice_lbl_rec = pygame.Rect(self.width - 150, self.height - 150, 140, 50)
        # Graphical board
        self.positions = [[200, 750], [315, 750], [440, 750], [580, 750], [680, 750], [800, 670], [940, 620],
                          [990, 510], [1010, 400], [940, 270], [930, 190], [840, 110], [700, 80], [550, 70], [450, 70],
                          [310, 75], [200, 100], [120, 170], [70, 270], [80, 395], [120, 510], [210, 580], [320, 620],
                          [430, 580], [580, 610], [710, 610], [820, 570], [905, 465], [885, 345], [815, 230],
                          [700, 190], [560, 190], [430, 180], [310, 180], [210, 230], [175, 325], [220, 440],
                          [325, 490], [435, 474], [560, 340]]

    def add_player(self, player):
        self.players.append(player)

    def add_color(self, color):
        self.colors.append(color)

    def create_popup(self, text):
        pygame.draw.rect(self.screen, (40, 90, 161), self.popup)
        throw_text = self.font_popup.render(text, True, (255, 255, 255))
        self.screen.blit(throw_text, (self.popup.x + 20, self.popup.y + 10))

        pygame.draw.rect(self.screen, (25, 25, 112), self.popup_ok_btn)
        ok_text = self.font_popup.render('OK', True, (255, 255, 255))
        self.screen.blit(ok_text, (self.popup_ok_btn.x + 20, self.popup_ok_btn.y + 10))

    def create_stats(self):
        # 6 lines of statistics text
        pygame.draw.rect(self.screen, (40, 90, 161), self.stat_pop)

        throw_text1 = self.font_S_txt.render(str(self.sText1), True, (255, 255, 255))
        self.screen.blit(throw_text1, (self.stat_pop.x + 20, self.stat_pop.y + 20))

        throw_text2 = self.font_S_txt.render(str(self.sText2), True, (255, 255, 255))
        self.screen.blit(throw_text2, (self.stat_pop.x + 20, self.stat_pop.y + 40))

        throw_text3 = self.font_S_txt.render(str(self.sText3), True, (255, 255, 255))
        self.screen.blit(throw_text3, (self.stat_pop.x + 20, self.stat_pop.y + 60))

        throw_text4 = self.font_S_txt.render(str(self.sText4), True, (255, 255, 255))
        self.screen.blit(throw_text4, (self.stat_pop.x + 20, self.stat_pop.y + 80))

        throw_text5 = self.font_S_txt.render(str(self.sText5), True, (255, 255, 255))
        self.screen.blit(throw_text5, (self.stat_pop.x + 20, self.stat_pop.y + 100))

        throw_text6 = self.font_S_txt.render(str(self.sText5), True, (255, 255, 255))
        self.screen.blit(throw_text6, (self.stat_pop.x + 20, self.stat_pop.y + 120))

        # OK button
        pygame.draw.rect(self.screen, (25, 25, 112), self.popup_ok_btn)
        ok_text = self.font_popup.render('OK', True, (255, 255, 255))
        self.screen.blit(ok_text, (self.popup_ok_btn.x + 20, self.popup_ok_btn.y + 10))

    def draw(self):
        self.screen.fill(0)  # screen
        self.screen.blit(self.board_img, (0, 0))  # Gooseboard image
        for player in self.players:
            pos = self.positions[player.get_position()]
            pygame.draw.circle(self.screen, self.colors[self.players.index(player)], pos, 20)  # Goose
        # Draw the dice result and current player name
        pygame.draw.rect(self.screen, (0, 0, 0), self.dice_lbl_rec)
        result_text = self.font_popup.render(f'{self.Owner} threw {str(self.Number)}', True, (255, 255, 255))
        self.screen.blit(result_text, (self.dice_lbl_rec.x + 10, self.dice_lbl_rec.y + 10))

        if self.draw_popup:
            self.create_popup(self.popup_text)
        if self.draw_stats:
            self.create_stats()
        pygame.draw.rect(self.screen, (100, 200, 0), self.throw_button)  # Draw throw button
        throw_text = self.font.render("Dice", True, (255, 255, 255))
        self.screen.blit(throw_text, (self.throw_button.x + 35, self.throw_button.y + 10))

        pygame.draw.rect(self.screen, (169, 169, 169), self.stats_button)  # Draw stats button
        self.stats_text = self.font.render("Statistics", True, (255, 255, 255))
        self.screen.blit(self.stats_text, (self.stats_button.x + 10, self.stats_button.y + 10))

        if self.draw_stats:
            self.create_stats()

        pygame.display.flip()

    pygame.time.Clock().tick(30)










