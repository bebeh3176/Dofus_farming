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

for i in ressource:
    if(i == 'final'):
        break
    info = i[8:-2].split(', ')
    color = int(info[2])

    R = color % 256
    G = (color // 256) % 256
    B = ((color // 256)// 256 % 256)

    print('ressource position, {0}, {1}, couleur, {2}, {3}, {4}'.format(info[0],info[1],R,G,B))

