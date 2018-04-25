# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_face.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_SignFaceWindow(object):
    def setupUi(self, SignFaceWindow):
        self.catching = False
        SignFaceWindow.setObjectName("SignFaceWindow")
        SignFaceWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SignFaceWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cam_label = QtWidgets.QLabel(self.centralwidget)
        self.cam_label.setGeometry(QtCore.QRect(250, 110, 231, 271))
        self.cam_label.setText("")
        self.cam_label.setObjectName("cam_label")
        self.catch_btn = QtWidgets.QPushButton(self.centralwidget)
        self.catch_btn.setGeometry(QtCore.QRect(320, 470, 99, 27))
        self.catch_btn.setObjectName("catch_btn")
        self.catch_btn.clicked.connect(self.catch_clicked)


        # self.sleep_box = QtWidgets.QSpinBox(self.centralwidget)
        # self.sleep_box.setGeometry(QtCore.QRect(290, 470, 48, 27))
        # self.sleep_box.setProperty("value", 5)
        # self.sleep_box.setObjectName("sleep_box")
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setGeometry(QtCore.QRect(220, 470, 67, 31))
        # self.label_2.setObjectName("label_2")
        # self.label_3 = QtWidgets.QLabel(self.centralwidget)
        # self.label_3.setGeometry(QtCore.QRect(350, 470, 67, 31))
        # self.label_3.setObjectName("label_3")
        SignFaceWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SignFaceWindow)
        self.statusbar.setObjectName("statusbar")
        SignFaceWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SignFaceWindow)
        QtCore.QMetaObject.connectSlotsByName(SignFaceWindow)

    def retranslateUi(self, SignFaceWindow):
        _translate = QtCore.QCoreApplication.translate
        SignFaceWindow.setWindowTitle(_translate("SignFaceWindow", "人脸数据录入"))
        self.catch_btn.setText(_translate("SignFaceWindow", "抓取"))
        #self.label_2.setText(_translate("SignFaceWindow", "延时"))
        #self.label_3.setText(_translate("SignFaceWindow", "秒"))

    def catch_clicked(self):
        #val = self.sleep_box.value()
        save_timer = QtCore.QTimer(self)
        save_timer.setSingleShot(True)
        save_timer.timeout.connect(self.save_dialog)
        save_timer.start()

    def save_dialog(self):
        self.show_save_diglog()
        self.face = None
        self.catching = False


    def show_save_diglog(self):
        pass