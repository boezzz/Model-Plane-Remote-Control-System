from webcam import webCam
from time import time
# One char can have val: 0 ~ 1114111
import numpy as np
def v_encode(img):
    y = len(img)
    x = len(img[0])
    arr = np.zeros((x * y * 4 + 16), dtype=bool)
    x = bin(x)[2:]
    y = bin(y)[2:]
    added_str = ""

    for i in range(8 - len(x)):
        added_str += "0"
    x = added_str + x
    
    for i in range(8):
        arr[i] = int(x[i])

    for i in range(8 - len(y)):
        added_str += "0"
    y = added_str + y

    for i in range(8, 16):
        arr[i] = int(y[i - 8])

    y = len(img)
    x = len(img[0])

    for i in range(y):
        for j in range(x):
            val = bin(int(img[i][j] / 16))[2:]
            added_str = ""
            for k in range(4 - len(val)):
                added_str += "0"
            val = added_str + val
            for k in range(4):
                arr[(i * x + j) * 4 + k + 16] = int(val[k])
    
    encoded = ""
    counter = 0
    flag = 0
    while True:
        current_char = ""
        for i in range(20):
            if counter >= x * y * 4 + 16:
                flag = 1
                break
            current_char += str(int(arr[counter]))
            counter += 1
        current_char = chr(int(current_char, 2))
        encoded += current_char
        if flag == 1:
            break
    return encoded

# def v_decode(encoded):




if __name__ == "__main__":
    W = webCam(10)
    img = W.read()
    t1 = time()
    encoded = v_encode(img)
    t2 = time()
    print(t2 - t1)
    print(len(encoded))