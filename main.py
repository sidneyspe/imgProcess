import cv2

from filters.highBoost import *
from filters.prewitt import *
from filters.gradient import *
from filters.median import *
from filters.sobel import *
from filters.highBasicPass import *
from filters.crossGradient import *
from filters.mean import *

#############################################################################

img = cv2.imread("img/lena.png", 0)
w, h = img.shape[::-1]
# img_high_boost = highBoost(img,w)
# img_prewitt = prewitt(img)
# img_gradient = gradient(img)
# img_median = median(img)
# img_sobel = sobel(img)
# img_high_basic_pass = highBasicPass(img)
# img_cross_gradient = crossGradient(img)
# img_mean = mean(img)

cv2.imshow("Original", img)
# cv2.imshow("High Boost", img_high_boost)
# cv2.imshow("Prewitt", img_prewitt)
# cv2.imshow("Gradient", img_gradient)
# cv2.imshow("Median", img_median)
# cv2.imshow("Sobel", img_sobel)
# cv2.imshow("High Basic Pass", img_high_basic_pass)
# cv2.imshow("Cross Gradient", img_cross_gradient)
# cv2.imshow("Mean", img_mean)

cv2.waitKey(0)
cv2.destroyAllWindows()
