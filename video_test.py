from cv2 import cv2
from time import sleep
import numpy as np

from Server.switch import Switch
from FMC.send_video import sendVideo as sendVideo_FMC
from Controller.recv_video import recvVideo as recvVideo_controller

from FMC.webcam import webCam

video_switch = Switch("127.0.0.1", 1234, 2345, 2048)
video_switch.run()

# SendFMC = sendVideo_FMC(float("inf"))
SendFMC = sendVideo_FMC(10)
RecvController = recvVideo_controller()

RecvController.run()
SendFMC.run()

if SendFMC.connect("127.0.0.1", 1234) == 0:
    print("CANT CONNECT!")
if RecvController.connect("127.0.0.1", 2345) == 0:
    print("CANT CONNECT!")

WC = webCam(0, 20)


while True:
    frame = WC.encoded_read()
    # cv2.imshow("ori", cv2.imdecode(frame, cv2.IMREAD_GRAYSCALE))
    SendFMC.change_video(frame)
    frame_get = RecvController.get_video()
    # print("fget", frame_get)
    if frame_get != None:
        frame_get = np.fromstring(frame_get, np.uint8)
        print(frame_get)
        try:
            frame_get = cv2.imdecode(frame_get, cv2.IMREAD_GRAYSCALE)
            # print(frame_get.size)
        # print("controller", frame_get)
            cv2.imshow("frame", frame_get)
        except:
            print("=======EXCEPTION=======")
            pass
    k = cv2.waitKey(5)& 0xFF
    if k==27:
        break
    sleep(0.1)


del(RecvController)
del(SendFMC)
del(video_switch)