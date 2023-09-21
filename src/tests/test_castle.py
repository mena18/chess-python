from Models.Board import Board
from Models.Position import Position
from Controller.GameLogic import Controller, GameLogic
from settings import Color, GameFlags


def test_castle():
    board = Board()
    game_logic = GameLogic(board)
    controller = Controller(board=board, game_logic=game_logic)
    black_king_pos = Position("e8")

    GameFlags.current_player = Color.BLACK

    board.set_board(
        [
            ["r", "", "", "", "k", "", "", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "", "", "", "K", "", "", "R"],
        ]
    )
    list_of_moves = controller.get_list_of_available_moves(black_king_pos.get_as_y_x())
    assert len(list_of_moves) == 4


def test_black_castle_right():
    board = Board()
    game_logic = GameLogic(board)
    controller = Controller(board=board, game_logic=game_logic)
    black_king_pos = Position("e8").get_as_y_x()
    black_king_to_pos = Position("g8").get_as_y_x()
    rock_new_pos = Position("f8").get_as_y_x()

    board.set_board(
        [
            ["r", "", "", "", "k", "", "", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "", "", "", "K", "", "", "R"],
        ]
    )
    controller.execute_move(black_king_pos, black_king_to_pos)
    assert board.get_piece(rock_new_pos).get_type() == "r"
    assert board.get_piece(black_king_to_pos).get_type() == "k"


def test_black_castle_left():
    board = Board()
    game_logic = GameLogic(board)
    controller = Controller(board=board, game_logic=game_logic)
    black_king_pos = Position("e8").get_as_y_x()
    black_king_to_pos = Position("c8").get_as_y_x()
    rock_new_pos = Position("d8").get_as_y_x()

    board.set_board(
        [
            ["r", "", "", "", "k", "", "", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "", "", "", "K", "", "", "R"],
        ]
    )
    controller.execute_move(black_king_pos, black_king_to_pos)
    assert board.get_piece(rock_new_pos).get_type() == "r"
    assert board.get_piece(black_king_to_pos).get_type() == "k"


def test_white_castle_right():
    board = Board()
    game_logic = GameLogic(board)
    controller = Controller(board=board, game_logic=game_logic)
    black_king_pos = Position("e1").get_as_y_x()
    black_king_to_pos = Position("g1").get_as_y_x()
    rock_new_pos = Position("f1").get_as_y_x()

    board.set_board(
        [
            ["r", "", "", "", "k", "", "", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "", "", "", "K", "", "", "R"],
        ]
    )
    controller.execute_move(black_king_pos, black_king_to_pos)
    assert board.get_piece(rock_new_pos).get_type() == "r"
    assert board.get_piece(black_king_to_pos).get_type() == "k"


def test_white_castle_left():
    board = Board()
    game_logic = GameLogic(board)
    controller = Controller(board=board, game_logic=game_logic)
    black_king_pos = Position("e1").get_as_y_x()
    black_king_to_pos = Position("c1").get_as_y_x()
    rock_new_pos = Position("d1").get_as_y_x()

    board.set_board(
        [
            ["r", "", "", "", "k", "", "", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "", "", "", "K", "", "", "R"],
        ]
    )
    controller.execute_move(black_king_pos, black_king_to_pos)
    assert board.get_piece(rock_new_pos).get_type() == "r"
    assert board.get_piece(black_king_to_pos).get_type() == "k"
