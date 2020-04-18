from socket import *

class socketClient:
    MAX_RECEIVE = 25600
    def __init__(self, ip, port):
        self.my_socket = socket(AF_INET, SOCK_STREAM)
        self.my_socket.connect((ip, port))
        self.my_socket.settimeout(2)
        print("CONNECTED")

    def send(self, data):
        self.my_socket.sendall(data)

    def receive(self):
        return self.my_socket.recv(self.MAX_RECEIVE)
        