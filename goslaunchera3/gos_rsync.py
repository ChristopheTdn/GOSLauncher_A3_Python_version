#! /usr/bin/python3
# -*- coding: utf-8 -*-
#from PyQt5.QtCore import QSettings
from PyQt5 import QtCore, QtWidgets


class GosRsync(QtCore.QObject):
        def __init__(self,  Ui, syncName, label_state, progressbar_fichier, progressbar_global, label_debit, pushbutton, argument):
                super(GosRsync, self).__init__()
                self.Ui = Ui
                self.syncname = syncName
                self.label_state = label_state
                self.progressbar_fichier = progressbar_fichier
                self.progressbar_global = progressbar_global
                self.label_debit = label_debit
                self.pushbutton = pushbutton
                self.totalFilesize = 0
                self.totalFileToTransfer = 0
                self.process = None
                self.argument = ["-vza"]+argument
                self.argumentdry = ["-vzan", "--stats"]+argument
                self.initClass()
                self.commande = self.os_cmdLine()

        def dataReady(self):
                u"""Exécuté lorsque le processus envoie des infos à afficher.

                   La chaine renvoyée par data() est de type byte, terminée
                   par une fin de ligne.
                   L'encodage dépend de la commande lancée.

                """
                cursor = self.output.textCursor()
                cursor.movePosition(cursor.End)
                data = str(self.process.readAllStandardOutput()).replace("\\n", "\n").replace("b'", "").replace("'", "").replace('\\r', "\r")
                self.output.insertPlainText(self.parserdata(data))
                self.output.ensureCursorVisible()

        def parserdata(self, data):
                u"""
                Parcours les données renvoyés par Rsync et parse les infos pour mettre a jours
                l'interface du GOS LAuncher via les controles QT transmis

                """
                listinfo = data.split("\n")
                for info in listinfo:
                        segments = info.strip().split(" ")
                        for segment in segments:
                                if "kB/s" in segment and self.syncname != "@GOS":
                                        self.label_debit.setText(segment)
                                        data = ""
                                if "%" in segment and self.progressbar_fichier is not None:
                                        valuemoins = int(segments[0].replace(",", ""))
                                        if round(self.totalFileToTransfer/1000000, 2) < 1000:
                                            self.label_state.setText("<font color='red'>"+str(round(self.totalFileToTransfer/1000000, 2))+" Mo</font>")
                                        else:
                                            self.label_state.setText("<font color='red'>"+str(round(self.totalFileToTransfer/1000000000, 2))+" Go</font>")
                                        self.progressbar_fichier.setValue(int(segment.replace("%", "")))
                                        value = ((self.totalFileToTransfer-valuemoins)*100)/self.totalFilesize
                                        self.progressbar_global.setValue(100-round(value))
                                        data = ""
                        if "xfr" in info and self.label_state is not None:
                                detail = info.strip().split(" ")
                                self.totalFileToTransfer -= int(detail[0].replace(",", ""))
                                if round(self.totalFileToTransfer/1000000, 2) < 1000:
                                        self.label_state.setText("<font color='red'>"+str(round(self.totalFileToTransfer/1000000, 2))+" Mo</font>")
                                else:
                                    self.label_state.setText("<font color='red'>"+str(round(self.totalFileToTransfer/1000000000, 2))+" Go</font>")
                                if self.label_debit is not None:
                                        self.label_debit.setText("0.00Kb/s")
                                data = ""

                        if "Total transferred file size:" in info:
                                detail = info.split(":")
                                self.totalFileToTransfer = int(detail[1].replace(",", "").replace("bytes", ""))
                                self.totalFilesize = self.totalFileToTransfer
                                if self.label_state.text() != "<font color='red'>***</font>":
                                        if self.totalFileToTransfer == 0:
                                                self.label_state.setText("<font color='black'>A jour</font>")
                                        else:
                                                if round(self.totalFileToTransfer/1000000, 2) < 1000:
                                                    self.label_state.setText("<font color='red'>"+str(round(self.totalFileToTransfer/1000000, 2))+" Mo</font>")
                                                else:
                                                    self.label_state.setText("<font color='red'>"+str(round(self.totalFileToTransfer/1000000000, 2))+" Go</font>")

                        if "speedup is" in info and "DRY RUN" not in info and self.progressbar_fichier is not None:
                                self.label_state.setText("<font color='black'>A jour</font>")
                                self.progressbar_fichier.setValue(0)
                                self.progressbar_global.setValue(0)                                
                                self.cancelbuton.setVisible(False)
                                self.pushbutton.setVisible(True)
                                data = "Synchronisation "+self.syncname + " terminée.\n"

                        if "deleting" in info:
                                self.label_state.setText("<font color='red'>***</font>")

                        if "receiving file list ..." in info and "DRY RUN" not in info:
                                data = "Synchronisation "+self.syncname + " en cours. \n"

                        if info != "":
                                if info[len(info)-1] == '/' or "files..." in info:
                                        data = ""
                return data

        def start(self):
                # Gestion affichage bouton Cancel
                self.pushbutton.setVisible(False)
                self.cancelbuton = QtWidgets.QPushButton(self.Ui.tab_synchro)
                self.cancelbuton.setGeometry(QtCore.QRect(self.pushbutton.geometry().x(), self.pushbutton.geometry().y(), self.pushbutton.geometry().width(), self.pushbutton.geometry().height()))
                self.cancelbuton.setText('Cancel')                
                self.cancelbuton.show()
                self.cancelbuton.clicked.connect(self.killProcess)
                # Lance Process
                self.process.start(self.commande, self.argumentdry)
                self.process.waitForFinished()
                self.process.start(self.commande, self.argument)

        def initClass(self):
                self.output = self.Ui.textEdit_synchro_log
                self.process = QtCore.QProcess(self)
                self.process.readyReadStandardOutput.connect(self.dataReady)

        def killProcess(self):
                # détruit le process
                self.process.kill()
                # gestion bouton Cancel
                self.cancelbuton.setVisible(False)
                self.pushbutton.setVisible(True)
                
                self.output.insertPlainText("Synchro Abandonné...\n")
                self.output.ensureCursorVisible()

        def getsize(self):
                self.process.start(self.commande, self.argumentdry)

        def os_cmdLine(self):
                from sys import platform as _platform
                cmdline = "rsync/rsync.exe"
                if _platform == "linux" or _platform == "linux2":
                        # linux
                        cmdline = "rsync"
                elif _platform == "win32":
                        # Windows
                        cmdline = "rsync/rsync.exe"
                return cmdline
