import sys
import os
sys.path.append(os.path.abspath("filters/"))
from util import *

def highBoost (img, w):
    imgOut = img.copy()
    w, h = img.shape[::-1]

    for i in range(1, w-1):
        for j in range(1, h-1):

            pixel = (w * img[i, j] - (img[i - 1, j - 1] + img[i - 1, j] +
            img[i - 1, j + 1] + img[i, j - 1] + img[i, j + 1] +
            img[i + 1, j - 1] + img[i + 1, j] + img[i + 1, j + 1]))

            imgOut[i,j] = pixel

            # print pixel

    min, max, _ , _ = cv2.minMaxLoc(imgOut)
    imgOut = normalize(imgOut, w, min, max)

    return imgOut
