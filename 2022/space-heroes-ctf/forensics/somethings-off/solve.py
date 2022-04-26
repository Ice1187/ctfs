from scapy.all import *

packets = rdpcap('./challenge.pcap')

icmps = packets[ICMP]
tcps = packets[TCP]
udps = packets[UDP]

flag = ''

# exfiltration from TCP sequence number
t_info = bytearray()
for t in tcps[:(100-19+1)]:
    t_info.append(t.seq)
t_info = t_info.decode()
flag += t_info[int(t_info[1:3])+7:int(t_info[4:6])+8] + '_'
print(t_info)

# exfiltration from ICMP code
i_info = bytearray()
for i in icmps[:75]:
    i_info.append(i.code)
for i in icmps[-30:]:
    i_info.append(i.code)
i_info = i_info.decode()
flag += i_info[int(i_info[1:3])+7:int(i_info[4:6])+8] + '_'
print(i_info)

# exfiltration from UDP dest. port
u_info = bytearray()
for u in udps[8:8+(204-140+1)]:
    u_info.append(u.dport)
u_info = u_info.decode()
flag += u_info[int(u_info[1:3])+7:int(u_info[4:6])+8] + '_'
print(u_info)

t_info = bytearray()
for t in tcps[(100-19+1):]:
    t_info.append(t.seq)
t_info = t_info.decode()
flag += t_info[int(t_info[1:3])+7:int(t_info[4:6])+8] + '_'
print(t_info)

# exfiltration from ICMP sequence number (BE)
i_info = bytearray()
for i in icmps:
    i_info.append(i.seq)

start = i_info.find(b']2E')
end = i_info.find(b'[', start+10)+1
i_info = i_info[start:end].decode()[::-1]
flag += i_info[int(i_info[1:3])+7:int(i_info[4:6])+8] + '_'
print(i_info)

print('Flag:', flag, '-->', 'New_base_on_planet_hoth')
