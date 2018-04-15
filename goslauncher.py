#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""GOS LAUNCHER Python version.

This app is a Python Version of GOS LAuncher C# program.
Initially developped for Clan GOS by ToF and ELDoktor.

Example:
        $ python goslauncher.py

Attributes:


Todo:


"""

import sys
from PyQt5 import QtWidgets, QtCore


if __name__ == "__main__":

    APP = QtWidgets.QApplication(sys.argv)
    # récupère arguments
    updater = False
    for arg in sys.argv:
        if arg.lower() == "-updater" or arg == "-u":
            updater = True

    if updater:
        from updater import Mw_updater
        MAINFORM = Mw_updater()
        MAINFORM.show()
        sys.exit(APP.exec_())
    else:
        from principale import Fenetre_Principale
        TRANSLATOR = QtCore.QTranslator()
        TRANSLATOR.load("languages/principale_fr.qm")
        APP.installTranslator(TRANSLATOR)
        MAINFORM = Fenetre_Principale()
        MAINFORM.show()
        sys.exit(APP.exec_())
