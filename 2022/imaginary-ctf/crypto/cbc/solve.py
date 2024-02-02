from Crypto.Cipher import AES

ct = b"\xa2\xb8 <\xf2\x85\xa3-\xd1\x1aM}\xa9\xfd4\xfag<p\x0e\xb7|\xeb\x05\xcbc\xc3\x1e\xc3\xefT\x80\xd3\xa4 ~$\xceXb\x9a\x04\xf0\xc6\xb6\xd6\x1c\x95\xd1(O\xcfx\xf2z_\xc3\x87\xa6\xe9\x00\x1d\x9f\xa7\x0bm\xca\xea\x1e\x95T[Q\x80\x07we\x96)t\xdd\xa9A 7dZ\x9d\xfc\xdbA\x14\xda9\xf3\xeag\xe3\x1a\xc8\xad\x1cnL\x91\xf6\x83'\xaa\xaf\xf3i\xc0t=\xcd\x02K\x81\xb6\xfa.@\xde\xf5\xaf\xa3\xf1\xe3\xb4?\xf9,\xb2:i\x13x\xea1\xa0\xc1\xb9\x84"

pt = b''
for b in range(0, len(ct)-16, 16):
    key = ct[b:b+16]
    aes = AES.new(key, AES.MODE_ECB)
    dec = aes.decrypt(ct[b+16:b+32])
    pt += dec

print(pt.decode())