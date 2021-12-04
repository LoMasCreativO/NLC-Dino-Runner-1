import pygame.font


from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = 'freesansbold.ttf'
color = (100, 100, 100)

def get_message(message, width = SCREEN_WIDTH//2 , height = SCREEN_HEIGHT//2):

    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(message, True, color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect