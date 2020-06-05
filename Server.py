import socketserver
import threading


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    def __init__(self):
        super().__init__()




class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        try:
            data = str(self.request.recv(1024), 'utf-8')
            current_thread = threading.current_thread()
            response = bytes(f'Answer from {current_thread.name}, CC: {data}', 'utf-8')
            self.request.sendall(response)
        except Exception as e:
            print(f'Excepted: {e} || in handle')


if __name__ == '__main__':
    ip = 'localhost'
    port = 27036
    server = ThreadedTCPServer((ip, port), ThreadedTCPRequestHandler)
    try:
        server_thread = threading.Thread(target=server.serve_forever(), daemon=True)
        server_thread.start()
    except Exception as e:
        print(f'Excepted: {e}')
