# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoFontComboBox.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 16))
        self.label.setObjectName("label")
        self.fontComboBox = QtWidgets.QFontComboBox(Dialog)
        self.fontComboBox.setGeometry(QtCore.QRect(120, 30, 222, 22))
        self.fontComboBox.setObjectName("fontComboBox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 47, 13))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(120, 80, 221, 151))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Selected Font:"))
        self.label_2.setText(_translate("Dialog", "Text:"))
