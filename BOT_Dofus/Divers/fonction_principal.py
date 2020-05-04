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
from datetime import datetime


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


def GoHavreSac(option, entre=True, pause=[False]):
    potion_rappel = True
    if(entre):
        compteur = 0
        while True:
            compteur = compteur + 1
            if compteur == 5:
                if potion_rappel:
                    potion_rappel = False
                    divers.move_mouse(809, 641, 13, 14, Click=2, pause=pause)
                    compteur = 3
                else:
                    kill_test = kill_dofus(option, restart=True, commentaire='1er bug en rentrant dans l havreSac')
                    potion_rappel = True
                    if kill_test == 1:
                        return 1
            if compteur == 10:
                if potion_rappel:
                    potion_rappel = False
                    divers.move_mouse(809, 641, 13, 14, Click=2, pause=pause)
                    compteur = 8
                else:
                    kill_dofus(option, restart=False, commentaire='2e bug en rentrant dans l havreSac, donc kill')
                    return 1
            divers.move_mouse(875, 683, 14, 15, pause=pause)
            time.sleep(0.5 + random.random() * 0.5)
            for i in range(0, 15):
                if i % 5 == 0:
                    Validation_erreur = Validation(option, pause=pause)
                    if Validation_erreur == 1:
                        return 1
                now = pyautogui.screenshot()
                color = now.getpixel((712, 147))
                colorECH = (161, 87, 11)
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
                    Validation_erreur = Validation(option, pause=pause)
                    if Validation_erreur == 1:
                        return 1
                now = pyautogui.screenshot()
                color = now.getpixel((712, 147))
                colorECH = (161, 87, 11)
                ECH1 = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 4
                if not ECH1:
                    break
                time.sleep(0.3)
            else:
                continue
            break
    return 0


def zaap(destination, dictozaap, option, pause=[False], retry=True):
    zaapNb = dictozaap[destination]
    Havre_sac_erreur = GoHavreSac(option, True, pause=pause)
    if Havre_sac_erreur == 1:
        return 1
    compteur = 0
    while True:
        compteur = compteur + 1
        if compteur == 12:
            if retry:
                kill_test = kill_dofus(option, restart=True, commentaire='bug durant la prise dun zaap premiere essaie')
                if kill_test == 1:
                    return 1
                zaap_erreur = zaap(destination, dictozaap, option, pause, False)
                return zaap_erreur
            else:
                kill_dofus(option, restart=False, commentaire='bug durant la prise dun zaap, on ferme')
                return 1
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
            divers.move_mouse(478, (238 + 29 * zaapNb), 200, 14, Click=1, pause=pause)
            continue
        break
    time.sleep(0.4+random.random()*0.3)
    divers.move_mouse(478, (238+29*zaapNb), 200, 14, Click = 2, pause= pause)
    time.sleep(5.8+random.random()*0.5)
    return 0


def VidePod(dictozaap, option, pause=[False], baspourcentage=True):
    now = pyautogui.screenshot()
    if baspourcentage:
        color = now.getpixel((786, 698))
    else:
        color = now.getpixel((825, 698))
    colorECH = (96, 190, 53)
    test = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 4
    videerror = 2
    if test:
        if option.EmplacementViderPod == 'Banque':
            videerror = Banque(dictozaap, option, pause)
        if option.EmplacementViderPod == 'Maison':
            videerror = GotoMaison(dictozaap, option, pause)
            if videerror == 2:
                kill_test = kill_dofus(option, restart=True, commentaire='Erreur survenur en allant se vider dans la maison')
                if kill_test == 1:
                    return 1
                videerror = GotoMaison(dictozaap, option, pause)
                if 0 < videerror:
                    return 1
    return videerror

