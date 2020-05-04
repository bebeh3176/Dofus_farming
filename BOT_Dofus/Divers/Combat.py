import pyautogui
import cv2
import numpy as np
import time
from Divers import Divers as divers
import random
import copy

def combat_fini():
    template = cv2.imread('Picture/fermer_combat.png', 0)
    template_BW = cv2.threshold(template, 100, 255, cv2.THRESH_BINARY)[1]
    image = pyautogui.screenshot(region=(571, 416, 90, 230))
    # image.show()
    img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_BW = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)[1]
    res2 = cv2.matchTemplate(img_BW, template_BW, cv2.TM_SQDIFF_NORMED)
    threshold = 0.1

    # Store the coordinates of matched area in a numpy array
    if np.any(res2 <= threshold):
        position = np.where(res2 <= threshold)
        result = (1, position[1][0]+571, position[0][0]+416)
    else:
        result = (0, 20, 20)
    return result


def click_combat_fini(pause=[False]):
    bool_fini = combat_fini()
    if bool_fini[0] == 1:
        divers.move_mouse(bool_fini[1], bool_fini[2], 60, 10, alea=False, pause=pause)


def findperso(color1, color2, color3, dist=10, tol=4):
    now = pyautogui.screenshot
    pos_nope = []
    while True:
        pos1 = divers.findcolor(color1, sauf=pos_nope, tol=tol)
        # print(pos1)
        # print(pos_nope)
        if pos1:
            if divers.findcolor(color2, initial=(pos1[0]-dist, pos1[1]-dist), final=(pos1[0]+dist, pos1[1]+dist), tol=tol):
                return pos1
            if divers.findcolor(color3, initial=(pos1[0]-dist, pos1[1]-dist), final=(pos1[0]+dist, pos1[1]+dist), tol=tol):
                return pos1
            pos_nope.append((pos1[0]-dist, pos1[1]-dist, pos1[0]+dist, pos1[1]+dist))
        else:
            break
    pos_nope = []
    while True:
        pos1 = divers.findcolor(color2, sauf=pos_nope, tol=tol)
        if pos1:
            if divers.findcolor(color3, initial=(pos1[0]-dist, pos1[1]-dist), final=(pos1[0]+dist, pos1[1]+dist), tol=tol):
                return pos1
            pos_nope.append((pos1[0]-dist, pos1[1]-dist, pos1[0]+dist, pos1[1]+dist))
        else:
            break
    return None


def obstacle(origine):
    dX = 2
    dY = 2
    color = (34, 51, 153)
    tol = 2

    color = np.uint8([[[color[0], color[1], color[2] ]]])
    hsv_color = cv2.cvtColor(color, cv2.COLOR_RGB2HSV)

    lower_limit = np.array([hsv_color[0][0][0]-tol, hsv_color[0][0][1]-tol, hsv_color[0][0][2]-tol])
    upper_limit = np.array([hsv_color[0][0][0]+tol, hsv_color[0][0][1]+tol, hsv_color[0][0][2]+tol])

    frame = pyautogui.screenshot()
    hsv = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_limit, upper_limit)

    height, width = mask.shape
    U = (28.2, 14)
    V = (28.2, -14)
    porte = 11
    obstacle_dico = {}
    for i in range(-porte, porte+1):
        porte2 = porte - abs(i)
        for j in range(-porte2, porte2 + 1):
            actuel = (np.int64(origine[0] + i * U[0] + j*V[0]), np.int64(origine[1] + i * U[1] + j*V[1]))
            zone_chercher = np.zeros((height, width, 1), np.uint8)
            initial = (actuel[0] - dX, actuel[1] - dY)
            final = (actuel[0] + dX, actuel[1] + dY)
            # print(initial,final)
            cv2.rectangle(zone_chercher, initial, final, (255), -1)
            res = cv2.bitwise_and(zone_chercher, zone_chercher, mask=mask)
            result1, result2 = np.where(res == 255)
            if(len(result1)):
                obstacle_dico[(i, j)] = True
            # else:
            #     obstacle_dico[(i,j)] = False
    return obstacle_dico
    # frame2 = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
    # for i in obstacle_dico.keys():
    #     if obstacle_dico[i]:
    #         actuel = (np.int64(origine[0] + i[0] * U[0] + i[1]*V[0]), np.int64(origine[1] + i[0] * U[1] + i[1]*V[1]))
    #         cv2.rectangle(frame2,(actuel[0] - 2,actuel[1] - 2),(actuel[0] + 2,actuel[1] + 2),(255,255,255),-1)
    #
    # cv2.imshow('frame',frame2)
    # k = cv2.waitKey()


