from Board import Board
from GameLogic import GameLogic


def test_pond_cant_move_if_pened():
    board = Board()
    # in that position the F pond shouldn't be able to move at all
    board.set_board(
        [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "Q"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ]
    )
    game_logic = GameLogic(board)
    game_logic.current_player = "black"
    game_logic.position_clicked((1, 5))  # clicking on f7
    assert len(game_logic.list_available_moves) == 0
    game_logic.position_clicked((0, 1))  # clicking on b8
    assert len(game_logic.list_available_moves) == 2
