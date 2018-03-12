#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Interface CORE

from PyQt5 import QtWidgets
from . import show
from . import vars
import sys


def init_application(self):
    # Définition Constantes
    vars.initVar(self)    
    # Gestion affichage 
    show.init_app_start(self)
    # version Arma3 Windows
    if vars.OSName()=="windows":
        self.label_info_arma3_version.setText(".".join ([str (i) for i in show.get_version_number (self.var_Arma3Path+"/arma3.exe")]))
    else:
        self.label_info_arma3_version.setText("Linux version")
    

def info_dialog_windows(self, titre, message, iconMessagebox):
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
    

