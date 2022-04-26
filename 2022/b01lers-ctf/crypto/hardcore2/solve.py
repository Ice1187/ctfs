from pwn import *
import multiprocessing as mp
import numpy as np
from itertools import product

thr_num = 10
results = mp.Array('i', range(thr_num))


def job(tmp):
    p = remote('ctf.b01lers.com', 9003)
    p.recv()
    p.sendline(b'2')
    p.recv()
    p.sendline(b''.join(tmp))
    ans = p.recv().decode().strip()
    p.close()

    #print(b''.join(tmp), ans)
    results[mp.current_process().name] = int(ans)
    return ans


def get_flag2():
    flag2 = []
    tmp = [b'0' for _ in range(256)]

    for i in range(32):
        tmp[i] = b'1'
        procs = []
        for id_ in range(thr_num):
            procs.append(mp.Process(target=job, args=(tmp,), name=id_))
            procs[id_].start()
        for id_ in range(thr_num):
            procs[id_].join()

        one_count = 0
        for j in range(len(results)):
            r = results[j]
            if r == 1:
                one_count += 1
            elif r != 0:
                print(f'Weird value: {r}')
                exit(1)
        if one_count > thr_num//2:
            flag2.append('1')
        else:
            flag2.append('0')
        print(results, flag2)
        tmp[i] = b'0'

    print(flag2)
    print(''.join(flag2))
    return flag2


def crack_rand(bin_flag2):
    for x_r in product([False, True], repeat=256):
        tmp = [int(c) for c in bin_flag2]
        np.random.seed(x_r)
        chance = np.random.rand()
        for i in range(256):
            if chance > 0.9:
                tmp[i] = 1 - tmp[i]
        tmp = ''.join(map(str, tmp))
        print_bin_flag(tmp)
        if tmp.startswith('bctf'):
            print_bin_flag(tmp)
            break


def print_bin_flag(bin_flag2):
    flag2 = ''
    for i in range(0, len(bin_flag2), 8):
        flag2 += chr(int(bin_flag2[i:i+8], 2))

    print(flag2)


'''
if __name__ == '__main__':
    bin_flag2 = ''.join(get_flag2())
    flag2 = ''
    for i in range(0, len(bin_flag2), 8):
        flag2 += chr(int(bin_flag2[i:i+8], 2))

    print(flag2)
'''

bin_flag2 = '0110001001101011011101001110011101111011011001110110111101101000001111000111001001100101011001000110001101101001001011010110110001100001011111101110100101101110001001010111010001111000010001011111111011110010111000011111110100101110000100100000010001011100'
crack_rand(bin_flag2)
