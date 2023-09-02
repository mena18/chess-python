from Controller.Engine import Engine
from settings import FenConvertor, Color, GameFlags
from Models.Board import Board
from Models.Piece import Piece


class GameLogic:
    def __init__(self, board):
        self.board: Board = board
        self.engine = Engine()
        self.list_available_moves = []

    def change_player(self):
        GameFlags.current_player = (
            Color.BLACK if GameFlags.current_player == Color.WHITE else Color.WHITE
        )

    def clear_data(self):
        self.list_available_moves = []
        GameFlags.last_position = None
        GameFlags.last_piece = None

    def suggest_best_move(self):
        fen = self.board.get_fen(GameFlags.current_player)
        print("suggest", end="  ")
        try:
            self.engine.set_fen(fen)
            move = self.engine.get_best_move()
            return move
        except:
            return None

    def make_computer_move(self):
        fen = self.board.get_fen(GameFlags.current_player)
        print("play ", end="  ")
        self.engine.set_fen(fen)
        move = self.engine.get_best_move()

        mv1, mv2 = move[0:2], move[2:]
        mv1 = FenConvertor.from_fen_to_pos(mv1)
        mv2 = FenConvertor.from_fen_to_pos(mv2)
        GameFlags.last_position = mv1
        GameFlags.last_piece = self.board.get_piece(mv1)
        self.execute_movement(mv1, mv2)
        self.after_movement_execution(self.board.get_piece(mv2))

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
            if piece and piece.color != GameFlags.current_player:
                moves = piece.generate_moevs(self.board, (y, x))
                final_moves = self.moves_after_removing_check(
                    (y, x), moves, piece.color
                )
                if len(final_moves) > 0:
                    return True
        return False

    def game_over(self):
        print("Game OVER")
        king_pos = self.board.get_king_position(
            Color.BLACK if GameFlags.current_player == Color.WHITE else Color.WHITE
        )
        GameFlags.finished_pos = king_pos
        GameFlags.game_over = True

    def end_castling_if_king_or_rock(self, pos):
        piece = self.board.get_piece(pos)

        if GameFlags.current_player == Color.WHITE:
            if piece.get_type() == "k" or pos == (7, 0):
                GameFlags.white_king_can_castle_left = 0
            if piece.get_type() == "k" or pos == (7, 7):
                GameFlags.white_king_can_castle_right = 0
        if GameFlags.current_player == Color.BLACK:
            if piece.get_type() == "k" or pos == (0, 0):
                GameFlags.black_king_can_castle_left = 0
            if piece.get_type() == "k" or pos == (0, 7):
                GameFlags.black_king_can_castle_right = 0

    def execute_movement(self, pos1, pos2):
        # remove castling if you moved a king or a rock
        self.end_castling_if_king_or_rock(pos1)

        # if it's a castle move made it and end castle
        if self.board.get_piece(pos1).get_type() == "k" and abs(pos1[1] - pos2[1]) == 2:
            king_pos = pos1
            rock_pos = GameFlags.rock_position_before_castle
            king = self.board.get_piece(king_pos)
            rock = self.board.get_piece(rock_pos)

            self.board.set_piece(king_pos, None)
            self.board.set_piece(rock_pos, None)
            self.board.set_piece(pos2, king)
            self.board.set_piece(GameFlags.rock_position_after_castle, rock)
            if GameFlags.current_player == Color.WHITE:
                GameFlags.white_king_can_castle_left = 0
                GameFlags.white_king_can_castle_right = 0
            else:
                GameFlags.black_king_can_castle_left = 0
                GameFlags.black_king_can_castle_right = 0
        # if it's just a king or a rock move make castling is 0

        # if it's a passwn move and x and y changed it's en-passwant
        elif GameFlags.en_passant:
            pass
        else:
            self.board.make_move(pos1, pos2)

        # replace with board.make_move
        self.board.get_piece(pos2).has_moved_before = True

        self.clear_data()

    def after_movement_execution(self, piece: Piece):
        piece.has_moved_before = True
        print("can the king move", self.can_the_king_move())
        if self.can_the_king_move():
            self.change_player()
        else:
            self.game_over()
            return


class Controller:
    def __init__(self, game_logic, board):
        self.game_logic: GameLogic = game_logic
        self.board: Board = board

    def get_piece_from_pos(self, position):
        return self.board.get_piece(position)

    def get_current_player(self):
        return GameFlags.current_player

    def get_list_of_available_moves(self, position):
        piece: Piece = self.board.get_piece(position)
        available_moves = piece.generate_moevs(self.board, position)
        available_moves = self.game_logic.moves_after_removing_check(
            position, available_moves, self.get_current_player()
        )
        return available_moves

    def is_valid(self, pos_from, pos_to):
        list_of_moves = self.get_list_of_available_moves(pos_from)
        return pos_to in list_of_moves

    def execute_move(self, pos_from, pos_to):
        piece: Piece = self.board.get_piece(pos_from)

        self.game_logic.execute_movement(pos_from, pos_to)
        self.game_logic.after_movement_execution(piece)

    def make_computer_move(self):
        self.game_logic.make_computer_move()
