import pygame


from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.life.lives_manager import LivesManager
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.text_utils import get_message
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, GAME_OVER_MESSAGE
from dino_runner.components import text_utils

class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = SCREEN_WIDTH
        self.y_pos_cloud = 70
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.running = True
        self.death_count = 0
        self.powerup_manager = PowerUpManager()
        self.lives_manager = LivesManager()

    def run(self):
        self.lives_manager.refill_lives()
        self.game_speed = 20
        self.points = 0
        self.create_components()
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def create_components(self):
        self.obstacle_manager.reset_obstacles()
        self.powerup_manager.reset_power_ups(self.points, self.player)

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.powerup_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        if self.points >= 500:
            self.screen.fill((30, 30, 30))
        else:
            self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_cloud()
        self.lives_manager.draw(self.screen)
        self.score()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.powerup_manager.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        score, score_rect = get_message('Points {}'.format(self.points), 100, 40)
        self.screen.blit(score, score_rect)
        self.player.check_invincibility(self.screen)

    def show_menu(self):
        self.running = True
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_elements(self.death_count, self.points)
        #the view of the game is update
        pygame.display.update()
        self.handle_key_events_on_menu()

    def print_menu_elements(self, death_count=0, score=0):
        #they are optional
        half_screen_height = SCREEN_HEIGHT//2
        death_count, death_count_rect = text_utils.get_message("Death count: {}".format(self.death_count), height = half_screen_height + 50)
        score, score_rect = text_utils.get_message("Score: {}".format(self.points), height = half_screen_height + 100)
        text, text_rect = get_message('Press any Key to start the game')
        self.screen.blit(text, text_rect)
        self.screen.blit(death_count, death_count_rect)
        self.screen.blit(score, score_rect)
        self.screen.blit(ICON, (500, 150))
        if self.death_count >= 1:
            self.screen.blit(GAME_OVER_MESSAGE, (350, 100))


    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_cloud(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = SCREEN_WIDTH
        self.x_pos_cloud -= self.game_speed - 10