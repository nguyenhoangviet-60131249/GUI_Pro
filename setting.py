# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setGeometry(1480, 50, 370, 75)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 160, 20))
        self.checkBox.setStyleSheet("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(210, 20, 200, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 50, 93, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.selectPath)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 52, 250, 16))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "    background-color:white\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cài đặt"))
        self.checkBox.setText(_translate("Form", "Nhận diện khuôn mặt"))

        self.checkBox_2.setText(_translate("Form", "Nhận diện qua camera"))
        self.pushButton.setText(_translate("Form", "Browse"))

    def selectPath(self):
        self.dir_path = QFileDialog.getExistingDirectory()
        return self.dir_path


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
