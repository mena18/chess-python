class Position:
    def __init__(self, position=None):
        if type(position) == str:
            self.set_as_fen(position)
        elif type(position) == tuple and len(position) == 2:
            self.position = position
        else:
            self.position = (0, 0)

    def get_as_fen(self):
        y, x = self.position
        num = 8 - int(y)
        letter = chr(97 + x)
        return f"{letter}{num}"

    def get_as_y_x(self):
        return self.position

    def set_as_y_x(self, position):
        self.position = position

    def set_as_fen(self, fen):
        letter, num = list(fen)
        x = ord(letter) - 97
        y = 8 - int(num)

        self.position = (y, x)

    def __str__(self):
        return self.get_as_fen()

    def __repr__(self):
        return self.get_as_fen()

    def __eq__(self, object):
        if type(object) == str:
            return self.get_as_fen() == object
        if type(object) == Position:
            return self.get_as_fen() == object.get_as_fen()
        if type(object) == tuple and len(object) == 2:
            return self.position == object
        return False

        pdb.set_trace()
        return super.__eq__(self, object)
