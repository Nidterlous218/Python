import sys

import pygame

class Image():

    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('images/sky.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)


def built_background():
    """Build the background of the game."""
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue!!!!")

    image = Image(screen)

    # Set the background colour
    bg_colour = (0, 0, 0)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

   
        
        # Redraw the screen during each pass through the loop.
        screen.fill(bg_colour)

        image.blitme()

        # Make the most recent drawn screen visible.
        pygame.display.flip()

built_background()

