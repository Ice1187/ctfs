from scapy.all import *

p = rdpcap('./capture.pcap')
ip = []
for i in range(0, len(p), 2):
    ip.append(list(map(int, p[i+1][DNSRR].rdata.split('.'))))

ip2 = []
for i in ip:
    if (i[3] & 0x1) == 0:
       ip2.append(i) 

ip2 = sorted(ip2, key=lambda x: (x[2] & 0xf))

flag = ''
data = '795ab8bcecd3dfdd99a5b6ac1536858d090877524d71547da7a70816fdd7'
for i in range(0, len(ip2)):
    idx = i*2*2
    flag += chr(ip2[i][1] ^ int(data[idx:idx+2], 16))
    idx = (i*2+1)*2
    flag += chr(ip2[i][1] ^ int(data[idx:idx+2], 16))

flag += '@flare-on.com'
print(flag)
