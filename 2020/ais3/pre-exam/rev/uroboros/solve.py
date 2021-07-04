def findchr(idx):
  n = 0
  while n < 256:
    k = (n*7-1)%313
    if k == idx:
       print chr(n) + ' (' + str(n) + ')'
       break
    n += 1


def encode(s):
    l = [0 for _ in range(313)]
    c = 1
    for i in range(len(s)):
        idx = (ord(s[i]) * 7-1)%313
        l[idx] = l[idx]*0x40 + c
        c += 1
    print l
    return l

enc_flag = map(int, '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 511847092 0 0 0 0 0 0 48 0 0 0 0 0 0 0 40984114273074 0 0 0 0 0 280 0 0 0 0 0 0 26022 26 0 0 0 0 0 0 2035 0 0 0 0 0 0 15 0 0 0 0 0 0 53 0 0 0 0 0 0 47 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 42350 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 40 0 0 0 0 0 0 29201 0 0 0 0 0 0 805 0 0 0 0 0 1 939 0 0 0 0 0 0 13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 7739889 0 0 0 0 0 0 1251 0 0 0 0 0 0 45 0 0 0 0 0 0 2950300 0 0 0 0 0 2 23 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 54 0 0 0 0 0 0 0 0 0 0 0 0 0 5 0 0 0 0 0 0 0 0 0 0 0 0 0 55 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'.split(' '))

def getidx(num):
    for i in range(len(enc_flag)):
        if enc_flag[i] == num:
            return i
'''
for i in range(1, 20):
    for j in range(len(enc_flag)):
        if enc_flag[j]==i:
            findchr(j)
'''

LEN = 0x139+1

s = raw_input('Input: ')
c = 1
l = [ 0 for _ in range(LEN)]
for i in s:
    num = ord(i)*7
    idx = 0
    for j in range(num):
        idx = (idx+1)%LEN
    l[idx] = c
    c+=1

for i in range(1, len(s)+1):
    for j in range(len(l)):
        if l[j] == i:
            print str(i), str(j).rjust(3), '|', getidx(i)
