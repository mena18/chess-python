import pygame
from settings import StartMenuActions


class button:
    # colours for button and text
    button_col = (21, 101, 192)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = (255, 255, 255)
    width = 300
    height = 70

    def __init__(self, parent, x, y, text):
        self.parent = parent
        self.screen = self.parent.screen
        self.x = x
        self.y = y
        self.text = text
        self.clicked = False

    def draw_button(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                pygame.draw.rect(self.screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False
                action = True
            else:
                pygame.draw.rect(self.screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(self.screen, self.button_col, button_rect)

        # add shading to button
        pygame.draw.line(
            self.screen,
            (255, 255, 255),
            (self.x, self.y),
            (self.x + self.width, self.y),
            2,
        )
        pygame.draw.line(
            self.screen,
            (255, 255, 255),
            (self.x, self.y),
            (self.x, self.y + self.height),
            2,
        )
        pygame.draw.line(
            self.screen,
            (0, 0, 0),
            (self.x, self.y + self.height),
            (self.x + self.width, self.y + self.height),
            2,
        )
        pygame.draw.line(
            self.screen,
            (0, 0, 0),
            (self.x + self.width, self.y),
            (self.x + self.width, self.y + self.height),
            2,
        )

        # add text to button
        text_img = self.parent.font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        self.screen.blit(
            text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25)
        )
        return action


class StartScreen:
    def __init__(self):
        screen_width = 500
        screen_height = 600
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.font = pygame.font.SysFont("Constantia", 30)

        self.play_vs_human = button(self, 100, 150, "Play VS human")
        self.play_as_white_vs_ai = button(self, 100, 300, "Play VS AI as White")
        self.play_as_black_vs_ai = button(self, 100, 450, "Play VS AI as Black")

    def render(self):
        run = True
        while run:
            self.screen.fill((243, 246, 249))

            if self.play_vs_human.draw_button():
                return StartMenuActions.PLAY_VS_HUMAN
            if self.play_as_white_vs_ai.draw_button():
                return StartMenuActions.PLAY_AS_WHITE_VS_AI
            if self.play_as_black_vs_ai.draw_button():
                return StartMenuActions.PLAY_AS_BLACK_VS_AI

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()
