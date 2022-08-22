import pygame
from pygame.locals import *
import sys
from random import randint
from threading import Thread
pygame.init()

red = (200, 0, 0)
green = (0, 200, 0)
dark_green = (0, 100, 0)
blue = (0, 0, 200)
purple = (200, 0, 200)
white = (255, 255, 255)
light_gray = (200, 200, 200)
gray = (150, 150, 150)
dark_gray = (65, 65, 65)
black = (0, 0, 0)
bgc = dark_gray

num_colors = [light_gray, blue, dark_green, red, purple, dark_gray, black, black, black]

clock = pygame.time.Clock()
fps = 30


class Organizer(object):
    def __init__(self):
        self.flags_left = 10
        self.tiles_left = 100
        self.Tiles = []
        self.locked = False
        self.time = 0
        self.going = True

    def update_tiles(self):
        total = 100
        for x in o.Tiles:
            if x.checked:
                total -= 1
        return total - (mine_count - o.flags_left)
o = Organizer()

grid_x = 20
grid_y = 20
margin = 1
mine_count = 10
y_offset = 100

screen_x = (grid_x * 10) + (2 * margin)
screen_y = (grid_y * 10) + (2 * margin) + y_offset
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption('Minesweeper try #1')


def write(text='[--Enter Text To Write!--]', _color=(0, 0, 0), pos=(0, 0), bold=False, size=20, font='Arial'):
    font = pygame.font.SysFont(font, size, bold)
    final_text = font.render(text, 1, _color)
    screen.blit(final_text, pos)


class Tile(object):
    def __init__(self, pos):
        self.rect = pygame.Rect((pos[0] * grid_x) + margin, (pos[1] * grid_y) + margin + y_offset, grid_x - margin, grid_y - margin)
        self.checked = False
        self.mined = False
        self.mine_id = 0
        self.flagged = False
        o.Tiles.append(self)

    def check(self):
        if not self.checked:
            self.checked = True
            if self.flagged:
                self.flagged = False
                o.flags_left += 1
            if self.mine_id == 0:
                test_rect = pygame.Rect(self.rect.x - (margin + 1), self.rect.y - (margin + 1),
                                        grid_x + (2 * margin + 1), grid_y + 2 * (margin + 1))
                for i in o.Tiles:
                    if test_rect.colliderect(i.rect):
                        i.check()
            if self.mined:
                o.locked = True

    def draw(self):
        if self.checked:
            if self.mined:
                pygame.draw.rect(screen, red, self.rect, 1)
                pygame.draw.rect(screen, red, (self.rect.x + 2, self.rect.y + 2, self.rect.width - 4,
                                               self.rect.height - 4))
            else:
                pygame.draw.rect(screen, gray, self.rect)
            if self.mine_id == 0 or (self.mined and self.checked):
                pass
            else:
                write(str(self.mine_id), pos=(self.rect.x + (grid_x / 2.5),
                                              self.rect.y + (grid_y / 4)), size=(int(grid_x / 2)),
                      _color=(num_colors[self.mine_id]))
        elif self.flagged:
            pygame.draw.rect(screen, green, self.rect)
        else:
            pygame.draw.rect(screen, light_gray, self.rect)

    def flag(self):
        if not self.flagged and (not self.checked):
            o.flags_left -= 1
            self.flagged = True


class Board(object):  # This is a class for general functions
    def __init__(self):
        self.filler = False

    def spread_mines(self):
        left_x = []
        left_y = []
        for t in range(0, mine_count):
            left_x.append(t)
            left_y.append(t)
        for i in range(0, mine_count):
            _x = randint(0, len(left_x) - 1)
            r_x = left_x.pop(_x)
            _y = randint(0, len(left_y) - 1)
            r_y = left_y.pop(_y)
            for tile in o.Tiles:
                if tile.rect.x == (r_x * grid_x) + margin and tile.rect.y == (r_y * grid_y) + margin + y_offset:
                    tile.mined = True

    def create(self):
        for x in range(0, 10):
            for y in range(0, 10):
                Tile((x, y))

    def update_cues(self):
        for tile in o.Tiles:
            if tile.mined:
                test_rect = pygame.Rect(tile.rect.x - (margin + 1), tile.rect.y - (margin + 1),
                                        grid_x + (2 * margin + 1), grid_y + 2 * (margin + 1))
                for i in o.Tiles:
                    if test_rect.colliderect(i.rect):
                        i.mine_id += 1

board = Board()


class ResetButton(object):
    def __init__(self):
        self.pos = ((screen_x - 50) / 2, 25)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 50, 50)
        self.happy = False

    def draw(self):
        if not self.happy:
            pygame.draw.rect(screen, black, self.rect)
            pygame.draw.rect(screen, red, (self.rect.x + 4, self.rect.y + 4, self.rect.width - 8, self.rect.height - 8), 2)
            pygame.draw.circle(screen, gray, (int(screen_x / 2), 50), 10)
            pygame.draw.circle(screen, red, (int(screen_x / 2), 50), 3)
        elif self.happy:
            pygame.draw.rect(screen, black, self.rect)
            pygame.draw.rect(screen, green, (self.rect.x + 4, self.rect.y + 4, self.rect.width - 8, self.rect.height - 8), 2)
            pygame.draw.circle(screen, gray, (int(screen_x / 2), 50), 10)
            pygame.draw.circle(screen, green, (int(screen_x / 2), 50), 3)
button = ResetButton()


def reset():
    o.Tiles = []
    o.tiles_left = 100
    o.flags_left = mine_count
    o.locked = False
    button.happy = False
    o.time = 0


def timer():
    while o.going:
        if not ((o.locked or button.happy) or o.tiles_left == 100):
            o.time += 1
        clock.tick(1)
timer_thread = Thread(target=timer)
