# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoListWidget1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(415, 279)
        self.listWidgetColors = QtWidgets.QListWidget(Dialog)
        self.listWidgetColors.setGeometry(QtCore.QRect(160, 30, 221, 121))
        self.listWidgetColors.setObjectName("listWidgetColors")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetColors.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetColors.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetColors.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetColors.addItem(item)
        self._label = QtWidgets.QLabel(Dialog)
        self._label.setGeometry(QtCore.QRect(30, 30, 101, 16))
        self._label.setObjectName("_label")
        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(100, 220, 191, 16))
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.listWidgetColors.isSortingEnabled()
        self.listWidgetColors.setSortingEnabled(False)
        item = self.listWidgetColors.item(0)
        item.setText(_translate("Dialog", "Red $10"))
        item = self.listWidgetColors.item(1)
        item.setText(_translate("Dialog", "Blue $5"))
        item = self.listWidgetColors.item(2)
        item.setText(_translate("Dialog", "Green $2"))
        item = self.listWidgetColors.item(3)
        item.setText(_translate("Dialog", "Pink $7"))
        self.listWidgetColors.setSortingEnabled(__sortingEnabled)
        self._label.setText(_translate("Dialog", "Choose Candy Color"))