from pwn import remote
import random

p = remote('rev.bcactf.com', 49157)
random.seed(123049)

for i in range(20):
    print(p.recv())
    p.sendline(b'1')
    print(p.recv())
    comp_choice = random.randint(-10000, 10000)
    comp_choice %= 10
    p.sendline(str(comp_choice).encode())

p.recv()
p.interactive()
