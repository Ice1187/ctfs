flag = b''

k1 = 0x1c417cf092edb590
k2 = 0x7870148bf499d6f9
key = (k1 ^ k2).to_bytes(8, 'little')
flag += key

k1 = 0x1c3bf8a352273e31
k2 = 0x435e9c9331495b55
key = (k1 ^ k2).to_bytes(8, 'little')
flag += key

k1 = 0x9b77a599c10f8a39
k2 = 0x910a96fdf83deb08
key = (k1 ^ k2).to_bytes(8, 'little')
flag += key

print(flag.decode())
