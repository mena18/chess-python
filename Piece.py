class Piece:
    def __init__(self, piece_code):
        self.code = piece_code
        self.has_moved_before = False

    def get_type(self):
        return self.code.lower()

    @property
    def color(self):
        return "white" if self.code.islower() else "black"

    def generate_moevs(self, board, position):
        if self.color == "white":
            return [(position[0] - 1, position[1]), (position[0] - 2, position[1])]
        return [(position[0] + 1, position[1]), (position[0] + 2, position[1])]

    def generate_direct_moves(self, board, position):
        data = []
        y, x = position
        directions_x = [1, -1, 0, 0]
        directions_y = [0, 0, 1, -1]

        for direction in range(4):
            new_x = x + directions_x[direction]
            new_y = y + directions_y[direction]
            while new_x < 8 and new_x >= 0 and new_y >= 0 and new_y < 8:
                new_pos = (new_y, new_x)
                piece = board.get_piece(new_pos)
                if piece:
                    if piece.color != self.color:
                        data.append(new_pos)
                    break
                data.append(new_pos)
                new_x += directions_x[direction]
                new_y += directions_y[direction]

        return data

    def generate_diagonal_moves(self, board, position):
        data = []
        y, x = position
        directions_x = [1, -1, 1, -1]
        directions_y = [1, 1, -1, -1]

        for direction in range(4):
            new_x = x + directions_x[direction]
            new_y = y + directions_y[direction]
            while new_x < 8 and new_x >= 0 and new_y >= 0 and new_y < 8:
                new_pos = (new_y, new_x)
                piece = board.get_piece(new_pos)
                if piece:
                    if piece.color != self.color:
                        data.append(new_pos)
                    break
                data.append(new_pos)
                new_x += directions_x[direction]
                new_y += directions_y[direction]

        return data

    def __str__(self):
        return f"{self.code} - {self.color}"
