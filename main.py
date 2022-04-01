import pygame
import sys
import time
from settings import *


class Game:
    def __init__(self):

        pygame.init()
        self.display_surface = pygame.display.set_mode(
            (screen_width, screen_height))
        pygame.display.set_caption('BrickBasher')
        self.bg = self.create_bg()

    def create_bg(self):
        bg_original = pygame.image.load(
            './graphics/other/space-background.jpg').convert()
        scaled_bg = pygame.transform.scale(
            bg_original, (screen_width, screen_height))
        return scaled_bg

    def run(self):
        last_time = time.time()
        while True:
            dt = time.time() - last_time
            last_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.display_surface.blit(self.bg, (0, 0))

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
