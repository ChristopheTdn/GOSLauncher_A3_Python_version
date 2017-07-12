#! /usr/bin/python3
# -*- coding: utf-8 -*-
#from PyQt5.QtCore import QSettings
from PyQt5 import (QtWidgets,  QtCore)


class GosRsync(QtCore.QObject):
        def __init__(self,  Ui, syncName, parent=None):    
            self.Ui = Ui
            self.process = None
            self.start()
            
        def start(self):  
            arguments = ["-vza","--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","'www.clan-gos.fr::@TEMPLATE'","'//cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@TEMPLATE'"]
  #          process = subprocess.Popen("rsync/rsync.exe "+arguments, 
 #                          stdout=subprocess.PIPE,
  #                         stderr=subprocess.PIPE,
   #                        stdin=subprocess.PIPE)
  #          stdout, stderr = process.communicate()
  #          self.Ui.textEdit_synchro_log.setPlainText(('STDOUT:{}\nSTDERR:{}\n'.format(stdout, stderr)))
            self.process = QtCore.QProcess()
            self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
            self.process.readyReadStandardOutput.connect(self.WorkReply)
            self.process.finished.connect(self.WorkFinished)
            commande = "rsync/rsync.exe"
            self.process.startDetached(commande, arguments)
            self.process.waitForStarted()
            
        def WorkFinished(self):
            """exécuté à la fin du processus
            """
            if self.process!=None:
                # le processus vient de se terminer: on fait le ménage
                self.process.readyReadStandardOutput.disconnect()
                self.process.finished.disconnect()
                print("Processus terminé")
                
        def WorkReply(self):
            """Exécuté lorsque le processus envoie des infos à afficher.
               La chaine renvoyée par data() est de type byte, terminée
               par une fin de ligne. 
               L'encodage dépend de la commande lancée.
            """
            data = self.process.readAllStandardOutput().data()
            ch = str(data, encoding="utf-8").rstrip()
            self.Ui.textEdit_synchro_log.setPlainText(ch+"\n")
            print(ch)

    
