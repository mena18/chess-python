from Models.Pieces import King, Rock, Bond, Queen, Knight, Bishop


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
        # R means white rock white r means black rock so get lower of code to get the piece type
        piece_code = code.lower()
        # getting piece class
        PieceClass = PieceFactory.list_of_pieces[piece_code]
        # return the piece itself
        return PieceClass(code)
