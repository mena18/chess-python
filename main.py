import pygame
from src.GameLogic import GameLogic, Controller
from src.Board import Board
from src.settings import Color, FenConvertor
from src.PygameGUI import PygameGUI


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
        you wait for user inputs and call game_logic.position_clicked()
        """

        self.render()
        best_move_saved = "e2e4"
        while True:
            if self.game_logic.current_player == Color.BLACK:
                # delete arrow from previous suggestion

                self.game_logic.make_computer_move()
                self.render()
                best_move_saved = self.game_logic.suggest_best_move()

            if self.game_logic.current_player == Color.WHITE:
                self.gui.draw_arrows(*FenConvertor.full_fen_to_pos(best_move_saved))
                pygame.display.flip()

            self.gui.listen_for_move()


game = Game()
game.start_game()
