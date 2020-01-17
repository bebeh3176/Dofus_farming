from pynput.keyboard import Listener, Key
import pyautogui
import time
import math
import numpy as np
ressource = []
confirmation = ''

def Press(key):
    try:
        global ressource
        global confirmation
        if (key.char == 'r'):
            x, y, color =  detectclick()
            ressource.append('ressource position, {0}, {1}, couleur, {2}, {3}, {4}'.format(x,y,color[0],color[1],color[2]))
        if (key.char == 'c'):
            x, y, color =  detectclick()
            confirmation = 'couleur, {2}, {3}, {4}, position, {0}, {1}'.format(x,y,color[0],color[1],color[2])
        if (key.char == 'm'):
            x, y, color =  detectclick()
            x2, y2, color =  detectclick()
            dx = x2 - x
            dy = y2 - y
            map = 'position, {0}, {1}, {2}, {3}, '.format(x,y,dx,dy)
            print('{0}{1}'.format(map, confirmation))
            for i in ressource:
                print(i)
            ressource = []
    except:
        return


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


listener = Listener(on_press = Press)
listener.start()
while(True):
    time.sleep(5)

