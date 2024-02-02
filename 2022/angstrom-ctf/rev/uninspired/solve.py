'''
from z3 import *

s = [BitVec(f's[{i}]', 8) for i in range(16)]
buf = Array('buf', IntSort(), IntSort())
for i in range(16):
    Store(buf, i, 0)
solver = Solver()

solver.add(s[10] == 0x0a)
solver.add(s[0] - 48 <= 9)

for i in range(16):
    tmp = Select(buf, s[i] - 48)+1
    Store(buf, s[i] - 48, tmp)
    # buf[s[i] - 48] += 1

for i in range(16):
    solver.add(buf[i] == s[i] - 48)

print(s.check())
print(s.model())
'''
