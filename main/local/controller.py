import socket
import os
from excute import excute

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost",5000))
s.listen()
while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    command = data.decode()
    output = excute(command)
    print(output)
    print(output.decode())
    conn.sendall(output)
