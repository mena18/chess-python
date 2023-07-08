from Board import Board
from GameLogic import GameLogic


def test_pond_cant_move_if_pened():
    board = Board()
    # in that position the F pond shouldn't be able to move at all
    board.set_board(
        [
            ["R", "N", "P", "Q", "K", "P", "N", "R"],
            ["B", "B", "B", "B", "B", "B", "B", "B"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "q"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["b", "b", "b", "b", "b", "b", "b", "b"],
            ["r", "n", "p", "", "k", "p", "n", "r"],
        ]
    )
    game_logic = GameLogic(board)
    game_logic.current_player = "black"
    game_logic.position_clicked((1, 5))  # clicking on f7
    assert len(game_logic.list_available_moves) == 0
    game_logic.position_clicked((0, 1))  # clicking on b8
    assert len(game_logic.list_available_moves) == 2
