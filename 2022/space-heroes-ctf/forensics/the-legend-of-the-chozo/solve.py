'''
The header of the file looks lik PNG file
  Normal PNG:
    00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
    00000010: 0000 1770 0000 06ef 0806 0000 00ce cdb4  ...p............
  Given File:
    00000000: 5047 890a 4e0d 0a1a 0d48 4400 5200 0049  PG..N....HD.R..I
    00000010: 0000 00f0 0000 0139 0806 0000 00ae c5ad  .......9........
'''

with open('./CorruptedData.chr', 'rb') as f:
    enc_data = f.read()

order = [0x2, 0x0, 0x4, 0x1, 0x5, 0x3, 0x7,
         0x6, 0xb, 0xd, 0xe, 0x8, 0xf, 0x9, 0xa, 0xc]
data = bytearray()
for i in order:
    data.append(enc_data[i])
data.extend(enc_data[0x10:])

with open('./CorruptedData.png', 'wb') as f:
    f.write(data)
