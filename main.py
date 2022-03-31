from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt
import os
from setting import Ui_Form


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        radius = 28
        self.createLayout()
        # x, y, width, height
        self.setGeometry(1200, 0, 240, 5)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.groupBox)
        self.setLayout(self.vbox)
        self.setStyleSheet(
            """
                background:rgb(0,0,0);
                border-top-left-radius:{0}px;
                border-bottom-left-radius:{0}px;
                border-top-right-radius:{0}px;
                border-bottom-right-radius:{0}px;   
            """.format(radius)
        )
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.8)

        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox()

        hbox = QHBoxLayout()

        # button start
        start = QPushButton()
        start.setIcon(QIcon("icons/start.png"))
        start.setGeometry(QRect(0, 15, 20, 0))
        start.setStyleSheet("background-color:black;")
        start.setIconSize(QtCore.QSize(50, 50))
        start.setMinimumHeight(40)
        start.setMinimumWidth(40)
        hbox.addWidget(start)

        # button image path
        folder = QPushButton()
        folder.setIcon(QIcon("icons/folder.png"))
        folder.setStyleSheet("background-color:black;")
        folder.setGeometry(QRect(20, 15, 40, 0))
        # QSize(width, height)
        folder.setIconSize(QtCore.QSize(73, 73))
        folder.setMinimumHeight(40)
        folder.setMinimumWidth(40)
        folder.clicked.connect(self.openStorageImagePath)
        hbox.addWidget(folder)

        # button stop
        stop = QPushButton()
        stop.setIcon(QIcon("icons/stop.png"))
        stop.setStyleSheet("background-color:black;")
        stop.setGeometry(QRect(0, 15, 60, 0))
        stop.setIconSize(QtCore.QSize(50, 50))
        stop.setMinimumHeight(40)
        stop.setMinimumWidth(40)
        hbox.addWidget(stop)

        # button dropdown
        setting = QPushButton()
        setting.setIcon(QIcon("icons/setting.png"))
        setting.setStyleSheet("background-color:black;")
        setting.setGeometry(QRect(0, 15, 60, 0))
        setting.setIconSize(QtCore.QSize(50, 50))
        setting.setMinimumHeight(30)
        setting.setMinimumWidth(40)
        setting.clicked.connect(self.openSetting)
        hbox.addWidget(setting)

        self.groupBox.setLayout(hbox)

    def openStorageImagePath(self):
        path = "C:/Users/Public/Pictures"
        path = os.path.realpath(path)
        return os.startfile(path)

    def openSetting(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    myapp.exec_()
    sys.exit()
