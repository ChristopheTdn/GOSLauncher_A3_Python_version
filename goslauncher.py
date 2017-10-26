 #! /usr/bin/python3
# -*- coding: utf-8 -*-
"""GOS LAUNCHER Python version.

This app is a Python Version of GOS LAuncher C# program.
Initially developpe for Clan GOS by ToF and ELDoktor.

Example:
        $ python goslauncher.py

Attributes:


Todo:
    

"""

import sys
from PyQt5 import QtWidgets, QtCore
from principale import Fenetre_Principale

if __name__ == "__main__":
    APP = QtWidgets.QApplication(sys.argv)
    TRANSLATOR = QtCore.QTranslator()
    TRANSLATOR.load("languages/principale_en.qm")
    APP.installTranslator(TRANSLATOR)
    MAINFORM = Fenetre_Principale()
    MAINFORM.show()
    sys.exit(APP.exec_())
