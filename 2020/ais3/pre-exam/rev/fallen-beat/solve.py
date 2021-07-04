f = open('./cache')
tmp = f.read().split('\n')
tmp.remove('')

cache = [int(x) for x in tmp]

flag = [89, 74, 75, 43, 126, 69, 120, 109, 68, 109, 109, 97, 73, 110, 45, 113, 102, 64, 121, 47, 111, 119, 111, 71, 114, 125, 68, 105, 127, 124, 94, 103, 46, 107, 97, 104]

for i in range(0, len(cache)):
  k = i % len(flag)
  flag[k] ^= cache[i]

flag_s = ''
for i in flag:
  flag_s += chr(i)
print flag_s
