from PyQt5 import QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        radius = 30
        self.createLayout()
        self.setGeometry(1200, 0, 200, 10)
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
        self.setWindowOpacity(0.9)

        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox()

        hbox = QHBoxLayout()
        edit = QLineEdit()

        # button start
        start = QPushButton()
        start.setIcon(QIcon("icons/start.png"))
        start.setGeometry(QRect(0, 25, 60, 0))
        start.setStyleSheet("background-color:black;")
        start.setIconSize(QtCore.QSize(60, 60))
        edit.setFont(QFont("START", 15, QFont.Bold))
        start.setMinimumHeight(50)
        hbox.addWidget(start)

        # button image path
        folder = QPushButton()
        folder.setIcon(QIcon("icons/folder.png"))
        folder.setStyleSheet("background-color:black;")
        folder.setGeometry(QRect(30, 25, 120, 0))
        folder.setIconSize(QtCore.QSize(75, 75))
        folder.setMinimumHeight(50)
        hbox.addWidget(folder)

        # button stop
        stop = QPushButton()
        stop.setIcon(QIcon("icons/stop.png"))
        stop.setStyleSheet("background-color:black;")
        stop.setGeometry(QRect(30, 25, 180, 0))
        stop.setIconSize(QtCore.QSize(60, 60))
        stop.setMinimumHeight(50)
        hbox.addWidget(stop)

        # button dropdown
        dropdown = QPushButton()
        dropdown.setIcon(QIcon("icons/dropdown.png"))
        dropdown.setStyleSheet("background-color:black;")
        dropdown.setGeometry(QRect(30, 25, 180, 0))
        dropdown.setIconSize(QtCore.QSize(60, 60))
        dropdown.setMinimumHeight(50)
        hbox.addWidget(dropdown)

        self.groupBox.setLayout(hbox)
    # def select(self):


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    window = Window()
    myapp.exec_()
    sys.exit()
