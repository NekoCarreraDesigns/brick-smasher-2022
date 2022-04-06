import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        # setup
        self.image = pygame.Surface((screen_width // 10, screen_height // 20))
        self.image.fill('red')
        # position
        self.rect = self.image.get_rect(midbottom=(
            screen_width // 2, screen_height - 20))
        self.direction = pygame.math.Vector2()
        self.speed = 400
        self.pos = pygame.math.Vector2(self.rect.topleft)
    # player input for movement

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def screen_constraint(self):
        if self.rect.right > screen_width:
            self.rect.right = screen_width
            self.pos.x = self.rect.x
        if self.rect.left < 0:
            self.rect.left = 0
            self.pos.x = self.rect.x

    # update the game
    def update(self, dt):
        self.input()
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.screen_constraint()
