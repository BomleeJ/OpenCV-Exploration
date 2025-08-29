import numpy as np
import cv2 as cv

"""
see docs: https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html
"""

### SCALING

img = cv.imread("files/messi.jpg")

res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_LINEAR)

cv.imwrite("files/messi_resized.jpg", res)

### TRANSLATION

"""
This uses a 2 x 3 matrix to translate the image.

| 1 0 Tx |
| 0 1 Ty |

Tx and Ty are the translation factors. (num pixels to move in x and y direction)
"""

rows, cols, _ = img.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])

translated = cv.warpAffine(img, M, (cols, rows))

cv.imwrite("files/messi_translated.jpg", translated)

### ROTATION

"""
This uses a 2 x 3 matrix to rotate the image.
"""

center = ((cols - 1)/2, (rows - 1)/2)
scale_factor = 1
angle = 90

M = cv.getRotationMatrix2D(center, angle, scale_factor)

rotated = cv.warpAffine(img, M, (cols, rows))

cv.imwrite("files/messi_rotated.jpg", rotated)

