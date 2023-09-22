import pygame
from Controller.GameLogic import GameLogic, Controller
from Models.Board import Board
from settings import Color, FenConvertor, GameFlags, StartMenuActions
from View.PygameGUI import PygameGUI
from View.StartScreen import StartScreen

import time


class Game:
    """
    the main class of the game
    it start with initalizing the board and the game options from pygame
    """

    def __init__(self):
        pygame.init()

        self.board = Board()
        self.game_logic: GameLogic = GameLogic(self.board)
        self.controller = Controller(board=self.board, game_logic=self.game_logic)

        self.gui = None
        self.start_screen = StartScreen()

        self.AI_GAME = True
        self.HUMAN_PLAYER = Color.WHITE

    def render(self):
        self.gui.render()

    def make_parameters_based_on_action(self, action):
        if action == StartMenuActions.PLAY_VS_HUMAN:
            self.AI_GAME = False
            self.HUMAN_PLAYER = Color.WHITE
            self.gui.flip_board = False
        elif action == StartMenuActions.PLAY_AS_WHITE_VS_AI:
            self.AI_GAME = True
            self.HUMAN_PLAYER = Color.WHITE
            self.gui.flip_board = False
        elif action == StartMenuActions.PLAY_AS_BLACK_VS_AI:
            self.AI_GAME = True
            self.HUMAN_PLAYER = Color.BLACK
            self.gui.flip_board = True

    def start_game(self):
        """
        the logic for starting the game
        """

        action = self.start_screen.render()

        self.gui = PygameGUI(controller=self.controller)
        self.make_parameters_based_on_action(action)

        self.render()

        while not GameFlags.game_over:
            if self.AI_GAME:
                if self.controller.get_current_player() != self.HUMAN_PLAYER:
                    # delete arrow from previous suggestion

                    self.controller.make_computer_move()
                    self.render()
                    self.gui.best_move_saved = self.game_logic.suggest_best_move()

                if (
                    GameFlags.current_player == self.HUMAN_PLAYER
                    and self.gui.view_best_move
                ):
                    self.gui.draw_arrows(
                        *FenConvertor.full_fen_to_pos(self.gui.best_move_saved)
                    )
                    pygame.display.flip()

            self.gui.listen_for_move()

        while True:
            self.render()
            time.sleep(0.2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


game = Game()
game.start_game()
