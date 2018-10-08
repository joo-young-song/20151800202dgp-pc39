from pico2d import *
import random


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

class bBall:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 600
        self.image = load_image('ball41x41.png')
        self.speed = random.randint(5,20)
        self.choice = random.randint(0 ,1)

    def update(self):
        if(self.y > 50):
            self.y = self.y - self.speed

    def draw(self):
        self.image.draw(self.x, self.y)


class sBall:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 600
        self.image = load_image('ball21x21.png')
        self.speed = random.randint(5,20)
        self.choice = random.randint(0 ,1)

    def update(self):
        if(self.y > 50):
            self.y = self.y - self.speed

    def draw(self):
        self.image.draw(self.x, self.y)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')


    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


open_canvas()
c = random.randint(0, 20)
team = [Boy() for i in range(11)]
small_ball = [sBall() for d in range(c)]
big_ball = [bBall() for f in range(20 - c)]
grass = Grass()

running = True

while running :
    handle_events()

    for boy in team:
        boy.update()

    for ball in small_ball:
        ball.update()

    for otherball in big_ball:
        otherball.update()

    clear_canvas()
    grass.draw()
    
    for boy in team:
        boy.draw()

    for ball in small_ball:
        ball.draw()

    for otherball in big_ball:
        otherball.draw()
    update_canvas()

    delay(0.05)

close_canvas()