import socket

hostname = socket.gethostname()
ips = socket.gethostbyname_ex(hostname)[2]
print(ips)

