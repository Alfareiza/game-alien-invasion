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

    # Starts main loop of the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()

run_game()