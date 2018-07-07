from numpy import *
from imutils import *
from matplotlib import pyplot as plt
import sys
import os
import shutil
import cv2
import math

def normalize(img, size, min, max):

    for i in range(size):
        for j in range(size):
                 img[i, j] = (255 * (img[i, j] - min)) / (max - min)

    return img
