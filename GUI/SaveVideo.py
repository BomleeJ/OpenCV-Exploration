"""
see docs: https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
"""

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(1)

fourcc = cv.VideoWriter_fourcc(*'XVID')
FPS = 10.0
WIDTH = 1920
HEIGHT = 1080

out = cv.VideoWriter("files/output.avi", fourcc, FPS, (WIDTH, HEIGHT), isColor=True)

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
