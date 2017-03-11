#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Interface Action

from PyQt5 import QtCore
import os, stat, sys
from . import vars
from . import language
from . import saveloadui
from . import priority
import subprocess

# 
#  Action Interface : LISTE MODS
#

def selectionTousMods(self,listeWidgetMods):
    for index in range(listeWidgetMods.count()):
        listeWidgetMods.item(index).setCheckState(QtCore.Qt.Checked)

def invSelectionTousMods(self,listeWidgetMods):
    for index in range(listeWidgetMods.count()):
        if listeWidgetMods.item(index).checkState() == QtCore.Qt.Checked:
            listeWidgetMods.item(index).setCheckState(QtCore.Qt.Unchecked)
        else:
            listeWidgetMods.item(index).setCheckState(QtCore.Qt.Checked)

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
# Action Widget Priority
# 

def initPriorityTabWidget(self):
    priority.initPriorityTabWidget(self)
    
# 
#  Action Interface : GENERAL
#

def saveProfil(self):
    saveloadui.guisave(self,QtCore.QSettings( "profil/"+self.comboBox_ChoixProfil.currentText()+'.ini', QtCore.QSettings.IniFormat))
 
def restoreProfil(self):
    saveloadui.guirestore(self, QtCore.QSettings("profil/"+self.comboBox_ChoixProfil.currentText()+'.ini', QtCore.QSettings.IniFormat))
    
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
        commandLine = '"'+self.var_Arma3Path+'/arma3.exe" "-MOD='+vars.CreatelisteModsLaunch(self)+'" '
        # 
        print("execution : "+commandLine)
        subprocess.Popen(commandLine)

################################################################

if __name__ == "__main__":

    # execute when run directly, but not when called as a module.
    # therefore this section allows for testing this module!

    #print "running directly, not as a module!"

    sys.exit() 
