import os
import pygame
from settings import GameFlags


class PygameGUI:
    def __init__(self, controller):
        self.controller = controller
        pygame.init()
        self.WIDTH = 800
        self.HEIGHT = 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.GAME_FOLDER = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "..", ".."
        )
        self.IMAGES_FOLDER = os.path.join(self.GAME_FOLDER, "images")

        self.SQUARE_SIZE = 100
        self.GAME_CAPTION = "CHESS"

        self.pieces_images = {
            "R": "white-rock",
            "B": "white-pishop",
            "P": "white-bond",
            "Q": "white-queen",
            "K": "white-king",
            "N": "white-knight",
            "r": "black-rock",
            "b": "black-pishop",
            "p": "black-bond",
            "q": "black-queen",
            "k": "black-king",
            "n": "black-knight",
        }
        self.initial_setup()
        self.keys = pygame.key.get_pressed()
        self.best_move_saved = "e2e4"

        # when users click on his piece the position of the piece is stored here
        # it only stored if it's your piece other wise this is set to null
        self.last_clicked_position = None
        self.last_clicked_piece = None
        # this contains the list of positions that the current piece can move
        self.list_of_available_moves = []
        self.view_best_move = False

    def clear(self):
        self.last_clicked_position = None
        self.last_clicked_piece = None
        self.list_of_available_moves = []

    def render(self):
        # reset the background
        self.screen.blit(self.background, self.background_rect)

        # draw the previous square you clicked
        if self.last_clicked_position:
            self.draw_square(self.last_clicked_position)

        # draw the king square in red if the king in check
        if GameFlags.finished_pos:
            self.draw_square(GameFlags.finished_pos, COLOR=(255, 0, 0))

        # draw the board
        self.draw_board(self.controller.board)

        # draw all available moves
        for move in self.list_of_available_moves:
            self.draw_possible_position(move)

        pygame.display.flip()

    def initial_setup(self):
        for piece_code in self.pieces_images:
            self.pieces_images[piece_code] = pygame.image.load(
                os.path.join(
                    self.IMAGES_FOLDER, f"{self.pieces_images[piece_code]}.svg"
                )
            )
        pygame.display.set_caption(self.GAME_CAPTION)

        self.background = pygame.transform.smoothscale(
            pygame.image.load(os.path.join(self.IMAGES_FOLDER, "board.png")).convert(),
            (self.WIDTH, self.HEIGHT),
        )
        self.background_rect = self.background.get_rect()

    def listen_for_move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.user_action_quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.user_action_clicked(event)
            elif event.type == pygame.KEYDOWN:
                self.keys = pygame.key.get_pressed()
            elif event.type == pygame.KEYUP:
                self.user_action_keyPressed()

    def user_action_quit(self):
        pygame.quit()
        exit()

    def user_action_clicked(self, event):
        x, y = event.pos
        x = x // self.SQUARE_SIZE
        y = y // self.SQUARE_SIZE
        print(y, x)

        position = (y, x)
        piece = self.controller.get_piece_from_pos(position)

        if piece and piece.color == self.controller.get_current_player():
            # add get_list_of_available_moves to controller
            self.list_of_available_moves = self.controller.get_list_of_available_moves(
                position
            )
            self.last_clicked_position = position
            # TODO remove later
            self.render()
            return

        pos_from = self.last_clicked_position
        pos_to = position
        # add validate to controller

        if pos_from and self.controller.is_valid(pos_from, pos_to):
            self.controller.execute_move(pos_from, pos_to)

        self.clear()
        self.render()

    def user_action_keyPressed(self):
        if self.keys[pygame.K_h]:
            self.view_best_move = not self.view_best_move
            self.render()

    def draw_piece(self, image, position):
        self.screen.blit(
            image, (position[0] * self.WIDTH / 8, position[1] * self.HEIGHT / 8)
        )

    def draw_possible_position(self, position):
        pygame.draw.circle(
            self.screen,
            (20, 85, 30),
            (
                position[1] * self.SQUARE_SIZE + 50,
                position[0] * self.SQUARE_SIZE + 50,
            ),
            15,
        )

    def draw_square(self, position, COLOR=(20, 85, 30)):
        pygame.draw.rect(
            self.screen,
            COLOR,
            pygame.Rect(
                position[1] * self.SQUARE_SIZE,
                position[0] * self.SQUARE_SIZE + 2,
                100,
                100,
            ),
        )

    def draw_board(self, board):
        for y, x, piece in board.get_pieces():
            if not piece:
                continue
            piece_image = self.pieces_images.get(piece.code, 0)
            self.draw_piece(piece_image, (x, y))

    def draw_arrows(self, pos1, pos2):
        start_pos = (
            pos1[1] * 100 + 50,
            pos1[0] * 100 + 50,
        )
        end_pos = (
            pos2[1] * 100 + 50,
            pos2[0] * 100 + 50,
        )

        pygame.draw.line(self.screen, (0, 0, 0), start_pos, end_pos, 8)
        pygame.draw.circle(
            self.screen,
            (255, 0, 0),
            (
                pos2[1] * self.SQUARE_SIZE + 50,
                pos2[0] * self.SQUARE_SIZE + 50,
            ),
            15,
        )
