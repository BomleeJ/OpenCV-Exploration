"""
docs: https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html
"""



"""
Function Arguements
img : The image where you want to draw the shapes

color : Color of the shape. for BGR, pass it as a tuple, 
eg: (255,0,0) for blue. For grayscale, just pass the scalar value.

thickness : Thickness of the line or circle etc. 
If -1 is passed for closed figures like circles, 
it will fill the shape. default thickness = 1

lineType : Type of line, whether 8-connected, 
anti-aliased line etc. By default, it is 8-connected. 
cv.LINE_AA gives anti-aliased line which looks great for curves.
"""

import numpy as np
import cv2 as cv
WIDTH = 512
HEIGHT = 512
COLOR_CHANNELS = 3

img = np.zeros((WIDTH, HEIGHT, COLOR_CHANNELS), np.uint8)

BLUE = (255, 0, 0)
THICKNESS = 5

"""
Lines take the starting and ending coordinates as arguments.
"""
cv.line(img, (0, 0), (WIDTH-1, HEIGHT-1), BLUE, THICKNESS)

cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0, 255, 255), 3)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "OpenCV", (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)

cv.imshow("img", img)
cv.imwrite("files/drawing.png", img)
time.sleep(10000)