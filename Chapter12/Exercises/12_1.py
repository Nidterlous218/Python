import sys

import pygame

def built_background():
    """Build the background of the game."""
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue!!!!")

    # Set the background colour
    bg_colour = (0, 0, 255)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

   
        
        # Redraw the screen during each pass through the loop.
        screen.fill(bg_colour)

        # Make the most recent drawn screen visible.
        pygame.display.flip()

built_background()

