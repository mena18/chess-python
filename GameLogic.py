from Handler import Handler

class GameLogic:
    def __init__(self,board):
        self.board = board
        self.current_player = 'white'
        self.list_available_moves = []
        self.last_position = None
        self.last_piece = None

    
    def change_player(self):
        self.current_player = 'black' if self.current_player == 'white' else 'white'

    def clear_data(self):
        self.list_available_moves = []
        self.last_position = None
        self.last_piece = None

    def position_clicked(self,position):
        y,x = position
        piece = self.board.get_piece((y,x))
        if piece and piece.color == self.current_player:
            self.my_piece_code(piece,position)
            return 
        
        self.moving_piece_code(piece,position)

    def my_piece_code(self,piece,position):
        print("my piece",piece,position)
        available_moves = piece.generate_moevs(self.board,position)
        self.list_available_moves = available_moves
        self.last_position = position
        self.last_piece = piece


    def is_king_in_check(self):
        check = self.board.is_king_in_check(self.current_player)
        if not check :
            return  
        
        new_available_list = self.list_available_moves

        # new_available_list = []
        for position in self.list_available_moves:
            copied_board = self.board.copy()
            # execute the movement
            # see if the king still in check or not and if it's in check don't add it 
            # else add the move 

        self.list_available_moves = new_available_list
        


    def can_the_king_move(self):
        return True

    
    def game_over(self):
        print("the game is finished")

    
    def moving_piece_code(self,piece,position):
        if position not in self.list_available_moves:
            self.clear_data()
            return 
        
        self.execute_movement(self.last_position,position)
        print("moving piece code",piece,position)

    def execute_movement(self,pos1,pos2):
        self.board.set_piece(pos2,self.board.get_piece(pos1))
        self.board.set_piece(pos1,None)
        self.last_piece.has_moved_before = True
        self.clear_data()
        if self.can_the_king_move():
            self.change_player()
        else:
            self.game_over()
    