def findpath(obstacleexterne, pos, but):
    try:
        obstacle_dico = copy.deepcopy(obstacleexterne)
        obstacle_dico[but] = True
        libre = list(obstacle_dico.keys())
        if pos in libre:
            libre.remove(pos)
        list_pos_actuelle = [pos]
        list_pos_nouvelle = []
        dico_pos = {pos: 0}
        accessible = []
        for i in range(1, 31):
            for j in list_pos_actuelle:
                for k in voisin(j):
                    if k in libre:
                        libre.remove(k)
                        dico_pos[k] = i
                        list_pos_nouvelle.append(k)
                        accessible.append(k)
            if not (but in libre):
                break
            list_pos_actuelle = list_pos_nouvelle
            list_pos_nouvelle = []

        pos_actuelle = but
        path = []
        if not (but in accessible):
            dist_min = 1000
            for i in accessible:
                if (abs(but[0]-i[0]) + abs(but[1]-i[1])) < dist_min:
                    dist_min = (abs(but[0]-i[0]) + abs(but[1]-i[1]))
                    pos_actuelle = i

        for i in range(dico_pos[pos_actuelle]-1, 0, -1):
            for j in voisin(pos_actuelle):
                try:
                    if dico_pos[j] == i:
                        path.append(j)
                        pos_actuelle = j
                        break
                except:
                    continue
        return path
    except:
        path = []


def voisin(pos):
    return [(pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0], pos[1]-1)]

def ligne_de_vue(obstacle, pos,but):
    try:
        obstacle_dico = copy.deepcopy(obstacle)
        obstacle_dico[pos] = True
        obstacle_dico[but] = True
        dist = abs(but[1]-pos[1]) + abs(but[0]-pos[0])
        if (but[0]-pos[0]) == 0:
            dX = np.arange(0, but[1]-pos[1], ((but[1]-pos[1])/dist))
            pente = (but[0]-pos[0])/(but[1]-pos[1])
            X = np.arange(pos[1], but[1], ((but[1]-pos[1])/dist))
        else:
            dX = np.arange(0, but[0]-pos[0], ((but[0]-pos[0])/dist))
            pente = (but[1]-pos[1])/(but[0]-pos[0])
            X = np.arange(pos[0], but[0], ((but[0]-pos[0])/dist))
        Y = []
        for i in dX:
            Y.append(pente*i + pos[1])

        # print(X)
        # print(Y)
        for i in range(len(X)):
            try:
                if (but[0]-pos[0]) == 0:
                    obstacle_dico[(round(Y[i]), round(X[i]))]
                else:
                    obstacle_dico[(round(X[i]), round(Y[i]))]
            except:
                return False
        return True
    except:
        return False


def pos_abs_2_rel(pos, origine):
    # U = (36.3, 18.1)
    # V = (36.3,-18.1)
    dX = 28.2
    dY = 14

    X = round((pos[0] - origine[0])/dX)
    Y = round((pos[1] - origine[1])/dY)

    a = (X + Y)/2
    b = X - a
    return (a,b)

def pos_rel_2_abs(pos, origine):
    U = (28.2, 14)
    V = (28.2, -14)
    pos_abs = (np.int64(origine[0] + pos[0] * U[0] + pos[1] * V[0]), np.int64(origine[1] + pos[0] * U[1] + pos[1] * V[1]))
    return pos_abs

def modeTacticCreature(pause= [False]):
    if(divers.findcolor((173, 173, 173),(872, 686),(879, 693))):
        divers.move_mouse(872, 686,6,7, vitesse=1.5, pause= pause)
        time.sleep(0.8 + random.random() * 0.5)

    if(divers.findcolor((173, 173, 173),(891, 686),(897, 693))):
        divers.move_mouse(891,686,6,7, vitesse=1.5, pause= pause)
        time.sleep(0.8 + random.random() * 0.5)
    return

