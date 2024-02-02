charset = '0123456789abcdef'
enc = '0d18001e060d090d1802131dcf011302080ccf0c070b0f080d0701cf00181116'

shuffled = '67234c0189ab5def'
d = {charset[i]: v for (i, v) in enumerate(shuffled)}

pt = ''.join(d[i] for i in enc)
print(pt)

s = ''
for i in range(0, len(pt), 2):
    c = int(pt[i:i+2], 16)
    if c >= 0x20 and c < 0x7f:
        c = chr(c)
    else:
        c = '@'
    s += c

print(s)
