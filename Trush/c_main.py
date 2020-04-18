from client import socketClient
from webcam import webCam

ip = "45.249.94.168"
port = "1234"

if __name__ == "__main__":
    
    # Initialize GPIO devices

    W = webCam()
    ip = "127.0.0.1"
    S = socketClient(ip, port)

    while True:
        video = W.read()
        message = {"video": video}
        S.send(str(message).encode("utf8"))
        message = S.receive()
        
        message = message.decode("utf8")
        # OPERATION