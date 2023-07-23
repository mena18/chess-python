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
