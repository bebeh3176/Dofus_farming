from Divers import Divers as divers
from Divers import Combat as combat
#import Divers as divers
#import Combat as combat
import threading
import os
import pyautogui
import cv2
import numpy as np
import time
import random


def Level_Up(pause=[False]):
    now = pyautogui.screenshot()
    color = now.getpixel((72, 425))
    colorECH = (214, 176, 0)
    ECH1 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 10
    color = now.getpixel((104, 421))
    colorECH = (214, 176, 0)
    ECH2 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 10
    color = now.getpixel((135, 425))
    colorECH = (170, 140, 0)
    ECH3 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 10
    if ((ECH1 and ECH2) or (ECH1 and ECH3) or (ECH3 and ECH2)):
        time.sleep(0.8 + random.random() * 0.4)
        while True:
            divers.move_mouse(242, 413, 10, 10, pause=pause)
            time.sleep(0.8 + random.random() * 0.5)
            for i in range(0, 10):
                now = pyautogui.screenshot()
                color = now.getpixel((72, 425))
                colorECH = (214, 176, 0)
                ECH1 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (
                            color[2] - colorECH[2]) ** 2) <= 10
                color = now.getpixel((104, 421))
                colorECH = (214, 176, 0)
                ECH2 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (
                            color[2] - colorECH[2]) ** 2) <= 10
                color = now.getpixel((135, 425))
                colorECH = (170, 140, 0)
                ECH3 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (
                            color[2] - colorECH[2]) ** 2) <= 10
                if not ((ECH1 and ECH2) or (ECH1 and ECH3) or (ECH3 and ECH2)):
                    break
                time.sleep(0.3)
            else:
                continue
            break

        return True
    else:
        return False


def GoHavreSac(entre=True, pause=[False]):
    if(entre):
        compteur = 0
        while True:
            compteur = compteur + 1
            if(compteur == 5):
                kill_dofus(restart = True, commentaire='bug en rentrant dans l havreSac')
            if(compteur == 10):
                kill_dofus(restart = False, commentaire='bug en rentrant dans l havreSac')
                while True:
                    time.sleep(200)
            divers.move_mouse(875, 683, 14, 15, pause = pause)
            time.sleep(0.5 + random.random() * 0.5)
            for i in range(0, 15):
                if (i%5 == 0):
                    Validation(pause= pause)
                now = pyautogui.screenshot()
                color = now.getpixel((712, 147))
                colorECH = (161,87,11)
                HavreSac = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 4
                if (HavreSac):
                    break
                time.sleep(0.3)
            else:
                continue
            break
    else:
        while True:
            divers.move_mouse(875, 683, 14, 15, pause = pause)
            time.sleep(0.5 + random.random() * 0.5)
            for i in range(0, 15):
                if (i%5 == 0):
                    Validation(pause= pause)
                now = pyautogui.screenshot()
                color = now.getpixel((712, 147))
                colorECH = (161,87,11)
                ECH1 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 4
                if not (ECH1):
                    break
                time.sleep(0.3)
            else:
                continue
            break


def zaap(destination, dictozaap, pause=[False], retry=True):
    zaapNb = dictozaap[destination]
    GoHavreSac(True, pause=pause)
    compteur = 0
    while True:
        compteur = compteur + 1
        if compteur == 12:
            if retry:
                kill_dofus(restart=True, commentaire='bug durant la prise dun zaap premiere essaie')
                zaap(destination, dictozaap, pause, False)
                return
            else:
                kill_dofus(restart=False, commentaire='bug durant la prise dun zaap, on ferme')
                while True:
                    time.sleep(200)
        divers.move_mouse(346, 279, 60, 12, alea=False, pause=pause)
        time.sleep(0.5 + random.random() * 0.5)
        for i in range(0, 10):
            now = pyautogui.screenshot()
            color = now.getpixel((635, 217))
            colorECH = (30, 31, 26)
            Test = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 4
            if (Test):
                break
            time.sleep(0.3)
        else:
            divers.move_mouse(478, (236 + 29 * zaapNb), 200, 14, Click=1, pause=pause)
            continue
        break
    time.sleep(0.4+random.random()*0.3)
    divers.move_mouse(478, (236+29*zaapNb), 200, 14, Click = 2, pause= pause)
    time.sleep(5.8+random.random()*0.5)


