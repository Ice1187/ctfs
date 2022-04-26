from z3 import *


def solve1(action):
    for i in range(len(action)):
        action[i] += i
    return action


def solve2(action):
    for i in range(len(action)):
        action[i] ^= i
    return action


def solve3(action):
    for i in range(len(action)):
        action[i] = action[i] - i - 7
    return action


def solves(ans, func):
    inp = [BitVec(f'out[{i}]', 8) for i in range(len(ans))]

    for f in func:
        inp = f(inp)
    for i in range(len(ans)):
        solve(inp[i] == ans[i])


outs = []

# case 1
solves(b'<aZk`^', [solve3, solve1, solve2, solve2])
out = ''.join(chr(x) for x in [67, 104, 97, 114, 103, 101])
outs.append(out)

# case 2
solves(b';eZnu', [solve1, solve2, solve1, solve3])
out = ''.join(chr(x) for x in [66, 108, 97, 115, 116])
outs.append(out)

# case 3
solves(b'6_RWW', [solve3, solve2, solve1, solve3])
out = ''.join(chr(x) for x in [68, 111, 100, 103, 101, ])
outs.append(out)

# case 4
solves(b'DaQYWd', [solve3, solve1, solve3, solve2])
out = ''.join(chr(x) for x in [82, 111, 99, 107, 101, 116, ])
outs.append(out)

# case 5
solves(b'4_Qfb', [solve3, solve1, solve1, solve3, solve2])
out = ''.join(chr(x) for x in [66, 108, 97, 115, 116])
outs.append(out)

out = ''.join(chr(x) for x in [67, 104, 97, 114, 103, 101])
outs.append(out)

solves(b'Fkvk1', [solve1, solve1, solve2, solve1])
out = ''.join(chr(x) for x in [70, 105, 114, 101,  33, ])
outs.append(out)

print(outs)
