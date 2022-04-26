key = b'evilzurgevilzurg'
with open('./buzz.enc', 'rb') as f:
    data = f.read()

dec_data = bytearray(len(data))
for i in range(len(data)):
    dec_data[i] = data[i] ^ key[i % len(key)]

with open('./buzz.dec', 'wb') as f:
    f.write(dec_data)
