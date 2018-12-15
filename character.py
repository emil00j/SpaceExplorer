import pygame

class Character():

    def __init__(self, pos):
        self.pos = pos
        self.texture = pygame.transform.scale(pygame.image.load("ressources/texture/character/{}.png".format(self.__class__.__name__.lower())).convert_alpha(), (50, 50))

    def blit(self, screen):
        screen.blit(self.texture, self.pos)

class Robot(Character):

    #def __init__(self, pos):
        # self.texture = pygame.transform.scale(pygame.image.load("ressources/texture/character/robot.png").convert_alpha(), (50, 50))
        # print(vars(self))

    def move(self, force):
        self.pos = (self.pos[0] + self.force[0], self.pos[1] + self.force[1])