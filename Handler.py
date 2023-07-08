import os
import pygame


class Handler:
    GAME_FOLDER = os.path.dirname(os.path.abspath(__file__))
    IMAGES_FOLDER = os.path.join(GAME_FOLDER, "images")
    WIDTH = 800
    HEIGHT = 800
    SQUARE_SIZE = 100
    GAME_CAPTION = "CHESS"
    screen = None

    pieces_images = {
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

    def draw_piece(image, position):
        Handler.screen.blit(
            image, (position[0] * Handler.WIDTH / 8, position[1] * Handler.HEIGHT / 8)
        )

    def draw_possible_position(position):
        pygame.draw.circle(
            Handler.screen,
            (20, 85, 30),
            (
                position[1] * Handler.SQUARE_SIZE + 50,
                position[0] * Handler.SQUARE_SIZE + 50,
            ),
            15,
        )

    def draw_square(position, COLOR=(20, 85, 30)):
        pygame.draw.rect(
            Handler.screen,
            COLOR,
            pygame.Rect(
                position[1] * Handler.SQUARE_SIZE,
                position[0] * Handler.SQUARE_SIZE + 2,
                100,
                100,
            ),
        )

    def draw_arrows(pos1, pos2):
        start_pos = (
            pos1[1] * 100 + 50,
            pos1[0] * 100 + 50,
        )
        end_pos = (
            pos2[1] * 100 + 50,
            pos2[0] * 100 + 50,
        )

        print(start_pos, end_pos)
        pygame.draw.line(Handler.screen, (0, 0, 0), start_pos, end_pos, 8)
        pygame.draw.circle(
            Handler.screen,
            (255, 0, 0),
            (
                pos2[1] * Handler.SQUARE_SIZE + 50,
                pos2[0] * Handler.SQUARE_SIZE + 50,
            ),
            15,
        )
