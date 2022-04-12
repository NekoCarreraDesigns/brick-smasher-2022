from numpy import full
import pygame
from settings import *
from os import walk


class SurfaceMaker:

    def import_folder(path):
        surface_list = []
        for _, __, img_files in walk(path):
            for image in img_files:
                full_path = path + '/' + image
                image_surf = pygame.image.load(full_path).convert()
                surface_list.append(image_surf)
        return surface_list

    def get_surf(self, size):
        image = pygame.Surface(size)
        image.fill('blue')
        return image
