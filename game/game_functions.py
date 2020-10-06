"""
This module will store some functions that will make the game works
"""
import sys
import pygame

def check_events():
    """Response to key and mouse press events"""
    for event in pygame.event.get():  # Observes keyboard and mouse events
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Updates the images on the screen and switches to the new screen"""
    # Redesign the screen and each passage through the while
    # screen.fill(ai_settings.bg_color)
    screen.blit(ai_settings.bg_image, [0, 0])
    ship.blitme()

    pygame.display.flip()  # Leave the most recent screen visible