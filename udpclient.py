import socket
from hexdump import hexdump

UDP_IP = "127.0.0.1"
UDP_PORT = 59001

HOST_IP = "127.0.0.1"
HOST_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.sendto(b"hihi", (HOST_IP, HOST_PORT))