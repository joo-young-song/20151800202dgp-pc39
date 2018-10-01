import random
from pico2d import*

open_canvas()

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')


def draw_character(p1, p2):
    frame = 0
    for i in range(0, 100 + 1, 2):

        clear_canvas()
        kpu_ground.draw(200,200)
        t = i / 100
        x = (1-t)*p1[0] + t*p2[0]
        y = (1-t)*p1[1] + t*p2[1]
        frame = (frame + 1) % 8
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()

        delay(0.05)

size = 10

points = [(random.randint(0,800), random.randint(0,600)) for i in range(size)]

n = 1

while True:
    draw_character(points[n-1], points[n])
    n = (n + 1) % size
