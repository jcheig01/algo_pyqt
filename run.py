import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import view

def main():
    os.environ['QT_IM_MODULE'] = 'fcitx'
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = view.MainView()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()