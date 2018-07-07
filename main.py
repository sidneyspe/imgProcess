import sys
import os

sys.path.append(os.path.abspath("filters/"))
from highBoost import *
from prewitt import *
from gradient import *
from median import *
from sobel import *
from highBasicPass import *
from crossGradient import *
from mean import *

#############################################################################

img = cv2.imread("img/lena.png",0)
w, h = img.shape[::-1]
# imgHighBoost = highBoost(img,w)
# imgPrewitt = prewitt(img)
# imgGradient = gradient(img)
# imgMedian = median(img)
# imgSobel = sobel(img)
# imgHighBasicPass = highBasicPass(img)
# imgCrossGradient = crossGradient(img)
# imgMean = mean(img)

cv2.imshow("Original", img)
# cv2.imshow("High Boost", imgHighBoost)
# cv2.imshow("Prewitt", imgPrewitt)
# cv2.imshow("Gradient", imgGradient)
# cv2.imshow("Median", imgMedian)
# cv2.imshow("Sobel", imgSobel)
# cv2.imshow("High Basic Pass", imgHighBasicPass)
# cv2.imshow("Cross Gradient", imgCrossGradient)
# cv2.imshow("Mean", imgMean)

cv2.waitKey(0)
cv2.destroyAllWindows()
