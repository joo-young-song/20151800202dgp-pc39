import random
from pico2d import *

character = load_image('animation_sheet.png')
kpu_map = load_image('KPU_GROUND.png')

open_canvas()

frame = 0

def draw_line(p1, p2):
    for i in range(0, 100 + 1, 2):
        clear_canvas()
        kpu_map.draw(800,600)
        t = i / 100
        x = (1-t)*p1[0] + t*p2[0]
        y = (1-t)*p1[1] + t*p2[1]
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8

size = 10

points = [(random.randint(0,800), random.randint(0,600)) for i in range(size)]

n = 1

while True:
    draw_line(points[n-1], points[n])
    n = (n + 1) % size