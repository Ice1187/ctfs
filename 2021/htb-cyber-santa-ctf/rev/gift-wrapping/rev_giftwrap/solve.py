import socket
import readline

host = '127.0.0.1'
port = 9000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

def recv(info=None):
  # TODO
  res = s.recv(4096)
  print(f'[<] {info if info else ""}')
  print(res.decode('utf-8'))
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


xor = lambda x: b''.join([(x[i] ^ 0xf3).to_bytes(1, 'little') for i in range(len(x))])

magic = b'\xBB\xA7\xB1\x88\x86\x83\x8B\xAC\xC7\xC2\x9D\x87\xAC\xC6\xC3\xAC\x9B\xC7\x81\x97\xD2\xD2\x8E'
flag = xor(magic)

send(flag)
recv()

print(f'Flag: {flag.decode()}')

