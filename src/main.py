import pygame
from Controller.GameLogic import GameLogic, Controller
from Models.Board import Board
from settings import Color, FenConvertor, GameFlags
from View.PygameGUI import PygameGUI


class Game:
    """
    the main class of the game
    it start with initalizing the board and the game options from pygame
    """

    def __init__(self):
        self.board = Board()
        self.game_logic: GameLogic = GameLogic(self.board)
        self.controller = Controller(board=self.board, game_logic=self.game_logic)

        self.gui = PygameGUI(controller=self.controller)

    def render(self):
        self.gui.render()

    def start_game(self):
        """
        the logic for starting the game
        """

        self.render()

        while True:
            if self.controller.get_current_player() == Color.BLACK:
                # delete arrow from previous suggestion

                self.controller.make_computer_move()
                self.render()
                if not GameFlags.game_over:
                    self.gui.best_move_saved = self.game_logic.suggest_best_move()

            if GameFlags.current_player == Color.WHITE and self.gui.view_best_move:
                self.gui.draw_arrows(
                    *FenConvertor.full_fen_to_pos(self.gui.best_move_saved)
                )
                pygame.display.flip()

            self.gui.listen_for_move()


game = Game()
game.start_game()
