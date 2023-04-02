import pygame,os,random
from GameLogic import GameLogic
from Board import Board
from Handler import Handler



class Game:

    def __init__(self):
        
        pygame.init()
        
        Handler.screen = pygame.display.set_mode((Handler.WIDTH,Handler.HEIGHT))
        for piece_code in Handler.pieces_images:
            Handler.pieces_images[piece_code] = pygame.image.load(os.path.join(Handler.IMAGES_FOLDER,f'{Handler.pieces_images[piece_code]}.svg'))

        
        pygame.display.set_caption(Handler.GAME_CAPTION)
        

        self.background = pygame.transform.smoothscale(pygame.image.load(os.path.join(Handler.IMAGES_FOLDER,"board.png")).convert(), (Handler.WIDTH,Handler.HEIGHT))
        self.background_rect = self.background.get_rect()

        self.board = Board()        
        self.game_logic = GameLogic(self.board)


    def draw(self):
        Handler.screen.blit(self.background, self.background_rect)
        if self.game_logic.last_position:
            Handler.draw_square(self.game_logic.last_position)
        self.board.draw()
        for move in self.game_logic.list_available_moves:
            Handler.draw_possible_position(move)

    def start_game(self):
        while True:
            
            self.draw()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x,y = event.pos
                    x=x//100;y=y//100;
                    square_num = y*8+x
                    self.game_logic.position_clicked((y,x))
                    
                    

            pygame.display.flip()

        pygame.quit()

game = Game()
game.start_game()