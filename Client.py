import socket
import threading
import json
import time


class Client:

    def __init__(self, ip, port):
        self.sock = socket.socket()
        self.ip = ip
        self.port = port
        self.permission_receive = True

    def connect(self):
        is_connected = False
        while not is_connected:
            try:
                self.sock.connect((self.ip, self.port))
            except Exception as e:
                print(e)
            else:
                is_connected = True
        print('Connected')

    def send(self, message):
        try:
            self.sock.sendall(bytes(message, 'utf-8'))
        except Exception as e:
            print(f'Excepted: {e} || in send')
        else:
            print('Sent')

    def receive(self):
        while True:
            try:
                data = str(self.sock.recv(1024), 'utf-8')
                if data:
                    print(f'Received: {data}')
            except Exception as e:
                print(f'Excepted: {e} || in receive')
                #self.connect()
            time.sleep(0)

    def infinity_sender(self):
        while True:
            client.send(json.dumps({'name': socket.gethostname(),
                                    'admin': False, 'command': None,
                                    'command_number': None}))
            time.sleep(10)


if __name__ == '__main__':
    client = Client('localhost', 27036)
    client.connect()
    threading.Thread(target=client.infinity_sender).start()
    threading.Thread(target=client.receive).start()
