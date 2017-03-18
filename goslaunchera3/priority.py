#! /usr/bin/python3
# -*- coding: utf-8 -*-
#
# Module ** INTERFACE PRIORITY **

"""
Module Interface Priority

this module manage the Priority TAB in the
GOS Launcher Apps.

"""

import os
import sys
from PyQt5.QtCore import Qt
from . import show


def genere_list(self):
    """
    Manage the list of Mods to add to the different listWidget of the
    interface.

    :param: self(QTWidget).
    :return: QTItems list.

    """
    items = []
    list_widget = [[self.listWidget_Template, "@GOS/@TEMPLATE/"],
                   [self.listWidget_Islands, "@GOS/@ISLANDS/"],
                   [self.listWidget_Framework, "@GOS/@FRAMEWORK/"],
                   [self.listWidget_Materiel, "@GOS/@MATERIEL/"],
                   [self.listWidget_Units, "@GOS/@UNITS/"],
                   [self.listWidget_Test, "@GOS/@TEST/"],
                   [self.listWidget_Client, "@GOS/@CLIENT/"],
                   [self.listWidget_Arma3, ""],
                   [self.listWidget_Workshop, "!Workshop/"]]
    for widget, prefix in list_widget:
        for index in range(widget.count()):
            if widget.item(index).checkState() == Qt.Checked and \
             len(self.listWidget_priority.findItems(prefix+widget.item(index).text(), Qt.MatchExactly)) == 0:
                items.append(prefix+widget.item(index).text())
                if widget.item(index).checkState() == Qt.Unchecked and \
                    len(self.listWidget_priority.findItems(prefix+widget.item(index).text(), Qt.MatchExactly)) > 0:
                    for index_priority in range(self.listWidget_priority.count()):
                        if prefix+widget.item(index).text() == self.listWidget_priority.item(index_priority).text():
                            self.listWidget_priority.takeItem(index_priority)
                        break
    return items


def init_priority_tabwidget(self):
    """Manages the display of the list of Mods in the listWidget of the main interface.

    :param: self(QTWidget).
    :return: none.

    """
    show.genereTabPriority(self.listWidget_priority, genere_list(self))
    clean_priority_tabwidget(self)


def clean_priority_tabwidget(self):
    """Clean listWidget_Priority item for obsolete Items

    :param: self(QTWidget).
    :return: none.

    """
    list_bad_index = []
    for index in range(self.listWidget_priority.count()):
        if not os.path.exists(self.var_Arma3Path+"/"+self.listWidget_priority.item(index).text()):
            list_bad_index.append(index)
    for index in reversed(list_bad_index):
        self.listWidget_priority.takeItem(index)

################################################################

if __name__ == "__main__":

    # execute when run directly, but not when called as a module.
    # therefore this section allows for testing this module!

    # print "running directly, not as a module!"
    sys.exit()
