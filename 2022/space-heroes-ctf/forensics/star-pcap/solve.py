from base64 import b64decode
from scapy.all import *

packets = rdpcap('./star.pcap')

flag = bytearray()
for p in packets:
    flag.append(p[2].code)

flag = flag.decode()
flag = b64decode(flag).decode()
print('Flag:', flag)
