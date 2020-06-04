import socketserver
import threading


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)


if __name__ == '__main__':
    ip = 'localhost'
    port = 27036
    with ThreadedTCPServer((ip, port), ThreadedTCPRequestHandler) as server:
        server_thread = threading.Thread(target=server.serve_forever())
        server_thread.daemon = True
        server_thread.start()
