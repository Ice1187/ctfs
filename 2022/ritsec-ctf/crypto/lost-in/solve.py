import base64
enc_flag = '324c6e597364696f3259725a6f646d673261453d'
b64_flag = ''.join(chr(int(enc_flag[x:x+2], 16))
                   for x in range(0, len(enc_flag), 2))
print(b64_flag)
