from enum import Enum

INITIAL_BOARD = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
]

INITIAL_BOARD = [
    ["r", "n", "b", "", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
]


class Color(Enum):
    BLACK = "black"
    WHITE = "white"


class Pieces(Enum):
    ROCK = "r"
    PISHOP = "b"
    BOND = "p"
    QUEEN = "q"
    KING = "k"
    KNIGHT = "n"


# White is capital letter while black is small
def get_color_from_type(piece: Pieces) -> Color:
    if piece.value.isupper():
        return Color.WHITE
    return Color.BLACK


class FenConvertor:
    dict = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7,
    }

    @staticmethod
    def from_pos_to_fen(pos):
        y, x = pos
        num = 8 - int(y)
        letter = chr(97 + x)
        return f"{letter}{num}"

    @staticmethod
    def from_fen_to_pos(fen):
        letter, num = list(fen)
        x = ord(letter) - 97
        y = 8 - int(num)

        return (y, x)

    @staticmethod
    def full_fen_to_pos(fen):
        fen1, fen2 = fen[0:2], fen[2:]
        pos1 = FenConvertor.from_fen_to_pos(fen1)
        pos2 = FenConvertor.from_fen_to_pos(fen2)
        return (pos1, pos2)


class GameFlags:
    white_king_can_castle_right = 1
    white_king_can_castle_left = 1
    black_king_can_castle_right = 1
    black_king_can_castle_left = 1
    en_passant = ""
    number_of_total_moves = 0
    number_of_moves_till_50 = 0
    current_player = Color.WHITE
    last_position = None
    last_piece = None
    finished_pos = None
    rock_position_before_castle = None
    rock_position_after_castle = None
    castle_flag = "-"
    game_over = False
