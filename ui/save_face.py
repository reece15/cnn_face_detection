# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_face.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(368, 546)
        self.face_label = QtWidgets.QLabel(Dialog)
        self.face_label.setGeometry(QtCore.QRect(70, 70, 231, 241))
        self.face_label.setText("")
        self.face_label.setObjectName("face_label")
        self.save_btn = QtWidgets.QPushButton(Dialog)
        self.save_btn.setGeometry(QtCore.QRect(80, 470, 99, 27))
        self.save_btn.setObjectName("save_btn")
        self.cancel_btn = QtWidgets.QPushButton(Dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(200, 470, 99, 27))
        self.cancel_btn.setObjectName("cancel_btn")

        self.name_input = QtWidgets.QLineEdit(Dialog)
        self.name_input.setGeometry(QtCore.QRect(180, 360, 113, 27))
        self.name_input.setObjectName("name_input")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 360, 71, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "录入"))
        self.save_btn.setText(_translate("Dialog", "录入"))
        self.cancel_btn.setText(_translate("Dialog", "取消"))
        self.name_input.setPlaceholderText(_translate("Dialog", "请输入姓名"))
        self.label.setText(_translate("Dialog", "    姓名"))

