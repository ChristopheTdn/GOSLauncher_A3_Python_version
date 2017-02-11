#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Interface SHOW
from PyQt5 import QtCore, QtGui, QtWidgets
import os


def initOuverture(self):
        ''' Affiche Liste Mods '''
        # Mods @GOS
        genereTabTemplate(self) #  Specifique @TEMPLATE GOS
        genereTab(self.listWidget_Framework,genereListMods(self,self.var_Arma3Path+"/@GOS/@FRAMEWORK/"))
        genereTab(self.listWidget_Islands,genereListMods(self,self.var_Arma3Path+"/@GOS/@ISLANDS/"))
        genereTab(self.listWidget_Units,genereListMods(self,self.var_Arma3Path+"/@GOS/@UNITS/"))
        genereTab(self.listWidget_Materiel,genereListMods(self,self.var_Arma3Path+"/@GOS/@MATERIEL/"))        
        genereTab(self.listWidget_Client,genereListMods(self,self.var_Arma3Path+"/@GOS/@CLIENT/"))        
        genereTab(self.listWidget_Test,genereListMods(self,self.var_Arma3Path+"/@GOS/@TEST/")) 
        # Mods @Arma3
        genereTab(self.listWidget_Arma3,genereListMods(self, self.var_Arma3Path+"/")) 

def genereTabTemplate(self):
    listeWidget = self.listWidget_Template
    repertoire = self.var_Arma3Path+"/@GOS/@TEMPLATE/"
    self.comboBox_ChoixApparence.addItem("")
    for mods in genereListMods(self, repertoire):
        if mods.find("@GOSSkin_") == -1:
            item = QtWidgets.QListWidgetItem()            
            item.setCheckState(QtCore.Qt.Unchecked)
            item.setText(mods)
            listeWidget.addItem(item)
        else :
            self.comboBox_ChoixApparence.addItem(mods.replace("@GOSSkin_", "").replace("_", " "))
        
def genereTab (listeWidget,listeMods):
    for mods in listeMods:
        item = QtWidgets.QListWidgetItem()            
        item.setCheckState(QtCore.Qt.Unchecked)
        item.setText(mods)
        listeWidget.addItem(item)

def genereListMods(self, repertoire):
    listeMods=[]  
    for root, dirs,  files in os.walk(repertoire):  
        for i in files:
                SearchedDir = root.replace(repertoire, "")
                if (((SearchedDir[0: (len(SearchedDir)-7)]) not  in listeMods) and (SearchedDir[-6:].lower()=="addons")):
                   #test @GOS
                   if ((root.find("@GOS") != -1 ) and (repertoire != self.var_Arma3Path+"/")): 
                       listeMods.append(SearchedDir[0: (len(SearchedDir)-7)]) 
                   #test #Arma
                   if ((root.find("@GOS") == -1 ) and
                      (repertoire == self.var_Arma3Path+"/") and
                      (SearchedDir.lower() != "addons")):
                       listeMods.append(SearchedDir[0: (len(SearchedDir)-7)]) 
    return listeMods
def LogoGosSkin(self, name) :
    self.label_GFX_Template.setPixmap(QtGui.QPixmap("gfx/camo_image/"+name.replace(" ", "_")+".jpg"))
