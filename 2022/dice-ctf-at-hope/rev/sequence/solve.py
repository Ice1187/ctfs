from pwn import *

p = remote('mc.ax', 31973)

p.recv()

ans = [12]
for i in range(1, 6):
    ans.append((3 * ans[i-1] + 7) % 16)
p.sendline(' '.join(map(str, ans)).encode())

print(p.recv().decode())
