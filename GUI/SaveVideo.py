"""
see docs: https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
"""

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(1)

fourcc = cv.VideoWriter_fourcc(*"MJPG")
FPS = 20.0
WIDTH = 640
HEIGHT = 480

out = cv.VideoWriter("output.mp4", fourcc, FPS, (WIDTH, HEIGHT))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    out.write(frame)
    
    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord("q"):
        break


cap.release()
out.release()
cv.destroyAllWindows()