def GotoMaison(dictozaap, option, pause=[False]):
    zaap_erreur = zaap('Bonta Centre-ville', dictozaap, option, pause=pause)
    if (zaap_erreur == 1):
        return 1
    Go_to_POS([-31, -52], option)
    Go_to_POS([-30, -52], option)
    # Click sur maison et click sur rentre
    if option.proprietairemaison:
        for j in range(0, 5):
            Validation_erreur = Validation(option, pause=pause)
            if Validation_erreur == 1:
                return 1
            posx = 405 + int(random.random() * 12)
            posy = 78 + int(random.random() * 20)
            divers.move_mouse(posx, posy, 0, 0, alea=False, pause=pause)
            time.sleep(1.2 + random.random() * 0.5)
            posx = posx + 15 + int(random.random() * 90)
            posy = posy + 20 + int(random.random() * 6)
            divers.move_mouse(posx, posy, 0, 0)
            time.sleep(1)
            for i in range(0, 10):
                now = pyautogui.screenshot()
                color = now.getpixel((666, 317))
                colorECH = (108, 160, 160)
                Test = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 4
                if Test:
                    break
                time.sleep(0.5)
            else:
                continue
            break
        else:
            return 2

    else:
        for j in range(0, 5):
            Validation_erreur = Validation(option, pause=pause)
            if Validation_erreur == 1:
                return 1
            divers.move_mouse(405, 78, 12, 20, alea=False, pause=pause)
            time.sleep(4 + random.random() * 1)
            pyautogui.typewrite(option.codemaison, interval=0.25)
            time.sleep(0.3 + random.random() * 0.2)
            pyautogui.press('enter')
            time.sleep(0.2 + random.random() * 0.2)
            pyautogui.press('enter')
            for i in range(0, 10):
                now = pyautogui.screenshot()
                color = now.getpixel((666, 317))
                colorECH = (108, 160, 160)
                Test = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 4
                if Test:
                    break
                time.sleep(0.5)
            else:
                continue
            break
        else:
            return 2
    # monte d'un etage
    for j in range(0, 5):
        Validation_erreur = Validation(option, pause=pause)
        if Validation_erreur == 1:
            return 1
        divers.move_mouse(361, 387, 30, 15)
        time.sleep(0.5)
        for i in range(0, 10):
            now = pyautogui.screenshot()
            color = now.getpixel((814, 265))
            colorECH = (172, 39, 9)
            Test = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 4
            if Test:
                break
            time.sleep(0.5)
        else:
            continue
        break
    else:
        return 2
    #click sur coffre et click ouvre
    if option.proprietairemaison:
        for j in range(0, 5):
            Validation_erreur = Validation(option, pause=pause)
            if Validation_erreur == 1:
                return 1
            posx = 699 + int(random.random() * 23)
            posy = 305 + int(random.random() * 16)
            divers.move_mouse(posx, posy, 0, 0, alea=False, pause=pause)
            time.sleep(1.2 + random.random() * 0.5)
            posx = posx + 11 + int(random.random() * 46)
            posy = posy + 21 + int(random.random() * 6)
            divers.move_mouse(posx, posy, 0, 0)
            time.sleep(1)
            for i in range(0, 10):
                now = pyautogui.screenshot()
                color = now.getpixel((885, 114))
                colorECH = (83, 84, 83)
                Test = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 4
                if Test:
                    break
                time.sleep(0.5)
            else:
                continue
            break
        else:
            return 2
    else:
        for j in range(0, 5):
            Validation_erreur = Validation(option, pause=pause)
            if Validation_erreur == 1:
                return 1
            divers.move_mouse(699, 305, 23, 16, alea=False, pause=pause)
            time.sleep(4 + random.random() * 1)
            pyautogui.typewrite(option.codecoffre, interval=0.25)
            time.sleep(0.3 + random.random() * 0.2)
            pyautogui.press('enter')
            time.sleep(0.2 + random.random() * 0.2)
            pyautogui.press('enter')
            for i in range(0, 10):
                now = pyautogui.screenshot()
                color = now.getpixel((885, 114))
                colorECH = (83, 84, 83)
                Test = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 4
                if Test:
                    break
                time.sleep(0.5)
            else:
                continue
            break
        else:
            return 2

    # transfert des shits
    posx = 834 + int(random.random() * 6)
    posy = 134 + int(random.random() * 5)
    divers.move_mouse(posx, posy, 0, 0, alea=False, pause=pause)
    time.sleep(1.2 + random.random() * 0.5)
    posx = posx + 20 + int(random.random() * 90)
    posy = posy + 35 + int(random.random() * 8)
    divers.move_mouse(posx, posy, 0, 0)
    # fermer coffre
    for j in range(0, 5):
        Validation_erreur = Validation(option, pause=pause)
        if Validation_erreur == 1:
            return 1
        divers.move_mouse(1023, 111, 7, 7, alea=False, pause=pause)
        time.sleep(1 + random.random() * 0.5)
        for i in range(0, 10):
            now = pyautogui.screenshot()
            color = now.getpixel((814, 265))
            colorECH = (172, 39, 9)
            Test = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 4
            if Test:
                break
            time.sleep(0.5)
        else:
            continue
        break
    else:
        return 2
    return 0

