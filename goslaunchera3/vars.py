#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Interface VAR
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import configparser, os
from . import  core


def initVar(self):
       createConfFile()
       self.var_Arma3Path=configArma3Dir(self)

def createConfFile():
    cfg = configparser.ConfigParser() 
    if (os.path.isfile("goslaunchera3.cfg")==False):
        cfg.add_section('Directory')
        cfg.set('Directory', 'Arma3Dir', '')
        cfg.write(open("goslaunchera3.cfg", 'w'))
        
def askConfig(section, option):
    #creation config.ini
    cfg = configparser.ConfigParser()    
    try:
        cfg.read('goslaunchera3.cfg')
        return cfg[section][option]
    except:
        return '' 
  

def locateArma3():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("IMPOSSIBLE DE LOCALISER ARMA 3\n\nVeuillez indiquer l'emplacement de Arma 3 sur votre disque dans la fenetre suivante.")
        msg.setWindowTitle("Where is ARMA3 Directory")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
        Arma3Dir = "none"
        if retval == 1024:
            Arma3Dir = str(QFileDialog.getExistingDirectory(msg, "ARMA3 Directory", "/"))
        return Arma3Dir

def configArma3Dir(self):
        Arma3Dir = askConfig('Directory','Arma3Dir')
        if (os.path.isfile(Arma3Dir+"/"+OSpec_ArmaName())== False):
            Arma3Dir=locateArma3()
            if (os.path.isfile(Arma3Dir+"/"+OSpec_ArmaName())== False):    
                core.infoDialogWindows(self, "Critical error","IMPOSSIBLE DE LOCALISER ARMA 3\n\nLe programme va maintenant se terminer...", QMessageBox.Critical)          
            cfg = configparser.ConfigParser()
            cfg.read("goslaunchera3.cfg")
            try:
                cfg.set("Directory",'Arma3Dir', Arma3Dir)
            except:
                cfg.add_section('Directory')
                cfg.set("Directory",'Arma3Dir', Arma3Dir)
            cfg.write(open('goslaunchera3.cfg', "w"))
        return Arma3Dir



def OSName():
    from sys import platform as _platform
    system = "inconnu"
    if _platform == "linux" or _platform == "linux2":
        # linux
        system="linux"
    elif _platform == "darwin":
        # MAC OS X
        system="mac"
    elif _platform == "win32":
        # Windows
        system="windows"
    return system

def OSpec_ArmaName():
    from sys import platform as _platform
    name = "inconnu"
    if _platform == "linux" or _platform == "linux2":
        # linux
        name="arma3"
    elif _platform == "darwin":
        # MAC OS X
        name="???"
    elif _platform == "win32":
        # Windows
        name="arma3.exe"
    return name

def CreatelisteModsLaunch(self):
    allModsListed = ""
    allListWidget = [self.listWidget_Template, self.listWidget_Framework, self.listWidget_Islands, self.listWidget_Materiel,  self.listWidget_Units,  self.listWidget_Client, self.listWidget_Test,  self.listWidget_Arma3]
    # @TEMPLATE
    allModsListed +=  getListMods(self,self.listWidget_Template, "@GOS/@TEMPLATE/" )
    if (self.comboBox_ChoixApparence.currentText() != ""): #Ajout choix de l'apparence
        allModsListed +=  "@GOSSkin_"+self.comboBox_ChoixApparence.currentText().replace(" ","_")+";"
    # @FRAMEWORK
    allModsListed +=  getListMods(self,self.listWidget_Framework, "@GOS/@FRAMEWORK/" )
    # @ISLANDS
    allModsListed +=  getListMods(self,self.listWidget_Islands, "@GOS/@ISLANDS/" ) 
    # @MATERIEL
    allModsListed +=  getListMods(self,self.listWidget_Materiel, "@GOS/@MATERIEL/" ) 
    # @UNITS
    allModsListed +=  getListMods(self,self.listWidget_Units, "@GOS/@UNITS/" ) 
    # @TEST
    allModsListed +=  getListMods(self,self.listWidget_Test, "@GOS/@TEST/" )
    # @ARMA3
    allModsListed +=  getListMods(self,self.listWidget_Arma3, "/" )
   
    return allModsListed
            
def getListMods (self, listWidget, directory):
    listeMods =""
    for index in range(listWidget.count()):
            if listWidget.item(index).checkState() == Qt.Checked:
                listeMods += directory+listWidget.item(index).text()+";"
    return listeMods
