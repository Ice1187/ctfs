s = b''
s += (0x1C4B0D0B043D2B37).to_bytes(8, 'little')
s += (0x200F0A204C12204C).to_bytes(8, 'little')
s += (0x184F18200A204B1D).to_bytes(8, 'little')
s += (0x24f).to_bytes(2, 'little')

flag = ''
for i in range(len(s)):
    flag += chr(s[i] ^ 127)

print(flag)
