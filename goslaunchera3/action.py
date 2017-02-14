#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Interface Action

from PyQt5 import QtCore
import os, stat, sys
from . import vars
from . import language
from . import datafilemanager

# 
#  Action Interface : LISTE MODS
#

def selectionTousMods(self,listeWidgetMods):
    for index in range(listeWidgetMods.count()):
        listeWidgetMods.item(index).setCheckState(Qt.Checked)

def invSelectionTousMods(self,listeWidgetMods):
    for index in range(listeWidgetMods.count()):
        if listeWidgetMods.item(index).checkState() == Qt.Checked:
            listeWidgetMods.item(index).setCheckState(Qt.Unchecked)
        else:
            listeWidgetMods.item(index).setCheckState(Qt.Checked)

# 
#  Action Interface : OPTIONS
#

def optionModifLangue(self, langue):
    language.changeLangage(self, langue)

def optionCustomCommand(self):
    if (self.checkBox_customCommand.checkState() ==QtCore.Qt.Checked):
        self.lineEdit_customCommand.setEnabled(True)
    else:
        self.lineEdit_customCommand.setEnabled(False)
        

# 
#  Action Interface : GENERAL
#
def saveProfil(self):
    datafilemanager.guisave(self, QtCore.QSettings('saved.ini', QtCore.QSettings.IniFormat))
 
def restoreProfil(self):
    datafilemanager.guirestore(self, QtCore.QSettings('saved.ini', QtCore.QSettings.IniFormat))
    
def launchArma3(self):
    newLine='\n'
    #Linux version
    if vars.OSName()=="linux":
        fichier = open("runArma3", "w")
        fichier.write('cd "'+self.var_Arma3Path+'" '+newLine)    
        fichier.write('./arma3'+' "-MOD='+vars.CreatelisteModsLaunch(self)+' " ')
        fichier.close()
        os.chmod('runArma3', stat.S_IRWXU)
        # TODO: change os.system Obsolete
        os.system('./runArma3')
        
    #Windows version
    if vars.OSName()=="windows":
        fichier = open("runArma3.bat", "w")
        fichier.write('cd "'+self.var_Arma3Path+'" '+newLine)    
        fichier.write('"'+self.var_Arma3Path+'/arma3.exe'+'" "-MOD='+vars.CreatelisteModsLaunch(self)+' " '+newLine)
        fichier.close()
        os.system('runArma3.bat')

################################################################

if __name__ == "__main__":

    # execute when run directly, but not when called as a module.
    # therefore this section allows for testing this module!

    #print "running directly, not as a module!"

    sys.exit() 
