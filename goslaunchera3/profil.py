#! /usr/bin/python3
# -*- coding: utf-8 -*-
import os
from . import saveloadui
from PyQt5.QtCore import QSettings


class Profil:
    def __init__(self, Ui,  directory):
        self.Name = "Defaut"
        self.Ui = Ui
        self.ProfilDir = directory + "/userconfig/GOS-LauncherA3_Py/"
        self.GestionProfil ()
        
    def Rename(self):
        print ("rename", self.name)
        
    def PathName(self):
        return ((self.A3_directory+self.Name+".profil.ini"))
     
    def InitProfil(self):
            self.Ui.comboBox_ChoixProfil.addItem("Defaut")
            FichList = [ f.replace(".profil.ini","") for f in os.listdir(self.ProfilDir) if os.path.isfile(os.path.join(self.ProfilDir,f)) and "profil.ini"in f]
            print (self.ProfilDir, FichList)

    def GestionProfil(self):
        if not os.path.exists(self.ProfilDir+"config.ini"):  # determine l existence du repertoire de config Profil
            try:
                os.mkdir(self.ProfilDir) 
            except FileExistsError:
                fichier = open(self.ProfilDir+"config.ini","w")
                fichier.writelines("Defaut")
                fichier.close()
            finally:          
                self.RestoreProfil()

    
    def SaveProfil(self):
        saveloadui.guisave(self.Ui,QSettings(self.ProfilDir+self.Name+".profil.ini",  QSettings.IniFormat))

    def RestoreProfil(self):
        saveloadui.guirestore(self.Ui, QSettings(self.ProfilDir+self.Name+".profil.ini",  QSettings.IniFormat))
