#!/usr/bin/env python3.7
import sys
import threading
import time
import tkinter as tk
import gc
from datetime import datetime
from tkinter import filedialog, simpledialog
from pynput.keyboard import Listener, Key
import pyautogui

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QLabel, QDoubleSpinBox, QCheckBox, QComboBox
from pynput.keyboard import Listener, Controller

from Divers import Class_bot
from Divers import fonction_principal, Fct_script, Fct_Ressource


class App(QWidget):

    def __init__(self):
        super().__init__()

        self.title = 'interface_script'
        self.left = 400
        self.top = 60
        self.width = 760
        self.height = 480
        self.initUI()
        self.listPath = []
        self.zaap = []
        self.nom = ''
        self.dicto_ressource = {}
        self.caverne = {}
        self.list_action = []


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.NameScriptLabel = QLabel('Nom du script: ', self)
        self.NameScriptLabel.setGeometry(60, 20, 120, 20)
        self.NameScript = QTextEdit(self)
        self.NameScript.setReadOnly(False)
        self.NameScript.setGeometry(190, 15, 200, 30)

        self.actionLabel = QLabel('liste d action:', self)
        self.actionLabel.setGeometry(200, 52, 280, 20)
        self.action = QTextEdit(self)
        self.action.setReadOnly(True)
        self.action.setGeometry(120, 75, 300, 230)

        self.Loadbutton = QPushButton('Load script', self)
        self.Loadbutton.setGeometry(10, 75, 90, 30)
        self.Loadbutton.clicked.connect(self.Load_click)

        self.Savebutton = QPushButton('Save script', self)
        self.Savebutton.setGeometry(10, 115, 90, 30)
        self.Savebutton.clicked.connect(self.Save_click)

        self.maps_numLabel = QLabel('liste des ressources:', self)
        self.maps_numLabel.setGeometry(440, 20, 180, 20)
        self.maps_num = QComboBox(self)
        self.maps_num.setGeometry(440, 45, 150, 30)
        self.maps_num.currentIndexChanged.connect(self.change_ressource_map)

        self.ressource = QTextEdit(self)
        self.ressource.setReadOnly(True)
        self.ressource.setGeometry(440, 80, 250, 200)

        self.addRessourceLabel = QLabel('', self)
        self.addRessourceLabel.setGeometry(600, 300, 150, 30)
        self.addRessourceButton = QPushButton('add ressource', self)
        self.addRessourceButton.setGeometry(440, 300, 150, 30)
        self.addRessourceButton.clicked.connect(self.add_ressource)

        self.delRessourceButton = QPushButton('delete ressource', self)
        self.delRessourceButton.setGeometry(440, 340, 150, 30)
        self.delRessourceButton.clicked.connect(self.delete_ressource)

        self.show()

    def Save_click(self):
        root = tk.Tk()
        root.withdraw()
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if len(path) != 0:
            Fct_script.ecrire_script(path, self.nom, self.list_action, self.dicto_ressource, self.zaap, self.caverne)

    def Load_click(self):
        root = tk.Tk()
        root.withdraw()
        path = filedialog.askopenfilename(defaultextension=".txt")
        if len(path) != 0:
            self.listPath.append(path)
            script = Fct_script.lire_path(path)
            self.nom = script[0]
            self.zaap = Fct_script.lire_zaap(script)
            [self.list_action, self.dicto_ressource, self.caverne] = Fct_script.lire_script(script)
            self.maps_num.clear()
            for i in list(self.dicto_ressource.keys()):
                self.maps_num.addItem('{},{}'.format(i[0], i[1]))

            self.action.clear()
            for i in self.list_action:
                self.action.append(i)

            self.NameScript.clear()
            self.NameScript.append(self.nom)

    def change_ressource_map(self):
        map_actuelle = self.maps_num.currentText()
        if map_actuelle == '':
            return
        map = map_actuelle.split(',')
        mapkey = (int(map[0]), int(map[1]))
        ressource_actuelle = self.dicto_ressource[mapkey]
        self.ressource.clear()
        for i in list(ressource_actuelle.keys()):
            self.ressource.append('pos {}, {}, couleur {}, {}, {}'.format(i[0], i[1], ressource_actuelle[i][0], ressource_actuelle[i][1], ressource_actuelle[i][2]))


    def add_ressource(self):
        self.addRessourceLabel.setText('when ready press w')
        self.addRessourceLabel.repaint()
        [x, y, color] = Fct_Ressource.ressource()
        map = tuple(fonction_principal.MAP_POS())
        self.addRessourceLabel.setText('')
        self.addRessourceLabel.repaint()
        pos = (x, y)
        if map in self.dicto_ressource.keys():
            self.dicto_ressource[map][pos] = color
            self.ressource.clear()
            ressource_actuelle = self.dicto_ressource[map]
            for i in list(ressource_actuelle.keys()):
                self.ressource.append('pos {}, {}, couleur {}, {}, {}'.format(i[0], i[1], ressource_actuelle[i][0],
                                                                              ressource_actuelle[i][1],
                                                                              ressource_actuelle[i][2]))
        else:
            ressource_seul = {pos: color}
            self.dicto_ressource[map] = ressource_seul
            self.maps_num.addItem('{},{}'.format(map[0], map[1]))


    def delete_ressource(self):
        map_actuelle = self.maps_num.currentText()
        if map_actuelle == '':
            return
        map = map_actuelle.split(',')
        mapkey = (int(map[0]), int(map[1]))
        answer = simpledialog.askstring('Input', 'what is the position (XX,XX)')
        if answer is not None:
            pos = answer.split(',')
            poskey = (int(pos[0]), int(pos[1]))
            del self.dicto_ressource[mapkey][poskey]
            ressource_actuelle = self.dicto_ressource[mapkey]
            if ressource_actuelle == {}:
                del self.dicto_ressource[mapkey]
                self.maps_num.clear()
                for i in list(self.dicto_ressource.keys()):
                    self.maps_num.addItem('{},{}'.format(i[0], i[1]))
            else:
                self.ressource.clear()
                for i in list(ressource_actuelle.keys()):
                    self.ressource.append('pos {}, {}, couleur {}, {}, {}'.format(i[0], i[1], ressource_actuelle[i][0],
                                                                              ressource_actuelle[i][1],
                                                                              ressource_actuelle[i][2]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
