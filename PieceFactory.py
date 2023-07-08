from Pieces import King, Rock, Bond, Queen, Knight, Bishop


class PieceFactory:
    list_of_pieces = {
        "r": Rock,
        "p": Bond,
        "n": Knight,
        "b": Bishop,
        "k": King,
        "q": Queen,
    }

    def create(code):
        return PieceFactory.list_of_pieces[code.lower()](code)
