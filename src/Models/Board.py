from Models.PieceFactory import PieceFactory
from copy import deepcopy
from settings import Color, Pieces, INITIAL_BOARD, GameFlags
from Models.Position import Position
from Models.Piece import Piece


class Board:
    def __init__(self, board=INITIAL_BOARD):
        self.set_board(board)

    # convert board to fen : Note that the fen has other states like is castle happen and
    # is there enpassawant and many other things so it should be handled in other place
    # and get fen should only convert the board to fen without carring about other variables
    def get_fen(self, current_player=Color.WHITE):
        fen = ""
        empty_count = 0
        current_player_color_letter = "b" if current_player == Color.BLACK else "w"
        castleConditions = ""
        if GameFlags.white_king_can_castle_right:
            castleConditions += "K"
        if GameFlags.white_king_can_castle_left:
            castleConditions += "Q"
        if GameFlags.black_king_can_castle_right:
            castleConditions += "k"
        if GameFlags.black_king_can_castle_left:
            castleConditions += "q"
        if len(castleConditions) == 0:
            castleConditions = "-"

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
        fen += f" {current_player_color_letter} {castleConditions} - 0 1"  # Add the remaining FEN fields for turn, castling, etc.

        return fen

    # loop over all the pieces
    def get_pieces(self):
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                yield (Position((y, x)), piece)

    # create board from array of pieces
    # TODO i should create another one to create board from fen
    def set_board(self, board):
        self.board = deepcopy(board)
        for x, row in enumerate(board):
            for y, piece_code in enumerate(row):
                if piece_code:
                    self.board[x][y] = PieceFactory.create(piece_code)
                else:
                    self.board[x][y] = None

    def get_piece(self, position: Position):
        y, x = position.get_as_y_x()
        return self.board[y][x] if (y >= 0 and y < 8 and x >= 0 and x < 8) else None

    def set_piece(self, position: Position, piece):
        y, x = position.get_as_y_x()
        self.board[y][x] = piece

    def is_king_in_check(self, color):
        king_position = self.get_king_position(color)
        for position, piece in self.get_pieces():
            if piece and piece.color != color:
                moves = piece.generate_moevs(self, position)
                if king_position in moves:
                    return True
        return False

    def get_king_position(self, color):
        for position, piece in self.get_pieces():
            if piece and piece.get_type() == Pieces.KING.value and piece.color == color:
                return position

    def make_move(self, from_pos, to_pos):
        self.set_piece(to_pos, self.get_piece(from_pos))
        self.set_piece(from_pos, None)

    def copy(self):
        new_board = Board()
        new_board.board = deepcopy(self.board)
        return new_board
