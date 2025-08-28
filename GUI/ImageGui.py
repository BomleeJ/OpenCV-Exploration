import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("files/starrynight.jpg"))

if img is None:
    sys.exist("Could not read the image.")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("files/starrynight.png", img)
    """
    cv.imwrite Write the image to a file?
    """