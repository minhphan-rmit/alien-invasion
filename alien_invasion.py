# import section

# import sys
import sys

# import pygame
import pygame


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        # class Clock from pygame.time module
        self.clock = pygame.time.Clock()

        # create a 1200x800 pixels game screen
        self.screen = pygame.display.set_mode((1200, 800))
        # set the name for the game screen
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible
            pygame.display.flip()
            # set the game frame rate to 60fps
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

