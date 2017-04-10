#! /usr/bin/python3
# -*- coding: utf-8 -*-

class Profil:
    def __init__(self, Ui, name, a3_directory):
        self.Name = name
        self.Ui = Ui
        self.A3_directory=a3_directory+"/userconfig/GOS-LauncherA3_Py/"
        self.gestion_profil()
        
    def rename(self):
        print ("rename", self.name)
        
    def activate(self, profil):
            self.Ui.comboBox_ChoixProfil.addItem(profil)
    
    def gestion_profil(self):
        print ("repertoire de travail :"+self.A3_directory)
