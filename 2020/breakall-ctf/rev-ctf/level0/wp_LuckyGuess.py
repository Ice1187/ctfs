from pwn import *

p = process('./LuckyGuess')

M = 999999999
m = 0
mid = 500000000

p.sendline(bytes(mid))
out = p.recv().strip()
while b'lo' in out or b'hi' in out:
    print(b'out: ' + out)
    print('mid: ' + str(mid))
    if b'lo' in out:
        mid = (mid+M)/2
    elif b'hi' in out:
        mid = (mid+m)/2
    else:
        break
    p.sendline(bytes(mid))
    out = p.recv().strip()

print(out)



