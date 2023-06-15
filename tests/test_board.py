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
