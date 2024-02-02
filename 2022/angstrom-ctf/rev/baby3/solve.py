flag = []
flag.append((0x686D657B66746361).to_bytes(8, 'little'))
flag.append((0x657A656D64696170).to_bytes(8, 'little'))
flag.append((0x72616C6C6F646F72).to_bytes(8, 'little'))
flag.append((0x74656B616D6F7473).to_bytes(8, 'little'))
flag.append((0x6C6C616863736968).to_bytes(8, 'little'))
flag.append((0x6F6D615F65676E65).to_bytes(8, 'little'))
flag.append((0x7D737567).to_bytes(4, 'little'))
print(b''.join(flag).decode())
