import socket
import threading
from threading import Thread

import statics
import main


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.177.106', 2445))
    server_socket.listen(1)
    (client_socket, adr) = server_socket.accept()

    while True:
        msg = client_socket.recv(1024)
        print("Receive>" + str(msg, "utf8" + "\n"))

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = ('192.168.177.106', 2445)
    client_socket.connect(server_addr)
    while statics.runServer:
        statics.message = input("Send>\n")
        if statics.message == "exitchat":
          t2.stop
          t1.stop()
        client_socket.send(bytes(statics.message, "utf8"))


