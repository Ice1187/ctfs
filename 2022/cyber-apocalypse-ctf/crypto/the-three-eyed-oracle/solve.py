from pwn import *
from Crypto.Util.Padding import pad
import random

'''
FLAG = b'HTB{AAAAAAAAAAAAAAAA}'
prefix = b'\xde\xad\be\xef'*3

while True:
    msg = input('> ').encode()
    padded = pad(prefix+msg+FLAG, 16)
    print(padded)
    print(padded[-16:])
'''

p = remote('167.172.56.180', 32116)

flag = b'}'


def guess(c):
    p.recv()
    dummy = b'A'*4
    dummy2 = b'B'*(11-4+len(flag)+1)
    oracle = pad(c + flag, 16)
    oracle_len = len(oracle)
    assert oracle_len % 16 == 0
    msg = (dummy + oracle + dummy2).hex().encode()
    p.sendline(msg)
    res = bytes.fromhex(p.recv().strip().decode())
    guess = res[16:16+oracle_len]
    answer = res[-oracle_len:]
    return guess == answer


p.recv()
while b'HTB{' not in flag:
    print('round:', len(flag))
    for i in range(0x20, 0x7f):
        c = chr(i).encode()
        print(c)
        if guess(c):
            flag = c + flag
            print('Flag:', flag.decode())
            break


print('Flag:', flag.decode())