def Banque(dictozaap, option, pause=[False]):
    zaap_erreur = zaap('Village des Eleveurs', dictozaap, option, pause=pause)
    if(zaap_erreur == 1):
        return 1
    Go_to_POS([-16, 4], option)
    # entre dans la banque
    while True:
        Validation_erreur = Validation(option, pause=pause)
        if Validation_erreur == 1:
            return 1
        divers.move_mouse(724, 302, 20, 5, pause=pause)
        for i in range(0, 10):
            now = pyautogui.screenshot()
            color = now.getpixel((495, 213))
            colorECH = (106, 76, 29)
            Test = ((color[0] - colorECH[0]) ** 2 + (color[1] - colorECH[1]) ** 2 + (color[2] - colorECH[2]) ** 2) <= 4
            if Test:
                break
            time.sleep(0.5)
        else:
            continue
        break
    # parle au gars
    while True:
        Validation_erreur = Validation(option, pause=pause)
        if Validation_erreur == 1:
            return 1
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
        Validation_erreur = Validation(option, pause=pause)
        if Validation_erreur == 1:
            return 1
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
        Validation_erreur = Validation(option, pause=pause)
        if Validation_erreur == 1:
            return 1
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
    return 0


def Echange(option, pause=[False]):
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

        havre_sac_erreur = GoHavreSac(option, True, pause=pause)
        if havre_sac_erreur == 1:
            return 1
        time.sleep(150 + random.random()*30)
        havre_sac_erreur = GoHavreSac(option, False, pause=pause)
        if havre_sac_erreur == 1:
            return 1

        return 0
    else:
        return 0


def Defi(option, pause=[False]):
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

        havre_sac_erreur = GoHavreSac(option, True, pause=pause)
        if havre_sac_erreur == 1:
            return 1
        time.sleep(150 + random.random() * 30)
        havre_sac_erreur = GoHavreSac(option, False, pause=pause)
        if havre_sac_erreur == 1:
            return 1

        return 0
    else:
        return 0


def Validation(option, pause=[False]):
    combat.combat(option, pause=pause)
    combat.click_combat_fini(pause=pause)
    Defi_test = Defi(option, pause=pause)
    if Defi_test == 1:
        return 1
    Echange_test = Echange(option, pause=pause)
    if Echange_test == 1:
        return 1
    Level_Up(pause=pause)
    return 0


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
        posnom = [-200, -200]
        if(TEST):
            return False
    if ((posnom == []) or (virgule != 2)):
        posnom = [-200, -200]
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


def ressource(dicto, option, pause=[False]):
    nombremaxressource = len(dicto) + 5
    retry = True
    nombreressource = 0
    while True:
        action = True
        Validation_erreur = Validation(option, pause=pause)
        if Validation_erreur == 1:
            return 1
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
                time.sleep(3.8 + random.random() * 0.5)
                now = pyautogui.screenshot()
                action = False
                nombreressource = nombreressource + 1
        if action:
            break
        if (nombreressource > nombremaxressource):
            if not retry:
                return 1
            retry = False
            nombreressource = 0
            kill_test = kill_dofus(option, restart=True, commentaire='recolte trop de ressource sur une carte')
            if kill_test == 1:
                return 1
    return 0


def Go_to_POS_Caverne(GOTO, Pos, Couleur, Pos_Couleur, now, option,  pause=[False]):
    now_Max = len(Couleur)
    compteur_changement_map = 0
    while(now != GOTO):
        screen = pyautogui.screenshot()
        color = screen.getpixel(Pos_Couleur[now])
        if 2 < ((color[0] - Couleur[now][0]) ** 2 + (color[1] - Couleur[now][1]) ** 2 + (color[2] - Couleur[now][2]) ** 2):
            compteur = 0
            while True:
                now = now + 1
                if compteur == 5:
                    kill_test = kill_dofus(option, restart=True, commentaire='Ne se reconnait pas dans la caverne')
                    if kill_test == 1:
                        return 2000000
                    compteur = compteur + 1
                if compteur == 10:
                    return 1000000
                if now == now_Max:
                    compteur = compteur + 1
                    Validation_erreur = Validation(option, pause=pause)
                    if Validation_erreur == 1:
                        return 2000000
                    divers.move_mouse(262, 694, 100, 4, alea=False, pause=pause)
                    screen = pyautogui.screenshot()
                    now = 0
                color = screen.getpixel(Pos_Couleur[now])
                if ((color[0] - Couleur[now][0]) ** 2 + (color[1] - Couleur[now][1]) ** 2 + (color[2] - Couleur[now][2]) ** 2) < 2:
                    break
        if now == GOTO:
            break
        divers.move_mouse(Pos[now][0], Pos[now][1], Pos[now][2], Pos[now][3], pause=pause)
        for i in range(1, 12):
            if i % 4 == 0:
                Validation_erreur = Validation(option, pause=pause)
                if Validation_erreur == 1:
                    return 2000000
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
        compteur_changement_map = compteur_changement_map + 1
        if compteur_changement_map == (now_Max+4):
            kill_test = kill_dofus(option, restart=True, commentaire='trop de changement de carte caverne')
            if kill_test == 1:
                return 2000000
            compteur_changement_map = compteur_changement_map + 1
        if compteur_changement_map == 2*(now_Max + 4):
            kill_dofus(option, restart=False, commentaire='trop de changement de carte caverne')
            return 2000000
    return now


