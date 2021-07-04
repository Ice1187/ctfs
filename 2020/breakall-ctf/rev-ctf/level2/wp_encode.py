s = 0x9cac105bc36a4
alpha = [chr(x) for x in range(0x41, 0x41+26)]

flag = ''
while s != 0:
    for c in alpha:
        if (s+0x41-ord(c)) % 0x1a == 0:
            flag += c
            s = (s+0x41-ord(c))/0x1a

print flag
print flag[::-1]

