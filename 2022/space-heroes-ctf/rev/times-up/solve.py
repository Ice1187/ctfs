from z3 import *

a = [BitVec(f'in[{i}]', 32) for i in range(3)]
solver = Solver()
solver.add(BV2Int(((a[1] + a[0] + a[2]) << (a[0] % a[1])) /
                  (a[2] * ((2 << a[0]) ^ 3)), True) == 10798448)

solver.check()
m = solver.model()
print(m)
for i in range(3):
    b = int(m[a[i]].as_binary_string(), 2)
    print(hex(b))
