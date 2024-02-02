from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open('./encrypted.bin', 'rb') as f:
    ct = f.read()

key = RSA.importKey(open('./privatekey.pem').read())
cipher_rsa = PKCS1_OAEP.new(key)
flag = cipher_rsa.decrypt(ct).decode()

print(flag)
