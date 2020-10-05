import pygame


class Ship():
    def __init__(self, screen):
        self.screen = screen

        # Load the img of spaceship and get his rectangle
        self.image = pygame.image.load('img/spaceship1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Starts every new spaceship in the inferior central part of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Design a spaceship in his current position"""
        self.screen.blit(self.image, self.rect)
