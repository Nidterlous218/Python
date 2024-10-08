import sys

import pygame

def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.Quit():
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screens."""

    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_colour)
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()