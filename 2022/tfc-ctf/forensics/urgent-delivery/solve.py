from pwn import *

p = remote('01.linux.challenges.ctf.thefewchosen.com', 54549)

txt = b''

while True:
    try:
        txt += p.recv()
        p.sendline()
    except:
        break

with open('murmur.txt', 'wb') as f:
    f.write(txt)
