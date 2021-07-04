from pwn import *

enc_flag1 = 'atd4`qdedtUpetepqeUdaaeUeaqau'
enc_flag2 = 'c`b bk`kj`KbababcaKbacaKiacki'

char_set = ''
for i in range(0, 26):
  char_set += chr(ord('A')+i)
for i in range(0, 26):
  char_set += chr(ord('a')+i)
for i in range(0, 10):
  char_set += chr(ord('0')+i)

p = process(['./mask', char_set])
p.recvline()
enc_char_set1 = p.recvline().strip()
enc_char_set2 = p.recvline().strip()
p.close()

char_set += '{}_'
p = process(['./mask', char_set[-3:]])
p.recvline()
enc_char_set1 += p.recvline().strip()
enc_char_set2 += p.recvline().strip()
p.close()

dict1 = {}
dict2 = {}
for i in range(0, len(char_set)):
  dict1[char_set[i]] = enc_char_set1[i]
  dict2[char_set[i]] = enc_char_set2[i]

flag = ''
for i in range(0, len(enc_flag1)):
  for c in char_set:
    if dict1[c] == enc_flag1[i] and dict2[c] == enc_flag2[i]:
      flag += c
      break

print flag
