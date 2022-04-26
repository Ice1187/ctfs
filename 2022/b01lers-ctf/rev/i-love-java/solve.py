from z3 import *

inp = [BitVec(f'inp[{i}]', 8) for i in range(22)]

ans = [116, 122, 54, 50, 93, 66, 98, 117, 75, 51, 97,
       78, 104, 119, 90, 53, 94, 36, 105, 84, 40, 69]

for i in range(len(inp)//2):
    c = inp[len(inp) - i - 1]
    inp[len(inp) - i - 1] = inp[i]
    inp[i] = c

iArr = [19, 17, 15, 6, 9, 4, 18, 8, 16, 13,
        21, 11, 7, 0, 12, 3, 5, 2, 20, 14, 10, 1]
# iArr2 = [0 for _ in range(len(iArr))]
iArr2 = [BitVec(f'iArr2[{i}]', 8) for i in range(22)]
for i in range(len(iArr)-1, -1, -1):
    iArr2[i] = inp[iArr[i]]

rand = [0, 1, 2, 1, 2, 5, 4, 1, 1, 7, 3, 7, 0, 10, 5, 5, 1, 16, 10, 2, 12, 17]
# iArr3 = [0 for _ in range(22)]
iArr3 = [BitVec(f'iArr3[{i}]', 8) for i in range(22)]
for i in range(len(iArr3)):
    iArr3[i] = iArr2[i] ^ rand[i]

solver = Solver()
for i in range(22):
    solver.add(iArr3[i] == ans[i])
print(solver.check())
m = solver.model()
flag = ''
for i in range(22):
    flag += chr(m[inp[i]].as_long())
print(''.join(reversed(flag)))
