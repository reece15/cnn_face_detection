# coding:utf-8

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from frame import Ui_MainWindow
import time
import sys
from driver.cam import cams
import cv2
from driver.face_search import search_one, load_feat, feats, images, net
import traceback
import config


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        # 定时器
        self.timer = QTimer()

        self.timer.setInterval(100)
        self.timer.timeout.connect(self.flush_image)
        self.timer.start()

        # 时间刷新
        self.timer_time = QTimer()

        self.timer_time.setInterval(60000) #60000
        self.timer_time.timeout.connect(self.flush_time)
        self.timer_time.start()
        self.flush_time()
        self.cnt_timer = 5 # 延时刷新

    def flush_image(self):
        print "timer running!"
        photo, face = cams.get_photo()
        if photo is not None:
            if face is not None:
                x, y, h, w = face

                gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
                roi = gray[y:y + h, x:x + w]
                faces = cv2.resize(roi, (128, 128), interpolation=cv2.INTER_CUBIC)
                try:
                    max_s, index, name = search_one(load_feat(faces, net), feats, images)
                    print "max_s:{max_s}|index:{index}|name:{name}".format(**vars())
                except:
                    print traceback.format_exc()
                else:
                    uname = "no name!"
                    if max_s > config.TH:
                        uname = name

                        self.cnt_timer = 5
                        self.label.setText("欢迎您, {uname}".format(uname=uname))
                        photo = cams.draw_text(photo, face_rects=face, text=u"welcome {} p:{:.2f}".format(unicode(uname, "utf-8"), max_s))
                    else:

                        self.cnt_timer -= 1

                        if self.cnt_timer <= 0:
                            self.label.setText("欢迎使用")
                        photo = cams.draw_text(photo, face_rects=face, text=u"Sorry {name}".format(name=uname))
            else:
                self.cnt_timer -= 1

                if self.cnt_timer == 0:
                    self.label.setText("欢迎使用")

            height, width, bytesPerComponent = photo.shape
            bytesPerLine = bytesPerComponent * width
            cv2.cvtColor(photo, cv2.COLOR_BGR2RGB, photo)
            image = QImage(photo.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.image = image
            self.label_2.setPixmap(QPixmap.fromImage(image).scaled(self.label_2.width(), self.label_2.height()))
            cv2.waitKey(1)

        else:
            print "err"

    def flush_time(self):
        now_day = time.strftime("%Y-%m-%d", time.localtime())
        self.calendarWidget.setSelectedDate(QDate.fromString(now_day, 'yyyy-MM-dd'))
        self.timeEdit.setTime(QTime.currentTime())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

