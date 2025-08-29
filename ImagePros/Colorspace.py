import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # COLOR CHANGE

    # Note: HSV Has three channels: Hue, Saturation, Value (Brightness)
    # 
    lower_blue = np.array([110, 50, 50]) 
    upper_blue = np.array([130, 255, 255])

    mask = cv.inRange(hsv, lower_blue, upper_blue) # Some sort of filtering Function? Haven't seen it before

    frame_mask = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("mask", mask)
    cv.imshow("frame_mask", frame_mask)
    cv.imshow("frame", frame)

    if cv.waitKey(1) == ord("q"):
        break

cap.release()
