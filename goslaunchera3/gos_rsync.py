#! /usr/bin/python3
# -*- coding: utf-8 -*-
#from PyQt5.QtCore import QSettings
from PyQt5 import QtCore


class GosRsync(QtCore.QObject):
        def __init__(self,  Ui, syncName,label_state, progressbar_fichier,progressbar_global, label_debit, pushbutton ):  
            super(GosRsync, self).__init__()
            self.Ui = Ui
            self.label_state = label_state
            self.progressbar_fichier=progressbar_fichier
            self.progressbar_global = progressbar_global
            self.label_debit=label_debit
            self.pushbutton = pushbutton
            self.totalFilesize = 0
            self.totalFileToTransfer = 0
            self.process = None
            self.argumentdry = ["-vzan","--stats", "--partial","--inplace", "--progress","--delete-after","--chmod=ugo=rwX","www.clan-gos.fr::@TEMPLATE","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@TEMPLATE"]
            self.argument = ["-vza","--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@TEMPLATE","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@TEMPLATE"]

            self.initClass()  
            self.start()
            
        def dataReady(self):
            """Exécuté lorsque le processus envoie des infos à afficher.
               La chaine renvoyée par data() est de type byte, terminée
               par une fin de ligne. 
               L'encodage dépend de la commande lancée.
            """
            cursor = self.output.textCursor()
            cursor.movePosition(cursor.End)
            data =str(self.process.readAllStandardOutput()).replace("\\n", "\n").replace("b'", "").replace("'", "").replace('\\r', "\r")
            self.output.insertPlainText(self.parserdata(data))
            self.output.ensureCursorVisible()
        
        def parserdata(self, data):
            listinfo= data.split("\n")
            for index, info in enumerate(listinfo):
                segments = info.strip().split(" ")
                for segment in segments:
                    if "kB/s" in segment:
                        self.label_debit.setText(segment)
                    if "%" in segment:
                        valuemoins = int(segments[0].replace(",", ""))
                        self.label_state.setText(str(round((self.totalFileToTransfer-valuemoins)/1000000, 2))+" Mo")
                        self.progressbar_fichier.setValue(int(segment.replace("%", "")))
                        value = ((self.totalFileToTransfer-valuemoins)*100)/self.totalFilesize
                        self.progressbar_global.setValue(100-round(value))
                if "xfr" in info:
                    detail = info.strip().split(" ")     
                    self.totalFileToTransfer -= int(detail[0].replace(",", ""))
                    self.label_state.setText(str(round((self.totalFileToTransfer)/1000000, 3))+" Mo")
                    self.label_debit.setText("0.00Kb/s")

                if "Total transferred file size:" in info:
                    detail = info.split(":")                    
                    self.totalFileToTransfer = int (detail[1].replace(",", "").replace("bytes", ""))
                    self.totalFilesize = self.totalFileToTransfer                    
                    self.label_state.setText(str(round(self.totalFileToTransfer/1000000, 2))+" Mo")
                
            return data
        def start(self):  
            commande = "rsync/rsync.exe"
            self.process.start(commande, self.argumentdry)
            self.process.waitForFinished()
            self.process.start(commande, self.argument)
            
        def initClass(self):
            self.output = self.Ui.textEdit_synchro_log
            self.process = QtCore.QProcess(self)
            self.process.readyReadStandardOutput.connect(self.dataReady)


    
