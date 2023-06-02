from .util import *


def prewitt(img):
    imgOut = img.copy()
    w, h = img.shape[::-1]

    for i in range(1, w-1):
        for j in range(1, h-1):

            value1 = math.fabs((img[i - 1, j - 1] + img[i - 1, j] + img[i - 1, j + 1]) - (
                img[i + 1, j - 1] + img[i + 1, j] + img[i + 1, j + 1]))
            value2 = math.fabs((img[i + 1, j + 1] + img[i, j + 1] + img[i - 1, j + 1]) - (
                img[i + 1, j - 1] + img[i, j - 1] + img[i - 1, j - 1]))
            pixel = value1 + value2
            imgOut[i, j] = pixel

    min, max, _, _ = cv2.minMaxLoc(imgOut)
    imgOut = normalize(imgOut, w, min, max)

    return imgOut
