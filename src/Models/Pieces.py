from Models.Piece import Piece, ChessMoves
from settings import Color, GameFlags
from Models.Position import Position


class Rock(Piece, ChessMoves):
    def generate_moevs(self, board, position):
        return self.generate_direct_moves(board, position)


class Bishop(Piece, ChessMoves):
    def generate_moevs(self, board, position):
        return self.generate_diagonal_moves(board, position)


class Queen(Piece, ChessMoves):
    def generate_moevs(self, board, position):
        return self.generate_diagonal_moves(
            board, position
        ) + self.generate_direct_moves(board, position)


class King(Piece):
    def generate_moevs(self, board, position: Position):
        data = []
        y, x = position.get_as_y_x()
        directions_x = [1, -1, 0, 0, 1, -1, 1, -1]
        directions_y = [0, 0, 1, -1, 1, 1, -1, -1]

        for direction in range(8):
            new_x = x + directions_x[direction]
            new_y = y + directions_y[direction]
            if new_x < 8 and new_x >= 0 and new_y >= 0 and new_y < 8:
                new_pos = Position((new_y, new_x))
                piece = board.get_piece(new_pos)
                data.append(new_pos)
                if piece and piece.color == self.color:
                    data.pop()

        if (
            GameFlags.current_player == Color.WHITE
            and GameFlags.white_king_can_castle_right
            and board.get_piece(Position((7, 5))) is None
            and board.get_piece(Position((7, 6))) is None
        ):
            data.append(Position((7, 6)))
        if (
            GameFlags.current_player == Color.WHITE
            and GameFlags.white_king_can_castle_left
            and board.get_piece(Position((7, 3))) is None
            and board.get_piece(Position((7, 2))) is None
            and board.get_piece(Position((7, 1))) is None
        ):
            data.append(Position((7, 2)))
        if (
            GameFlags.current_player == Color.BLACK
            and GameFlags.black_king_can_castle_left
            and board.get_piece(Position((0, 3))) is None
            and board.get_piece(Position((0, 2))) is None
            and board.get_piece(Position((0, 1))) is None
        ):
            data.append(Position((0, 2)))
        if (
            GameFlags.current_player == Color.BLACK
            and GameFlags.black_king_can_castle_right
            and board.get_piece(Position((0, 5))) is None
            and board.get_piece(Position((0, 6))) is None
        ):
            data.append(Position((0, 6)))
        return data


class Bond(Piece):
    def generate_moevs(self, board, position):
        factor = 1
        if self.color == Color.BLACK:
            factor = -1

        data = []
        y, x = position.get_as_y_x()

        piece_one = board.get_piece(Position((y - 1 * factor, x - 1)))
        if piece_one and piece_one.color != self.color:
            data.append(Position((y - 1 * factor, x - 1)))

        piece_two = board.get_piece(Position((y - 1 * factor, x + 1)))
        if piece_two and piece_two.color != self.color:
            data.append(Position((y - 1 * factor, x + 1)))

        piece = board.get_piece(Position((y - 1 * factor, x)))
        if piece:
            return data
        data.append(Position((y - 1 * factor, x)))

        if not self.has_moved_before and not board.get_piece(
            Position((y - 2 * factor, x))
        ):
            data.append(Position((y - 2 * factor, x)))

        return data


class Knight(Piece):
    def generate_moevs(self, board, position: Position):
        data = []
        y, x = position.get_as_y_x()
        directions_x = [2, 2, 1, 1, -2, -2, -1, -1]
        directions_y = [1, -1, 2, -2, 1, -1, 2, -2]

        for direction in range(8):
            new_x = x + directions_x[direction]
            new_y = y + directions_y[direction]
            if new_x < 8 and new_x >= 0 and new_y >= 0 and new_y < 8:
                new_pos = Position((new_y, new_x))
                piece = board.get_piece(new_pos)
                data.append(new_pos)
                if piece and piece.color == self.color:
                    data.pop()

        return data
