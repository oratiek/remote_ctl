import socket
import os

def save(content, filename):
    with open(filename, "wb") as f:
        f.write(content)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 5000))
command = "ftp"
s.send(command.encode())
data = s.recv(8192)
save(data, "test.jpg")
