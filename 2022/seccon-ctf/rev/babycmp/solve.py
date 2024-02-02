from z3 import *

check = (0x2B2D3675357F1A44591E2320202F2004).to_bytes(16, 'little')
check += (0x362B470401093C150736506D035A1711).to_bytes(16, 'little')
check += (0x380a41).to_bytes(16, 'little')
key = (0x4F43434553206F7420656D6F636C6557).to_bytes(16, 'little')
key += b'N 2022'
print(key, check)

flag = [BitVec(f'flag[{i}]', 8) for i in range(0x24)]

flag[0] = flag[0] ^ 0x57
for i in range(len(flag)):
    for i in range(1, len(flag)):
        v14 = (i // 0x16 + 2 * (i // 0x16 + (((0x2E8BA2E8BA2E8BA3 * i)
               >> 64) & 0xFFFFFFFFFFFFFFFC))) & 0xffffffffffffffff
        flag[i] ^= key[(i - 2*v14) % 16]

s = Solver()
for i in range(len(flag)):
    s.add(flag[i] == check[i])

print(s.check())
print(s.model())

print(bytes(flag))
