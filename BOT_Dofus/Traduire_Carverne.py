import math
import numpy as np
from Divers import Fct_script
import tkinter as tk
from tkinter import filedialog

def Load_click():
    try:
        root = tk.Tk()
        root.withdraw()
        path = filedialog.askopenfilename()
        script = Fct_script.lire_path(path)
    except:
        return
    return path


path = Load_click()
ressource = Fct_script.lire_path(path)
conteur = 0
for i in ressource:
    if(i == 'final'):
        break
    info = i.split('= ')
    color = int(info[1])
    if conteur == 0:
        posx = color
    if conteur == 1:
        posy = color
    if conteur == 2:
        colx = color
    if conteur == 3:
        coly = color
    if conteur == 4:
        R = color % 256
        G = (color // 256) % 256
        B = ((color // 256)// 256 % 256)
        print('position, {5}, {6}, 10, 5, couleur, {2}, {3}, {4}, pos, {0}, {1}'.format(colx,coly,R,G,B,posx,posy))
    conteur = conteur + 1
    if(conteur == 5):
        conteur = 0
