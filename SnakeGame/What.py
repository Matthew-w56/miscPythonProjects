import pygame
from pygame.locals import*
import time
import random
import math
import sys

pygame.init()

class Line(object):
    def __init__(self, start, end):
        self.start = list(start)
        self.end = list(end)

        x = (start[0]-end[0])
        y = (start[1]-end[1])
        distance = math.sqrt(x**2+y**2)
        x /= distance
        y /= distance
        self.center = [(x*distance*0.25)+end[0], (y*distance*0.25)+end[1]]

    def render(self, screen):

        pygame.draw.line(screen, [255, 100, 100], self.start, self.center, 3)
        pygame.draw.line(screen, [100, 100, 255], self.center, self.end, 3)
        return pygame.draw.line(screen, [0, 0, 0], self.start, self.end, 0)

    def delete_render(self,screen,bg_color):
        pygame.draw.line(screen, bg_color, self.start, self.end, 3)


class Walker(object):
    def __init__(self, pos):
        self.pos = list(pos)
        self.prev_pos = list(pos)
        self.destination = None
        self.vector=[0.0,0.0]
        self.steps = 0
        self.speed = 3

        self.prev_dir = 0

    def update(self, lines, direction):


        if self.destination==None or self.prev_dir!=direction: #If just started
            self.destination = None
            distance = None
            for line in lines:
                points=[line.start,line.end]
                for point in points:
                    if distance==None:
                        x=(point[0]-self.pos[0])
                        y=(point[1]-self.pos[1])
                        distance = math.sqrt(x**2+y**2)
                        self.destination = list(point)
                        if x!=0:
                            x/=distance
                        if y!=0:
                            y/=distance
                        self.vector=[x,y]
                    else:
                        x=(point[0]-self.pos[0])
                        y=(point[1]-self.pos[1])
                        d=math.sqrt(x**2+y**2)
                        if d<=distance:
                            distance=float(d)
                            self.destination = list(point)
                            if x!=0:
                                x/=d
                            if y!=0:
                                y/=d
                            self.vector = [x,y]
            if self.destination!=None:
                if distance==0:
                    self.steps = 0
                else:
                    self.steps=int(distance/float(self.speed))
                    self.prev_pos = list(self.pos)


        else:
            if self.steps==0:

                self.pos = list(self.destination)
                self.destination = None
                paths = []


                vector = list(self.vector)
                for line in lines:
                    if direction==0:
                        start = line.start
                        end = line.end
                    elif direction==1:
                        start = line.end
                        end = line.start


                    if start==self.pos:
                        point = end
                        x=(point[0]-self.pos[0])
                        y=(point[1]-self.pos[1])
                        d=math.sqrt(x**2+y**2)

                        if x!=0:
                            x/=d
                        if y!=0:
                            y/=d
                        vector = [x,y]

                        paths.append( [list(point),list(vector),float(d)] )


                """
                for line in lines:
                    points=[line.start,line.end]
                    for point in points:
                        if self.pos in points:
                            x=(point[0]-self.pos[0])
                            y=(point[1]-self.pos[1])
                            d=math.sqrt(x**2+y**2)
                            if point!=self.prev_pos and point!=self.pos:

                                if x!=0:
                                    x/=d
                                if y!=0:
                                    y/=d
                                vector = [x,y]

                                paths.append( [list(point),list(vector),float(d)] )
                """


                if len(paths)!=0:
                    n = random.randint(0,len(paths)-1)
                    self.destination = paths[n][0]
                    self.vector = paths[n][1]

                    if paths[n][2]==0:
                        self.steps = 0
                    else:
                        self.steps=int(paths[n][2]/float(self.speed))
                        self.prev_pos = list(self.pos)


            else:
                self.steps-=1
                self.pos[0]+=self.vector[0]*self.speed
                self.pos[1]+=self.vector[1]*self.speed


        self.prev_dir = direction

    def render(self, screen):
        return pygame.draw.rect(screen,[0,127,0],[self.pos[0],self.pos[1],3,3])


class TextImage(object):
    def __init__(self, text, message, color, pos, bg_color=None):
        self.text = text
        self.message = message
        self.color = color
        self.bg_color = bg_color
        self.pos = pos

        self.get_new_image()

    def change_message(self, new_message):
        self.message = new_message
        self.get_new_image()
    def change_pos(self, new_pos):
        self.pos = new_pos
        self.get_new_image()
    def change_color(self, new_color):
        self.color = new_color
        self.get_new_image()

    def get_new_image(self):
        if self.bg_color!=None:
            self.image = self.text.render(self.message, True, self.color, self.bg_color)
        else:
            self.image = self.text.render(self.message, True, self.color)
        self.rect = self.image.get_rect(topleft = self.pos)

    def render(self, screen):
        screen.blit(self.image, self.rect)
        return self.rect


