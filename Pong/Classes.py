import pygame, sys
from pygame.locals import *
from random import randint
from threading import Thread
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pong game!  |  Enjoy!')
icon_image = pygame.image.load('icon.ico')
pygame.display.set_icon(icon_image)

white = (255, 255, 255)
gray1 = (200, 200, 200)
gray2 = (150, 150, 150)
gray3 = (100, 100, 100)
gray4 = (50, 50, 50)
black = (0, 0, 0)

ball_max_speed = 7
clock = pygame.time.Clock()
not_started = True
player_score_box = pygame.Rect(-5, 0, 10, 400)
computer_score_box = pygame.Rect(590, -10, 15, 400)
win_amount = 5


class Organizer(object):
    def __init__(self):
        self.cs = 0
        self.ps = 0
o = Organizer()


class Wall(object):
    def __init__(self, tb):
        if tb == 't':
            self.rect = pygame.Rect(-5, -5, 610, 25)
        else:
            self.rect = pygame.Rect(-5, 380, 610, 25)
        self.type = tb

    def draw(self):
        pygame.draw.rect(screen, white, self.rect)
top_wall = Wall('t')
bottom_wall = Wall('b')


class Ball(object):
    def __init__(self):
        self.rect = pygame.Rect(290, 190, 21, 21)
        self.x_vel = 0
        self.y_vel = 0

    def draw(self):
        pygame.draw.circle(screen, white, (self.rect.x + 10, self.rect.y + 10), 10)

    def reset(self, p):
        self.rect = pygame.Rect(290, 190, 21, 21)
        if p == 'p':
            self.x_vel = -5
        elif p == 'c':
            self.x_vel = 5
        self.y_vel = randint(1, 2)
        if self.y_vel == 1:
            self.y_vel = 4
        else:
            self.y_vel = -4
        if o.cs > win_amount - 1:
            print('You lose!')
            pygame.quit()
            sys.exit()
        elif o.ps > win_amount - 1:
            print('You win!')
            pygame.quit()
            sys.exit()
        else:
            pygame.time.wait(30)

    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        if self.rect.colliderect(top_wall.rect):
            self.rect.top = top_wall.rect.bottom
            self.y_vel = -self.y_vel
        if self.rect.colliderect(bottom_wall):
            self.rect.bottom = bottom_wall.rect.top
            self.y_vel = -self.y_vel
        if self.rect.colliderect(player.rect):
            self.x_vel = -self.x_vel
        if self.rect.colliderect(computer.rect):
            self.x_vel = -self.x_vel
            self.rect.x -= 2
        if self.rect.colliderect(player_score_box):
            o.cs += 1
            self.reset('c')
        if self.rect.colliderect(computer_score_box):
            o.ps += 1
            self.reset('p')
        if self.x_vel > ball_max_speed:
            self.x_vel = ball_max_speed
        if self.y_vel > ball_max_speed:
            self.y_vel = ball_max_speed
        if self.x_vel < -ball_max_speed:
            self.x_vel = -ball_max_speed
        if self.y_vel < -ball_max_speed:
            self.y_vel = -ball_max_speed

    def check(self):
        if self.rect.colliderect(top_wall.rect):
            self.rect.top = top_wall.rect.bottom
            self.y_vel = -self.y_vel
        if self.rect.colliderect(bottom_wall):
            self.rect.bottom = bottom_wall.rect.top
            self.y_vel = -self.y_vel
        if self.rect.colliderect(player.rect):
            if 0 < self.x_vel < 2:
                self.x_vel = 2
            self.x_vel = -self.x_vel
            if 0 < self.x_vel < 2:
                self.x_vel = 2
        if self.rect.colliderect(computer.rect):
            self.x_vel = -self.x_vel
        if self.rect.colliderect(player_score_box):
            o.cs += 1
            self.reset('c')
        if self.rect.colliderect(computer_score_box):
            o.ps += 1
            self.reset('p')
        if self.x_vel > ball_max_speed:
            self.x_vel = ball_max_speed
        if self.y_vel > ball_max_speed:
            self.y_vel = ball_max_speed
        if self.x_vel < -ball_max_speed:
            self.x_vel = -ball_max_speed
        if self.y_vel < -ball_max_speed:
            self.y_vel = -ball_max_speed
ball = Ball()


class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(10, 163, 15, 75)
        self.speed = 5

    def draw(self):
        pygame.draw.rect(screen, white, self.rect)

    def move(self, a):
        self.rect.y += a
        if self.rect.colliderect(top_wall.rect):
            self.rect.top = top_wall.rect.bottom
        elif self.rect.colliderect(bottom_wall.rect):
            self.rect.bottom = bottom_wall.rect.top
        if self.rect.colliderect(ball.rect):
            ball.y_vel += (a / 10)
            ball.x_vel = -ball.x_vel
player = Player()


class Computer(object):
    def __init__(self):
        self.rect = pygame.Rect(575, 163, 15, 75)
        self.speed = 3
        self.center = self.rect.y + 36

    def draw(self):
        pygame.draw.rect(screen, white, self.rect)

    def move(self):
        self.center = self.rect.y + 36
        if self.center - 15 > ball.rect.y:
            self.rect.y -= self.speed
        elif self.center + 15 < ball.rect.y:
            self.rect.y += self.speed

        if self.rect.colliderect(ball.rect):
            ball.x_vel = -ball.x_vel
            ball.rect.x -= 5

        if self.rect.colliderect(top_wall.rect):
            self.rect.top = top_wall.rect.bottom
        elif self.rect.colliderect(bottom_wall):
            self.rect.bottom = bottom_wall.rect.top
computer = Computer()


def write(text='[--Enter Text To Write!--]', colors=(0, 0, 0), pos=(0, 0), bold=False, size=20):
    font = pygame.font.SysFont('Arial', size, bold)
    final_text = font.render(text, 1, colors)
    screen.blit(final_text, pos)