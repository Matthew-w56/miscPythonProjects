import pygame
from pygame.locals import *
pygame.init()

from TailAndHead import *


class Apple(object):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)

    def draw(self):
        pygame.draw.rect(Screen, red, self.rect)