with open('./output.txt', 'r') as f:
    ct = f.read()

ct = int(ct, 16).to_bytes(len(ct)//2+1, 'big').strip(b'\x00')

key = b'\xe0\xf3\x1f}\xb7\t\xd7' + b'\x3c'

padding = 8
pad_key = b''
for i in range(1, padding+1):
    pad_key = (0x3f ^ ct[-i]).to_bytes(1, 'big') + pad_key
key += pad_key

flag = b''
j = 0
for i in range(len(ct)):
    flag += (key[j] ^ ct[i]).to_bytes(1, 'big')
    j += 1
    j %= 16

print(flag.decode())
