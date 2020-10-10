import pygame


class Settings():
    def __init__(self):
        """A class to store all the configurations of the Alien Invasion"""
        self.screen_width = 1100
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.bg_image = pygame.image.load('img/bg.png')

        # Settings of spaceship
        self.ship_speed = 3.5
        self.ship_limit = 3

        # Settings of projectiles
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 250, 88
        self.bullets_allowed = 3

        # Settings of Aliens
        self.alien_speed = 1
        self.fleet_drop_speed = 10

        # fleet_direction equal to 1 means to right; -1 means to left
        self.fleet_direction = 1
