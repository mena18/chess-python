import pygame
import os
from src.GameLogic import GameLogic
from src.Board import Board
from src.Handler import Handler
from src.FenConvertor import FenConvertor
from src.settings import Color


class Game:
    """
    the main class of the game
    it start with initalizing the board and the game options from pygame
    """

    def __init__(self):
        pygame.init()

        Handler.screen = pygame.display.set_mode((Handler.WIDTH, Handler.HEIGHT))
        for piece_code in Handler.pieces_images:
            Handler.pieces_images[piece_code] = pygame.image.load(
                os.path.join(
                    Handler.IMAGES_FOLDER, f"{Handler.pieces_images[piece_code]}.svg"
                )
            )

        pygame.display.set_caption(Handler.GAME_CAPTION)

        self.background = pygame.transform.smoothscale(
            pygame.image.load(
                os.path.join(Handler.IMAGES_FOLDER, "board.png")
            ).convert(),
            (Handler.WIDTH, Handler.HEIGHT),
        )
        self.background_rect = self.background.get_rect()

        self.board = Board()
        self.game_logic: GameLogic = GameLogic(self.board)

    def draw(self):
        """
        drawing in the game
        1. draw the square you clicked having the piece
        2. draw the red square on the king if the king in check
        3. draw all pieces
        4. draw green circle on squares if they are in available moves
        """
        Handler.screen.blit(self.background, self.background_rect)
        if self.game_logic.last_position:
            Handler.draw_square(self.game_logic.last_position)
        if self.game_logic.finished_pos:
            Handler.draw_square(self.game_logic.finished_pos, COLOR=(255, 0, 0))
        self.board.draw()
        for move in self.game_logic.list_available_moves:
            Handler.draw_possible_position(move)

    def start_game(self):
        """
        the logic for starting the game
        you wait for user inputs and call game_logic.position_clicked()
        """
        self.draw()
        best_move_saved = "e2e4"
        while True:
            if self.game_logic.current_player == Color.BLACK:
                # delete arrow from previous suggestion

                self.game_logic.make_computer_move()
                self.draw()
                best_move_saved = self.game_logic.suggest_best_move()

            if self.game_logic.current_player == Color.WHITE:
                Handler.draw_arrows(*FenConvertor.full_fen_to_pos(best_move_saved))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = event.pos
                    x = x // Handler.SQUARE_SIZE
                    y = y // Handler.SQUARE_SIZE
                    self.game_logic.position_clicked((y, x))
                    self.draw()

            pygame.display.flip()


game = Game()
game.start_game()
