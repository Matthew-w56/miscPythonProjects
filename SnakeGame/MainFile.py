__author__ = 'Matthew Williams'
from pygame.locals import *
from random import randint
from TailAndHead import *
from apple import *
from Border import *
import pygame
from pygame.locals import *
pygame.init()


def game(mode):
    if mode == 'n':
        speed = 13
    else:
        speed = 20
    dire = ''
    head = Head()
    snake = Snake(head)
    snake.length = 1
    o.Tails = []

    rand1 = (randint(1, 18) * 20) + 10
    rand2 = (randint(1, 28) * 20) + 10
    apple = Apple(rand1, rand2)
    if (apple.rect.x > 580) or (apple.rect.y > 380):
        apple.rect.x = (randint(1, 28) * 20) + 10
        apple.rect.y = (randint(1, 18) * 20) + 10
    Border(Screen, 0, 0, 600, 10)
    Border(Screen, 0, 390, 600, 10)
    Border(Screen, 0, 0, 10, 400)
    Border(Screen, 590, 0, 10, 400)

    clock = pygame.time.Clock()

    print('')
    print('Current High Score:')
    print(high_score)
    print('')
    print('Current Hard Mode High Score:')
    print(h_high_score)

    gaming = True

    while gaming:
        Screen.fill(blue)
        if dire == '':
            write('Press any arrow', (0, 0, 0), (200, 100), True)
            write('key to start', (0, 0, 0), (200, 130), True)
            snake.length = 1
            o.Tails = []
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if (event.key == K_RIGHT) and (snake.head.lastdire != 'l'):
                    dire = 'r'
                if (event.key == K_LEFT) and (snake.head.lastdire != 'r'):
                    dire = 'l'
                if (event.key == K_UP) and (snake.head.lastdire != 'd'):
                    dire = 'u'
                if (event.key == K_DOWN) and (snake.head.lastdire != 'u'):
                    dire = 'd'
                if event.key == K_w:
                    speed -= 10
                if event.key == K_s:
                    speed += 10

        apple.draw()

        if dire != '':
            gaming = snake.move(dire)
        if snake.head.rect.colliderect(apple.rect):
            snake.length += 4
            apple.rect.x = (randint(1, 28) * 20) + 10
            apple.rect.y = (randint(1, 18) * 20) + 10
            for tail in o.Tails:
                if apple.rect.colliderect(tail.rect):
                    apple.rect.x = (randint(1, 28) * 20) + 10
                    apple.rect.y = (randint(1, 18) * 20) + 10
            if (apple.rect.x >= 600) or (apple.rect.y >= 400):
                apple.rect.x = (randint(1, 28) * 20) + 10
                apple.rect.y = (randint(1, 18) * 20) + 10

        snake.draw()
        for bord in borders:
            bord.draw()
            if snake.head.rect.colliderect(bord.rect):
                print('Good job!  You got to a length of ' + str(snake.length))
                if mode == 'n':
                    replace_line('Highscore.txt', 3, str(snake.length))
                    if snake.length > int(high_score):
                        replace_line('Highscore.txt', 1, str(snake.length))
                        print('---[That\'s a new record!]---')
                        print('New Record: ' + str(snake.length))
                elif mode == 'h':
                    replace_line('Highscore.txt', 9, str(snake.length))
                    if snake.length > int(h_high_score):
                        replace_line('Highscore.txt', 7, str(snake.length))
                        print('---[That\'s a new record!]---')
                        print('New Hard Mode Record: ' + str(snake.length))
                gaming = False
                return snake.length
        for tai in o.Tails:
            if snake.head.rect.colliderect(tai.rect):
                return snake.length
        write('Highscore', (0, 0, 0), (500, 20))
        if mode == 'n':
            write(str(high_score), (0, 0, 0), (550, 40))
        elif mode == 'h':
            write(str(h_high_score), (0, 0, 0), (550, 40))
        write('Current', (0, 0, 0), (500, 80))
        write(str(snake.length), (0, 0, 0), (550, 100))
        pygame.display.update()
        clock.tick(speed)