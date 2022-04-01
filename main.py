import pygame
import sys
import time
from settings import *


class Game:
    def __init__(self):

        pygame.init()
        self.display_surface = pygame.display.set_mode(
            screen_width, screen_height)
        pygame.display.set_caption('BrickBasher')

    def run(self):
        last_time = time.time()
        while True:
            dt = time.time() - last_time
            last_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
