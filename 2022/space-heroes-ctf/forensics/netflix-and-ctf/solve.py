from scapy.all import *

packets = rdpcap('./netflix-and-ctf.pcap')

flag = bytearray()
for p in packets:
    try:
        c = p.load[p.load.index(b'Lit_')+4]
        flag.append(c)
    except:
        continue

flag = flag.decode()
start = flag.find('%')-5
end = flag.find('%', start+7)+1
flag = flag[start:end]
print(flag)
