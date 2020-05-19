import socket
import pickle


class Connect:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.0.0.183"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            # return pickle.loads(self.client.recv(2048))
        except:
            return None

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
            return None