# coding:utf-8
import os
import config
import caffe
import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy
import re

cnn_model = os.path.join(config.MODEL_PATH, "cnn_iter_3560000.caffemodel")
pro_txt = os.path.join(config.MODEL_PATH, "cnn_deploy.prototxt")


def load_cnn_net():
    caffe.set_mode_cpu()
    net = caffe.Net(pro_txt, cnn_model, caffe.TEST)
    return net


def load_image_paths(p):
    res = []
    if os.path.isdir(p):
        files = os.listdir(p)
        for file in files:
            f = os.path.join(config.DATA_PATH, file)
            yield f
            res.append(f)


def load_feats(net, images):
    feats = np.zeros((100, 256), dtype=np.float32)
    inp = []
    for i, image in enumerate(images):
        input = cv2.imread(image, 0)
        input = cv2.resize(input, (128, 128), interpolation=cv2.INTER_CUBIC)
        inp.append(input)
        img_blobinp = input[np.newaxis, np.newaxis, :, :] / 255.0
        net.blobs['data'].reshape(*img_blobinp.shape)
        net.blobs['data'].data[...] = img_blobinp
        net.blobs['data'].data.shape
        net.forward()
        feature = net.blobs['eltwise_fc1'].data
        feats[i, :] = feature
    return feats, inp


def load_feat(image, net):

    input = cv2.resize(image, (128, 128), interpolation=cv2.INTER_CUBIC)
    img_blobinp = input[np.newaxis, np.newaxis, :, :] / 255.0
    net.blobs['data'].reshape(*img_blobinp.shape)
    net.blobs['data'].data[...] = img_blobinp
    net.blobs['data'].data.shape
    out = net.forward()
    feature = net.blobs['eltwise_fc1'].data
    return feature


def search_one(feat, feats, images):

    max_s = 0
    max_item = None
    for index, item in enumerate(images):
        s = scipy.spatial.distance.cosine(feats[index, :], feat)
        similar = 1 - s
        print similar,  s
        if similar > max_s:
            max_s = similar
            max_item = index

    return max_s, max_item, re.split("[\./]", images[max_item])[-2]

net = load_cnn_net()
images = list(load_image_paths(config.DATA_PATH))
feats, inps =load_feats(net, images)

