from src.Engine import Engine
from src.settings import FenConvertor, Color, GameFlags
from src.Board import Board


class GameLogic:
    def __init__(self, board):
        self.board: Board = board
        self.flags = GameFlags
        self.engine = Engine()
        self.current_player = self.flags.current_player
        self.list_available_moves = []

    def change_player(self):
        self.current_player = (
            Color.BLACK if self.current_player == Color.WHITE else Color.WHITE
        )

    def clear_data(self):
        self.list_available_moves = []
        self.flags.last_position = None
        self.flags.last_piece = None

    def position_clicked(self, position=()):
        y, x = position
        piece = self.board.get_piece((y, x))
        if piece and piece.color == self.current_player:
            self.my_piece_code(piece, position)
            return

        self.moving_piece_code(piece, position)

    def my_piece_code(self, piece, position):
        available_moves = piece.generate_moevs(self.board, position)
        self.flags.last_position = position
        self.flags.last_piece = piece
        self.list_available_moves = self.moves_after_removing_check(
            self.flags.last_position, available_moves, self.current_player
        )
        print("available moves", self.list_available_moves)

    def suggest_best_move(self):
        fen = self.board.get_fen(self.current_player)

        self.engine.set_fen(fen)
        move = self.engine.get_best_move()
        return move

    def make_computer_move(self):
        fen = self.board.get_fen(self.current_player)
        self.engine.set_fen(fen)
        move = self.engine.get_best_move()

        mv1, mv2 = move[0:2], move[2:]
        mv1 = FenConvertor.from_fen_to_pos(mv1)
        mv2 = FenConvertor.from_fen_to_pos(mv2)
        self.flags.last_position = mv1
        self.flags.last_piece = self.board.get_piece(mv1)
        self.execute_movement(mv1, mv2)

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
            Color.BLACK if current_player == Color.WHITE else Color.WHITE
        )
        self.finished_pos = king_pos

    def moving_piece_code(self, piece, position):
        if position not in self.list_available_moves:
            self.clear_data()
            return

        self.execute_movement(self.flags.last_position, position)

    def execute_movement(self, pos1, pos2):
        # check if it's en-passant
        # check if it's castle
        if self.board.get_piece(pos1).get_type() == "k" and abs(pos1[1] - pos2[1]) == 2:
            king_pos = pos1
            rock_pos = GameFlags.rock_position_before_castle
            king = self.board.get_piece(king_pos)
            rock = self.board.get_piece(rock_pos)

            self.board.set_piece(king_pos, None)
            self.board.set_piece(rock_pos, None)
            self.board.set_piece(pos2, king)
            self.board.set_piece(GameFlags.rock_position_after_castle, rock)
            if self.flags.current_player == Color.WHITE:
                self.flags.white_king_can_castle_left = 0
                self.flags.white_king_can_castle_right = 0
            else:
                self.flags.black_king_can_castle_left = 0
                self.flags.black_king_can_castle_right = 0
        else:
            self.board.make_move(pos1, pos2)

        # replace with board.make_move
        self.flags.last_piece.has_moved_before = True
        self.clear_data()
        if self.can_the_king_move():
            self.change_player()
        else:
            self.game_over()


class Controller:
    def __init__(self, game_logic, board):
        self.game_logic: GameLogic = game_logic
        self.board: Board = board

    def position_clicked(self, position=()):
        y, x = position
        piece = self.board.get_piece((y, x))
        if piece and piece.color == self.game_logic.current_player:
            self.game_logic.my_piece_code(piece, position)
            return

        self.game_logic.moving_piece_code(piece, position)

    def get_render_context_object(self):
        return {
            "list_available_moves": self.game_logic.list_available_moves,
            "board": self.game_logic.board,
            "last_position": self.game_logic.flags.last_position,
            "finished_pos": self.game_logic.flags.finished_pos,
        }