def Banque(dictozaap, pause = [False]):
    now = pyautogui.screenshot()
    color = now.getpixel((818, 698))
    colorECH = (96, 190, 53)
    Test = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 4
    if (Test):
        zaap('Village des Eleveurs', dictozaap)
        Go_to_POS([-16, 4])
        # entre dans la banque
        while True:
            Validation(pause=pause)
            divers.move_mouse(724, 302, 20, 5, pause=pause)
            for i in range(0, 10):
                now = pyautogui.screenshot()
                color = now.getpixel((495, 213))
                colorECH = (106, 76, 29)
                Test = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 4
                if (Test):
                    break
                time.sleep(0.5)
            else:
                continue
            break
        # parle au gars
        while True:
            Validation(pause=pause)
            divers.move_mouse(709, 322, 19, 10, alea=False, pause=pause)
            time.sleep(1.5 + random.random() * 0.5)
            for i in range(0, 10):
                now = pyautogui.screenshot()
                color = now.getpixel((404, 439))
                colorECH = (251, 241, 191)
                Test = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 4
                if (Test):
                    break
                time.sleep(0.5)
            else:
                continue
            break
        # ouvrir banque
        while True:
            Validation(pause=pause)
            divers.move_mouse(563, 521, 25, 5, alea=False, pause=pause)
            time.sleep(1.5 + random.random() * 0.5)
            for i in range(0, 10):
                now = pyautogui.screenshot()
                color = now.getpixel((427, 113))
                colorECH = (105, 107, 105)
                Test = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 4
                if (Test):
                    break
                time.sleep(0.5)
            else:
                continue
            break
        # transfert des shits
        posx = 834 + int(random.random()*6)
        posy = 134 + int(random.random()*5)
        divers.move_mouse(posx, posy, 0, 0, alea = False, pause= pause)
        time.sleep(1.2 + random.random() * 0.5)
        posx = posx + 20 + int(random.random()*90)
        posy = posy + 35 + int(random.random()*8)
        divers.move_mouse(posx, posy, 0, 0)
        # fermer banque
        while True:
            Validation(pause= pause)
            divers.move_mouse(1023, 111, 7, 7, alea = False, pause= pause)
            time.sleep(1 + random.random() * 0.5)
            for i in range(0, 10):
                now = pyautogui.screenshot()
                color = now.getpixel((428, 241))
                colorECH = (98, 65, 21)
                Test = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 4
                if Test:
                    break
                time.sleep(0.5)
            else:
                continue
            break


def Echange(pause=[False]):
    # regarde si un echange est lancer
    now = pyautogui.screenshot()
    color = now.getpixel((629, 349))
    colorECH = (157, 137, 23)
    ECH1 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 10
    color = now.getpixel((688, 353))
    colorECH = (221, 186, 7)
    ECH2 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 10
    color = now.getpixel((511, 396))
    colorECH = (191, 231, 0)
    ECH3 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 10
    if (ECH1 and ECH2) or (ECH1 and ECH3) or (ECH3 and ECH2):
        time.sleep(0.8 + random.random() * 0.4)
        while True:
            # Accepte lechance
            divers.move_mouse(511, 396, 50, 8, pause= pause)
            time.sleep(0.8 + random.random() * 0.5)
            for i in range(0, 10):
                # regarde si lechange a ete accepter ou refuser, si aucun des deux, refait accpeter echange
                now = pyautogui.screenshot()
                color = now.getpixel((629, 349))
                colorECH = (157, 137, 23)
                ECH1 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (
                            color[2] - colorECH[2]) ** 2) <= 10
                color = now.getpixel((688, 353))
                colorECH = (221, 186, 7)
                ECH2 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (
                            color[2] - colorECH[2]) ** 2) <= 10
                color = now.getpixel((511, 396))
                colorECH = (191, 231, 0)
                ECH3 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (
                            color[2] - colorECH[2]) ** 2) <= 10
                if not ((ECH1 and ECH2) or (ECH1 and ECH3) or (ECH3 and ECH2)):
                    break
                time.sleep(0.3)
            else:
                continue
            break

        time.sleep(2 + random.random() * 0.5)
        # Si l'echange est encore ouvert, ferme l'echange
        now = pyautogui.screenshot()
        color = now.getpixel((591, 168))
        colorECH = (93, 93, 93)
        ECH1 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 4
        if (ECH1):
            while True:
                divers.move_mouse(1021, 110, 7, 8, pause= pause)
                time.sleep(0.5 + random.random() * 0.5)
                for i in range(0, 10):
                    now = pyautogui.screenshot()
                    color = now.getpixel((591, 168))
                    colorECH = (93, 93, 93)
                    ECH1 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (
                                color[2] - colorECH[2]) ** 2) <= 4
                    if not (ECH1):
                        break
                    time.sleep(0.3)
                else:
                    continue
                break

        GoHavreSac(True, pause = pause)
        time.sleep(150 + random.random()*30)
        GoHavreSac(False, pause = pause)

        return True
    else:
        return False


