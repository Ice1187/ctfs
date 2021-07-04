# By trying, when input 7 char, the length of output increase a block, and the length of output wth 6 char is (96/2)=48 bytes(hexilify, 2 digit is 1 char). So, the length of FLAG is (48-16)-7=25.

from pwn import *

# p = process('./best_crypto_service.py')

flag = 'd0n7_7ruzt_DeF4uL7_V4lu3z'
find = True 

while find:
    find = False
    for i in range(32, 127):
        p = remote('baby_homework.ichsa.ctf.today', 8010, level='error')
        p.recvline()
        s = 'A'*(64-len(flag)-1) + flag + chr(i) + 'A'*(64-len(flag)-1)
        p.sendline(s)
        ret = p.recvline()
        if ret[:128] == ret[128:128+128]:
            flag += chr(i)
            find = True
            break
        p.close()
    print(f'Flag: {flag}')
