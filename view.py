# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import *
from PyQt5 import QtGui, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from login import Login

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        form, _ = uic.loadUiType("view.ui")
        self.ui = form()
        self.ui.setupUi(self)
        self._show_login_dialog()

    def _show_login_dialog(self):
        ld = Login()
        ld.exec_()
        self.username, self.password = ld.get_user()


