import pygame
import sys
pygame.init()
Screen = pygame.display.set_mode((600, 400))  # 30x20 grid blocks
pygame.display.set_caption("Enjoy my Snake game!")


class Organizer(object):
    def __init__(self):
        self.Tails = []
o = Organizer()


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text + '\n'
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


def get_line(file, line):
    data = open(file, 'r').readlines()
    return data[line]

high_score = get_line('Highscore.txt', 1)
h_high_score = get_line('Highscore.txt', 7)


class Head(object):
    def __init__(self, color=(0, 0, 0), size=20, x=10, y=10):
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, size, size)
        self.lastdire = ''

    def draw(self):
        pygame.draw.rect(Screen, self.color, self.rect)

    def move(self):
        pass


def write(text='[--Enter Text To Write!--]', color=(0, 0, 0), pos=(0, 0), bold=False, size=20):
    Font = pygame.font.SysFont('Arial', size, bold)
    Finaltext = Font.render(text, 1, color)
    Screen.blit(Finaltext, pos)


class Tail(object):
    def __init__(self, x, y, color=(150, 150, 150), size=20):
        self.color = color
        o.Tails.append(self)
        self.rect = pygame.Rect(x, y, size, size)

    def draw(self):
        pygame.draw.rect(Screen, self.color, self.rect)
        pygame.draw.rect(Screen, black, self.rect, 1)


class Snake(object):
    def __init__(self, head):
        self.head = head
        self.length = 1

    def draw(self):
        for tail in o.Tails:
            tail.draw()
        self.head.draw()

    def move(self, dire, ex='no'):
        fx = self.head.rect.x
        fy = self.head.rect.y

        for tail in o.Tails:
            if self.head.rect.colliderect(tail.rect):
                if ex != 'inf':
                    print('Good try!  You got to the length of: ' + str(self.length))
                    replace_line('Highscore.txt', 3, str(self.length))
                    if self.length > int(high_score):
                        replace_line('Highscore.txt', 1, str(self.length))
                        print('---[That\'s a new record!]---')
                        print('New Record: ' + str(self.length))
                    self.length = 0
                    return False

        if dire == 'r':
            self.head.rect.x += 20
        if dire == 'l':
            self.head.rect.x -= 20
        if dire == 'u':
            self.head.rect.y -= 20
        if dire == 'd':
            self.head.rect.y += 20
        self.head.lastdire = dire
        Tail(fx, fy)
        if ex != 'inf':
            if len(o.Tails) > self.length + 1:
                o.Tails.remove(o.Tails[0])
        return True


red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)