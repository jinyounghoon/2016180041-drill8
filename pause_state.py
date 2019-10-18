import game_framework
from pico2d import *

import main_state

name = "PauseState"
image = None


def enter():
   global image
   image = load_image('pause.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def update():
    pass


def pause():
    pass


def resume():
    pass




