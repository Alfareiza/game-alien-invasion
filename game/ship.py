import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the img of spaceship and get his rectangle
        self.image = pygame.image.load('img/spaceship1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Starts every new spaceship in the inferior central part of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store every decimal value for the center of the spaceship
        self.center = float(self.rect.centerx)

        # Motion flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Design a spaceship in his current position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updates the spaceship's position according to the motion flag."""
        if self.moving_right:
            self.center += self.ai_settings.ship_speed
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed

        # Update the object rect according to the self.center
        self.rect.centerx = self.center
