import os
from dotenv import load_dotenv

load_dotenv()
STOCKFISH_PATH = os.getenv("STOCKFISH_PATH")

from stockfish import Stockfish

stockfish = Stockfish(
    path=STOCKFISH_PATH,
    depth=18,
    parameters={"Threads": 2, "Minimum Thinking Time": 30},
)
stockfish.set_fen_position(
    "r3kbnr/pppb1ppp/2nqp3/1B2N3/2PPp3/8/PP3PPP/RNBQ1RK1 w kq - 2 8"
)

# print(stockfish.get_top_moves(3))
print(stockfish.get_best_move())