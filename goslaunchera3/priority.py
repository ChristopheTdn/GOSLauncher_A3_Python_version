#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Interface Priority

#-*- coding: utf-8 -*-

from PyQt5 import QtCore
from . import show
import os

def initPriorityTabWidget(self):
    #self.listWidget_priority.clear()
    show.genereTabPriority(self.listWidget_priority, genereList(self))
    cleanPriorityTabWidget(self)
    
def genereList(self):
    items = []
    listWidget = [[self.listWidget_Template, "@GOS/@TEMPLATE/"], [self.listWidget_Islands, "@GOS/@ISLANDS/"], [self.listWidget_Framework,"@GOS/@FRAMEWORK/"] , [self.listWidget_Materiel,"@GOS/@MATERIEL/"],[self.listWidget_Units, "@GOS/@UNITS/"],[self.listWidget_Test, "@GOS/@TEST/"], [self.listWidget_Client, "@GOS/@CLIENT/"]]
    for widget,prefix in listWidget:
        for index in range(widget.count()):
            if widget.item(index).checkState() == QtCore.Qt.Checked and len(self.listWidget_priority.findItems(prefix+widget.item(index).text(), QtCore.Qt.MatchExactly))==0 :
                items.append(prefix+widget.item(index).text())
            if widget.item(index).checkState() == QtCore.Qt.Unchecked and len(self.listWidget_priority.findItems(prefix+widget.item(index).text(), QtCore.Qt.MatchExactly))>0 :
                for indexPriority in range(self.listWidget_priority.count()):
                    print (indexPriority)
                    if prefix+widget.item(index).text() == self.listWidget_priority.item(indexPriority).text(): #self.listWidget_priority.item(indexPriority).text()
                        self.listWidget_priority.takeItem(indexPriority)
                        break
    return items

def  cleanPriorityTabWidget(self):
        for index in range(self.listWidget_priority.count()):
            try:
                if not os.path.exists(self.var_Arma3Path+"/"+self.listWidget_priority.item(index).text()):
                    self.listWidget_priority.takeItem(index)
            except:
                self.listWidget_priority.takeItem(index)
                
            
                
                



