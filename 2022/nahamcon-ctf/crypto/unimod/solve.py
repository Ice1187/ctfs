with open('out', 'r') as f:
    enc_flag = f.read()

for c in range(0, 0xFFFD):
    partial = ''
    for i in range(4):
        partial += chr((ord(enc_flag[i]) + c) % 0xFFFD)
    if (partial == 'flag'):
        key = c
        break

flag = ''
for i in range(len(enc_flag)):
    flag += chr((ord(enc_flag[i]) + key) % 0xfffd)

print(flag)
