"""
This module will store some functions that will make the game works
"""
import sys
import pygame

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


def update_screen(ai_settings, screen, ship, alien, bullets):
    """Updates the images on the screen and switches to the new screen"""
    # Redesign the screen and each passage through the while
    # screen.fill(ai_settings.bg_color)
    screen.blit(ai_settings.bg_image, [0, 0])

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    alien.blitme()

    pygame.display.flip()  # Leave the most recent screen visible


def update_bullets(bullets):
    bullets.update()
    # Eliminate the projectiles out of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
