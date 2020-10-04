import sys
import pygame
from game.settings import Settings


def run_game():
    """
    Starts the game
    :return:
    """
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")
    # Starts main loop of the game
    while True:
        for event in pygame.event.get():  # Observes keyboard and mouse events
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)  # Redesign the screen and each passage through the while
        pygame.display.flip()  # Leave the most recent screen visible


run_game()
