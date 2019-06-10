# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(833, 466)
        self.pushButton = QtWidgets.QPushButton(MainForm)
        self.pushButton.setGeometry(QtCore.QRect(70, 110, 161, 71))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(MainForm)
        self.lineEdit.setGeometry(QtCore.QRect(380, 140, 113, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(MainForm)
        self.pushButton.clicked.connect(MainForm.testButton1)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "北蔡大调研辅助工具"))
        self.pushButton.setText(_translate("MainForm", "测试按钮"))

