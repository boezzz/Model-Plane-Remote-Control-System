from socket import *
import threading
class socketServer:
    def __init__(self, ip, port):
        self.data_cache = None
        self.command_cache = None

        self.my_socket = socket(AF_INET, SOCK_STREAM)
        self.my_socket.bind((ip, port))

        self.my_socket.listen(10)

    def run(self, function):
        while True:
            conn, addr = self.my_socket.accept()
            t = threading.Thread(target=function, args=(conn,))
            t.start()