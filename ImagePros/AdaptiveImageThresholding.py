import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("files/noisy_background.png", cv.IMREAD_GRAYSCALE)

img = cv.medianBlur(img,5) # THIS CAN BE USED TO REMOVE NOISE??

ThresholdValue = 127

ret, binary_global = cv.threshold(img, ThresholdValue, 255, cv.THRESH_BINARY)
"""
The mean is calculated over a block of odd size. the mean is subtracted by
This constant C. any pixel value lower than this mean - C is set to 0, otherwise it is set to 255. 
without this constant, and pixel value lower than the mean is immeditely set to 0.
"""
Constant = 2  
BlockSize = 9 # ODD numbered Value for the block size

adaptive_mean = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, BlockSize, Constant)

adaptive_gaussian = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, BlockSize, Constant)

titles = ['Original Image', 'Global Thresholding (v = 127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, binary_global, adaptive_mean, adaptive_gaussian]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
