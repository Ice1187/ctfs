from pwn import *
from Crypto.Util.strxor import strxor


def try_key(enc, key):
    assert len(key) == 16

    flags = b''
    for i in range(0, len(enc), 16):
        block = enc[i:i+16]
        flags += strxor(block, key)
    return flags


def try_pad(enc, key):
    last = enc[-16:]
    for i in range(0x1, 17):
        print('Padding:', i)
        pad = (i).to_bytes(1, 'big') * i
        k = key[:16-i] + pad
        real_pad = strxor(last, k)[-i:]
        print(real_pad)
        k = key[:16-i] + real_pad
        try_key(enc, k)
        print('')


#p = remote('mc.ax', 31968)
#
#p.recvuntil(b'> ')
#enc = p.recv().strip()
enc = b'd971846a7d5f367dd1c28642ad6b5c38c26a9d6c6d6b2470d1c29a58be61670fd4419f6169432340ec82dd18e0635a50d426cc3c6350652bf3b6e92adf003f60'
enc = int(enc, 16).to_bytes(len(enc)//2, 'big')
print('enc:', enc.hex())

key = b'\xb1\x1e\xf4\x0f\x06\x34\x50\x1f\x8e\xb1\xee-\xd8\x078g'
#try_pad(enc, key)
print(try_key(enc, key))
