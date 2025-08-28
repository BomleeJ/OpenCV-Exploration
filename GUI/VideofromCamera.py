"""
see docs: https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
"""

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(1) #IT WORKS WITH 1, 0 DOES NOT WORK MacOS

if not cap.isOpened(): #Video Capture Object https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html
    cap.open(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # Images are processed as numpy arrays in BGR config. to see in grey we use the Macro? cv.COLOR_BGR2GRAY
    cv.imshow("frame", gray)
    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()