import random
from pico2d import *

open_canvas(1280,1024)

BASE = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')


def draw_infinity_4_points(p1, p2, p3, p4):
    frame = 0
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2

        clear_canvas()
        BASE.draw(640, 512)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
        get_events()

size = 10

points = [(random.randint(0, 1200), random.randint(0, 1000)) for i in range(size)]

n1 = 0
n2 = 1
n3 = 2
n4 = 3

while True:
    draw_infinity_4_points(points[n1], points[n2],points[n3],points[n4])
