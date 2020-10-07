import pygame


class Settings():
    def __init__(self):
        """A class to store all the configurations of the Alien Invasion"""
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.bg_image = pygame.image.load('img/bg.png')

        # Settings of spaceship
        self.ship_speed = 3.5

        # Settings of projectiles
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 250, 88
