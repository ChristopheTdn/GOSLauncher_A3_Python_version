# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Zone Documents\ToF\Documents\GitHub\GOSLauncher_A3_Python_version\updater.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 140)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(380, 140))
        MainWindow.setMaximumSize(QtCore.QSize(380, 140))
        MainWindow.setBaseSize(QtCore.QSize(380, 140))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/gfx/GOSLauncherA3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(5, 10, 116, 116))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/gfx/logo-goslauncher.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_titre = QtWidgets.QLabel(self.centralWidget)
        self.label_titre.setGeometry(QtCore.QRect(125, 5, 286, 36))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_titre.setFont(font)
        self.label_titre.setObjectName("label_titre")
        self.pushButton_ok = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_ok.setGeometry(QtCore.QRect(200, 105, 75, 23))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(135, 50, 231, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.label_feedback = QtWidgets.QLabel(self.centralWidget)
        self.label_feedback.setGeometry(QtCore.QRect(135, 70, 226, 31))
        self.label_feedback.setText("")
        self.label_feedback.setObjectName("label_feedback")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GOS Launcher A3 Updater"))
        self.label_titre.setText(_translate("MainWindow", "GOS Launcher A3 Updater"))
        self.pushButton_ok.setText(_translate("MainWindow", "Commencer"))

import ressources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

