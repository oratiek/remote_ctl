import socket
import os
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost",5000))
s.listen(10)
while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    command = data.decode()
    if command == "ftp":
        print("sending file")
        with open("image.jpg","rb") as f:
            content = f.read()
        print("packet size : {}".format(sys.getsizeof(content)))
        conn.sendall(content)

