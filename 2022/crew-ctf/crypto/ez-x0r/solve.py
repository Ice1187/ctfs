from base64 import b64decode
from string import printable

with open('./flag.enc', 'rb') as f:
    b64_enc_flag = f.read().strip()

enc_flag = b64decode(b64_enc_flag)

for k in printable:
    flag = bytearray()
    for c in enc_flag:
        flag += (c ^ ord(k)).to_bytes(1, 'little')
    if flag.startswith(b'crew'):
        print(flag.decode())
        break
