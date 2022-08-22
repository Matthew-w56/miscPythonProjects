from Classes import *

board.create()
board.spread_mines()
board.update_cues()
timer_thread.start()

while o.going:
    if len(o.Tiles) == 0:
        board.create()
        board.spread_mines()
        board.update_cues()
    mouse_buttons = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
    screen.fill(bgc)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            o.going = False

        elif event.type == MOUSEBUTTONDOWN:
            if mouse_rect.colliderect(button.rect):
                reset()
    if not (o.locked or button.happy):
        if mouse_buttons[0]:
            for tile in o.Tiles:
                if mouse_rect.colliderect(tile.rect):
                    tile.check()
        elif mouse_buttons[2]:
            for tile in o.Tiles:
                if mouse_rect.colliderect(tile.rect):
                    tile.flag()

    for tile in o.Tiles:
        tile.draw()
    o.tiles_left = o.update_tiles()
    if o.tiles_left == 0 and (o.flags_left == 0):
        button.happy = True
    button.draw()

    pygame.draw.rect(screen, light_gray, (20, 25, 40, 40))
    pygame.draw.rect(screen, gray, (20, 25, 40, 1))
    write(str(o.flags_left), pos=(22, 30), _color=red, size=30)
    write('Flags Left', pos=(13, 11), size=12)
    pygame.draw.rect(screen, light_gray, (145, 25, 45, 40))
    write(str(o.time), pos=(152, 30), _color=red, size=30)
    write('Time', pos=(152, 12), size=12)

    pygame.display.update()
    clock.tick(fps)