import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",5000))
#command = "scp main.py localhost:/Users/keitaro/Desktop/projects4/remote_ctl/"
command = "ls"
s.send(command.encode())
output = s.recv(1024)
print(output.decode())
