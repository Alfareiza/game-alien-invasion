import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class that manages projectiles fired by the spacecraft"""

    def __init__(self, ai_settings, screen, ship):
        """Creates an object for the projectile at the spacecraft's position"""
        super(Bullet, self).__init__()
        self.screen = screen

        """Create a rectangle for the projectile at (0, 0) and then set the correct position"""
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        """Stores the position of the projectile as a decimal value"""
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

    def update(self):
        """Moves the projectile up the screen"""
        # Updates the projectile's decimal position
        self.y -= self.speed
        # Updates the rect's position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the projectile on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

