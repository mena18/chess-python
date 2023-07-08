from Board import Board


def test_king_in_check():
    board = Board()
    board.set_board(
        [
            ["R", "N", "P", "Q", "K", "P", "N", "R"],
            ["B", "B", "B", "B", "B", "q", "B", "B"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["b", "b", "b", "b", "b", "b", "b", "b"],
            ["r", "n", "p", "", "k", "p", "n", "r"],
        ]
    )
    assert board.is_king_in_check(color="black") is True
    board.set_board(
        [
            ["R", "N", "P", "Q", "K", "P", "N", "R"],
            ["B", "B", "B", "B", "B", "b", "B", "B"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["b", "b", "b", "b", "b", "b", "b", "b"],
            ["r", "n", "p", "", "k", "p", "n", "r"],
        ]
    )
    assert board.is_king_in_check(color="black") is True
    board.set_board(
        [
            ["R", "N", "P", "Q", "K", "P", "N", "R"],
            ["B", "B", "B", "B", "B", "B", "B", "B"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["b", "b", "b", "b", "b", "b", "b", "b"],
            ["r", "n", "p", "", "k", "p", "n", "r"],
        ]
    )
    assert board.is_king_in_check(color="black") is False


def test_draw_all_pieces():
    board = Board()
    lis_1 = []
    for y, row in enumerate(board.board):
        for x, piece in enumerate(row):
            lis_1.append((y, x, piece))
    lis_2 = []
    for y, x, piece in board.get_pieces():
        lis_2.append((y, x, piece))

    assert lis_1 == lis_2
