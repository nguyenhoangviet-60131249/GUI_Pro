from PyQt5 import QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt
import os


class Window(QWidget):
    def __init__(self):
        super().__init__()
        radius = 28
        self.createLayout()
        self.setGeometry(1200, 0, 250, 10)
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
        start.setIconSize(QtCore.QSize(63, 63))
        start.setMinimumHeight(50)
        start.setMinimumWidth(60)
        hbox.addWidget(start)

        # button image path
        folder = QPushButton()
        folder.setIcon(QIcon("icons/folder.png"))
        folder.setStyleSheet("background-color:black;")
        folder.setGeometry(QRect(20, 15, 40, 0))
        folder.setIconSize(QtCore.QSize(85, 85))
        folder.setMinimumHeight(50)
        folder.setMinimumWidth(60)
        folder.clicked.connect(self.openStorageImagePath)
        hbox.addWidget(folder)

        # button stop
        stop = QPushButton()
        stop.setIcon(QIcon("icons/stop.png"))
        stop.setStyleSheet("background-color:black;")
        stop.setGeometry(QRect(0, 15, 60, 0))
        stop.setIconSize(QtCore.QSize(60, 60))
        stop.setMinimumHeight(50)
        stop.setMinimumWidth(60)
        hbox.addWidget(stop)

        # button dropdown
        setting = QPushButton()
        setting.setIcon(QIcon("icons/setting.png"))
        setting.setStyleSheet("background-color:black;")
        setting.setGeometry(QRect(0, 15, 60, 0))
        setting.setIconSize(QtCore.QSize(60, 60))
        setting.setMinimumHeight(10)
        setting.setMinimumWidth(50)
        hbox.addWidget(setting)

        self.groupBox.setLayout(hbox)

    def openStorageImagePath(self):
        path = "C:/Users/Public/Pictures"
        path = os.path.realpath(path)
        return os.startfile(path)


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    myapp.exec_()
    sys.exit()
