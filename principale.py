# -*- coding: utf-8 -*-

"""
Module implementing Fenetre_Principale.
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
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
        goslaunchera3.core.init_application(self)
    
    @pyqtSlot()
    def on_pushButton_Mods_A3_SelectAll_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.selection_tous_mods(self,self.listWidget_Arma3)
    
    @pyqtSlot()
    def on_pushButton_Mods_A3_InvSelect_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.inv_selection_tous_mods(self,self.listWidget_Arma3)
    
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
        goslaunchera3.action.inv_selection_tous_mods(self,self.listWidget_Template)
    
    @pyqtSlot()
    def on_pushButton_Mods_Template_SelectAll_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.selection_tous_mods(self,self.listWidget_Template)
    
    @pyqtSlot()
    def on_pushButton_Mods_Islands_SelectAll_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.selection_tous_mods(self,self.listWidget_Islands)
    
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
        goslaunchera3.action.inv_selection_tous_mods(self,self.listWidget_Islands)
    
    @pyqtSlot()
    def on_pushButton_LaunchArma3_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.launch_arma3(self)
    
    @pyqtSlot()
    def on_pushButton_Mods_Client_SelectAll_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.selection_tous_mods(self,self.listWidget_Client)
    
    @pyqtSlot()
    def on_pushButton_Mods_Client_InvSelect_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.inv_selection_tous_mods(self,self.listWidget_Client)
    
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
        goslaunchera3.action.selection_tous_mods(self,self.listWidget_Framework)
    
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
        goslaunchera3.action.inv_selection_tous_mods(self,self.listWidget_Framework)
    
    @pyqtSlot()
    def on_pushButton_Mods_Materiel_SelectAll_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.selection_tous_mods(self,self.listWidget_Materiel)
    
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
        goslaunchera3.action.inv_selection_tous_mods(self,self.listWidget_Materiel)
    
    @pyqtSlot()
    def on_pushButton_Mods_Test_SelectAll_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.selection_tous_mods(self,self.listWidget_Test)

    
    @pyqtSlot()
    def on_pushButton_Mods_Test_InvSelect_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.inv_selection_tous_mods(self,self.listWidget_Test)

    
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
        goslaunchera3.action.inv_selection_tous_mods(self,self.listWidget_Units)

    
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
        goslaunchera3.action.selection_tous_mods(self,self.listWidget_Units)
    
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
    def on_toolButton_saveProfil_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.initPriorityTabWidget(self)
        self.var_Profil.SaveProfil()
    
    @pyqtSlot(str)
    def on_comboBox_ChoixProfil_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        try:
            self.var_Profil.RestoreProfil()
        except:
            print()
            
            
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
        goslaunchera3.action.inv_selection_tous_mods(self, self.listWidget_Workshop)
    
    @pyqtSlot()
    def on_pushButton_Mods_Workshop_SelectAll_clicked(self):
        """
        Slot documentation goes here.
        """
        goslaunchera3.action.selection_tous_mods(self,self.listWidget_Workshop)
    
    @pyqtSlot()
    def on_pushButton_priorityTop_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        while self.listWidget_priority.currentRow()>0:
            textSplit=self.listWidget_priority.currentItem().text()
            self.listWidget_priority.currentItem().setText(self.listWidget_priority.item(self.listWidget_priority.currentRow()-1).text())
            self.listWidget_priority.item(self.listWidget_priority.currentRow()-1).setText(textSplit)
            self.listWidget_priority.setCurrentRow(self.listWidget_priority.currentRow()-1)
    
    @pyqtSlot()
    def on_pushButton_priorityPlus_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.listWidget_priority.currentRow()>0:
            textSplit=self.listWidget_priority.currentItem().text()
            self.listWidget_priority.currentItem().setText(self.listWidget_priority.item(self.listWidget_priority.currentRow()-1).text())
            self.listWidget_priority.item(self.listWidget_priority.currentRow()-1).setText(textSplit)
            self.listWidget_priority.setCurrentRow(self.listWidget_priority.currentRow()-1)
        
        
        
    @pyqtSlot()
    def on_pushButton_priorityMinus_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.listWidget_priority.currentRow()<self.listWidget_priority.count()-1  and self.listWidget_priority.currentRow() >-1:
            textSplit=self.listWidget_priority.currentItem().text()
            self.listWidget_priority.currentItem().setText(self.listWidget_priority.item(self.listWidget_priority.currentRow()+1).text())
            self.listWidget_priority.item(self.listWidget_priority.currentRow()+1).setText(textSplit)
            self.listWidget_priority.setCurrentRow(self.listWidget_priority.currentRow()+1)
        
    
    @pyqtSlot()
    def on_pushButton_priorityBottom_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        while self.listWidget_priority.currentRow()<self.listWidget_priority.count()-1 and self.listWidget_priority.currentRow() >-1:
            textSplit=self.listWidget_priority.currentItem().text()
            self.listWidget_priority.currentItem().setText(self.listWidget_priority.item(self.listWidget_priority.currentRow()+1).text())
            self.listWidget_priority.item(self.listWidget_priority.currentRow()+1).setText(textSplit)
            self.listWidget_priority.setCurrentRow(self.listWidget_priority.currentRow()+1)
    
    @pyqtSlot(int)
    def on_checkBox_windowedMode_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        self.lineEdit_WindowedModeX.setEnabled((p0 == 2))
        self.lineEdit_WindowedModeY.setEnabled((p0 == 2))
        
    
    @pyqtSlot(int)
    def on_tabWidget_currentChanged(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type int
        """
        if index == 2:
           goslaunchera3.action.initPriorityTabWidget(self)
    
    @pyqtSlot(int)
    def on_horizontalSlider_procNumber_valueChanged(self, value):
        """
        Slot documentation goes here.
        
        @param value DESCRIPTION
        @type int
        """
        self.lineEdit_procNumber.setText(str(value))
        
    
    @pyqtSlot(int)
    def on_horizontalSlider_maxMemory_valueChanged(self, value):
        """
        Slot documentation goes here.
        
        @param value DESCRIPTION
        @type int
        """
        self.lineEdit_maxMemory.setText(str(value))
    
    @pyqtSlot(int)
    def on_horizontalSlider_maxVIDEOMemory_valueChanged(self, value):
        """
        Slot documentation goes here.
        
        @param value DESCRIPTION
        @type int
        """
        self.lineEdit_maxVIDEOMemory.setText(str(value))
    
    @pyqtSlot(int)
    def on_checkBox_maxMemory_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        self.horizontalSlider_maxMemory.setEnabled((p0 == 2))
        self.lineEdit_maxMemory.setEnabled((p0 == 2))
        self.lineEdit_maxMemory.setText(str(self.horizontalSlider_maxMemory.value()))
    
    @pyqtSlot(int)
    def on_checkBox_procNumber_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        self.horizontalSlider_procNumber.setEnabled((p0 == 2))
        self.lineEdit_procNumber.setEnabled((p0 == 2))
        self.lineEdit_procNumber.setText(str(self.horizontalSlider_procNumber.value()))
    
    @pyqtSlot(int)
    def on_checkBox_maxVideoMemory_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        self.horizontalSlider_maxVIDEOMemory.setEnabled((p0 == 2))
        self.lineEdit_maxVIDEOMemory.setEnabled((p0 == 2))
        self.lineEdit_maxVIDEOMemory.setText(str(self.horizontalSlider_maxVIDEOMemory.value()))
    

    
    @pyqtSlot(int)
    def on_checkBox_customCommand_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        self.lineEdit_customCommand.setEnabled((p0 == 2))
    
    @pyqtSlot()
    def on_pushButton_AddProfil_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.var_Profil.AddProfil(self.lineEdit_AddProfilName.text())
    
    @pyqtSlot(int)
    def on_checkBox_extraThreads_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        self.comboBox_extraThreads.setEnabled((p0 == 2))
        self.label_GFX_geometryLoading.setEnabled((p0 == 2))
        self.label_GFX_textureLoading.setEnabled((p0 == 2))
        self.label_GFX_fileOperations.setEnabled((p0 == 2))
        self.label_geometryLoading.setEnabled((p0 == 2))
        self.label_textureLoading.setEnabled((p0 == 2))
        self.label_fileOperations.setEnabled((p0 == 2))
    
    @pyqtSlot(str)
    def on_comboBox_extraThreads_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        if p0 == "0":
            self.label_GFX_geometryLoading.setPixmap(QPixmap("gfx/supprimer.png"))
            self.label_GFX_textureLoading.setPixmap(QPixmap("gfx/supprimer.png"))
            self.label_GFX_fileOperations.setPixmap(QPixmap("gfx/supprimer.png"))
        if p0 == "1":
            self.label_GFX_geometryLoading.setPixmap(QPixmap("gfx/supprimer.png"))
            self.label_GFX_textureLoading.setPixmap(QPixmap("gfx/supprimer.png"))
            self.label_GFX_fileOperations.setPixmap(QPixmap("gfx/valide.png"))
        if p0 == "3":
            self.label_GFX_geometryLoading.setPixmap(QPixmap("gfx/supprimer.png"))
            self.label_GFX_textureLoading.setPixmap(QPixmap("gfx/valide.png"))
            self.label_GFX_fileOperations.setPixmap(QPixmap("gfx/valide.png"))
        if p0 == "5":
            self.label_GFX_geometryLoading.setPixmap(QPixmap("gfx/valide.png"))
            self.label_GFX_textureLoading.setPixmap(QPixmap("gfx/supprimer.png"))
            self.label_GFX_fileOperations.setPixmap(QPixmap("gfx/valide.png"))
        if p0 == "7":
            self.label_GFX_geometryLoading.setPixmap(QPixmap("gfx/valide.png"))
            self.label_GFX_textureLoading.setPixmap(QPixmap("gfx/valide.png"))
            self.label_GFX_fileOperations.setPixmap(QPixmap("gfx/valide.png"))
    
    @pyqtSlot()
    def on_pushButton_synchro_template_launch_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
