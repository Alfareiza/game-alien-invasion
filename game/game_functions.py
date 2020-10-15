"""
This module will store some functions that will make the game works
"""
import sys
from time import sleep

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


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset Game Settings
        ai_settings.initialize_dynamic_settings()

        # Hide the cursor mouse
        pygame.mouse.set_visible(False)

        # Reset game statistics
        stats.reset_stats()
        stats.game_active = True

        # Restart the images from the panel of puntuation
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()

        # Empty the list of aliens and projectiles
        aliens.empty()
        bullets.empty()

        # Create a new fleet and centralize the spacecraft
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """Response to key and mouse press events"""
    for event in pygame.event.get():  # Observes keyboard and mouse events
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Updates the images on the screen and switches to the new screen"""
    # Redesign the screen and each passage through the while
    # screen.fill(ai_settings.bg_color)
    screen.blit(ai_settings.bg_image, [0, 0])

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Draws information about puntuation
    sb.show_score()

    # Draws the Play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()  # Leave the most recent screen visible


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Update the position of projetiles and get rid of two old projectiles"""
    bullets.update()
    # Eliminate the projectiles out of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Responds to collisions between projectiles and aliens"""
    # Checks if any projectiles hit the aliens
    # If so, get rid of the projectile and the alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # Destroy existing projectiles and create a new fleet
        bullets.empty()
        ai_settings.increase_speed()

        # Increase the level
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a complete fleet of aliens"""
    # Creating an alien y calculates the number of aliens in a row
    # The spacing between the aliens is equal to the width of an alien
    alien = Alien(ai_settings, screen)
    numbers_aliens_x = get_numbers_aliens_x(ai_settings, alien.rect.width)

    # Creates the first line of aliens
    for alien_number in range(numbers_aliens_x):
        create_alien(ai_settings, alien_number, aliens, screen)


def create_alien(ai_settings, alien_number, aliens, screen):
    """Creates an alien and places it on the line"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def get_numbers_aliens_x(ai_settings, alien_width):
    """Determines the number of aliens that fit in a row"""
    avaliable_space_x = ai_settings.screen_width - 2 * alien_width
    numbers_aliens_x = int(avaliable_space_x / (2 * alien_width))
    return numbers_aliens_x


def change_fleet_direction(ai_settings, aliens):
    """Make all the fleet down and move the direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if some alien reaches the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Verify if the fleet is on the limit of the screen, then
    Update the positions of all aliens of the fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Checks for collisions between aliens and the spaceship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Responds to the fact that the spaceship was hit by an alien."""
    if stats.ships_left > 0:
        # Decrementa a ships_left
        stats.ships_left -= 1

        # Empty the list of aliens and projectiles
        aliens.empty()
        bullets.empty()

        # Create a new fleet and centralize the spacecraft
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause all the game
        sleep(0.7)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Checks if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # This case is treated in the same way as when the spacecraft is hit
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def check_high_score(stats, sb):
    """Checks for a new maximum score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
