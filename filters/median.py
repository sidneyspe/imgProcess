from .util import *


def median(img):
    imgOut = img.copy()
    w, h = img.shape[::-1]

    pixels = [0]*10

    for i in range(1, w-1):
        for j in range(1, h-1):

            pixels[0] = img[i - 1, j - 1]
            pixels[1] = img[i - 1, j]
            pixels[2] = img[i - 1, j - 1]
            pixels[3] = img[i - 1, j + 1]
            pixels[4] = img[i, j - 1]
            pixels[5] = img[i, j]
            pixels[6] = img[i, j + 1]
            pixels[7] = img[i + 1, j - 1]
            pixels[8] = img[i + 1, j]
            pixels[9] = img[i + 1, j + 1]

            pixels.sort()
            pixel = pixels[4]

            imgOut[i, j] = pixel

    return imgOut
