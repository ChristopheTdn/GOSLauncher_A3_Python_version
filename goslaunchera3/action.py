#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Interface Action

from PyQt5.QtCore import *
import os, stat
from . import vars
from . import language

def selectionTousMods(self,listeWidgetMods):
    for index in range(listeWidgetMods.count()):
        listeWidgetMods.item(index).setCheckState(Qt.Checked)

def invSelectionTousMods(self,listeWidgetMods):
    for index in range(listeWidgetMods.count()):
        if listeWidgetMods.item(index).checkState() == Qt.Checked:
            listeWidgetMods.item(index).setCheckState(Qt.Unchecked)
        else:
            listeWidgetMods.item(index).setCheckState(Qt.Checked)

def modifLangue(self, langue):
    language.changeLangage(self, langue)

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

