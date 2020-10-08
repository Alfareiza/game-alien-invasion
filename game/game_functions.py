"""
This module will store some functions that will make the game works
"""
import sys
import pygame

from game.alien import Alien
from game.bullet import Bullet


def check_keyup_events(event, ship):
    """Response to keydown press events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Response to keyup press events"""
    if event.key == pygame.K_RIGHT:
        # Move the spaceship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the spaceship to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, bullets, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, bullets, screen, ship):
    """Shoot a target if the limit has not yet been reached"""
    # Create a new projectile and add to the projectile group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_events(ai_settings, screen, ship, bullets):
    """Response to key and mouse press events"""
    for event in pygame.event.get():  # Observes keyboard and mouse events
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Updates the images on the screen and switches to the new screen"""
    # Redesign the screen and each passage through the while
    # screen.fill(ai_settings.bg_color)
    screen.blit(ai_settings.bg_image, [0, 0])

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    pygame.display.flip()  # Leave the most recent screen visible


def update_bullets(bullets):
    bullets.update()
    # Eliminate the projectiles out of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a complete fleet of aliens"""
    # Creating an alien y calculates the number of aliens in a row
    # The spacing between the aliens is equal to the width of an alien
    alien = Alien(ai_settings, screen)
    numbers_aliens_x = get_numbers_aliens_x(ai_settings, alien.rect.width)
    numbers_row = get_numbers_row(ai_settings, ship.rect.height, alien.rect.height)

    # Creates the first line of aliens
    for row_number in range(numbers_row):
        for alien_number in range(numbers_aliens_x):
            create_alien(ai_settings, alien_number, aliens, screen, row_number)


def create_alien(ai_settings, alien_number, aliens, screen, row_number):
    """Creates an alien and places it on the line"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_numbers_aliens_x(ai_settings, alien_width):
    """Determines the number of aliens that fit in a row"""
    avaliable_space_x = ai_settings.screen_width - 2 * alien_width
    numbers_aliens_x = int(avaliable_space_x / (2 * alien_width))
    return numbers_aliens_x

def get_numbers_row(ai_settings, ship_height, alien_height):
    """Determines the numbers of row with aliens who fit in the screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    numbers_rows = int(available_space_y / (2 * alien_height))
    return numbers_rows
