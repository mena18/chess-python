import os
import pygame


class PygameGUI:
    def __init__(self, controller):
        self.controller = controller
        pygame.init()
        self.WIDTH = 800
        self.HEIGHT = 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.GAME_FOLDER = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), ".."
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
        self.load_images()

        pygame.display.set_caption(self.GAME_CAPTION)

        self.background = pygame.transform.smoothscale(
            pygame.image.load(os.path.join(self.IMAGES_FOLDER, "board.png")).convert(),
            (self.WIDTH, self.HEIGHT),
        )
        self.background_rect = self.background.get_rect()

    def render(self):
        context_obj = self.controller.get_render_context_object()

        # reset the background
        self.screen.blit(self.background, self.background_rect)

        # draw the previous square you clicked
        if context_obj["last_position"]:
            self.draw_square(context_obj["last_position"])

        # draw the king square in red if the king in check
        if context_obj["finished_pos"]:
            self.draw_square(context_obj["finished_pos"], COLOR=(255, 0, 0))

        # draw the board
        self.draw_board(context_obj["board"])

        # draw all available moves
        for move in context_obj["list_available_moves"]:
            self.draw_possible_position(move)

        pygame.display.flip()

    def load_images(self):
        for piece_code in self.pieces_images:
            self.pieces_images[piece_code] = pygame.image.load(
                os.path.join(
                    self.IMAGES_FOLDER, f"{self.pieces_images[piece_code]}.svg"
                )
            )

    def listen_for_move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                x = x // self.SQUARE_SIZE
                y = y // self.SQUARE_SIZE
                print(y, x)
                self.controller.position_clicked((y, x))
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
