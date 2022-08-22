import sys
import pygame
from pygame.locals import *
from random import randint

pygame.init()

ScreenX = 600
ScreenY = 400
Screen = pygame.display.set_mode((ScreenX, ScreenY))

Buttons = []

red = (255, 0, 0)
orange = (255, 150, 0)
yellow = (255, 255, 20)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

Font = pygame.font.SysFont('Arial', 30, True)


class Button(object):
    def __init__(self, screen, pos, img, text=''):
        self.rect = pygame.Rect(pos[0], pos[1], 200, 40)
        self.screen = screen
        self.img = img
        self.text = text
        Buttons.append(self)

    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.img, (self.rect.x, self.rect.y))

        '''text = Font.render(self.text, 1, black)
        self.screen.blit(text, (self.rect.x + 5, self.rect.y + 5, self.rect[2], self.rect[3]))'''


def blit_alpha(screen, color, rect, alpha):
    temp_screen = pygame.Surface((rect[2], rect[3]))
    temp_screen.set_alpha(alpha)           # Alpha is 0(transparent) to 255(opaque)
    temp_screen.fill(color)
    screen.blit(temp_screen, (rect[0], rect[1]))