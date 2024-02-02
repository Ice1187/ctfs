from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import hashlib
import random
import pwn

p = pwn.remote('134.209.177.202', 30183)
#p = pwn.remote('127.0.0.1', 1337)


def encrypt(msg, shared_secret):
    key = hashlib.md5(long_to_bytes(shared_secret)).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    enc = cipher.encrypt(msg)
    return enc


def decrypt(encrypted, shared_secret):
    key = hashlib.md5(long_to_bytes(shared_secret)).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    message = cipher.decrypt(encrypted)
    return message


print(p.recv())
p.sendline(b'1')
print(p.recv())
p.sendline(encrypt(b"Initialization Sequence - Code 0", 1).hex())
print(p.recv())
print(p.recv())
