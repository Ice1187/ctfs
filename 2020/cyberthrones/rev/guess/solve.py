from pwn import *

p = process('./guess')

# p.recvuntil('number:')
p.send('1\n')
print p.recvuntil('is: ')
num = p.recvline().strip()
p.send('1\n')
print num
p.sendline(num)
print p.recv()
