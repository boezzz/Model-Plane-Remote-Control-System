from cv2 import cv2
from numpy import fromstring
from numpy import uint8

def video_decode(encoded):
    try:
        return cv2.imdecode(fromstring(encoded, uint8), cv2.IMREAD_COLOR)
    except:
        return None