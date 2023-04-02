import os,pygame



class Handler:
    GAME_FOLDER = os.path.dirname(os.path.abspath(__file__))
    IMAGES_FOLDER = os.path.join(GAME_FOLDER,'images')
    WIDTH = 800
    HEIGHT = 800
    SQUARE_SIZE = 100 
    GAME_CAPTION = "CHESS"
    screen = None

    

    pieces_images = {
        'r':"white-rock",
        'b':"white-bond",
        'p':"white-pishop",
        'q':"white-queen",
        'k':"white-king",
        'n':"white-knight",
        'R':"black-rock",
        'B':"black-bond",
        'P':"black-pishop",
        'Q':"black-queen",
        'K':"black-king",
        'N':"black-knight",
    }

    def draw_piece(image,position):
        Handler.screen.blit(image,(position[0]*Handler.WIDTH/8,position[1]*Handler.HEIGHT/8))

    def draw_possible_position(position):
        pygame.draw.circle(Handler.screen, (20,85,30), (position[1]*Handler.SQUARE_SIZE+50,position[0]*Handler.SQUARE_SIZE+50),15)
        
    def draw_square(position):
        pygame.draw.rect(Handler.screen, (20,85,30), pygame.Rect(position[1]*Handler.SQUARE_SIZE,position[0]*Handler.SQUARE_SIZE+2,100,100))




    
