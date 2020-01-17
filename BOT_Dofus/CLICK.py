import pyautogui
from pynput.mouse import Listener, Button
import time


def on_click(x, y, button, pressed):
    if pressed:
        if (button == Button.left):
            return False


def detectclick():
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

for i in range(7):
    x, y, couleur = detectclick()
    x, y, couleur = detectclick()
    print('position, {0}, {1}, couleur, {2}, {3}, {4}'.format(x,y,couleur[0],couleur[1],couleur[2]))










