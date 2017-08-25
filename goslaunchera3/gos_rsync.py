#! /usr/bin/python3
# -*- coding: utf-8 -*-
#from PyQt5.QtCore import QSettings
from PyQt5 import QtCore


class GosRsync(QtCore.QObject):
        def __init__(self,  Ui, syncName,label_state, progressbar_fichier,progressbar_global, label_debit, pushbutton, argument ):  
            super(GosRsync, self).__init__()
            self.Ui = Ui
            self.syncname = syncName
            self.label_state = label_state
            self.progressbar_fichier=progressbar_fichier
            self.progressbar_global = progressbar_global
            self.label_debit = label_debit
            self.pushbutton = pushbutton
            self.totalFilesize = 0
            self.totalFileToTransfer = 0
            self.process = None
            self.argument=["-vza"]+argument
            self.argumentdry =["-vzan","--stats"]+argument
            self.initClass()  
            
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
            for info in listinfo:
                segments = info.strip().split(" ")
                for segment in segments:
                    if "kB/s" in segment:
                        self.label_debit.setText(segment)
                        data=""
                    if "%" in segment:
                        valuemoins = int(segments[0].replace(",", ""))                        
                        self.label_state.setText("<font color='red'>"+str(round((self.totalFileToTransfer-valuemoins)/1000000, 2))+" Mo</font>")
                        self.progressbar_fichier.setValue(int(segment.replace("%", "")))
                        value = ((self.totalFileToTransfer-valuemoins)*100)/self.totalFilesize
                        self.progressbar_global.setValue(100-round(value))
                        data=""
                if "xfr" in info:
                    detail = info.strip().split(" ")     
                    self.totalFileToTransfer -= int(detail[0].replace(",", ""))
                    self.label_state.setText(str(round((self.totalFileToTransfer)/1000000, 3))+" Mo")
                    self.label_debit.setText("0.00Kb/s")
                    data=""

                if "Total transferred file size:" in info:
                    detail = info.split(":")                    
                    self.totalFileToTransfer = int (detail[1].replace(",", "").replace("bytes", ""))
                    self.totalFilesize = self.totalFileToTransfer   
                    if self.totalFileToTransfer ==0: 
                        self.label_state.setText("<font color='black'>A jour</font>")
                    else:
                        self.label_state.setText("<font color='red'>"+str(round(self.totalFileToTransfer/1000000, 2))+" Mo</font>")
                    data=""
                    
                if "speedup is" in info and "DRY RUN" not in info:
                    self.label_state.setText("A jour")
                    self.progressbar_fichier.setValue(0)
                    self.progressbar_global.setValue(0)
                    self.pushbutton.setEnabled(True)
                    self.pushbutton.setText('Lancer')
                    data="Synchronisation "+self.syncname + " terminée.\n"

                    
                if "receiving file list ..." in info and "DRY RUN" not in info:                    
                    data="Synchronisation "+self.syncname + " en cours. \n"    
                    
                if info != "": 
                    if info[len(info)-1]=='/' or "files..." in info:
                        data =""
                
            return data
            
        def start(self):  
            self.pushbutton.setText('Abandonner')
            commande = "rsync/rsync.exe"
            self.process.start(commande, self.argumentdry)  
            self.process.waitForFinished()
            self.process.start(commande, self.argument) 
             
        def initClass(self):
            self.output = self.Ui.textEdit_synchro_log
            self.process = QtCore.QProcess(self)
            self.process.readyReadStandardOutput.connect(self.dataReady)            
            
        
        def killProcess(self):
            self.process.kill()
            self.pushbutton.setText("Lancer")            
            self.output.insertPlainText("Synchro Abandonné...\n")
            self.output.ensureCursorVisible()
        
        def getsize(self):
            commande = "rsync/rsync.exe" 
            self.process.start(commande, self.argumentdry)  
            
    

    
