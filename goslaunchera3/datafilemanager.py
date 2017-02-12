#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Serialize

from PyQt5 import QtWidgets
import pickle

def serialize(self):
    fichier= open("save.mydata", "wb")
    pickle.dump(self.checkBox_noCB, fichier) 
    
def deserialize(self):
    fichier= open("save.mydata", "rb")
    self.checkBox_noCB=pickle.load(fichier)
