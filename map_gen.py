from os import listdir as lsd
from random import randint
import texture_loader as tl
import pygame

class Map():

    # 1/1000
    chance = {"water": 333,
              "iron": 333 + 150,
              "gold": 333 + 150 + 100}

    def __init__(self, size):
        self.surface = pygame.surface.Surface(size)
        self.elements = {}

    def create(self, pos):
        r = randint(0, 1000)
        texture = -1
        for i in list(self.chance):
            if self.chance[i] >= r:
                texture = i
                break
        if texture == -1:
            texture = "floor"

        self.elements[pos] = texture

    def blit(self, screen): # A modifier pour mouvement personnage
        for i in range(9):
            for j in range(6):
                try:
                    self.surface.blit(tl.texture["evr"][self.elements[(i, j)]], (100 * i, 100 * j))
                except KeyError:
                    self.create((i, j))
                    self.surface.blit(tl.texture["evr"][self.elements[(i, j)]], (100 * i, 100 * j))

        screen.blit(self.surface, (0, 0))

    def save(self):
        pass

    def load(self):
        pass
