from Handler import Handler
from Piece import Piece
from PieceFactory import PieceFactory
class Board:
    
    def __init__(self):
        self.board = [
            ['R','N','P','Q','K','P','N','R'],
            ['B','B','B','B','B','B','B','B'],
            [None,None,None,None,None,None,None,None,],
            [None,None,None,None,None,None,None,None,],
            [None,None,None,None,None,None,None,None,],
            [None,None,None,None,None,None,None,None,],
            ['b','b','b','b','b','b','b','b'],
            ['r','n','p','q','k','p','n','r'],
        ]

        for x,row in enumerate(self.board):
            for y,piece_code in enumerate(row):
                if piece_code:
                    self.board[x][y] = PieceFactory.create(piece_code)
    

    def draw(self):
        for x,row in enumerate(self.board):
            for y,piece in enumerate(row):
                if not piece:
                    continue
                piece_image = Handler.pieces_images.get(piece.code,0)
                Handler.draw_piece(piece_image,(y,x))
    
    def get_piece(self,position):
        y,x = position
        return self.board[y][x] if (y>=0 and y < 8 and x>=0 and x<8) else None
    
    def set_piece(self,position,piece):
        y,x = position
        self.board[y][x] = piece
    
    def is_king_in_check(color):
        # find the king and return whether the king is in check or not
        return False
    
    def get_king_position(color):
        pass
    
    def copy():
        return None
    
