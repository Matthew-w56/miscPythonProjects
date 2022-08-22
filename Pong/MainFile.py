__author__ = 'Matthew Williams'
#Started on 9/5/16

from Classes import *
from SoundManager import sound

#thread1 = Thread(target=sound)
#thread1.start()


while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and not_started:
            not_started = False
            ball.x_vel = randint(1, 2)
            if ball.x_vel == 1:
                ball.x_vel = 5
            else:
                ball.x_vel = -5
            ball.y_vel = randint(-4, 4)
            if ball.y_vel == 0:
                ball.y_vel = 1

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        player.move(-player.speed)
        ball.check()
    if keys[K_DOWN]:
        player.move(player.speed)
        ball.check()

    ball.update()
    player.draw()
    top_wall.draw()
    bottom_wall.draw()
    ball.draw()
    computer.draw()
    computer.move()
    #pygame.draw.rect(screen, (200, 0, 0), player_score_box, 1)
    #pygame.draw.rect(screen, (0, 0, 200), computer_score_box, 1)

    write(str(o.ps), pos=(1, 0), size=20)
    if o.cs <= 9:
        write(str(o.cs), pos=(588, 0), size=20)
    else:
        write(str(o.cs), pos=(579, 0), size=20)
    if not_started:
        write("Press any key to start", pos=(150, 250), size=30, colors=white)

    pygame.display.update()
    clock.tick(30)