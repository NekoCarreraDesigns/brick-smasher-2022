import pygame
import sys
import time
from settings import *
from sprites import Player, Ball


class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.display_surface = pygame.display.set_mode(
            (screen_width, screen_height))
        pygame.display.set_caption('BrickBasher')
        # background
        self.bg = self.create_bg()
        # sprite group
        self.all_sprites = pygame.sprite.Group()
        # sprite setup
        self.player = Player(self.all_sprites)
        self.ball = Ball(self.all_sprites, self.player)
        self.stage_setup()

    def create_bg(self):
        bg_original = pygame.image.load(
            './graphics/other/space-background.jpg').convert()
        scaled_bg = pygame.transform.scale(
            bg_original, (screen_width, screen_height))
        return scaled_bg

    def stage_setup(self):
        # cycle through the rows in the block map
        for row_index, row in enumerate(block_map):
            for col_index, col in enumerate(row):
                # find the x and y positions
                x = col_index * (block_width + gap_size) + gap_size // 2
                y = row_index * (block_height + gap_size) + gap_size // 2
                Block(type, pos, groups)

    def run(self):
        last_time = time.time()
        while True:
            # delta time
            dt = time.time() - last_time
            last_time = time.time()
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.ball.active = True

            # update the game
            self.all_sprites.update(dt)

            # draw frame
            self.display_surface.blit(self.bg, (0, 0))
            self.all_sprites.draw(self.display_surface)

            # update window
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
