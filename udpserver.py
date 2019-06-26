import socket
from hexdump import hexdump

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
print("Listen on {}:{}".format(UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("From [{}], message {} bytes:".format(addr, len(data)))
    hexdump(data)
