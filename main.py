import sys
from PyQt5 import QtGui, QtCore
from PyQt5.Qt import Qt
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.WIDTH = 75
        self.HEIGHT = 225
        self.resize(self.WIDTH, self.HEIGHT)

        # Widget
        self.centralwidget = QWidget(self)
        self.centralwidget.resize(self.WIDTH, self.HEIGHT)

        # Initial
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.6)

        radius = 30
        self.centralwidget.setStyleSheet(
            """
            background:rgb(0,0,0);
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )
        self.ShowLayOut()

    def ShowLayOut(self):
        self.vbox = QVBoxLayout()
        self.createLayOut()
        self.leftWindow()
        self.show()

    def createLayOut(self):
        # camera
        self.camera = QPushButton(self)
        # left, top,width,height
        self.camera.setGeometry(QRect(0, 30, 75, 80))
        self.camera.setStyleSheet("background-color:black;")
        self.camera.setIcon(QtGui.QIcon("icons/cam.png"))
        self.camera.setIconSize(QtCore.QSize(65, 65))
        self.camera.setMinimumHeight(50)

        # image path
        self.image = QPushButton(self)
        self.image.setGeometry(QRect(0, 90, 75, 120))
        self.image.setStyleSheet("background-color:black;")
        self.image.setIcon(QtGui.QIcon("icons/folder.png"))
        self.image.setIconSize(QtCore.QSize(85, 75))
        self.image.setMinimumHeight(50)

    # move app to left of Window
    def leftWindow(self):
        qr = self.frameGeometry()
        qr.moveRight(1850)
        self.move(qr.bottomRight())


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())
