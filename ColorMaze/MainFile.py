from Classes import *
__author__ = 'Matthew Williams'
# Started on 4/26/16


parse_map(tutorial_level)

while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                coll = True
                for x in o.blocks:
                    if player.rect.colliderect(x.rect):
                        coll = False
                if coll:
                    player.switch('l')
            if event.button == 3:
                coll = True
                for x in o.blocks:
                    if player.rect.colliderect(x.rect):
                        coll = False
                if coll:
                    player.switch('r')
    keys = pygame.key.get_pressed()
    mods = pygame.key.get_mods()
    left, middle, right = pygame.mouse.get_pressed()
    if keys[K_a]:
        player.move_x(-player.speed)
    if keys[K_d]:
        player.move_x(player.speed)
    if keys[K_w]:
        player.move_y(-player.speed)
    if keys[K_s]:
        player.move_y(player.speed)
    if mods & KMOD_LSHIFT:
        player.speed = player.normal_speed * 1.5
    else:
        player.speed = player.normal_speed

    for b in borders:
        pygame.draw.rect(screen, (214, 224, 20), b)
    for i in o.blocks:
        i.draw()
    for i in o.whites:
        i.draw()
    pygame.draw.rect(screen, black, (o.end_point.x, o.end_point.y, o.end_point.width, o.end_point.height))
    player.draw()

    if player.color == blue:
        write('Red', pos=(90, 0), size=18)
        write('Blue', pos=(135, -2), size=20, font='impact')
        write('Green', pos=(180, 0), size=18)
    elif player.color == green:
        write('Red', pos=(90, 0), size=18)
        write('Blue', pos=(135, 0), size=18)
        write('Green', pos=(180, -2), size=20, font='impact')
    elif player.color == red:
        write('Red', pos=(90, -2), size=20, font='impact')
        write('Blue', pos=(135, 0), size=18)
        write('Green', pos=(180, 0), size=18)

    if player.level == 0:
        write('Welcome!  use WASD to move', pos=(250, 10), bold=True)
        write('Your goal is to get to the', pos=(250, 40), bold=True)
        write('little black box in the', pos=(250, 70), bold=True)
        write('opposite corner', pos=(250, 100), bold=True)
        write('Use left and right click to switch colors', pos=(230, 140), bold=True)
        write('Also, you can only go onto a square', pos=(250, 180), bold=True)
        write('that is the same color as you', pos=(250, 210), bold=True)

    pygame.display.update()
    pygame.time.wait(10)