def Go_to_POS(GOTO, option, HorizontaleFirst=True, sauf={}, pause=[False], retry=1):
    try:
        now = tuple(MAP_POS())
        if (200 + now[0] == 0) and (200 + now[1] == 0):
            kill_test = kill_dofus(option, restart=True, commentaire='Erreur dans la lecture de la map')
            if kill_test == 1:
                return 2
        nombre_max_changement = abs(GOTO[0] - now[0]) + abs(GOTO[1] - now[1]) + 8
        nombre_changement = 0
        Now_inchangeant = 0
        while ((GOTO[0] - now[0] != 0) or (GOTO[1] - now[1] != 0)):
            nombre_changement = nombre_changement + 1
            if (nombre_max_changement == nombre_changement) or (Now_inchangeant == 4):
                return 1
            Validation_erreur = Validation(option, pause=pause)
            if Validation_erreur == 1:
                return 2
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
            Now_inchangeant = Now_inchangeant + 1
            for i in range(1, 13):
                if i % 5 == 0:
                    Validation_erreur = Validation(option, pause=pause)
                    if Validation_erreur == 1:
                        return 2
                time.sleep(0.3)
                if now != tuple(MAP_POS()):
                    Now_inchangeant = 0
                    break
            time.sleep(0.4 + random.random() * 0.2)
            now = tuple(MAP_POS())
            if (GOTO[0] - now[0] == 0) and (GOTO[1] - now[1] == 0):
                break
    except:
        if retry == 1:
            time.sleep(5)
            Go_to_POS(GOTO, option, HorizontaleFirst, sauf, pause, retry=2)
        else:
            if retry == 2:
                kill_test = kill_dofus(option, restart=True, commentaire='bug dans go to pos, ferme et reouvre')
                if kill_test == 1:
                    return 2
                Go_to_POS(GOTO, option, HorizontaleFirst, sauf, pause, retry=3)
            else:
                kill_dofus(option, restart=False, commentaire='bug dans go to pos, une erreur est survenue 2e fois')
                return 2
    time.sleep(2 + random.random() * 1)
    now = tuple(MAP_POS())
    if (200 + now[0] == 0) and (200 + now[1] == 0):
        kill_test = kill_dofus(option, restart=True, commentaire='Erreur dans la lecture de la map')
        if kill_test == 1:
            return 2
    if (GOTO[0] - now[0] != 0) or (GOTO[1] - now[1] != 0):
        Go_to_POS(GOTO, option, HorizontaleFirst, sauf, pause, retry)
    return 0


def kill_dofus(option, restart=True, commentaire = 'Pas de commentaire'):
    picture_erreur = pyautogui.screenshot()
    time_erreur = datetime.today()
    time_erreur = datetime(time_erreur.year, time_erreur.month, time_erreur.day, time_erreur.hour, time_erreur.minute)
    name = 'LOG/{}.png'.format(time_erreur)
    text_name = 'LOG/{}.txt'.format(time_erreur)
    Log_message = open(text_name, "w")
    Log_message.write(commentaire)
    Log_message.close()
    picture_erreur.save(name)
    kill_result = 0
    if restart:
        thread_kill = threading.Thread(target=xkill_short)
        thread_kill.start()
        time.sleep(0.5)
        divers.move_mouse(500, 300, 100, 100, alea=False)
        time.sleep(1)
        kill_result = ouverture_dofus(option, text_name)
    else:
        # kill le jeu et retourne rien
        thread_kill = threading.Thread(target=xkill_short)
        thread_kill.start()
        time.sleep(0.5)
        divers.move_mouse(500, 300, 100, 100, alea=False)
        Log_message = open(text_name, "a")
        Log_message.write('\nLe jeu a fermer comme prevue')
        Log_message.close()
    return kill_result


