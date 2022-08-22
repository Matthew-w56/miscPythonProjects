__author__ = 'Matthew Williams'

from ButtonClass import *
from TailAndHead import *
pygame.init()
clock = pygame.time.Clock()
fps = 30
# def write(text='[--Enter Text To Write!--]', color=(0, 0, 0), pos=(0, 0), bold=False, size=20):


def die(info):
    length = info
    dying = True
    pygame.time.wait(800)
    while dying:
        Screen.fill((201, 208, 107))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    dying = False

        pygame.draw.rect(Screen, red, (20, 15, 560, 370))
        write('Good Job!', pos=(220, 50), bold=True, size=35)
        pygame.draw.rect(Screen, black, (210, 85, 190, 5))
        write('You died, but that is to be expected', pos=(130, 110), bold=True, size=20)
        write('in the game of Snake', pos=(205, 135), bold=True, size=20)
        write('You ended up getting to a length of', pos=(135, 190), bold=True, size=20)
        write(str(length), pos=((ScreenX / 2) - (len(str(length)) * 5), 220), bold=True, size=20)
        write('(Press ESCAPE to go back to the main menu)', pos=(23, ScreenY-35), size=15, bold=True)

        pygame.display.update()
        clock.tick(fps)