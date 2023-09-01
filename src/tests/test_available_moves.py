from Models.Board import Board
from Controller.GameLogic import GameLogic, Controller
from settings import Color


def test_pond_cant_move_if_pened():
    # TODO update the test so it replaces position clicked
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
    controller = Controller(board=board, game_logic=game_logic)
    game_logic.current_player = Color.BLACK
    controller.get_list_of_available_moves((1, 5))  # clicking on f7
    assert len(game_logic.list_available_moves) == 0
    controller.get_list_of_available_moves((0, 1))  # clicking on b8
    assert len(game_logic.list_available_moves) == 2