def ouverture_dofus(option, text_name="LOG/test.txt"):
    for k in range(3):
        Log_message = open(text_name, "a")
        Log_message.write('\nattempt number {}'.format(k))
        Log_message.close()
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
            if np.any(res2 <= threshold):
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
        connexion_BW = cv2.threshold(template, 160, 255, cv2.THRESH_BINARY)[1]
        # lance le personnage
        template = cv2.imread('Picture/personnage.png', 0)
        personnage_BW = cv2.threshold(template, 160, 255, cv2.THRESH_BINARY)[1]
        template = cv2.imread('Picture/choix.png', 0)
        perso_BW = cv2.threshold(template, 160, 255, cv2.THRESH_BINARY)[1]
        bool_not_connexion = True

        for i in range(10):
            time.sleep(3)
            if bool_not_connexion:
                image = pyautogui.screenshot()
                image = image.crop((525, 184, 778, 244))
                img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                img_BW = cv2.threshold(img_gray, 160, 255, cv2.THRESH_BINARY)[1]
                res_connexion = cv2.matchTemplate(img_BW, connexion_BW, cv2.TM_SQDIFF_NORMED)
                threshold = 0.4
                if (np.any(res_connexion <= threshold)):
                    Log_message = open(text_name, "a")
                    Log_message.write('\nconnecter a laide du mot de passe')
                    Log_message.close()
                    divers.move_mouse(553, 300, 100, 8, alea=False)
                    pyautogui.typewrite(option.motDePasse, interval=0.25)
                    time.sleep(2)
                    divers.move_mouse(587, 390, 60, 10, alea=False)
                    bool_not_connexion = False
                    time.sleep(4)

            image = pyautogui.screenshot()
            image = image.crop((400, 60, 950, 150))
            img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            img_BW = cv2.threshold(img_gray, 160, 255, cv2.THRESH_BINARY)[1]
            res_personnage = cv2.matchTemplate(img_BW, personnage_BW, cv2.TM_SQDIFF_NORMED)
            res_perso = cv2.matchTemplate(img_BW, perso_BW, cv2.TM_SQDIFF_NORMED)
            threshold = 0.4
            if np.any(res_perso <= threshold) or np.any(res_personnage <= threshold):
                divers.move_mouse(736, 547, 100, 19, alea=False)
                break
        else:
            thread_kill = threading.Thread(target=xkill_short)
            thread_kill.start()
            time.sleep(0.5)
            divers.move_mouse(500, 300, 100, 100, alea=False)
            time.sleep(1)
            continue

        # regarde si le click a fonctionne
        for i in range(9):
            time.sleep(5)
            image = pyautogui.screenshot()
            image = image.crop((448, 82, 878, 132))
            img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            img_BW = cv2.threshold(img_gray, 160, 255, cv2.THRESH_BINARY)[1]
            res_personnage = cv2.matchTemplate(img_BW, personnage_BW, cv2.TM_SQDIFF_NORMED)
            res_perso = cv2.matchTemplate(img_BW, perso_BW, cv2.TM_SQDIFF_NORMED)
            threshold = 0.4
            if np.any(res_perso <= threshold) or np.any(res_personnage <= threshold):
                divers.move_mouse(736, 547, 100, 19, alea=False)
            else:
                break
        #attend que le jeu load, apres 40 sec ferme le jeu et reouvre
        test = False
        for i in range(20):
            time.sleep(2)
            if(MAP_POS(True)): #regarde si le jeu est loader en verifiant si on peut lire la carte
                break
        else:
            thread_kill = threading.Thread(target=xkill_short)
            thread_kill.start()
            time.sleep(0.5)
            divers.move_mouse(500, 300, 100, 100, alea=False)
            time.sleep(1)
            continue

        divers.move_mouse(310, 610, 130, 0, Click=0, alea=False)
        time.sleep(0.5)
        pyautogui.drag(0, (40+random.random() * 15), 0.5+random.random()*0.7)
        Log_message = open(text_name, "a")
        Log_message.write('\nreussite')
        Log_message.close()
        return 0
        # une fois qu'il kill le jeu 3 foie et ca marche pas kill une derniere fois et et bloque

    Log_message = open(text_name, "a")
    Log_message.write('\nfermeture apres 3 essaie')
    Log_message.close()
    return 1


def xkill_short():
    os.system("xkill")

