# coding=utf-8
from pwn import *

char_set = '{}_'
for i in range(0, 25):  # no Z
  char_set += chr(ord('A')+i)
for i in range(0, 26):
  char_set += chr(ord('a')+i)
for i in range(0, 10):
  char_set += chr(ord('0')+i)


p = process(['./TsaiBro', char_set])
p.recvline()
enc_char_set = p.recv().strip().replace('發財', '-')

dict_ = {}
for c in char_set:
  dash_cnt = 0
  for i in range(0, len(enc_char_set)):
    if enc_char_set[i] == '-':
      dash_cnt += 1
    if dash_cnt == 3:
      dict_[enc_char_set[0:i]] = c
      enc_char_set = enc_char_set[i:]
      break


said = ''
with open('./TsaiBroSaid', 'r') as f:
  f.readline()
  said = f.read().strip().replace('發財', '-')

flag = ''
dash_cnt = 0
while dash_cnt != 2:
  dash_cnt = 0
  for i in range(0, len(said)):
    if said[i] == '-':
      dash_cnt += 1
    if dash_cnt == 3:
      flag += dict_[said[:i]]
      said = said[i:]
      break
flag += dict_[said]

print flag
