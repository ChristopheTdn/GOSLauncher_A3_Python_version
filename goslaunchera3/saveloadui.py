#! /usr/bin/python3
#-*- coding: utf-8 -*-
#
# Module Sauvegarde UI
# Based on Panofish Work : http://stackoverflow.com/questions/23279125/python-pyqt4-functions-to-save-and-restore-ui-widget-values

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import  *
import inspect
from distutils.util import strtobool

excludeWidgetList=["comboBox_ChoixProfil"]
#===================================================================
# save "ui" controls and values to registry "setting"
# currently only handles comboboxes editlines & checkboxes
# ui = qmainwindow object
# settings = qsettings object
#===================================================================

def guisave(ui, settings):

    #for child in ui.children():  # works like getmembers, but because it traverses the hierarachy, you would have to call guisave recursively to traverse down the tree

    for name, obj in inspect.getmembers(ui):
  
        # if type(obj) is QComboBox:  # this works similar to isinstance, but missed some field... not sure why?
        if isinstance(obj, QComboBox) and obj.objectName() not in excludeWidgetList:
            name = obj.objectName()  # get combobox name
            index = obj.currentIndex()  # get current index from combobox
            text = obj.itemText(index)  # get the text for current index
            settings.setValue(name, text)  # save combobox selection to registry

        if isinstance(obj, QLineEdit) and obj.objectName() not in excludeWidgetList:
            name = obj.objectName()
            value = obj.text()
            settings.setValue(name, value)  # save ui values, so they can be restored next time

        if isinstance(obj, QCheckBox) and obj.objectName() not in excludeWidgetList:
            name = obj.objectName()
            state = obj.isChecked()
            settings.setValue(name, state)

        if isinstance(obj, QRadioButton) and obj.objectName() not in excludeWidgetList:
            name = obj.objectName()
            value = obj.isChecked()  # get stored value from registry
            settings.setValue(name, value)
            
        if isinstance(obj, QSpinBox) and obj.objectName() not in excludeWidgetList:
            name  = obj.objectName()
            value = obj.value()             # get stored value from registry
            settings.setValue(name, value)

        if isinstance(obj, QSlider) and obj.objectName() not in excludeWidgetList:
            name  = obj.objectName()
            value = obj.value()             # get stored value from registry
            settings.setValue(name, value)    

#===================================================================
# restore "ui" controls with values stored in registry "settings"
# currently only handles comboboxes, editlines &checkboxes
# ui = QMainWindow object
# settings = QSettings object
#===================================================================

def guirestore(ui, settings):

    for name, obj in inspect.getmembers(ui):
        if isinstance(obj, QComboBox) and obj.objectName() not in excludeWidgetList:
            index = obj.currentIndex()  # get current region from combobox
            # text   = obj.itemText(index)   # get the text for new selected index
            name = obj.objectName()

            value = (settings.value(name))

            if value == "":
                continue

            index = obj.findText(value)  # get the corresponding index for specified string in combobox

            if index == -1:  # add to list if not found
                obj.insertItems(0, [value])
                index = obj.findText(value)
                obj.setCurrentIndex(index)
            else:
                obj.setCurrentIndex(index)  # preselect a combobox value by index

        if isinstance(obj, QLineEdit) and obj.objectName() not in excludeWidgetList:
            name = obj.objectName()
            value = (settings.value(name))  # get stored value from registry
            obj.setText(value)  # restore lineEditFile

        if isinstance(obj, QCheckBox) and obj.objectName() not in excludeWidgetList:
            name = obj.objectName()
            value = settings.value(name)  # get stored value from registry
            if value != None:
                obj.setChecked(strtobool(value))  # restore checkbox

        if isinstance(obj, QRadioButton) and obj.objectName() not in excludeWidgetList:
           name = obj.objectName()
           value = settings.value(name)  # get stored value from registry
           if value != None:
               obj.setChecked(strtobool(value))

        if isinstance(obj, QSlider) and obj.objectName() not in excludeWidgetList:
            name = obj.objectName()
            value = settings.value(name)    # get stored value from registry
            if value != None:           
                obj. setValue(int(value))   # restore value from registry

        if isinstance(obj, QSpinBox) and obj.objectName() not in excludeWidgetList:
            name = obj.objectName()
            value = settings.value(name)    # get stored value from registry
            if value != None:
                obj. setValue(int(value))   # restore value from registry        

################################################################

if __name__ == "__main__":

    # execute when run directly, but not when called as a module.
    # therefore this section allows for testing this module!

    #print "running directly, not as a module!"

    sys.exit() 
