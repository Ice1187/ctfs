
with open('output.txt', 'rb') as f:
    data = f.read().strip()

ct = int(data, 16).to_bytes(len(data)//2, 'big')
print(ct.hex())

for key in range(0, 256):
    pt = ''.join([chr(key ^ byte) for byte in ct])
    if pt.startswith('hope'):
        print(pt)
