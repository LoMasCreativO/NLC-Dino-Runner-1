import random

import pygame

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(random.choice([Cactus(random.choice([LARGE_CACTUS, SMALL_CACTUS])), Bird(BIRD)]))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.powerup_manager.hammer.rect.colliderect(obstacle.rect):
                if obstacle in self.obstacles:
                    self.obstacles.remove(obstacle)

            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    self.obstacles.remove(obstacle)
                    game.lives_manager.delete_lives()
                    if game.lives_manager.lives_counter() == 0:
                        pygame.time.delay(1000)
                        game.playing = False
                        game.death_count += 1
                    break
                else:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []