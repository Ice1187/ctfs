from z3 import *
from string import ascii_letters, digits

s = 'hope{' + ascii_letters + digits
s = s[:54] + '}'
print(s)

n = [BitVec(f'n[{i}]', 8) for i in range(55)]

solver = Solver()
solver.add(n[0] == ord('h'))
solver.add(n[1] == ord('o'))
solver.add(n[2] == ord('p'))
solver.add(n[3] == ord('e'))
solver.add(n[4] == ord('{'))
solver.add(n[s.find('o')] ^ n[s.find('N')] == 3)
solver.add(n[s.find('V')] ^ 1 == 7)
solver.add(n[s.find('a')] == 0x78)
solver.add(n[s.find('c')] ^ n[s.find('M')] == 0xd)
solver.add(n[s.find('i')] + n[s.find('m')] == 0xd4)
solver.add(n[s.find('B')] - 0x4a == 0x42)
solver.add(n[s.find('n')] == 0x68)
solver.add(n[s.find('b')] ^ n[s.find('u')] == 3)
solver.add(n[s.find('y')] ^ n[s.find('P')] == 0x5b)
solver.add(n[s.find('t')] ^ 0x71 == 0xb)
solver.add(n[s.find('F')] == 0x67)
solver.add(n[s.find('I')] == n[s.find('p')])
solver.add(n[s.find('U')] != 0x6f)  # or equal?
solver.add(n[s.find('e')] + n[s.find('G')] == 0xc7)
solver.add(n[s.find('E')] - n[s.find('k')] == 0xf)

solver.check()
print(solver.model())
