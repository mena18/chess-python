from src.Engine import Engine
from src.FenConvertor import FenConvertor
from src.Board import Board


class GameLogic:
    def __init__(self, board):
        self.board: Board = board
        self.current_player = "white"
        self.list_available_moves = []
        self.last_position = None
        self.last_piece = None
        self.finished_pos = None
        self.engine = Engine()

    def change_player(self):
        self.current_player = "black" if self.current_player == "white" else "white"

    def clear_data(self):
        self.list_available_moves = []
        self.last_position = None
        self.last_piece = None

    def position_clicked(self, position=()):
        y, x = position
        piece = self.board.get_piece((y, x))
        if piece and piece.color == self.current_player:
            self.my_piece_code(piece, position)
            return

        self.moving_piece_code(piece, position)

    def my_piece_code(self, piece, position):
        available_moves = piece.generate_moevs(self.board, position)
        self.last_position = position
        self.last_piece = piece
        self.list_available_moves = self.moves_after_removing_check(
            self.last_position, available_moves, self.current_player
        )

    def suggest_best_move(self):
        fen = self.board.get_fen(self.current_player[0])
        print(fen)
        self.engine.set_fen(fen)
        move = self.engine.get_best_move()
        print("Best Engine move is ", move)
        return move

    def make_computer_move(self):
        fen = self.board.get_fen(self.current_player[0])
        print(fen)
        self.engine.set_fen(fen)
        move = self.engine.get_best_move()
        print("Engine best move is ", move)

        mv1, mv2 = move[0:2], move[2:]
        mv1 = FenConvertor.from_fen_to_pos(mv1)
        mv2 = FenConvertor.from_fen_to_pos(mv2)
        self.position_clicked(mv1)
        self.position_clicked(mv2)

    def moves_after_removing_check(self, from_pos, list_available_moves, color):
        new_available_list = []

        for position in list_available_moves:
            copied_board = self.board.copy()
            copied_board.make_move(from_pos, position)
            if not copied_board.is_king_in_check(color):
                new_available_list.append(position)

        return new_available_list

    def can_the_king_move(self):
        for y, x, piece in self.board.get_pieces():
            if piece and piece.color != self.current_player:
                moves = piece.generate_moevs(self.board, (y, x))
                final_moves = self.moves_after_removing_check(
                    (y, x), moves, piece.color
                )
                if len(final_moves) > 0:
                    return True
        return False

    def game_over(self):
        current_player = self.current_player
        king_pos = self.board.get_king_position(
            "black" if current_player == "white" else "white"
        )
        self.finished_pos = king_pos

    def moving_piece_code(self, piece, position):
        if position not in self.list_available_moves:
            self.clear_data()
            return

        self.execute_movement(self.last_position, position)

    def execute_movement(self, pos1, pos2):
        # replace with board.make_move
        self.board.make_move(pos1, pos2)
        self.last_piece.has_moved_before = True
        self.clear_data()
        if self.can_the_king_move():
            self.change_player()
        else:
            self.game_over()
