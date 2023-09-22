def generate_fen(board):
    fen = ""
    empty_count = 0

    for row in board:
        for square in row:
            if square == "":
                empty_count += 1
            else:
                if empty_count > 0:
                    fen += str(empty_count)
                    empty_count = 0
                fen += square

        if empty_count > 0:
            fen += str(empty_count)
            empty_count = 0

        fen += "/"

    fen = fen[:-1]  # Remove the trailing '/'
    fen += " w - - 0 1"  # Add the remaining FEN fields for turn, castling, etc.

    return fen


board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
]

fen = generate_fen(board)
