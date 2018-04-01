#! /usr/bin/python3
# -*- coding: utf-8 -*-
#
# Module ** INTERFACE PRIORITY **

u"""
Module Interface Priority.

this module manage the Priority TAB in the
GOS Launcher Apps.
           > recupere tous les Mods coché dans une liste
           >Compare Liste Mods avec Liste Tab prioritaire
           > Efface ceux qui ne sont plus selectionné
           > Ajoute ceux qui manque en fin de liste
           > Affiche la liste par priorité dans la listeBox

"""

import sys
from PyQt5.QtCore import Qt
from . import show


def init_priority_tabwidget(self):
    """Manages the display of the list of Mods in the listWidget of the main interface.

    :param: self(QTWidget).
    :return: none.

    """
    show.genereTabPriority(self.listWidget_priority, genere_list(self))


def genere_list(self):
    """
    Manage the list of Mods to add to the different listWidget of the
    interface.

    :param: self(QTWidget).
    :return: QTItems list.

    """
    return list_mod_prioritaire(self)


def list_mod_all(self):
    #recupere tous les Mods cochés dans une liste
    list_mod_all = []
    for widget, prefix in self.var_list_widget:
        for index in range(widget.count()):
            if widget.item(index).checkState() == Qt.Checked:
                list_mod_all.append(prefix+widget.item(index).text())
    # recupere type apparence
    if self.comboBox_ChoixApparence.currentText() != "":
        list_mod_all.append("@GOS/@TEMPLATE/@GOSSkin_"+self.comboBox_ChoixApparence.currentText().replace(" ", "_"))

    return list_mod_all


def list_mod_prioritaire(self):
    list_mods_priority = []
    list_mods = list_mod_all(self)
    #Conserve dans une liste les Mods deja dans la liste prioritaire et toujours coché
    for index in range(self.listWidget_priority.count()):
        if (self.listWidget_priority.item(index).text()) in list_mods:
            list_mods_priority.append(self.listWidget_priority.item(index).text())
            list_mods.remove(self.listWidget_priority.item(index).text())

    # Ajoute a cette liste les Mods coché qui ne sont pas dans la liste prioritaire initial.
    for mod in list_mods:
        list_mods_priority.append(mod)

    return list_mods_priority

    return

################################################################

if __name__ == "__main__":

    # execute when run directly, but not when called as a module.
    # therefore this section allows for testing this module!

    # print "running directly, not as a module!"
    sys.exit()
