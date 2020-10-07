import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class that manages projectiles fired by the spacecraft"""

    def __init__(self, ai_settings, screen):
        """Creates an object for the projectile at the spacecraft's position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        """Create a rectangle for the projectile at (0, 0) and then set the correct position"""
        # Load the img of spaceship and get his rectangle
        self.image = pygame.image.load('img/alien2.png')
        self.rect = self.image.get_rect()  # Rect of the image

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Stores the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Design a spaceship in his current position"""
        self.screen.blit(self.image, self.rect)

