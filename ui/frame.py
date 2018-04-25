# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from config import IMG_PATH

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(835, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(50, 400, 721, 51))


        font = QtGui.QFont()
        font.setFamily("TlwgTypewriter")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAccessibleName("")
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setEnabled(False)
        self.calendarWidget.setGeometry(QtCore.QRect(350, 130, 451, 201))
        self.calendarWidget.setNavigationBarVisible(False)
        self.calendarWidget.setDateEditEnabled(False)
        self.calendarWidget.setObjectName("calendarWidget")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setEnabled(False)
        self.timeEdit.setGeometry(QtCore.QRect(530, 60, 118, 27))
        self.timeEdit.setObjectName("timeEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 291, 311))
        self.label_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.setScaledContents(True)
        self.label_2.setPixmap(QtGui.QPixmap(os.path.join(IMG_PATH, "black.jpg")))
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.show()

        self.image = None
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人脸识别智能考勤"))
        self.label.setText(_translate("MainWindow", "欢迎使用"))



