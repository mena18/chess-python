from Piece import Piece
class Rock(Piece):
    def generate_moevs(self,board,position):
        return self.generate_direct_moves(board,position)

class Bishop(Piece):
    def generate_moevs(self,board,position):
        return self.generate_diagonal_moves(board,position)

class Queen(Piece):
    def generate_moevs(self,board,position):
        return self.generate_diagonal_moves(board,position) + self.generate_direct_moves(board,position)


class King(Piece):
    def generate_moevs(self,board,position):
        data = [] 
        y,x = position
        directions_x = [1,-1,0,0,1,-1,1,-1]
        directions_y = [0,0,1,-1,1,1,-1,-1]

        for direction in range(8):
            new_x = x + directions_x[direction]
            new_y = y + directions_y[direction]
            if new_x < 8 and new_x>=0 and new_y>=0 and new_y<8 :
                
                new_pos = (new_y,new_x)
                piece = board.get_piece(new_pos)
                data.append(new_pos)
                if(piece and piece.color==self.color):
                    data.pop()

        return data

class Bond(Piece):
    def generate_moevs(self,board,position):
        factor = 1 
        if self.color== 'black':
            factor = -1

        data = []
        y,x = position

        piece = board.get_piece((y-1*factor,x))
        if(piece):
            return []
        data.append((y-1*factor,x))

        if not self.has_moved_before and not board.get_piece((y-2*factor,x)):
            data.append((y-2*factor,x))

        piece_one = board.get_piece((y-1*factor,x-1))
        if piece_one and piece_one.color!=self.color:
            data.append((y-1*factor,x-1))

        piece_two = board.get_piece((y-1*factor,x+1))
        if piece_two and piece_two.color!=self.color:
            data.append((y-1*factor,x+1))
        return data


class Knight(Piece):
        def generate_moevs(self,board,position):
            data = [] 
            y,x = position
            directions_x = [2,2,1,1,-2,-2,-1,-1]
            directions_y = [1,-1,2,-2,1,-1,2,-2]

            for direction in range(8):
                new_x = x + directions_x[direction]
                new_y = y + directions_y[direction]
                if new_x < 8 and new_x>=0 and new_y>=0 and new_y<8 :
                    
                    new_pos = (new_y,new_x)
                    piece = board.get_piece(new_pos)
                    data.append(new_pos)
                    if(piece and piece.color==self.color):
                        data.pop()

            return data



        