def Defi(pause=[False]):
    now = pyautogui.screenshot()
    color = now.getpixel((651, 347))
    colorECH = (60, 64, 43)
    ECH1 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 10
    color = now.getpixel((640, 345))
    colorECH = (58, 66, 45)
    ECH2 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 10
    color = now.getpixel((632, 341))
    colorECH = (60, 65, 47)
    ECH3 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 10
    if ((ECH1 and ECH2) or (ECH1 and ECH3) or (ECH3 and ECH2)):
        time.sleep(0.8 + random.random() * 0.4)
        while True:
            divers.move_mouse(598, 400, 80, 11, pause= pause)
            time.sleep(0.8 + random.random() * 0.5)
            for i in range(0, 10):
                now = pyautogui.screenshot()
                color = now.getpixel((651, 347))
                colorECH = (60, 64, 43)
                ECH1 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (
                            color[2] - colorECH[2]) ** 2) <= 10
                color = now.getpixel((640, 345))
                colorECH = (58, 66, 45)
                ECH2 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (
                            color[2] - colorECH[2]) ** 2) <= 10
                color = now.getpixel((632, 341))
                colorECH = (60, 65, 47)
                ECH3 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (
                            color[2] - colorECH[2]) ** 2) <= 10
                if not ((ECH1 and ECH2) or (ECH1 and ECH3) or (ECH3 and ECH2)):
                    break
                time.sleep(0.3)
            else:
                continue
            break

        GoHavreSac(True, pause = pause)
        time.sleep(150 + random.random()*30)
        GoHavreSac(False, pause = pause)

        return True
    else:
        return False


def Validation(pause=[False]):
    combat.combat(pause=pause)
    Defi(pause=pause)
    Echange(pause=pause)
    Level_Up(pause=pause)


def NUM_POS(img, template):
    # Perform match operations.

    template_BW = cv2.threshold(template, 100, 255, cv2.THRESH_BINARY)[1]

    res2 = cv2.matchTemplate(img, template_BW, cv2.TM_SQDIFF_NORMED)


    # Specify a threshold
    threshold = 0.1

    # Store the coordinates of matched area in a numpy array
    loc = np.where(res2 <= threshold)
    pos = []
    for pt in zip(*loc[::-1]):
        pos.append(pt[0])
    return pos


