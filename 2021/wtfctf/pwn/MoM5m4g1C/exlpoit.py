from pwn import *

p = process('./a.out')

p.recvline()

p.send
