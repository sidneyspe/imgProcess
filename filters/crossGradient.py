from .util import *


def crossGradient(img):
    imgOut = img.copy()
    w, h = img.shape[::-1]

    for i in range(1, w-1):
        for j in range(1, h-1):

            pixel = abs(img[i, j] - img[i - 1, j + 1]) + \
                abs(img[i, j + 1] - img[i - 1, j])
            imgOut[i, j] = pixel

    min, max, _, _ = cv2.minMaxLoc(imgOut)
    imgOut = normalize(imgOut, w, min, max)

    return imgOut
