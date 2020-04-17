import socketserver
import time
from PIL import Image
import matplotlib
matplotlib.use('Agg')

SIZE = 224

class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            while True:
                self.data = self.request.recv(1024).strip()
                self.request.send("receive")
                """
                buf = ''
                recvlen = 0
                while recvlen < int(self.data):
                    receivedstr = self.request.recv(1024*1024)
                    recvlen += len(receivedstr)
                    buf += receivedstr
                """
                self.request.send(self.data)
        except KeyboardInterrupt:
            pass

HOST = "" #サーバーのホスト名を入力
PORT = 12345 #クライアントと同じPORTを入力

socketserver.TCPServer.allow_reuse_address = True
SERVER = socketserver.TCPServer((HOST, PORT), TCPHandler)

try:
    SERVER.serve_forever()
except KeyboardInterrupt:
    pass
SERVER.shutdown()
