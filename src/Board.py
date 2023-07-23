from src.Handler import Handler
from src.PieceFactory import PieceFactory
from copy import deepcopy
from src.settings import Color


class Board:
    def __init__(self, board=None):
        if board is None:
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

        self.set_board(board)

    def get_fen(self, current_player=Color.WHITE):
        fen = ""
        empty_count = 0
        current_player_color_letter = "b" if current_player == Color.BLACK else "w"

        for row in self.board:
            for square in row:
                if square is None:
                    empty_count += 1
                else:
                    if empty_count > 0:
                        fen += str(empty_count)
                        empty_count = 0
                    fen += str(square)

            if empty_count > 0:
                fen += str(empty_count)
                empty_count = 0

            fen += "/"

        fen = fen[:-1]  # Remove the trailing '/'
        fen += f" {current_player_color_letter} - - 0 1"  # Add the remaining FEN fields for turn, castling, etc.

        return fen

    def get_pieces(self):
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                yield (y, x, piece)

    def set_board(self, board):
        self.board = deepcopy(board)
        for x, row in enumerate(board):
            for y, piece_code in enumerate(row):
                if piece_code:
                    self.board[x][y] = PieceFactory.create(piece_code)
                else:
                    self.board[x][y] = None

    def draw(self):
        for y, x, piece in self.get_pieces():
            if not piece:
                continue
            piece_image = Handler.pieces_images.get(piece.code, 0)
            Handler.draw_piece(piece_image, (x, y))

    def get_piece(self, position):
        y, x = position
        return self.board[y][x] if (y >= 0 and y < 8 and x >= 0 and x < 8) else None

    def set_piece(self, position, piece):
        y, x = position
        self.board[y][x] = piece

    def is_king_in_check(self, color):
        king_y, king_x = self.get_king_position(color)
        for y, x, piece in self.get_pieces():
            if piece and piece.color != color:
                moves = piece.generate_moevs(self, (y, x))
                if (king_y, king_x) in moves:
                    return True
        return False

    def get_king_position(self, color):
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                if piece and piece.get_type() == "k" and piece.color == color:
                    return (y, x)

    def make_move(self, from_pos, to_pos):
        self.set_piece(to_pos, self.get_piece(from_pos))
        self.set_piece(from_pos, None)

    def copy(self):
        new_board = Board()
        new_board.board = deepcopy(self.board)
        return new_board
