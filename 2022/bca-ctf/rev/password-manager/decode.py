HASHEDPWD = '111210122915474114123027144625104141324527134638392719373948'
key = {
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15,
    'g': 16,
    'h': 17,
    'i': 18,
    'j': 19,
    'k': 20,
    'l': 21,
    'm': 22,
    'n': 23,
    'o': 24,
    'p': 25,
    'q': 26,
    'r': 27,
    's': 28,
    't': 29,
    'u': 30,
    'v': 31,
    'w': 32,
    'x': 33,
    'y': 34,
    'z': 35,
    '0': 36,
    '1': 37,
    '2': 38,
    '3': 39,
    '4': 40,
    '5': 41,
    '6': 42,
    '7': 43,
    '8': 44,
    '0': 45,
    '_': 46,
    '{': 47,
    '}': 48
}

flag = ''
for i in range(0, len(HASHEDPWD), 2):
    val = int(HASHEDPWD[i:i+2])
    c = (lambda k, v: [x for x, y in k.items() if y == v][0])(key, val)
    flag += c

print(flag)