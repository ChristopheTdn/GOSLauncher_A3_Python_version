#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Interface CORE
from PyQt5 import QtWidgets
from . import show
from . import vars
import pickle

def initApplication(self):
    # Définition Constantes
    vars.initVar(self)
    # Gestion affichage
    show.initOuverture(self)

def infoDialogWindows(self, titre, message, iconMessagebox):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(iconMessagebox)
    msg.setText(message)
    msg.setWindowTitle(titre)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok) 
    msg.exec_()
    exit()

def changeLangage(self, langue):
    self.close()
    exit()
    
def serialize(self):
    fichier= open("save.mydata", "wb")
    pickle.dump(self.checkBox_noCB, fichier) 
    
def deserialize(self):
    fichier= open("save.mydata", "rb")
    self.checkBox_noCB=pickle.load(fichier)
