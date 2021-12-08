import socket
import readline

host = '127.0.0.1'
port = 9000
host = '134.209.30.250'
port = 30035

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

def recv(info=None):
  res = s.recv(4096)
  return res

def send(data):
  s.send(data)

# Stage 1
res = recv()
first = res[:16]
second = res[16:]
#print(first.hex(' '))
#print(second.hex(' '))

enc_f1 = (first[15] | (first[14] | (first[13] | (first[12] | (first[11] | (first[10] | (first[9] | (first[8] << 8)) << 8) << 8) << 8) << 8) << 8) << 8).to_bytes(8, 'little')
enc_f2 = (first[ 7] | (first[ 6] | (first[ 5] | (first[ 4] | (first[ 3] | (first[ 2] | (first[1] | (first[0] << 8)) << 8) << 8) << 8) << 8) << 8) << 8).to_bytes(8, 'little')
enc_s1 = (second[15] | (second[14] | (second[13] | (second[12] | (second[11] | (second[10] | (second[9] | (second[8] << 8)) << 8) << 8) << 8) << 8) << 8) << 8).to_bytes(8, 'little')
enc_s2 = (second[ 7] | (second[ 6] | (second[ 5] | (second[ 4] | (second[ 3] | (second[ 2] | (second[1] | (second[0] << 8)) << 8) << 8) << 8) << 8) << 8) << 8).to_bytes(8, 'little') 

enc_first = enc_s1 + enc_s2
enc_second = enc_f1 + enc_f2
ans = enc_first + enc_second
print(ans)
send(ans)

# Stage 2
res = recv()
first = res[:16]
second = res[16:]

xor = lambda x,y: b''.join([(x[i] ^ y[i]).to_bytes(1, 'little') for i in range(len(x))])

ans1 = xor(first, enc_first)
ans2 = xor(second, enc_second)
ans = ans1 + ans2
print(ans)

send(ans)

recv()
flag = recv().decode()
print(f'Flag: {flag}')
