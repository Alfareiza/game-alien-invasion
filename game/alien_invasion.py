import sys
import pygame
from game.settings import Settings
from game.ship import Ship


def run_game():
    """
    Starts the game
    :return:
    """
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create a spaceship
    ship = Ship(screen)

    # Starts main loop of the game
    while True:
        for event in pygame.event.get():  # Observes keyboard and mouse events
            if event.type == pygame.QUIT:
                sys.exit()

        # Redesign the screen and each passage through the while
        # screen.fill(ai_settings.bg_color)
        screen.blit(ai_settings.bg_image, [0, 0])
        ship.blitme()

        pygame.display.flip()  # Leave the most recent screen visible


run_game()
