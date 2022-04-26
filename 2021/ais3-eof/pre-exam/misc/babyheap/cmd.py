import socket
import readline

host = 'eof.h4ck3r.quest'
port = 7122 

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


while True:
  recv()
  cmd = input().encode()
  send(cmd)

