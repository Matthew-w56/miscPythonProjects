import pygame

borders = []


class Border(object):
    def __init__(self, screen, x, y, w, h, color=(40, 40, 40)):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.screen = screen
        borders.append(self)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)