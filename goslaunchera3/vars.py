#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Interface VAR

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import configparser, os, sys
from . import  core
from . import  profil


def initVar(self):
    createConfFile()
    self.var_Arma3Path=configArma3Dir(self) 
    # Genere List Widget 
    self.var_list_widget = [[self.listWidget_Template, "@GOS/@TEMPLATE/"],
                   [self.listWidget_Islands, "@GOS/@ISLANDS/"],
                   [self.listWidget_Framework, "@GOS/@FRAMEWORK/"],
                   [self.listWidget_Materiel, "@GOS/@MATERIEL/"],
                   [self.listWidget_Units, "@GOS/@UNITS/"],
                   [self.listWidget_Test, "@GOS/@TEST/"],
                   [self.listWidget_Client, "@GOS/@CLIENT/"],
                   [self.listWidget_Arma3, ""],
                   [self.listWidget_Workshop, "!Workshop/"]]
    #Genere Class PROFIL
    self.var_Profil = profil.Profil(self,self.var_Arma3Path)

       
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
                core. info_dialog_windows(self, "Critical error","IMPOSSIBLE DE LOCALISER ARMA 3\n\nLe programme va maintenant se terminer...", QMessageBox.Critical)          
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

def createListeModsLaunch(self):
    allModsListed = ""
    for index in range(self.listWidget_priority.count()):
        allModsListed += self.listWidget_priority.item(index).text()+";"
    return allModsListed

def  createListeOptions(self):
    '''
    Fonction : CreateListeOtions
    Param : self
    return value  : STRING
    Genere la liste des options a ajouter a la ligne de commande pour lancer Arma 3
    Les options sont determiné dans l'onglet "Option" du Launcher
    '''
    allOptionsListed = ""
    if  self.checkBox_AllowFileChange.checkState():
        allOptionsListed +="-filePatching "
    if  self.checkBox_nosplash.checkState():
        allOptionsListed +="-noSplash "
    if self.checkBox_noLogs.checkState():
        allOptionsListed +="-noLogs "
    if self.checkBox_emptyWorld.checkState():
        allOptionsListed +="-skipIntro "
    if self.checkBox_customCommand.checkState():
        allOptionsListed +=self.lineEdit_customCommand.text()+" "
    if self.checkBox_noPause.checkState():
        allOptionsListed +="-noPause "
    if self.checkBox_noCB.checkState():
        allOptionsListed +="-noCB "  
    if self.checkBox_showScriptError.checkState():
        allOptionsListed +="-showScriptErrors "
    if self.checkBox_xpMode.checkState():
        allOptionsListed +="-showScriptErrors "   
    return allOptionsListed





################################################################

if __name__ == "__main__":

    # execute when run directly, but not when called as a module.
    # therefore this section allows for testing this module!

    #print "running directly, not as a module!"

    sys.exit() 
