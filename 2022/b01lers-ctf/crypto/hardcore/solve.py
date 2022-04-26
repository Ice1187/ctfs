from pwn import *


def get_flag1():
    flag1 = []
    tmp = [b'0' for _ in range(256)]

    for i in range(256):
        tmp[i] = b'1'
        # p = process('./hardcore.py')
        p = remote('ctf.b01lers.com', 9003)
        p.recv()
        p.sendline(b'1')
        p.recv()
        p.sendline(b''.join(tmp))
        ans = p.recv().decode().strip()
        print(b''.join(tmp), ans)
        flag1.append(ans)
        p.close()
        tmp[i] = b'0'

    print(''.join(flag1))
    return flag1


bin_flag1 = '0110001001100011011101000110011001111011011001000110111101011111011110010110111101110101010111110110110001101001011010110110010101011111011010000110000101110010011001000110001101101111011100100110010101011111011000110110100001100001011011000111001101111101'
flag1 = ''
for i in range(0, len(bin_flag1), 8):
    flag1 += chr(int(bin_flag1[i:i+8], 2))

print(flag1)
