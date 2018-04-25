# coding:utf-8

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from sign_face import Ui_SignFaceWindow
from save_face import Ui_Dialog
import time
import sys
from driver.cam import cams
import cv2
import config
import os


class MainWindow(QMainWindow, Ui_SignFaceWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        # 定时器
        self.timer = QTimer()

        self.timer.setInterval(100)
        self.timer.timeout.connect(self.flush_image)
        self.timer.start()
        self.face = None

    def flush_image(self):
        photo, face = cams.get_photo()
        if photo is not None:
            if face is not None:
                x, y, h, w = face
                roi = photo[y:y + h, x:x + w]
                img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
                self.face = img

                photo = cams.draw_text(photo, face_rects=face, text=u"scaning")
            height, width, bytesPerComponent = photo.shape
            bytesPerLine = bytesPerComponent * width
            cv2.cvtColor(photo, cv2.COLOR_BGR2RGB, photo)
            image = QImage(photo.data, width, height, bytesPerLine, QImage.Format_RGB888)

            self.cam_label.setPixmap(QPixmap.fromImage(image).scaled(self.cam_label.width(), self.cam_label.height()))
            cv2.waitKey(1)
        else:
            print "err"

    def show_save_diglog(self):
        if self.face is not None:
            save_dialog = SaveDialog(self)
            save_dialog.show()


class SaveDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(SaveDialog, self).__init__(parent=parent)
        self.setupUi(self)

        self.cancel_btn.clicked.connect(self.close)
        self.save_btn.clicked.connect(self.save)

        photo = parent.face
        self.photo = photo
        height, width, bytesPerComponent = photo.shape
        bytesPerLine = bytesPerComponent * width

        with open(os.path.join(config.BUFFER_DIR, "buffer"), "wb") as f:
            photo.tofile(f)

        with open(os.path.join(config.BUFFER_DIR, "buffer"), "rb") as f:
            image = QImage(f.read(), width, height, bytesPerLine, QImage.Format_RGB888)

            self.face_label.setPixmap(QPixmap.fromImage(image).scaled(self.face_label.width(), self.face_label.height()))
            self.image = image

    def save(self):
        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.timeout.connect(self.save_image)
        timer.start()

    def save_image(self):
        t = self.name_input.text()
        if len(t) >= 2:
            self.image.save(os.path.join(config.DATA_PATH, t + ".jpg"), "jpg", 100)
            button = QMessageBox.warning(
                self,
                u"提示",
                u"录入成功",
                QMessageBox.Close
            )
            self.close()

        else:
            QMessageBox.warning(
                self,
                u"错误",
                u"姓名长度必须大于1！",
                QMessageBox.Yes
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())