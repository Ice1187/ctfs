from z3 import *

a = [BitVec(f'a[{i}]', 8) for i in range(14)]
solver = Solver()

solver.add(a[0] == 98)
solver.add(a[1] == 99)
solver.add(a[2] == 116)
solver.add(a[3] == 102)
solver.add(a[4] == 123)
solver.add(a[5] == 52)
solver.add(a[6] ^ 0x33 == 95)
solver.add(a[7] == 103)
solver.add(a[8] == 51)
solver.add(a[9] ^ 0x10 == 114)
solver.add(a[10] ^ a[9] == 16)
solver.add(a[11]-1 == a[8])
solver.add(a[12] == 33)
solver.add(a[13] == 125)


print(solver.check())
m = solver.model()
flag = ''
for i in a:
    flag += chr(m[i].as_long())
print(flag)
