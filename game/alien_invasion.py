import sys
import pygame


def run_game():
    """
    Starts the game
    :return:
    """
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)  # Background Color
    # Starts main loop of the game
    while True:
        for event in pygame.event.get():  # Observes keyboard and mouse events
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)  # Redesign the screen and each passage through the while
        pygame.display.flip()  # Leave the most recent screen visible


run_game()
9