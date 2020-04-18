from cv2 import cv2
# import numpy as np
class webCam:
    def __init__(self, crate):
        self.cap = cv2.VideoCapture(0)
        self.crate = crate

    def read(self):
        ret, frame = self.cap.read()
        y, x = frame.shape[0:2]
        x = int(x / self.crate)
        y = int(y / self.crate)
        frame = cv2.resize(frame, (x, y))
        frame = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
        return frame

if __name__ == "__main__":
    W = webCam(10)
    print(W.read())
    while True:
        cv2.imshow("frame", W.read())
        k = cv2.waitKey(5)& 0xFF
        if k==27:
            break