import pygame

pygame.init()
size = (900, 600)
from game import Engine

Engine(pygame.display.set_mode(size)).run()

pygame.quit()