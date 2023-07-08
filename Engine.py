import os
from dotenv import load_dotenv
from stockfish import Stockfish

load_dotenv()


STOCKFISH_PATH = os.getenv("STOCKFISH_PATH")


class Engine:
    def __init__(self):
        self.engine: Stockfish = Stockfish(
            path=STOCKFISH_PATH,
            depth=18,
            parameters={"Threads": 2, "Minimum Thinking Time": 30},
        )

        self.engine.set_fen_position(
            "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 0 1"
        )

    def set_fen(self, fen):
        self.engine.set_fen_position(fen)

    def next_move(self, move):
        return self.engine.make_moves_from_current_position([""])

    def get_best_move(self):
        return self.engine.get_best_move()
