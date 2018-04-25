# coding: utf-8

import os


BASE_PATH = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_PATH, "models")

DATA_PATH = os.path.join(BASE_PATH, "data")

IMG_PATH = os.path.join(BASE_PATH, "images")

FACE_POINT = 8

BUFFER_DIR = os.path.join(BASE_PATH, "tmp")

FONT_PATH = os.path.join(BASE_PATH, "font")

TH = 0.7