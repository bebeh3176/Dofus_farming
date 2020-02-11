#!/usr/bin/env python3.7
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QLabel, QDoubleSpinBox
from pynput.keyboard import Listener, Controller
import time
import threading
from Divers import fonction_principal, Fct_script

import tkinter as tk
from tkinter import filedialog


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Bot dofus'
        self.left = 400
        self.top = 60
        self.width = 700
        self.height = 480
        self.dictoZaap = {'Village des Eleveurs':0}
        self.listPath = []
        self.initUI()
        self.Pause = [False]

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        self.Loadbutton = QPushButton('Load script', self)
        self.Loadbutton.setGeometry(20,30,150,30)
        self.Loadbutton.clicked.connect(self.Load_click)

        self.Deletebutton = QPushButton('Delete script', self)
        self.Deletebutton.setGeometry(20,80,150,30)
        self.Deletebutton.clicked.connect(self.Delete_click)

        self.Runbutton = QPushButton('Run script', self)
        self.Runbutton.setGeometry(20,130,150,30)
        self.Runbutton.clicked.connect(self.Run_click)

        self.Pausebutton = QPushButton('Pause script', self)
        self.Pausebutton.setGeometry(20,180,150,30)
        self.Pausebutton.clicked.connect(self.Pause_click)
        self.Pausebutton.setEnabled(False)

        self.Resumebutton = QPushButton('Resume script', self)
        self.Resumebutton.setGeometry(20,230,150,30)
        self.Resumebutton.clicked.connect(self.Resume_click)
        self.Resumebutton.setEnabled(False)


        self.RuntimeLabel = QLabel('Durer du Bot (heures):',self)
        self.RuntimeLabel.setGeometry(20,330,110,30)
        self.Runtime = QDoubleSpinBox(self)
        self.Runtime.setGeometry(135,330,50,30)
        self.Runtime.setDecimals(1)
        self.Runtime.setMaximum(12.0)
        self.Runtime.setMinimum(0.1)
        self.Runtime.setValue(1.5)


        self.ZaapLabel = QLabel('Zaap a mettre en favorie:',self)
        self.ZaapLabel.setGeometry(420,20,150,20)
        self.Zaap = QTextEdit(self)
        self.Zaap.setReadOnly(True)
        self.Zaap.setGeometry(420,45,200,230)

        self.ScriptLabel = QLabel('Script choisie:',self)
        self.ScriptLabel.setGeometry(200,20,150,20)
        self.Script = QTextEdit(self)
        self.Script.setReadOnly(True)
        self.Script.setGeometry(200,45,200,230)

        self.show()

    def run_scripts(self):
        listener = Listener(on_press = self.Faire_Pause)
        listener.start()
        test = listener.running
        duration = int(float(self.Runtime.value()) * 3600)
        start_time = time.time()

        time_start_log = (time.time() / 60) % 10000
        text_name = 'LOG/{}.txt'.format(time_start_log)
        Log_message = open(text_name, "w")
        Log_message.write('Le bot a ete lance a {}'.format(time_start_log))
        Log_message.close()
        while True:
            for i in self.listPath:
                script = Fct_script.lire_path(i)
                action, Dicto_ressource, Dicto_Caverne = Fct_script.lire_script(script)
                fonction_principal.Banque(self.dictoZaap,pause=self.Pause)
                Fct_script.run_action(action, Dicto_ressource, self.dictoZaap, Dicto_Caverne, self.Pause)
                if start_time + duration < time.time():
                    break
            else:
                continue
            break
        fonction_principal.kill_dofus(restart=False,commentaire='le script a ete execute sans erreur')
        listener.stop()
        self.Resumebutton.setEnabled(False)
        self.Pausebutton.setEnabled(False)
        self.Runbutton.setEnabled(True)
        self.Deletebutton.setEnabled(True)
        self.Loadbutton.setEnabled(True)
        self.Runtime.setEnabled(True)


    def Resume_click(self):
        keyboard = Controller()
        keyboard.press("r")
        keyboard.release("r")
        self.Resumebutton.setEnabled(False)
        self.Pausebutton.setEnabled(True)
        pass

    def Pause_click(self):
        self.Pause[0] = True
        self.Resumebutton.setEnabled(True)
        self.Pausebutton.setEnabled(False)

    #@pyqtSlot()
    def Load_click(self):
        try:
            root = tk.Tk()
            root.withdraw()
            path = filedialog.askopenfilename()
            self.listPath.append(path)
            script = Fct_script.lire_path(path)
        except:
            return
        nom = Fct_script.lire_nom(script)
        self.Script.append(nom)
        print(self.dictoZaap.keys())
        listZaap = Fct_script.lire_zaap(script, list(self.dictoZaap.keys()))
        self.dictoZaap = Fct_script.list2dicto_Zaap(listZaap)
        self.Zaap.clear()
        for i in list(self.dictoZaap.keys()):
            self.Zaap.append(i)

    def Faire_Pause(self, key):
        try:
            if (key.char == 'p'):
                self.Pause[0] = True
                self.Resumebutton.setEnabled(True)
                self.Pausebutton.setEnabled(False)
                return
            if (key.char == 'r'):
                self.Pause[0] = False
                self.Resumebutton.setEnabled(False)
                self.Pausebutton.setEnabled(True)
                return
        except:
            return

    def Run_click(self):
        self.thread_bot = threading.Thread(target=self.run_scripts)
        self.thread_bot.daemon = True
        self.thread_bot.start()
        self.Pausebutton.setEnabled(True)
        self.Runbutton.setEnabled(False)
        self.Deletebutton.setEnabled(False)
        self.Loadbutton.setEnabled(False)
        self.Runtime.setEnabled(False)

    def Delete_click(self):
        self.dictoZaap = {}
        self.listPath = []
        self.Zaap.clear()
        self.Script.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
