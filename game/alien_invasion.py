import pygame
from pygame.sprite import Group

from game import game_functions
from game.alien import Alien
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
    ship = Ship(ai_settings, screen)
    # Create a group in which the projectiles will be stored
    bullets = Group()
    # Create a group of Aliens
    aliens = Group()

    game_functions.create_fleet(ai_settings, screen, ship, aliens)

    # Starts main loop of the game
    while True:
        game_functions.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        game_functions.update_bullets(ai_settings, screen, ship, aliens, bullets)
        game_functions.update_aliens(ai_settings, aliens)
        game_functions.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
