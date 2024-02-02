#!/usr/bin/env python2
from __future__ import print_function

BLOCK_SIZE = 8

with open('./output.txt', 'r') as f:
    ct = f.read()

key = [ord(c) ^ ord(f)
       for c, f in zip(ct[:7], 'hope{ma')] + [ord(ct[-2]) ^ ord('}')]

flag = ''
for i, c in enumerate(ct):
    flag += chr(ord(c) ^ key[i % BLOCK_SIZE])

print(flag, end='')
