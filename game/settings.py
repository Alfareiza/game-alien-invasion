import pygame


class Settings():
    def __init__(self):
        """A class to store all the configurations of the Alien Invasion"""
        self.screen_width = 1100
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.bg_image = pygame.image.load('img/bg.png')

        # Settings of spaceship
        # self.ship_speed = 3.5
        self.ship_limit = 3

        # Settings of projectiles
        # self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 250, 88
        self.bullets_allowed = 3

        # Settings of Aliens
        # self.alien_speed = 3
        self.fleet_drop_speed = 10

        # The rate at which the game speed increases
        self.speedup_scale = 2.1
        self.initialize_dynamic_settings()

        # The rate at which points for each alien increase
        self.score_scale = 1.5

        # Puntuation
        self.alien_points = 50

    def initialize_dynamic_settings(self):
        """Inicializa as configurações"""
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1.5

        # fleet_direction equal to 1 means to right; -1 means to left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and the points for every alien killed"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

