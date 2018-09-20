from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x,y
    global Cx, Cy
    global Mx, My
    global Gx, Gy
    global head
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x,y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            Cx,Cy = event.x - 25, KPU_HEIGHT - 1 - event.y + 26
            Gx, Gy = Cx - Mx, Cy - My
            if(Gx < 0):
                head = 1
            else:
                head = 0



open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
Cx = 0
Cy = 0
Mx = 0
My = 0
Gx = 0
Gy = 0
head = 0
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand.draw(x, y)
    if(Gx < 0):
        if (Mx > Cx):
            Mx = Mx + Gx / 10
            My = My + Gy / 10
            if(Mx < Cx):
                Mx = Cx
                My = Cy
        else:
            Mx = Cx
            My = Cy
    elif(Gx > 0):
        if(Mx < Cx):
            Mx = Mx + Gx / 10
            My = My + Gy / 10
            if (Mx > Cx):
                Mx = Cx
                My = Cy
        else:
            Mx = Cx
            My = Cy
    if head == 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, Mx, My)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, Mx, My)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)
    handle_events()

close_canvas()




