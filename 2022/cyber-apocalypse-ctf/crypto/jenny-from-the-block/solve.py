from hashlib import sha256
from pwn import *

BLOCK_SIZE = 32

p = remote('167.71.137.43', 30576)
cmd = b'Command executed: ' + b'cat secret.txt' + b'\n'


def decrypt(block, password=b''):
    if password == b'':
        for idx in range(BLOCK_SIZE):
            for c in range(256):
                if (block[idx] - c + 256) % 256 == cmd[idx]:
                    password += bytes([c])
    msg = b''
    for i in range(BLOCK_SIZE):
        msg += bytes([(block[i] - password[i] + 256) % 256])
    #print('Message:', msg)
    #print('Password:', password)
    return msg, password


flag = b''

p.recv()
p.recv()
p.sendline(b'cat secret.txt')
ct = p.recv().strip().decode()
ct = bytes.fromhex(ct)
blocks = [ct[i:i+BLOCK_SIZE] for i in range(0, len(ct), BLOCK_SIZE)]
msg, password = decrypt(blocks[0])
flag += msg
h = sha256(password).digest()
h = sha256(blocks[0] + msg).digest()

for block in blocks[1:]:
    msg, password = decrypt(block, password=h)
    flag += msg
    h = sha256(block + msg).digest()

print(flag.decode())
