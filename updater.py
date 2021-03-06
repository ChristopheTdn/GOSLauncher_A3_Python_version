# -*- coding: utf-8 -*-

"""
Module implementing Mw_updater.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_updater import Ui_MainWindow
import gos_updater


class Mw_updater(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Mw_updater, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_ok_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        gos_updater.core.init_maj_process(self, "http://www.clan-gign.net/goslaunchera3py/goslauncher.zip", "tmp", "goslauncher.zip")
