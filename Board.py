from Handler import Handler
from PieceFactory import PieceFactory
from copy import deepcopy


class Board:
    def __init__(self, board=None):
        if board is None:
            board = [
                ["R", "N", "P", "Q", "K", "P", "N", "R"],
                ["B", "B", "B", "B", "B", "B", "B", "B"],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["b", "b", "b", "b", "b", "b", "b", "b"],
                ["r", "n", "p", "q", "k", "p", "n", "r"],
            ]

        self.set_board(board)

    def set_board(self, board):
        self.board = deepcopy(board)
        for x, row in enumerate(board):
            for y, piece_code in enumerate(row):
                if piece_code:
                    self.board[x][y] = PieceFactory.create(piece_code)
                else:
                    self.board[x][y] = None

    def draw(self):
        for x, row in enumerate(self.board):
            for y, piece in enumerate(row):
                if not piece:
                    continue
                piece_image = Handler.pieces_images.get(piece.code, 0)
                Handler.draw_piece(piece_image, (y, x))

    def get_piece(self, position):
        y, x = position
        return self.board[y][x] if (y >= 0 and y < 8 and x >= 0 and x < 8) else None

    def set_piece(self, position, piece):
        y, x = position
        self.board[y][x] = piece

    def is_king_in_check(self, color):
        king_y, king_x = self.get_king_position(color)
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
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
