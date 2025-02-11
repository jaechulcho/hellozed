#!/usr/bin/env python

"""cam_capture_opencv.py"""

# import os
import cv2
from datetime import datetime

# os.environ["XGD_SESSION_TYPE"] = "xcb"
# os.environ["QT_QPA_PLATFORM"] = "xcb"

# W, H = 320, 240

capture = cv2.VideoCapture(0, cv2.CAP_V4L)
w = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
h = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)
delay = round(1000 / fps)
print(f"Width: {w} Height: {h} fps: {fps}")
capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
ret = capture.set(cv2.CAP_PROP_FPS, round(fps))
print(f"ret={ret}")
capture.set(cv2.CAP_PROP_FRAME_WIDTH, round(w))
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, round(h))

lastDate = datetime.now().second
counter = 0

if not capture.isOpened():
    exit(0)

while True:
    if datetime.now().second != lastDate:
        lastDate = datetime.now().second
        print(f"{lastDate} Fps: {counter}")
        counter = 1
    else:
        counter += 1
    ret, frame = capture.read()
    if not ret:
        break
    # inversed = ~frame
    cv2.imshow("VideoFrame", frame)
    # cv2.imshow("Inversed", inversed)

    # 정상적으로 동작 하기 위해서는 아래 waitKey가 반드시 필요 함.
    # waitKey(33)은 camera shutter time과 같기 때문에 frame drop 발생
    # frame drop은 회피 하기 위해서는 1 ~ 20 msec 정도로 설정 할 것.
    if cv2.waitKey(20) == 27:
        break

capture.release()
cv2.destroyAllWindows()