def combat(option, pause= [False]):
    try:
        ColorNextTurn = (213, 243, 0)
        #cra = [(253, 190, 45),(216, 138, 22),(119, 74, 2)]#Couleur Enutrof
        cra = [(253, 57, 36), (196, 19, 0), (101, 11, 1)]#Couleur Cra
        creature = [(77, 77, 93), (46, 54, 61), (126, 126, 142)]
        Sort_Sans_Vue = (595, 667)
        Sort_Avec_Vue = (621, 667)
        PO_Sort = option.po
        pm = option.pm

        pos_ennemi = (0, 0)
        obst = {}
        if divers.findcolor(ColorNextTurn, (882, 646), (949, 669)):
            bool_fini = (1, 570, 433)
            modeTacticCreature()
            ColorEndFight = (191, 230, 0)
            pos_perso = findperso(cra[0], cra[1], cra[2])
            if (pos_perso == None):
                pos_perso = findperso(cra[0], cra[1], cra[2])
            origine = (pos_perso[0]+2, pos_perso[1]+15)

            while(True):
                modeTacticCreature()
                #lance le combat au premier tour et ensuite passe son tour
                for i in range(0, 20):
                    time.sleep(0.3)
                    if divers.findcolor(ColorNextTurn, (882, 646), (949, 669)):
                        break
                    if combat_fini()[0] == 1:
                        i = 19
                        bool_fini = combat_fini()
                        break
                    if ((i+1) % 10) == 0:
                        divers.move_mouse(262, 694, 100, 4, alea=False, pause=pause)
                if i == 19:
                    break

                divers.move_mouse(882, 646, 65, 20, alea=False, pause=pause)
                divers.move_mouse(1083, 388, 150, 160, alea=False, pause=pause)

                #attend son tour de jeu
                for i in range(0, 50):
                    time.sleep(0.3)
                    if divers.findcolor(ColorNextTurn, (882, 646), (949, 669)):
                        break
                    if combat_fini()[0] == 1:
                        i = 49
                        bool_fini = combat_fini()
                        break
                    if ((i + 1) % 15) == 0:
                        divers.move_mouse(262, 694, 100, 4, alea=False, pause=pause)
                if i == 49:
                    break

                #Click sort sans ligne de vue
                bool_sort = False
                if not(pos_ennemi in list(obst.keys())):
                    bool_sort = True
                    divers.move_mouse(Sort_Sans_Vue[0], Sort_Sans_Vue[1], 13, 14, vitesse=2, alea=False, pause=pause)
                    divers.move_mouse(72, 146, 130, 450, Click=0, vitesse=3, alea=False, pause=pause)
                    obst = obstacle(origine)
                    # divers.move_mouse(70, 475, 100, 230, vitesse = 2, pause= pause)

                pos_perso = findperso(cra[0], cra[1], cra[2])
                if pos_perso == None:
                    pos_perso = findperso(cra[0], cra[1], cra[2])

                pos_ennemi = findperso(creature[0], creature[1], creature[2])
                if pos_ennemi == None:
                    pos_ennemi = findperso(creature[0], creature[1], creature[2])
                    if pos_ennemi == None:
                        break
                pos_perso = (pos_perso[0]+2, pos_perso[1] + 19)
                pos_ennemi = (pos_ennemi[0]+2, pos_ennemi[1] + 19)
                pos_perso = pos_abs_2_rel(pos_perso, origine)
                pos_ennemi = pos_abs_2_rel(pos_ennemi, origine)

                dist = abs(pos_perso[0]-pos_ennemi[0]) + abs(pos_perso[1]-pos_ennemi[1])
                # if too far, get closer
                if dist > PO_Sort:
                    # enleve click sort pour bouger
                    if bool_sort:
                        bool_sort = False
                        divers.move_mouse(72, 146, 130, 450, vitesse=2, pause= pause)
                    path = findpath(obst, pos_perso, pos_ennemi)
                    if len(path) < pm:
                        pm = len(path)
                    Go_to = pos_rel_2_abs(path[len(path)-pm], origine)
                    divers.move_mouse(Go_to[0]-6, Go_to[1]-4, 6, 6, vitesse=2, pause=pause)
                    pos_perso = path[len(path)-5]
                    dist = abs(pos_perso[0]-pos_ennemi[0]) + abs(pos_perso[1]-pos_ennemi[1])

                if dist <= PO_Sort:
                    if ligne_de_vue(obst, pos_perso, pos_ennemi):
                        Go_to = pos_rel_2_abs(pos_ennemi, origine)

                        divers.move_mouse(Sort_Avec_Vue[0], Sort_Avec_Vue[1], 13, 14, alea=False, vitesse=2, pause=pause)
                        divers.move_mouse(Go_to[0]-6, Go_to[1]-4, 9, 6, alea=False, vitesse=2, pause=pause)

                        time.sleep(0.3 + random.random() * 0.3)
                        if combat_fini()[0] == 1:
                            bool_fini = combat_fini()
                            break

                        divers.move_mouse(Sort_Avec_Vue[0], Sort_Avec_Vue[1], 13, 14, alea=False, vitesse=2, pause=pause)
                        if combat_fini()[0] == 1:
                            bool_fini = combat_fini()
                            break
                        divers.move_mouse(Go_to[0]-6, Go_to[1]-4, 9, 6, vitesse=2, pause= pause)
                        # Sort à ligne de vue
                        # 2e sort à ligne de vue
                    else:
                        Go_to = pos_rel_2_abs(pos_ennemi,origine)
                        if (not(bool_sort)):
                            divers.move_mouse(Sort_Sans_Vue[0], Sort_Sans_Vue[1], 13, 14,alea=False, vitesse=2, pause= pause)
                        divers.move_mouse(Go_to[0]-6, Go_to[1]-4, 9, 6, alea=False, vitesse=2, pause=pause)

                        time.sleep(0.3 + random.random() * 0.3)
                        if combat_fini()[0] == 1:
                            bool_fini = combat_fini()
                            break

                        divers.move_mouse(Sort_Sans_Vue[0], Sort_Sans_Vue[1], 13, 14, alea=False, vitesse=2, pause=pause)
                        if combat_fini()[0] == 1:
                            bool_fini = combat_fini()
                            break
                        divers.move_mouse(Go_to[0]-6, Go_to[1]-4, 9, 6, vitesse=2, pause=pause)

            time.sleep(0.3 + random.random() * 0.3)
            divers.move_mouse(bool_fini[1], bool_fini[2], 60, 10, alea=False, pause=pause)
    except:
        return

