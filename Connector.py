import socket
import pickle


class Connect:
    def __init__(self):
        self.port = 5555
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, ip):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect((ip, self.port))
            return True
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

    def disconnect(self):
        self.client.shutdown(socket.SHUT_RDWR)
        self.client.close()