import socketserver
import threading
import openpyxl as ex
import json
#   A    B       C          D             E             F
# Name, IP, last connect, Admin, command to execute, number


class TCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            data = str(self.request.recv(1024), 'utf-8')
            data_json = json.loads(data)
            response = bytes('No commands', 'utf-8')
            self.request.sendall(response)
        except Exception as e:
            print(f'Excepted: {e} || in handle')


if __name__ == '__main__':
    ip = 'localhost'
    port = 27036
    server = socketserver.TCPServer((ip, port), TCPRequestHandler)
    try:
        server_thread = threading.Thread(target=server.serve_forever(), daemon=True)
        server_thread.start()
    except Exception as e:
        print(f'Excepted: {e}')
