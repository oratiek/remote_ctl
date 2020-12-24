import socket
import os

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.105.38",5000))
    command = input("command;")
    if command.lower() == "exit":
        print("client session closed")
        break
    else:
        s.send(command.encode())
        output = s.recv(1024)
        print(output.decode())
