# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, uic
import os
import pandas as pd
import pathlib

class Login(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        UIFormCls, QtBaseCls = uic.loadUiType("login.ui")
        self.ui = UIFormCls()
        self.ui.setupUi(self)
        curr_path = pathlib.Path().absolute()

        if not os.path.isfile(curr_path+'/log.csv'):
            df = pd.DataFrame(columns = ['username', 'password'])
            df.to_csv(curr_path+'/log.csv')

        self.df = pd.read_csv(curr_path+'/log.csv')


    def get_user(self):
        return self.ui.username_value.text(), self.ui.password_value.text()

    def signup(self):
        pass

    def is_valid(self):
        pass


