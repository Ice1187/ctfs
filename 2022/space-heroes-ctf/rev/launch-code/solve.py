import socket
import readline
from z3 import *
import subprocess as sp

host = '0.cloud.chals.io'
port = 12499

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


def recv(info=None, decode=True):
    # TODO
    res = s.recv(4096)
    print(f'[<] {info if info else ""}')
    if decode:
        print(res.decode('utf-8'))
    else:
        print(res)
    return res


def recvuntil(stop, decode=True):
    res = b''
    while stop not in res:
        res += recv(decode=decode)
    return res


def send(data):
    # TODO
    data = data + b'\n' if data[-1] != b'\n' else data
    s.send(data)


def interact():
    for _ in range(100):
        cmd = input('> ').encode('ascii')
        send(cmd)
        recv()


# get random number
recv()
res = recv()
res = res[res.find(b' = ')+3:]
res = res[:res.find(b'\n')].strip()
random = int(res.decode())

a = [BitVec(f'a[{i}]', 32) for i in range(4)]

solver = Solver()
solver.add(a[2]-a[3]+1 == 0, (a[1]/a[2]) ^ 2
           == 0, 8*(a[0]+a[1]+random) == 0)
solver.check()
m = solver.model()
ans = [m[a[i]].as_long() for i in range(4)]
ans = ' '.join(map(hex, ans))
print('ans:', ans)
send(ans.encode())
recv()