class DelaySwitch(object):
    """This is something I made (Dylan J. Raub) so that your game can run at
    an almost constant speed. It works really well and has
    been made to mimic the speed of a Macromedia Flash
    Video. In other words, this runs using frame rate.

    Note: Every time the proccecing time passes the limit that you have set,
    'drop_frame' will equal True, so you can tell your program not to render or update
    the screen on the next frame. in other words, it will still try to keep it
    running at a constant speed."""

    def __init__(self, frame_rate):
        self.frame_rate = 1.0/(frame_rate/100.0) # should be in milliseconds
        self.time = 0
        self.prev_time = 0
        self.time_passed = 0
        self.drop_frame = False

    def update(self):
        if self.drop_frame==True:
            self.drop_frame=False

        self.time=time.time()
        self.time_passed = self.time-self.prev_time

        if self.time_passed<self.frame_rate:
            time.sleep((self.frame_rate-self.time_passed)/100.0)
        else:
            self.drop_frame=True

        self.prev_time = self.time






def get_snapped_mouse(grid_size):
    mouse_pos = list(pygame.mouse.get_pos())

    mouse_pos[0]+=grid_size/2
    mouse_pos[0]/=grid_size
    mouse_pos[0]*=grid_size
    mouse_pos[1]+=grid_size/2
    mouse_pos[1]/=grid_size
    mouse_pos[1]*=grid_size


    return mouse_pos

def get_input(events):
    for event in events:
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()



def main():

    size = (800,600)
    screen = pygame.display.set_mode(size,FULLSCREEN)

    bg_color = [255,255,255]
    text_color = [100,100,100]
    screen.fill(bg_color)


    delay = DelaySwitch(60)


    lines = []
    walkers = []
    walker_number=2000
    for x in range(1, walker_number):
        walkers.append(Walker([0,size[1]]))

    text = pygame.font.SysFont(pygame.font.get_default_font(), 14)
    textimages = [TextImage(text,"Press '1' to have the walkers follow the lines. Press '2' to have them follow the lines backwards. Press the number you just pressed again to pause.",text_color,[0,0]),
                  TextImage(text,"Press and let go of the left button on the mouse to draw a line. (Note: make sure the ends and beginnings of each lines touch another! Walkers can get stuck!)",text_color,[0,text.get_height()]),
                  TextImage(text,"Press the BackSpace key to remove a line. (Note: they are removed in the reverse order)",text_color,[0,text.get_height()*2]),
                  TextImage(text,"Press 'R' to reset the walkers.",text_color,[0,text.get_height()*3]),
                  TextImage(text,"Press Escape to exit out of the program.",text_color,[0,text.get_height()*5]),
                  TextImage(text,"Made by Dylan J. Raub in 2008.",text_color,[0,size[1]-text.get_height()]),
                  TextImage(text,"INFO",text_color,[200,size[1]-text.get_height()])]

    pressed = False
    play = None
    grid_size = 20



    while True:
        rects = []


        events = pygame.event.get()
        mouse_pos = get_snapped_mouse(grid_size)
        mouse_but = pygame.mouse.get_pressed()[0]




        bad_line = False

        if mouse_but and not pressed:
            start = list(mouse_pos)
        elif not mouse_but and pressed:
            end = list(mouse_pos)
            if  start!=end:
                new_line1 = Line(start,end)
                new_line2 = Line(end,start)
                if lines.count(new_line1)==0 and lines.count(new_line2)==0:
                    lines.append(new_line1)

        if mouse_but:
            end = list(mouse_pos)
            if end!=start:
                new_line1 = Line(start,end)
                new_line2 = Line(end,start)
                if lines.count(new_line1)>0 or lines.count(new_line2)>0 or start==end:
                    bad_line=True

        pressed = mouse_but

        for event in events:
            if event.type==KEYDOWN:

                if event.key == K_BACKSPACE:
                    if len(lines)>0:
                        lines[-1].delete_render(screen,bg_color)
                        lines.pop()

                if event.key == K_1 or event.key == K_2:
                    if event.key == K_1:
                        n=0
                    else:
                        n=1

                    if n==play:
                        play = None
                    else:
                        play = int(n)

                if event.key == K_r:
                    walkers=[]
                    for x in range(1, walker_number):
                        walkers.append(Walker([0,size[1]]))







        for x in range(1, int(size[1]/grid_size)):
            rects.append(pygame.draw.line(screen, [200,200,200], [0,x*grid_size], [size[0],x*grid_size]))
        for y in range(1, int(size[0]/grid_size)):
            rects.append(pygame.draw.line(screen, [200,200,200], [y*grid_size,0], [y*grid_size, size[1]]))

        for textobject in textimages:
                rects.append(textobject.render(screen))


        for line in lines:
            rects.append(line.render(screen))
        if pressed:
            if not bad_line:
                rects.append(pygame.draw.line(screen,[100,100,255],start, mouse_pos))
            else:
                rects.append(pygame.draw.line(screen,[255,0,0],start, mouse_pos))







        if play!=None:
            for walker in walkers:
                walker.update(lines, play)

        for walker in walkers:
                rects.append(walker.render(screen))





        get_input(events)

        pygame.display.flip()



        delay.update()





        for rect in rects:
            pygame.draw.rect(screen, bg_color, rect)

        if int(time.time())%5==0:
            screen.fill(bg_color)

        if int(time.time())%2==0:
            textimages[-1].change_message("Lines:"+str(len(lines))+"   Walkers:"+str(len(walkers))+"   FPS: UNKNOWN")









if __name__ == "__main__":
    main()






