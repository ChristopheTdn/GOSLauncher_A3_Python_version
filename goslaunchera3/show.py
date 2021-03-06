#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Interface SHOW
import os
import sys
import inspect
from PyQt5 import QtCore, QtGui, QtWidgets
from . import action


def init_app_start(self):
        # Gestion Profil
        """ Affiche Liste Mods."""

        # Mods @GOS
        #genere_tab_ui(self)
        #genere size Mods
        action.rsyncTaille(self)


def genere_tab_ui(self):
    genereTabTemplate(self)  # Specifique @TEMPLATE GOS
    genereTab(self, self.listWidget_Framework, self.var_Arma3Path+"/@GOS/@FRAMEWORK/")
    genereTab(self, self.listWidget_Islands, self.var_Arma3Path+"/@GOS/@ISLANDS/")
    genereTab(self, self.listWidget_Units, self.var_Arma3Path+"/@GOS/@UNITS/")
    genereTab(self, self.listWidget_Materiel, self.var_Arma3Path+"/@GOS/@MATERIEL/")
    genereTab(self, self.listWidget_Client, self.var_Arma3Path+"/@GOS/@CLIENT/")
    genereTab(self, self.listWidget_Test, self.var_Arma3Path+"/@GOS/@TEST/")
    genereTab(self, self.listWidget_Interclan, self.var_Arma3Path+"/@GOS/@INTERCLAN/")
    # Mods @Arma3
    genereTab(self, self.listWidget_Arma3, self.var_Arma3Path+"/")
    # Mods @WorkShop
    genereTab(self, self.listWidget_Workshop, self.var_Arma3Path+"/!Workshop/")


def itemCheckState(self, mods):
    if len(self.listWidget_priority.findItems(mods, QtCore.Qt.MatchExactly)) > 0:
        return QtCore.Qt.Checked
    else:
        return QtCore.Qt.Unchecked


def genereTabTemplate(self):
    listeWidget = self.listWidget_Template
    listeWidget.clear()
    repertoire = self.var_Arma3Path+"/@GOS/@TEMPLATE/"
    self.comboBox_ChoixApparence.addItem("")
    for mods in genereListMods(self, repertoire):
        if mods.find("@GOSSkin_") == -1:
            item = QtWidgets.QListWidgetItem()
            item.setCheckState(itemCheckState(self, "@GOS/@TEMPLATE/"+mods))
            item.setText(mods)
            listeWidget.addItem(item)
        else:
            self.comboBox_ChoixApparence.addItem(mods.replace("@GOSSkin_", "").replace("_", " "))


def genereTab(self, listeWidget,  repertoire):
    listeMods = genereListMods(self, repertoire)
    listeWidget.clear()
    for mods in listeMods:
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(itemCheckState(self, (repertoire+mods).replace(self.var_Arma3Path+"/", "")))
        item.setText(mods)
        listeWidget.addItem(item)


def genereTabPriority(listeWidget, listeMods):
    if listeMods != []:
        listeWidget.clear()
        for mods in listeMods:
            item = QtWidgets.QListWidgetItem()
            item.setText(mods)
            listeWidget.addItem(item)


def genereListMods(self, repertoire):
    listeMods = []
    for root, dirs,  files in os.walk(repertoire):
        for i in files:
                SearchedDir = root.replace(repertoire, "")
                if (((SearchedDir[0: (len(SearchedDir)-7)]) not in listeMods) and (SearchedDir.lower().endswith("addons"))):
                    #test @GOS
                    if ((root.find("@GOS") != -1) and (repertoire != self.var_Arma3Path+"/")):
                        listeMods.append(SearchedDir[0: (len(SearchedDir)-7)])
                    #test #Arma
                    if ((root.find("@GOS") == -1) and
                        (repertoire == self.var_Arma3Path+"/") and
                          ("!Workshop" not in root) and
                          (SearchedDir.lower() != "addons")):
                        listeMods.append(SearchedDir[0: (len(SearchedDir)-7)])
                    #test #Workshop
                    if ((root.find("@GOS") == -1) and
                        ("/!Workshop/" in repertoire) and
                          (SearchedDir.lower() != "addons")):
                        listeMods.append(SearchedDir[0: (len(SearchedDir)-7)])
    return listeMods


def get_version_number(filename):
    try:
        from win32api import GetFileVersionInfo, LOWORD, HIWORD
        info = GetFileVersionInfo(filename, "\\")
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        return HIWORD(ms), LOWORD(ms), HIWORD(ls), LOWORD(ls)
    except:
        return 0, 0, 0, 0


def LogoGosSkin(self, name):
    self.label_GFX_Template.setPixmap(QtGui.QPixmap(":/gfx/camo_image/"+name.replace(" ", "_")+".jpg"))


def CleanInterface(self):
    for name, obj in inspect.getmembers(self.Ui):
        if isinstance(obj, QtWidgets.QCheckBox) and obj.objectName() not in self.excludeWidgetList:
            obj.setChecked(False)
        if isinstance(obj, QtWidgets.QListWidget) and obj.objectName() not in self.excludeWidgetList:
            obj.clear()
        if isinstance(obj, QtWidgets.QComboBox) and obj.objectName() not in self.excludeWidgetList:
            obj.clear()

    genere_tab_ui(self.Ui)

################################################################

if __name__ == "__main__":

    # execute when run directly, but not when called as a module.
    # therefore this section allows for testing this module!

    #print "running directly, not as a module!"

    sys.exit()
