from pwn import *

r = remote('35.221.81.216', 30718)

ans = '3141592653589793/0001000000000000000'
print(ans)
print(b64d(ans))
print(b64d(ans))

r.recv()
r.sendline(b64d(ans))
r.interactive()

