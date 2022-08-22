'''
Enjoy my simple Snake    | Lines:        ~545
Game!  Run this file     | Characters:   ~17,500
to start.
'''
__author__ = 'Matthew Williams'

from MainFile import *
from settings import *
from DeathScreen import *
from InfGame import *


class Mouse(object):
    def __init__(self, color=blue, size=10):
        self.rect = pygame.Rect(0, 0, size, size)
        self.color = color

    def draw(self):
        pygame.draw.rect(Screen, self.color, self.rect)
mouse = Mouse()

img1 = pygame.image.load('buttons/title.png')
img2 = pygame.image.load('buttons/normal.png')
img3 = pygame.image.load('buttons/hard.png')
img4 = pygame.image.load('buttons/settings.png')
img5 = pygame.image.load('buttons/exit.png')

Button(Screen, (175, 40), img1, 'Snake Game')
Button(Screen, (200, 120), img2, 'Game Normal')
Button(Screen, (200, 180), img3, 'Game Hard')
Button(Screen, (200, 240), img4, 'Settings')
Button(Screen, (240, 300), img5, 'Exit')

mouse_down = False

while True:
    Screen.fill((201, 208, 107))
    mouse_pos = pygame.mouse.get_pos()
    mouse.rect.x = mouse_pos[0]
    mouse.rect.y = mouse_pos[1]
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            mouse_down = True
            for button in Buttons:
                if mouse.rect.colliderect(button.rect):
                    if button.text == 'Snake Game':
                        info = infinity_game('n')
                        die(info)
                    if button.text == 'Game Normal':
                        info = game('n')
                        die(info)
                    elif button.text == 'Game Hard':
                        info = game('h')
                        die(info)
                    elif button.text == 'Settings':
                        sett()
                    elif button.text == 'Exit':
                        pygame.quit()
                        sys.exit()
        if event.type == MOUSEBUTTONUP:
            mouse_down = False

    # mouse.draw()
    for button in Buttons:
        button.draw()

    pygame.display.update()