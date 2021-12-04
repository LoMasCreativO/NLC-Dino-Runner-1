from pygame.sprite import Sprite

from dino_runner.utils.constants import HEART


class Lives(Sprite):
    def __init__(self, pos_x):
        self.image = HEART
        self.x_pos = pos_x
        self.rect = self.image.get_rect()
        self.rect.y = 30
        self.rect.x = self.x_pos

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

