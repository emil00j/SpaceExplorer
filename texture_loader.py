import pygame
from os import listdir as lsd

texture = {}
for typ in lsd("ressources/texture"):
    texture[typ] = {}

    for img in lsd("ressources/texture/{}".format(typ)):
        texture[typ][img.split(".png")[0]] = pygame.image.load("ressources/texture/{}/{}".format(typ, img)).convert_alpha()