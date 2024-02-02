from z3 import *

#key = b'\x68\x75\x6d\x61\x6e\x73'
key = b'\x61\x6c\x69\x65\x6e\x73'
encrypted = b'\x29\x38\x2B\x1E\x06\x42\x05\x5D\x07\x02\x31\x42\x0F\x33\x0A\x55\x00\x00\x15\x1E\x1C\x06\x1A\x43\x13\x59\x36\x54\x00\x42\x15\x11\x00'

arr = [BitVec(f'arr{i}', 8) for i in range(32)]

solver = Solver()
for i in range(32):
    solver.add((key[i % 6] ^ encrypted[i]) == arr[i])

flag = ''

# print(solver.check())
solver.check()
m = solver.model()
for i in range(32):
    flag += chr(m[arr[i]].as_long())

print(flag)
