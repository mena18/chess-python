from Piece import Piece
from Pieces import King,Rock,Bond,Queen,Knight,Bishop

class PieceFactory:
    list_of_pieces = {
        'r':Rock,
        'b':Bond,
        'n':Knight,
        'p':Bishop,
        'k':King,
        'q':Queen

    }
    def create(code):
        return PieceFactory.list_of_pieces[code.lower()](code)