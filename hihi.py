import socket

UDP_IP = "127.0.0.1"
#UDP_IP = "159.65.140.240"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.setblocking(0)
#sock.bind(("0.0.0.0", 9999))
print("Listen on {}:{}".format(UDP_IP, UDP_PORT))

try: input = raw_input
except NameError: pass

while True:
    d = input("hi:")
    sock.sendto(d.encode(), (UDP_IP, UDP_PORT))
    data, addr = sock.recvfrom(1024)
    print("From [{}], message {} bytes: {}".format(addr, len(data), repr(data)))