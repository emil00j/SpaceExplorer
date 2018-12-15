import pygame
from pygame.locals import *

class Engine():

    FPS = [pygame.time.Clock(), 60]

    def __init__(self, screen):
        import map_gen as mp
        import character as char
        
        self.screen = screen
        self.size = screen.get_size()
        self.player = char.Robot((int(self.size[0] / 2), int(self.size[1] / 2)))
        self.map = mp.Map(self.size)

    def run(self):
        self.stop = False

        while not(self.stop):
            self.FPS[0].tick(self.FPS[1])
            self.map.blit(self.screen)
            self.player.blit(self.screen)

            a = pygame.event.get()
            for i in a:
                if i.type == QUIT:
                    self.stop = True

            pygame.display.update()
