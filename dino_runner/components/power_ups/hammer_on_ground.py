import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import HAMMER, SCREEN_WIDTH


class HammerOnGround(Sprite):

    def __init__(self, screen): #, rect_x, rect_y
        self.screen = screen
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.pos_x = 0
        self.pos_y = 0


      #  self.rect.x = rect_x
       # self.rect.y = rect_y


    def draw(self, game):
        self.pos_x_when_throw = game.player.dino_rect.x
        self.pos_y_when_throw = game.player.dino_rect.y
        print('pocision inicial puesta')
        self.screen.blit(self.image, (hammer_movement(self.pos_x_when_throw , self.pos_y_when_throw )))
        print('dibujando martillo')


    def throw_hammer(self, game, user_input, type):
        if user_input[pygame.K_SPACE] and game.player.type == type:
            game.player.update_to_default(type)
            game.hammer_is_throw = True
            print('martillo lanzado')

def hammer_movement(inicial_rect_x, inicial_rect_y):
    rect_x = inicial_rect_x + 6
    rect_y = inicial_rect_y
    return rect_x, rect_y
    #self.rect.x += 6
    #self.pos_x = pos_x_when_throw + 6
    print('moviendo martillo')
  #  if self.rect.x > SCREEN_WIDTH:
   #    game.hammer_is_throw = False