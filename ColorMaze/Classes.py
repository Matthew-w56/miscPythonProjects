__author__ = 'Matthew Williams'
# Started on 4/26/16

import pygame
from pygame.locals import *
import sys
from random import randint
pygame.init()
from Other import *


def write(text='[--Enter Text To Write!--]', color=(0, 0, 0), pos=(0, 0), bold=False, size=20, font='Arial'):
    font = pygame.font.SysFont(font, size, bold)
    final_text = font.render(text, 1, color)
    screen.blit(final_text, pos)


red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (200, 200, 100)
border = 10

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Color Maze: 0.1')
borders = [
    pygame.Rect(0, 0, 600, 20), pygame.Rect(0, 0, 20, 600),
    pygame.Rect(0, 600 - 20, 600, 20), pygame.Rect(600 - 20, 0, 20, 600)
]


class Organizer(object):
    def __init__(self):
        self.blocks = []
        self.whites = []
        self.end_point = pygame.Rect(-10, -10, 10, 10)
o = Organizer()


def parse_map(maap):
    o.blocks = []
    o.whites = []
    x, y = (border, border)
    size = (600 - (border * 4)) / len(maap[0])
    for row in maap:
        for col in row:
            if col != ' ':
                if col == 'R':
                    Block(x + border, y + border, size, red)
                elif col == 'G':
                    Block(x + border, y + border, size, green)
                elif col == 'B':
                    Block(x + border, y + border, size, blue)
                elif col == 'W':
                    WhiteBlock(x + border, y + border, size)
                elif col == 'E':
                    WhiteBlock(x + border, y + border, size)
                    o.end_point = pygame.Rect(x + border + (size / 4), y + border + (size / 4), size / 2, size / 2)
                x += size
        x = border
        y += size
    player.rect = pygame.Rect(player.rect.x, player.rect.y, size / 2, size / 2)
    player.normal_speed = size / 20


def die(message="You died!  Good luck next time!"):
    while True:
        screen.fill(white)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        write(message, pos=(200, 200), bold=True, size=40)

        pygame.display.update()


class Block(object):
    def __init__(self, x, y, size, color):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        o.blocks.append(self)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, black, self.rect, 1)


class WhiteBlock(object):
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = white
        o.whites.append(self)

    def draw(self):
        pygame.draw.rect(screen, white, self.rect)
        pygame.draw.rect(screen, black, self.rect, 1)


class Player(object):
    def __init__(self, size):
        self.color = blue
        self.colorind = 0
        self.colors = [blue, red, green]
        self.rect = pygame.Rect(480, 480, size, size)
        self.can_switch = False
        self.speed = 3
        self.level = 0
        self.normal_speed = 0

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, black, self.rect, 2)

    def switch(self, d):
        if d == 'l':
            self.colorind += 1
        elif d == 'r':
            self.colorind -= 1

        if self.colorind > 2:
            self.colorind = 0
        elif self.colorind < 0:
            self.colorind = 2
        self.color = self.colors[self.colorind]

    def move_x(self, dx):
        self.rect.x += dx

        for block in o.blocks:
            if (block.color in self.colors) and (block.color != self.color):
                if self.rect.colliderect(block.rect):
                    if dx > 0:
                        self.rect.right = block.rect.left
                    elif dx < 0:
                        self.rect.left = block.rect.right

        for bordeer in borders:
            if self.rect.colliderect(bordeer):
                if dx > 0:
                    self.rect.right = bordeer.left
                elif dx < 0:
                    self.rect.left = bordeer.right

    def move_y(self, dy):
        self.rect.y += dy

        for block in o.blocks:
            if (block.color in self.colors) and (block.color != self.color):
                if self.rect.colliderect(block):
                    if dy > 0:
                        self.rect.bottom = block.rect.top
                    elif dy < 0:
                        self.rect.top = block.rect.bottom
        for bordeer in borders:
            if self.rect.colliderect(bordeer):
                if dy > 0:
                    self.rect.bottom = bordeer.top
                elif dy < 0:
                    self.rect.top = bordeer.bottom
        if player.rect.colliderect(o.end_point):
            self.next_lvl()

    def next_lvl(self):
        self.level += 1
        if self.level < len(maps):
            parse_map(maps[self.level])
        else:
            pygame.quit()
            print('Good job!')
            print('More levels coming soon, Maybe!')
            sys.exit()


player = Player(35)
