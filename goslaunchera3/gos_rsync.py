#! /usr/bin/python3
# -*- coding: utf-8 -*-
#from PyQt5.QtCore import QSettings
from PyQt5 import QtWidgets,QtCore


class GosRsync(QtCore.QObject):
        def __init__(self,  Ui, syncName):  
            super(GosRsync, self).__init__()
            self.Ui = Ui  
            self.initUi()  
        def dataReady(self):
            """Exécuté lorsque le processus envoie des infos à afficher.
               La chaine renvoyée par data() est de type byte, terminée
               par une fin de ligne. 
               L'encodage dépend de la commande lancée.
            """
            cursor = self.output.textCursor()
            cursor.movePosition(cursor.End)
            cursor.insertText(str(self.process.readAll()))
            self.output.ensureCursorVisible()
        def start(self):  
            arguments = ["-vza","--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@TEMPLATE","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@TEMPLATE"]
             # ' -vza --partial --inplace --progress --delete-after --bwlimit=0 --chmod=ugo=rwX "www.clan-gos.fr::@TEMPLATE" "cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@TEMPLATE"'
            commande = "rsync/rsync.exe"
            self.process.start(commande, arguments)
            self.process.waitForFinished()
            
        def initUi(self):
            self.output = self.Ui.textEdit_synchro_log
            self.process = QtCore.QProcess(self)
            self.process.readyRead.connect(self.dataReady)


    
