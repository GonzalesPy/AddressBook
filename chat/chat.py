import socket
from threading import Thread
from time import sleep

import statics



def server():
    print(statics.chatPort + statics.myIp)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.177.106', 4455))
    server_socket.listen(1)
    (client_socket, adr) = server_socket.accept()

    while True:
        msg = client_socket.recv(4455)
        print("Receive>" + str(msg, "utf8" + "\n"))

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = ('192.168.177.102', 4455)
    client_socket.connect(server_addr)
    while True:
        message = input("Send>\n")
        client_socket.send(bytes(message, "utf8"))



