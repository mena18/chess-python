from Models.Board import Board
from settings import Color


def test_king_in_check():
    board = Board()
    board.set_board(
        [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "Q", "p", "p"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ]
    )
    assert board.is_king_in_check(color=Color.BLACK) is True
    board.set_board(
        [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "P", "p", "p"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ]
    )
    assert board.is_king_in_check(color=Color.BLACK) is True
    board.set_board(
        [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ]
    )
    assert board.is_king_in_check(color=Color.BLACK) is False


def test_draw_all_pieces():
    board = Board()
    lis_1 = []
    for position, piece in board.get_pieces():
        lis_1.append((position, piece))
    lis_2 = []
    for y, row in enumerate(board.board):
        for x, piece in enumerate(row):
            lis_2.append((y, x, piece))

    assert lis_1 == lis_2
