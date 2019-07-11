import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.setblocking(0)
#sock.bind((UDP_IP, 9999))
print("Listen on {}:{}".format(UDP_IP, UDP_PORT))

while True:
    d = raw_input("hi:")
    sock.sendto(d, ("159.65.140.240", 5005))
    data, addr = sock.recvfrom(1024)
    print("From [{}], message {} bytes: {}".format(addr, len(data), repr(data)))