from Crypto.Cipher import ARC4

enc_flag = '855E6EAD057B46A9D75F3E072F350438'

dummy = b'A'*32
key = 'Hello'
rc4 = ARC4.new(key)
enc_dummy = rc4.encrypt(dummy)
