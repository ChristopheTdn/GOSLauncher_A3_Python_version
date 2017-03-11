# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
from principale import Fenetre_Principale
import sys
# VARIABLES GLOBALES
global app, app, trans


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    translator = QtCore.QTranslator()
    translator.load("languages/principale_en.qm")
    app.installTranslator(translator)
    mainForm = Fenetre_Principale()
    mainForm.show()
    sys.exit(app.exec_())
