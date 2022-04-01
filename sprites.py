from turtle import window_height
import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.image = pygame.Surface((screen_width // 10, screen_height // 20))
        self.image.fill('red')

        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height - 20
                                                ))
