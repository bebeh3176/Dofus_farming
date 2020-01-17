import pyautogui
import cv2
import numpy as np
import time
import random
from pyclick import HumanClicker
from pynput.keyboard import Listener, Key, KeyCode

def on_press(key):
    try:
        if (key.char == 'r'):
            return False
    except:
        return

def detectR():
    listener = Listener(on_press = on_press)
    listener.start()
    test = listener.running
    while test:
        test = listener.running
        pass
    return

def Check_Pause(pause):
    if pause[0]:
        detectR()
        pause[0] = False
    return

def findcolor(color,initial = (0,0),final = (1440,900), tol = 2, sauf = []):
    color = np.uint8([[[color[0],color[1],color[2] ]]])
    hsv_color = cv2.cvtColor(color,cv2.COLOR_RGB2HSV)

    lower_limit = np.array([hsv_color[0][0][0]-tol, hsv_color[0][0][1]-tol, hsv_color[0][0][2]-tol])
    upper_limit = np.array([hsv_color[0][0][0]+tol, hsv_color[0][0][1]+tol, hsv_color[0][0][2]+tol])

    frame = pyautogui.screenshot()
    hsv = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_limit, upper_limit)

    height, width =  mask.shape
    zone_chercher = np.zeros((height,width,1), np.uint8)
    cv2.rectangle(zone_chercher,initial,final,(255),-1)
    for k in range(len(sauf)):
        cv2.rectangle(zone_chercher,(sauf[k][0],sauf[k][1]),(sauf[k][2],sauf[k][3]),(0),-1)

    res = cv2.bitwise_and(zone_chercher,zone_chercher, mask= mask)

    # if(len(sauf)):
    #     cv2.imshow('mask',mask)
    #     cv2.imshow('mask2',zone_chercher)

    # if(test):
        # affiche = cv2.rectangle(mask,initial,final,(200),-1)
        # for k in range(len(sauf)):
        #     cv2.rectangle(affiche,(sauf[k][1],sauf[k][0]),(sauf[k][3],sauf[k][2]),(100),-1)
        # cv2.imshow('mask',mask)
        # cv2.imshow('cherche',zone_chercher)
        # cv2.imshow('res',res)
        # k = cv2.waitKey()

    result1,result2 = np.where(res == 255)

    length = len(result1)
    if(length):
        return (result2[0],result1[0])
    return None

def move_mouse(GoX, GoY, dX, dY, Click=1, alea=True, vitesse = 1, pause = [False]):
    Check_Pause(pause)
    x, y = pyautogui.position()
    GoX = GoX + int(random.random() * dX)
    GoY = GoY + int(random.random() * dY)
    norm = (np.linalg.norm([(GoY - y), (GoX - x)]))
    vit = 500 * vitesse
    dur = (norm / vit) * (random.random() * 0.6 + 0.7)
    hc = HumanClicker()
    hc.move((GoX, GoY), dur)
    inter = 0.3 + random.random() * 0.3
    time.sleep(inter)
    inter = 0.13 + random.random() * 0.1
    pyautogui.click(clicks=Click, interval=inter)
    if (alea):
        inter = 0.75 + random.random() * 0.75
        time.sleep(inter)
        x, y = pyautogui.position()
        GoX = x + int(random.random() * 300 - 150)
        GoY = y + int(random.random() * 150 - 75)
        norm = (np.linalg.norm([(GoY - y), (GoX - x)]))
        vit = 250
        dur = (norm / vit) * (random.random() * 0.6 + 0.7)
        hc = HumanClicker()
        hc.move((GoX, GoY), dur)
        inter = 0.3 + random.random() * 0.3
        time.sleep(inter)
    Check_Pause(pause)
