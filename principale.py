# -*- coding: utf-8 -*-

"""
Module implementing Fenetre_Principale.
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from Ui_principale import Ui_Fenetre_Principale
import goslaunchera3

class Fenetre_Principale(QMainWindow, Ui_Fenetre_Principale):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Fenetre_Principale, self).__init__(parent)
        self.setupUi(self)
        goslaunchera3.core.initApplication(self)
    
    @pyqtSlot()
    def on_pushButton_Mods_A3_SelectAll_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.selectionTousMods(self,self.listWidget_Arma3)
    
    @pyqtSlot()
    def on_pushButton_Mods_A3_InvSelect_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.invSelectionTousMods(self,self.listWidget_Arma3)
    
    @pyqtSlot()
    def on_pushButton_Mods_A3_RefreshList_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_Mods_Template_RefreshList_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_Mods_Template_InvSelect_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.invSelectionTousMods(self,self.listWidget_Template)
    
    @pyqtSlot()
    def on_pushButton_Mods_Template_SelectAll_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.selectionTousMods(self,self.listWidget_Template)
    
    @pyqtSlot()
    def on_pushButton_Mods_Islands_SelectAll_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.selectionTousMods(self,self.listWidget_Islands)
    
    @pyqtSlot()
    def on_pushButton_Mods_Islands_RefreshList_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_Mods_Islands_InvSelect_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.invSelectionTousMods(self,self.listWidget_Islands)
    
    @pyqtSlot()
    def on_pushButton_LaunchArma3_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.launchArma3(self)
    
    @pyqtSlot()
    def on_pushButton_Mods_Client_SelectAll_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.selectionTousMods(self,self.listWidget_Client)
    
    @pyqtSlot()
    def on_pushButton_Mods_Client_InvSelect_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.invSelectionTousMods(self,self.listWidget_Client)
    
    @pyqtSlot()
    def on_pushButton_Mods_Client_RefreshList_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_Mods_Framework_SelectAll_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.selectionTousMods(self,self.listWidget_Framework)
    
    @pyqtSlot()
    def on_pushButton_Mods_Framework_RefreshList_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_Mods_Framework_InvSelect_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        goslaunchera3.action.invSelectionTousMods(self,self.listWidget_Framework)
    
    @pyqtSlot()
    def on_pushButton_Mods_Materiel_SelectAll_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.selectionTousMods(self,self.listWidget_Materiel)
    
    @pyqtSlot()
    def on_pushButton_Mods_Materiel_RefreshList_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_Mods_Materiel_InvSelect_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.invSelectionTousMods(self,self.listWidget_Materiel)
    
    @pyqtSlot()
    def on_pushButton_Mods_Test_SelectAll_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.selectionTousMods(self,self.listWidget_Test)

    
    @pyqtSlot()
    def on_pushButton_Mods_Test_InvSelect_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.invSelectionTousMods(self,self.listWidget_Test)

    
    @pyqtSlot()
    def on_pushButton_Mods_Test_RefreshList_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_Mods_Units_InvSelect_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.invSelectionTousMods(self,self.listWidget_Units)

    
    @pyqtSlot()
    def on_pushButton_Mods_Units_RefreshList_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_Mods_Units_SelectAll_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.selectionTousMods(self,self.listWidget_Units)
    
    @pyqtSlot(str)
    def on_comboBox_ChoixApparence_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        goslaunchera3.show.LogoGosSkin(self, p0)
    
    @pyqtSlot()
    def on_radioButton_language_French_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action. optionModifLangue(self, "fr")
    
    @pyqtSlot()
    def on_radioButton_language_English_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action. optionModifLangue(self, "en")
    
    @pyqtSlot()
    def on_checkBox_customCommand_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action. optionCustomCommand(self)
    
    @pyqtSlot()
    def on_toolButton_saveProfil_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.saveProfil(self)
    
    @pyqtSlot(str)
    def on_comboBox_ChoixProfil_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        goslaunchera3.action.restoreProfil(self)
    
    @pyqtSlot()
    def on_pushButton_Mods_Workshop_RefreshList_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_Mods_Workshop_InvSelect_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.invSelectionTousMods(self,self.listWidget_Workshop)
    
    @pyqtSlot()
    def on_pushButton_Mods_Workshop_SelectAll_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.selectionTousMods(self,self.listWidget_Workshop)
