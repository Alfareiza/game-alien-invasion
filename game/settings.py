import pygame


class Settings():
    def __init__(self):
        """A class to store all the configurations of the Alien Invasion"""
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.bg_image = pygame.image.load('img/bg.png')
