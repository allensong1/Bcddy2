# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formAutoClick.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_formAutoClick(object):
    def setupUi(self, formAutoClick):
        formAutoClick.setObjectName("formAutoClick")
        formAutoClick.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(formAutoClick)
        self.pushButton.setGeometry(QtCore.QRect(130, 110, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(formAutoClick)
        self.lineEdit.setGeometry(QtCore.QRect(120, 200, 113, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(formAutoClick)
        self.pushButton.clicked.connect(formAutoClick.closeAndReturn1)
        QtCore.QMetaObject.connectSlotsByName(formAutoClick)

    def retranslateUi(self, formAutoClick):
        _translate = QtCore.QCoreApplication.translate
        formAutoClick.setWindowTitle(_translate("formAutoClick", "Form"))
        self.pushButton.setText(_translate("formAutoClick", "关闭并返回"))

