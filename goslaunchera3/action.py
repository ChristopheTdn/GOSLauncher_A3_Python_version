#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Interface Action

import os
import stat
import sys
import subprocess

from . import vars
from . import language
from . import saveloadui
from . import priority

from PyQt5.QtCore import Qt, QSettings


# 
#  Action Interface : LISTE MODS
#

def selection_tous_mods(self,listeWidgetMods):
    for index in range(listeWidgetMods.count()):
        listeWidgetMods.item(index).setCheckState(Qt.Checked)

def inv_selection_tous_mods(self,listeWidgetMods):
    for index in range(listeWidgetMods.count()):
        if listeWidgetMods.item(index).checkState() == Qt.Checked:
            listeWidgetMods.item(index).setCheckState(Qt.Unchecked)
        else:
            listeWidgetMods.item(index).setCheckState(Qt.Checked)

# 
#  Action Interface : OPTIONS
#

def optionModifLangue(self, langue):
    language.change_language(self, langue)

def optionCustomCommand(self):
    if (self.checkBox_customCommand.checkState() ==Qt.Checked):
        self.lineEdit_customCommand.setEnabled(True)
    else:
        self.lineEdit_customCommand.setEnabled(False)

#
# Action Widget Priority
# 

def initPriorityTabWidget(self):
    priority.init_priority_tabwidget(self)

    
# 
#  Action Interface : GENERAL
#

def saveProfil(self):
    saveloadui.guisave(self,QSettings( "profil/"+self.comboBox_ChoixProfil.currentText()+'.ini', QSettings.IniFormat))
 
def restoreProfil(self):
    saveloadui.guirestore(self, QSettings("profil/"+self.comboBox_ChoixProfil.currentText()+'.ini', QSettings.IniFormat))
    
def launchArma3(self):
    newLine='\n'
    #Linux version
    if vars.OSName()=="linux":
        fichier = open("runArma3", "w")
        fichier.write('cd "'+self.var_Arma3Path+'" '+newLine)    
        fichier.write('./arma3'+' "-MOD='+vars.createListeModsLaunch(self)+'" '+vars.createListeOptions(self))
        fichier.close()
        os.chmod('runArma3', stat.S_IRWXU)
        # TODO: change os.system Obsolete
        os.system('./runArma3')
        
    #Windows version
    if vars.OSName()=="windows":
        commandLine = '"'+self.var_Arma3Path+'/arma3.exe" "-MOD='+vars.createListeModsLaunch(self)+'" '+vars.createListeOptions(self)
        # 
        print("execution : "+commandLine)
        subprocess.Popen(commandLine)

################################################################

if __name__ == "__main__":

    # execute when run directly, but not when called as a module.
    # therefore this section allows for testing this module!

    #print "running directly, not as a module!"

    sys.exit() 