def MAP_POS(TEST=False):
    image = pyautogui.screenshot()
    image = image.crop((22, 84, 95, 106))
    # image.show()
    img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Convert it to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_BW = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)[1]
    names = [',', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
    # Read the template
    pos = {}
    for i in names:
        template = cv2.imread('Picture/{}.png'.format(i), 0)
        num = NUM_POS(img_BW, template)
        check = -3
        for j in num:
            if(2 < j - check):
                pos[j] = i
                check = j
    posfin = ''
    posnom = []
    virgule = 0
    try:
        for i in sorted(pos):
            if pos[i] == ',':
                posnom.append(int(posfin))
                posfin = ''
                virgule = virgule + 1
                if virgule == 2:
                    break
            if pos[i] != ',':
                posfin = '{}{}'.format(posfin, pos[i])
                if(virgule == 1) & TEST:
                    return True
    except:
        posnom = [0, 0]
        if(TEST):
            return False
    if posnom == []:
        posnom = [0, 0]
        if (TEST):
            return False
    return posnom


def isBlack():
    image = pyautogui.screenshot()
    maxi = 0
    blackpos = [(274, 67), (371, 403), (400, 653), (647, 585), (960, 614), (988, 432), (674, 438), (674, 233),
                (1005, 251)]
    for j in blackpos:
        maxi = max(maxi, max(image.getpixel(j)))
    if (maxi < 5):
        return True
    else:
        return False


def ressource(dicto, pause=[False]):
    while True:
        action = True
        Validation(pause=pause)
        now = pyautogui.screenshot()
        for key in dicto.keys():
            color = now.getpixel(key)
            look = dicto[key]
            d = ((color[0] - look[0]) ** 2 + (color[1] - look[1]) ** 2 + (color[2] - look[2]) ** 2)
            if (d < 9):
                divers.move_mouse(key[0], key[1], 10, 10, pause=pause)
                for i in range(0, 6):
                    now = pyautogui.screenshot()
                    color = now.getpixel(key)
                    d = ((color[0] - look[0]) ** 2 + (color[1] - look[1]) ** 2 + (color[2] - look[2]) ** 2)
                    if (d < 9):
                        break
                now = pyautogui.screenshot()
                time.sleep(3.8 + random.random() * 0.5)
                action = False
        if action:
            break


def Go_to_POS_Caverne(GOTO, Pos, Couleur, Pos_Couleur, now, pause=[False]):
    now_Max = len(Couleur)
    while(now != GOTO):
        screen = pyautogui.screenshot()
        color = screen.getpixel(Pos_Couleur[now])
        if 2 < ((color[0] - Couleur[now][0]) ** 2 + (color[1] - Couleur[now][1]) ** 2 + (color[2] - Couleur[now][2]) ** 2):
            compteur = 0
            while True:
                now = now + 1
                if (compteur == 5):
                    kill_dofus(restart=True, commentaire='bug dans le changement de carte de caverne')
                    compteur = compteur + 1
                if (compteur == 10):
                    kill_dofus(restart=False, commentaire='bug dans le changement de carte de caverne')
                    while (True):
                        time.sleep(200)
                if now == now_Max:
                    compteur  = compteur + 1
                    Validation(pause= pause)
                    divers.move_mouse(262, 694, 100, 4,alea=False, pause= pause)
                    screen = pyautogui.screenshot()
                    now = 0
                color = screen.getpixel(Pos_Couleur[now])
                if ((color[0] - Couleur[now][0]) ** 2 + (color[1] - Couleur[now][1]) ** 2 + (color[2] - Couleur[now][2]) ** 2) < 2:
                    break
        if now == GOTO:
            break
        divers.move_mouse(Pos[now][0], Pos[now][1], Pos[now][2], Pos[now][3], pause= pause)
        for i in range(1, 12):
            if (i%4 == 0):
                Validation(pause= pause)
            time.sleep(0.4)
            screen = pyautogui.screenshot()
            now_temp = now + 1
            color = screen.getpixel(Pos_Couleur[now_temp])
            if ((color[0] - Couleur[now_temp][0]) ** 2 + (color[1] - Couleur[now_temp][1]) ** 2 + (color[2] - Couleur[now_temp][2]) ** 2) < 2:
                now = now + 1
                if now == now_Max:
                    now = 0
                time.sleep(random.random() * 0.5)
                break
    return now


def Go_to_POS(GOTO, HorizontaleFirst=True, sauf={}, pause=[False], retry=1):
    try:
        now = tuple(MAP_POS())
        nombre_max_changement = abs(GOTO[0] - now[0]) + abs(GOTO[1] - now[1]) + 8
        nombre_changement = 0
        while ((GOTO[0] - now[0] != 0) or (GOTO[1] - now[1] != 0)):
            nombre_changement = nombre_changement + 1
            if(nombre_max_changement == nombre_changement):
                kill_dofus(True, commentaire='bug dans go to pos trop de changement')
            if (2*nombre_max_changement == nombre_changement):
                kill_dofus(False, commentaire='bug dans go to pos trop de changement')
                while True:
                    time.sleep(200)
            Validation(pause=pause)
            dx = GOTO[0] - now[0]
            dy = GOTO[1] - now[1]
            if tuple(now) in sauf:
                 divers.move_mouse(sauf[now][0], sauf[now][1], sauf[now][2], sauf[now][3], pause= pause)
            else:
                if (HorizontaleFirst):
                    if dx > 0:
                        divers.move_mouse(1029, 180, 13, 320, pause=pause)
                    elif dx < 0:
                        divers.move_mouse(239, 180, 13, 320, pause=pause)
                    elif dy > 0:
                        divers.move_mouse(425, 619, 425, 6, pause=pause)
                    elif dy < 0:
                        divers.move_mouse(425, 58, 425, 6, pause=pause)
                else:
                    if (dy > 0):
                        divers.move_mouse(425, 619, 425, 6, pause= pause)
                    elif (dy < 0):
                        divers.move_mouse(425, 58, 425, 6, pause= pause)
                    elif (dx > 0):
                        divers.move_mouse(1029, 180, 13, 320, pause= pause)
                    elif (dx < 0):
                        divers.move_mouse(239, 180, 13, 320, pause= pause)
            for i in range(1, 13):
                if i%5 == 0:
                        Validation(pause= pause)
                time.sleep(0.3)
                if now != tuple(MAP_POS()):
                    break
            time.sleep(0.4 + random.random() * 0.2)
            now = tuple(MAP_POS())
            if (GOTO[0] - now[0] == 0) and (GOTO[1] - now[1] == 0):
                break
    except:
        if retry == 1:
            time.sleep(5)
            Go_to_POS(GOTO, HorizontaleFirst, sauf, pause, retry=2)
        else:
            if retry ==2:
                kill_dofus(restart=True, commentaire='bug dans go to pos, ferme et reouvre')
                Go_to_POS(GOTO, HorizontaleFirst, sauf, pause, retry=3)
            else:
                kill_dofus(restart=False, commentaire='bug dans go to pos, une erreur est survenue')
                while True:
                    time.sleep(200)
    time.sleep(2 + random.random() * 1)
    now = tuple(MAP_POS())
    if (GOTO[0] - now[0] != 0) or (GOTO[1] - now[1] != 0):
        Go_to_POS(GOTO, HorizontaleFirst, sauf, pause, retry)
    return


def kill_dofus(restart=True, commentaire = 'Pas de commentaire'):
    picture_erreur = pyautogui.screenshot()
    time_erreur = time.time()
    name = 'LOG/{}.png'.format(time_erreur)
    text_name = 'LOG/{}.txt'.format(time_erreur)
    Log_message = open(text_name, "w")
    Log_message.write(commentaire)
    Log_message.close()
    picture_erreur.save(name)
    if restart:
        for k in range(3):
            Log_message = open(text_name, "a")
            Log_message.write('\nattempt number {}'.format(k))
            Log_message.close()
            thread_kill = threading.Thread(target=xkill_short)
            thread_kill.start()
            time.sleep(0.5)
            divers.move_mouse(500, 300, 100, 100, alea=False)
            template = cv2.imread('Picture/ankama.png', 0)
            template_BW = cv2.threshold(template, 160, 255, cv2.THRESH_BINARY)[1]
            for i in range(18):
                divers.move_mouse(32+i*66,739,1,1,Click = 0,alea = False)
                image = pyautogui.screenshot()
                image = image.crop((5, 670, 1274, 696))
                # image.show()
                img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                img_BW = cv2.threshold(img_gray, 160, 255, cv2.THRESH_BINARY)[1]
                res2 = cv2.matchTemplate(img_BW, template_BW, cv2.TM_SQDIFF_NORMED)
                threshold = 0.4
                # Store the coordinates of matched area in a numpy array
                if(np.any(res2 <= threshold)):
                    print("found")
                    print(i)
                    pyautogui.click()
                    time.sleep(2)
                    divers.move_mouse(1106, 572,1,1,alea = False)
                    time.sleep(10)
                    break
            # Close warning windows
            template = cv2.imread('Picture/warning.png', 0)
            template_BW = cv2.threshold(template, 160, 255, cv2.THRESH_BINARY)[1]
            while(True):
                image = pyautogui.screenshot()
                image = image.crop((54, 61, 320, 92))
                img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                img_BW = cv2.threshold(img_gray, 160, 255, cv2.THRESH_BINARY)[1]
                res2 = cv2.matchTemplate(img_BW, template_BW, cv2.TM_SQDIFF_NORMED)
                threshold = 0.4
                if np.any(res2 <= threshold):
                    divers.move_mouse(113, 210, 1, 1, alea = False)
                else:
                    break
            time.sleep(10)

            # Login
            template = cv2.imread('Picture/connexion.png', 0)
            template_BW = cv2.threshold(template, 160, 255, cv2.THRESH_BINARY)[1]
            image = pyautogui.screenshot()
            image = image.crop((525, 184, 778, 244))
            img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            img_BW = cv2.threshold(img_gray, 160, 255, cv2.THRESH_BINARY)[1]
            res2 = cv2.matchTemplate(img_BW, template_BW, cv2.TM_SQDIFF_NORMED)
            threshold = 0.4
            if (np.any(res2 <= threshold)):
                Log_message = open(text_name, "a")
                Log_message.write('\nconnecter a laide du mot de passe')
                Log_message.close()
                divers.move_mouse(553, 300, 100, 8, alea=False)
                pyautogui.typewrite('darkside94', interval=0.25)
                time.sleep(2)
                divers.move_mouse(587, 390, 60, 10, alea=False)

            # lance le personnage
            template = cv2.imread('Picture/personnage.png', 0)
            template_BW = cv2.threshold(template, 160, 255, cv2.THRESH_BINARY)[1]
            for i in range(4):
                time.sleep(10)
                image = pyautogui.screenshot()
                image = image.crop((448, 82, 878, 132))
                img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                img_BW = cv2.threshold(img_gray, 160, 255, cv2.THRESH_BINARY)[1]
                res2 = cv2.matchTemplate(img_BW, template_BW, cv2.TM_SQDIFF_NORMED)
                threshold = 0.4
                if np.any(res2 <= threshold):
                    divers.move_mouse(736, 547, 100, 19, alea=False)
                    break
            # regarde si le click a fonctionne
            for i in range(3):
                time.sleep(15)
                image = pyautogui.screenshot()
                image = image.crop((448, 82, 878, 132))
                img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                img_BW = cv2.threshold(img_gray, 160, 255, cv2.THRESH_BINARY)[1]
                res2 = cv2.matchTemplate(img_BW, template_BW, cv2.TM_SQDIFF_NORMED)
                threshold = 0.4
                if (np.any(res2 <= threshold)):
                    divers.move_mouse(736, 547, 100, 19, alea=False)
                else:
                    break
            #attend que le jeu load, apres 1 min ferme le jeu et reouvre
            test = False
            for i in range(12):
                time.sleep(5)
                if(MAP_POS(True)): #regarde si le jeu est loader en verifiant si on peut lire la carte
                    test = True
                    break
            if(test): #si oui descend le chat et retourne la fonction
                divers.move_mouse(310, 611, 130, 0, Click=0, alea=False)
                pyautogui.drag(0, (45+random.random() * 20), 0.5+random.random()*0.7)
                Log_message = open(text_name, "a")
                Log_message.write('\nreussite')
                Log_message.close()
                return 0
        # une fois qu'il kill le jeu 3 foie et ca marche pas kill une derniere fois et et bloque
        thread_kill = threading.Thread(target=xkill_short)
        thread_kill.start()
        time.sleep(0.5)
        divers.move_mouse(500, 300, 100, 100, alea=False)
        Log_message = open(text_name, "a")
        Log_message.write('\nfermeture apres 3 essaie')
        Log_message.close()
        while(True):
            time.sleep(200)
    else:
        # kill le jeu et retourne rien
        thread_kill = threading.Thread(target=xkill_short)
        thread_kill.start()
        time.sleep(0.5)
        divers.move_mouse(500, 300, 100, 100, alea=False)
        Log_message = open(text_name, "a")
        Log_message.write('\nLe jeu a fermer comme prevue')
        Log_message.close()
        return 0


def xkill_short():
    os.system("xkill")

