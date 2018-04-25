# coding:utf-8

import cv2
import config
import os
import numpy
from PIL import Image, ImageFont, ImageDraw
ttfont = ImageFont.truetype(os.path.join(config.FONT_PATH, "fzyy.TTF"), 26)


class Cam(object):

    CONFIG_PATH = "haarcascade_frontalface_alt.xml"

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.classifier = cv2.CascadeClassifier(os.path.join(os.path.dirname(os.path.abspath(__file__)), self.CONFIG_PATH))
        self.mark = Image.open(os.path.join(config.IMG_PATH, "yellow.png"))

    def get_photo(self):
        if self.cap.isOpened():
            ret, img = self.cap.read()
            if ret:
                h, w = img.shape[:2]
                min_size = (int(h/config.FACE_POINT), int(w/config.FACE_POINT))
                face_rects = self.classifier.detectMultiScale(img, 1.2, 2, cv2.CASCADE_SCALE_IMAGE, min_size)
                if len(face_rects) > 0:
                    return img, face_rects[0]
                return img, None
        return None, None

    def draw_text(self, img, face_rects, text=u"welcome admin"):
        x, y, h, w = face_rects
        # cv2.rectangle(img, (int(x), int(y)), (int(x) + int(w), int(y) + int(h)), (0, 255, 0), 2, 0)
        image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(image)
        out = self.mark.resize((w + 50, h + 20))
        image.paste(out, (x - 20, y - 15), mask=out)
        draw.text((int(x + 20), int(y - 20)), text, fill="red", font=ttfont)

        img = cv2.cvtColor(numpy.asarray(image), cv2.COLOR_RGB2BGR)

        return img

    def show_image(self, image):
        pass


cams = Cam()


if __name__ == "__main__":
    while True:

        photo, face = cams.get_photo()
        if photo is None:
            break
        cv2.imshow("img", photo)
        k = cv2.waitKey(1)
        if(k== ord('q')):
            break