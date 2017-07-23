#! /usr/bin/python3
# -*- coding: utf-8 -*-
#
# Module Interface Action

import os
import stat
import sys
import subprocess
from . import vars
from . import language
from . import priority
from . import gos_rsync

from PyQt5.QtCore import Qt


#
#  Action Interface : Liste MODS
#

def selection_tous_mods(self, liste_widget_mods):
    for index in range(liste_widget_mods.count()):
        liste_widget_mods.item(index).setCheckState(Qt.Checked)


def inv_selection_tous_mods(self, liste_widget_mods):
    for index in range(liste_widget_mods.count()):
        if liste_widget_mods.item(index).checkState() == Qt.Checked:
            liste_widget_mods.item(index).setCheckState(Qt.Unchecked)
        else:
            liste_widget_mods.item(index).setCheckState(Qt.Checked)


#
#  Action Interface : OPTIONS
#

def optionModifLangue(self, langue):
    language.change_language(self, langue)

#
# Action Widget Priority
#

def initPriorityTabWidget(self):
    priority.init_priority_tabwidget(self)


#
#  Action Interface : GENERAL
#




def launch_arma3(self):
    newLine = '\n'
    # Linux version
    if vars.OSName() == "linux":
        fichier = open("runArma3", "w")
        fichier.write('cd "' + self.var_Arma3Path + '" ' + newLine)
        fichier.write('./arma3' + ' "-MOD=' + vars.createListeModsLaunch(self) + '" ' + vars.createListeOptions(self))
        fichier.close()
        os.chmod('runArma3', stat.S_IRWXU)
        # TODO: change os.system Obsolete
        os.system('./runArma3')

    # Windows version
    if vars.OSName() == "windows":
        commandLine = '"' + self.var_Arma3Path + '/arma3.exe" "-MOD=' + vars.createListeModsLaunch(
            self) + '" ' + vars.createListeOptions(self)
        #
        print("execution : " + commandLine)
        subprocess.Popen(commandLine)
        
#
#  Action Interface : RSYNC
#

def rsyncGos(self, syncname):
    self.clyde = gos_rsync.GosRsync(self, syncname,self.label_synchro_template_state, self.progressBar_synchro_template_fichier,self.progressBar_synchro_template_global,self.label_synchro_template_debit,self.pushButton_synchro_template_launch)


    
################################################################

if __name__ == "__main__":
    # execute when run directly, but not when called as a module.
    # therefore this section allows for testing this module!

    # print "running directly, not as a module!"

    sys.exit()
