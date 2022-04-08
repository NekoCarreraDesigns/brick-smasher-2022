import pygame
from settings import *
from random import choice


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        # setup
        self.image = pygame.Surface((screen_width // 10, screen_height // 20))
        self.image.fill('red')
        # position
        self.rect = self.image.get_rect(midbottom=(
            screen_width // 2, screen_height - 20))
        self.old_rect = self.rect.copy()
        self.direction = pygame.math.Vector2()
        self.speed = 300
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
        self.old_rect = self.rect.copy()
        self.input()
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.screen_constraint()


class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, player):
        super().__init__(groups)

        # collsion objects
        self.player = player

        # graphics setup
        self.image = pygame.image.load(
            './graphics/other/ball.png').convert_alpha()

        # position setup
        self.rect = self.image.get_rect(midbottom=player.rect.midtop)
        self.old_rect = self.rect.copy
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2((choice((1, -1)), -1))
        self.speed = 400

        # active
        self.active = False

    def window_collision(self, direction):
        if direction == 'horizontal':
            if self.rect.left < 0:
                self.rect.left = 0
                self.pos.x = self.rect.x
                self.direction.x *= -1

            if self.rect.right > screen_width:
                self.rect.right = screen_width
                self.pos.x = self.rect.x
                self.direction.x *= -1

        if direction == 'vertical':
            if self.rect.top < 0:
                self.rect.top = 0
                self.pos.y = self.rect.y
                self.direction.y *= -1

            if self.rect.bottom > screen_height:
                self.active = False
                self.direction.y = -1

    def collision(self, direction):
        overlap_sprites = []
        if self.rect.colliderect(self.player.rect):
            overlap_sprites.append(self.player)

        if overlap_sprites:
            if direction == 'horizontal':
                for sprite in overlap_sprites:
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                        self.pos.x = self.rect.x
                        self.direction.x *= -1

                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                        self.pos.x = self.rect.x
                        self.direction.x *= -1

            if direction == 'vertical':
                for sprite in overlap_sprites:
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                        self.pos.y = self.rect.y
                        self.direction.y *= -1

                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                        self.pos.y = self.rect.y
                        self.direction.y *= -1

    def update(self, dt):
        if self.active:

            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()
            # create old rect
            self.old_rect = self.rect.copy()

            # horizontal movement + collision
            self.pos.x += self.direction.x * self.speed * dt
            self.rect.x = round(self.pos.x)
            self.collision('horizontal')
            self.window_collision('horizontal')
            # vertical movement + collision
            self.pos.y += self.direction.y * self.speed * dt
            self.rect.y = round(self.pos.y)
            self.collision('vertical')
            self.window_collision('vertical')
        else:
            self.rect.midbottom = self.player.rect.midtop
            self.pos = pygame.math.Vector2(self.rect.topleft)


class Block(pygame.sprite.Sprite):
    def __init__(self, type, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((block_width, block_height))
        self.rect = self.image.get_rect(topleft=pos)
