from pynput.keyboard import Listener, Key
from Divers import fonction_principal
import pyautogui
import time
import math
import numpy as np


def Press_map(key):
    try:
        if (key.char == 'm'):
            return False
    except:
        pass


def Press_ressource(key):
    try:
        if (key.char == 'w'):
            return False
    except:
        pass


def on_click(x, y, button, pressed):
    from pynput.mouse import Button
    if pressed:
        if (button == Button.left):
            return False


def detectclick():
    from pynput.mouse import Listener
    listener = Listener(on_click = on_click)
    listener.start()
    test = listener.running
    while test:
        test = listener.running
        pass
    x, y = pyautogui.position()
    im = pyautogui.screenshot()
    couleur = im.getpixel((x, y))
    return x,y,couleur




# def map():
#     listener = Listener(on_press=Press_map)
#     listener.start()
#     test = listener.running
#     while test:
#         test = listener.running
#         pass
#     return fonction_principal.MAP_POS()


def ressource():
    listener = Listener(on_press=Press_ressource)
    listener.start()
    test = listener.running
    while test:
        test = listener.running
        pass
    x, y, color = detectclick()
    return x, y, color


def map():
    listener = Listener(on_press=Press_map)
    listener.start()
    test = listener.running
    while test:
        test = listener.running
        pass
    return fonction_principal.MAP_POS()


