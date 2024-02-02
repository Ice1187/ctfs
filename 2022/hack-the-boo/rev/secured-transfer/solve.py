from Crypto.Cipher import AES

c_len = 0x20
c = (0x5f558867993dccc99879f7ca39c5e406972f84a3a9dd5d48972421ff375cb18c).to_bytes(
    0x100, 'big').strip(b'\x00')
key = b'supersecretkeyusedforencryption!'
iv = b'someinitialvalue'

aes = AES.new(key, AES.MODE_CBC, iv)
flag = aes.decrypt(c)
print(flag)
