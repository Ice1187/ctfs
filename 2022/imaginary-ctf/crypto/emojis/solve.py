with open('./emojis.txt', 'r') as f:
    enc = f.read()

b = ''
for e in enc:
    if e == '👎':
        b += '0'
    elif e == '👍':
        b += '1'
    else:
        print('Error code:', e)

n = int(b, 2)
print(n.to_bytes(0x100, 'big').strip(b'\x00').decode())
