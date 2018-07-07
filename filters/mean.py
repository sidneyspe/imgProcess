import sys
import os
sys.path.append(os.path.abspath("filters/"))
from util import *

def mean (img):
    imgOut = img.copy()
    w, h = img.shape[::-1]

    pixels = [0]*10

    for i in range(1, w-1):
        for j in range(1, h-1):

            pixel = img[i - 1, j - 1] + img[i - 1, j] + img[i - 1, j + 1] + img[i, j - 1] + img[i, j] + img[i, j + 1] + img[i + 1, j - 1] + img[i + 1, j] + img[i + 1, j + 1]
            pixel = pixel/9
            imgOut[i,j] = pixel

    return imgOut
