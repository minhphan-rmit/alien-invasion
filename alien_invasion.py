# import section

# import sys
import sys

# import pygame
import pygame

# import settings
from settings import Settings


# main section
class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        # class Clock from pygame.time module
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # create a 1200x800 pixels game screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # set the name for the game screen
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible
            pygame.display.flip()
            # set the game frame rate to 60fps
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

