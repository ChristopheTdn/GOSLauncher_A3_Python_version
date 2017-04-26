#! /usr/bin/python3
# -*- coding: utf-8 -*-
import os
import inspect
from distutils.util import strtobool
from PyQt5.QtCore import QSettings
from PyQt5 import QtWidgets


class Profil:
    def __init__(self, Ui,  directory):
        #Attributs
        self.Name = "Defaut"
        self.Ui = Ui
        self.ProfilDir = directory + "/userconfig/GOSLauncherA3Py/"        
        self.excludeWidgetList=["comboBox_ChoixProfil", "lineEdit_AddProfilName"]
        #Methodes
        self.InitUi()
        self.GestionProfil ()
        
    def InitUi(self):
        ''' Create necessary file environnement for 
           Interface '''
           #Create profi directory
        self.InitEnvironnement()
           
        #Gestion liste Profil
        self.AfficheListeProfil()
           
    def InitEnvironnement(self):
        ''' Create GOSLauncherA3Py directory in main Arma3/userconfig dir'''
         
        try:
            fichier = open(self.ProfilDir+"config.ini","w")
            fichier.writelines("Defaut")
            fichier.close()
        except:
            os.mkdir(self.ProfilDir)
            self.InitEnvironnement()    
        
        
        
        
    def Rename(self):
        print ("rename", self.name)
        
    def PathName(self):
        return ((self.A3_directory+self.Name+".profil.ini"))
     
    def AfficheListeProfil(self):
            FichList = [ f.replace(".profil.ini","") for f in os.listdir(self.ProfilDir) if os.path.isfile(os.path.join(self.ProfilDir,f)) and "profil.ini"in f]
            for profil in FichList:
                self.Ui.listWidget_profil.addItem(profil)                
                self.Ui.comboBox_ChoixProfil.addItem(profil)

    def GestionProfil(self):
        
        self.RestoreProfil()
                
    def CleanInterface(self):        
        for name, obj in inspect.getmembers(self.Ui):  
            if isinstance(obj, QtWidgets.QCheckBox) and obj.objectName() not in self.excludeWidgetList:
                obj.setChecked(False)
 
    def SaveProfil(self):
        self.Name = self.Ui.comboBox_ChoixProfil.currentText()
        self.SaveGUI(QSettings(self.ProfilDir+self.Name+".profil.ini",  QSettings.IniFormat))
        self.CleanInterface()
        self.RestoreProfil()
        
    def SaveGUI(self, settings):
        excludeWidgetList= self.excludeWidgetList
        #for child in ui.children():  # works like getmembers, but because it traverses the hierarachy, you would have to call guisave recursively to traverse down the tree
    
        for name, obj in inspect.getmembers(self.Ui):  
            # if type(obj) is QComboBox:  # this works similar to isinstance, but missed some field... not sure why?
            if isinstance(obj, QtWidgets.QComboBox) and obj.objectName() not in excludeWidgetList:
                name = obj.objectName()  # get combobox name
                index = obj.currentIndex()  # get current index from combobox
                text = obj.itemText(index)  # get the text for current index
                settings.setValue(name, text)  # save combobox selection to registry
    
            if isinstance(obj, QtWidgets.QLineEdit) and obj.objectName() not in excludeWidgetList:
                name = obj.objectName()
                value = obj.text()
                settings.setValue(name, value)  # save ui values, so they can be restored next time
    
            if isinstance(obj, QtWidgets.QCheckBox) and obj.objectName() not in excludeWidgetList:
                name = obj.objectName()
                state = obj.isChecked()
                settings.setValue(name, state)
    
            if isinstance(obj, QtWidgets.QRadioButton) and obj.objectName() not in excludeWidgetList:
                name = obj.objectName()
                value = obj.isChecked()  # get stored value from registry
                settings.setValue(name, value)
                
            if isinstance(obj, QtWidgets.QSpinBox) and obj.objectName() not in excludeWidgetList:
                name  = obj.objectName()
                value = obj.value()             # get stored value from registry
                settings.setValue(name, value)
    
            if isinstance(obj, QtWidgets.QSlider) and obj.objectName() not in excludeWidgetList:
                name  = obj.objectName()
                value = obj.value()             # get stored value from registry
                settings.setValue(name, value)    
                
            if isinstance(obj, QtWidgets.QListWidget) and obj.objectName()== "listWidget_priority":  #Seulement le listeWidget_priority:
                name  = obj.objectName()
                value=[]
                for index in range(obj.count()):        
                    value.append(obj.item(index).text())
                settings.setValue(name, value)  
            



    def RestoreProfil(self):
        #self.CleanInterface()
        self.Name = self.Ui.comboBox_ChoixProfil.currentText()
        self.RestoreGUI(QSettings(self.ProfilDir+self.Name+".profil.ini",  QSettings.IniFormat))
    
    #===================================================================
    # restore "ui" controls with values stored in registry "settings"
    # currently only handles comboboxes, editlines &checkboxes
    # ui = QMainWindow object
    # settings = QSettings object
    #===================================================================
    
    def RestoreGUI(self, settings):
        
        excludeWidgetList= self.excludeWidgetList
        for name, obj in inspect.getmembers(self.Ui):
            if isinstance(obj, QtWidgets.QComboBox) and obj.objectName() not in excludeWidgetList:
                index = obj.currentIndex()  # get current region from combobox
                # text   = obj.itemText(index)   # get the text for new selected index
                name = obj.objectName()    
                value = (settings.value(name))
    
                if value == "":
                    continue    
                index = obj.findText(value)  # get the corresponding index for specified string in combobox
                if index == -1:  # add to list if not found
                    obj.insertItems(0, [value])
                    index = obj.findText(value)
                    obj.setCurrentIndex(index)
                else:
                    obj.setCurrentIndex(index)  # preselect a combobox value by index
    
            if isinstance(obj, QtWidgets.QLineEdit) and obj.objectName() not in excludeWidgetList:
                name = obj.objectName()
                value = (settings.value(name))  # get stored value from registry
                obj.setText(value)  # restore lineEditFile
    
            if isinstance(obj, QtWidgets.QCheckBox) and obj.objectName() not in excludeWidgetList:
                name = obj.objectName()
                value = settings.value(name)  # get stored value from registry
                if value != None:
                    if type(value) == bool :
                        obj.setChecked(value)
                    else:   
                        print (type(value), value)
                        obj.setChecked(strtobool(value))
    
            if isinstance(obj, QtWidgets.QRadioButton) and obj.objectName() not in excludeWidgetList:
               name = obj.objectName()
               value = settings.value(name)  # get stored value from registry
               if value != None:
                    if type(value) == bool :
                        obj.setChecked(value)
                    else:   
                        print (type(value), value)
                        obj.setChecked(strtobool(value))
    
            if isinstance(obj, QtWidgets.QSlider) and obj.objectName() not in excludeWidgetList:
                name = obj.objectName()
                value = settings.value(name)    # get stored value from registry
                if value != None:           
                    obj. setValue(int(value))   # restore value from registry
    
            if isinstance(obj, QtWidgets.QSpinBox) and obj.objectName() not in excludeWidgetList:
                name = obj.objectName()
                value = settings.value(name)    # get stored value from registry
                if value != None:
                    obj. setValue(int(value))   # restore value from registry        
    
            if isinstance(obj, QtWidgets.QListWidget) and obj.objectName()== "listWidget_priority":  #Seulement le listeWidget_priority:
                name  = obj.objectName()             
                value = settings.value(name)    # get stored value from registry
                obj.clear()
                if value != None:
                    for mod in value:
                        item = QtWidgets.QListWidgetItem()
                        item.setText(mod)
                        obj.addItem(item)

    
    def AddProfil(self, nameProfil):
        list_profil = []
        for index in range(self.Ui.listWidget_profil.count()):
            list_profil.append(self.Ui.listWidget_profil.item(index).text())
        print (list_profil)    
        if nameProfil in list_profil:   
            print ("ajout du profil : IMPOSSIBLE >",nameProfil, " existe déjà")
        else:   
            self.CleanInterface()
            self.SaveGUI(QSettings(self.ProfilDir+nameProfil+".profil.ini",  QSettings.IniFormat))
            print ("ajout du profil : ",nameProfil)
