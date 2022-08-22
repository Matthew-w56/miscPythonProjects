import pygame
from pygame.locals import *
import sys
pygame.init()

from ButtonClass import *

def write(text='[--Enter Text To Write!--]', color=(0, 0, 0), pos=(0, 0), bold=False, size=20, font='Arial'):
    Font = pygame.font.SysFont(font, size, bold)
    Finaltext = Font.render(text, 1, color)
    Screen.blit(Finaltext, pos)

def sett():
    setting = True
    while setting:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                setting = False

        write('(Press ESCAPE to go back to the main menu)', pos=(23, ScreenY-35), size=15)

        pygame.display.update()