class FenConvertor:
    dict = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7,
    }

    @staticmethod
    def from_pos_to_fen(pos):
        y, x = pos
        num = 8 - int(y)
        letter = chr(97 + x)
        return f"{letter}{num}"

    @staticmethod
    def from_fen_to_pos(fen):
        letter, num = list(fen)
        x = ord(letter) - 97
        y = 8 - int(num)

        return (y, x)

    @staticmethod
    def full_fen_to_pos(fen):
        fen1, fen2 = fen[0:2], fen[2:]
        pos1 = FenConvertor.from_fen_to_pos(fen1)
        pos2 = FenConvertor.from_fen_to_pos(fen2)
        return (pos1, pos2)
