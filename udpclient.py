import socket
import argparse
from hexdump import hexdump

parser = argparse.ArgumentParser(description="UDP Client")
parser.add_argument("--remote-host", type=str, default="127.0.0.1", help="Host of remote server")
parser.add_argument("--remote-port", type=int, default=9999, help="Port of remote server")
parser.add_argument("--local-host", type=str, default=None, help="Host of local client")
parser.add_argument("--local-port", type=int, default=None, help="Port of local client")
args = parser.parse_args()

UDP_IP = args.local_host
UDP_PORT = args.local_port

HOST_IP = args.remote_host
HOST_PORT = args.remote_port

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if UDP_IP != None and UDP_PORT != None:
    sock.bind((UDP_IP, UDP_PORT))
    print("[+] Bind client socket at {}:{}".format(UDP_IP, UDP_PORT))
else:
    print("[+] Client socket is random")

sock.sendto(b"init", (HOST_IP, HOST_PORT))
print("[+] Send init data")
print("[+] Receiving...")

while True:
    try:
        data, addr = sock.recvfrom(1024)
        print("> [{}] message {} bytes".format(addr, len(data)))
        hexdump(data)
    except KeyboardInterrupt:
        break