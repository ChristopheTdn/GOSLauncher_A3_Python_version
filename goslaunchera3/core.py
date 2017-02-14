#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Interface CORE

from PyQt5 import QtWidgets
from . import show
from . import vars

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
    
################################################################

if __name__ == "__main__":

    # execute when run directly, but not when called as a module.
    # therefore this section allows for testing this module!

    #print "running directly, not as a module!"

    sys.exit() 
    

