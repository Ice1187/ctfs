from pwn import *

s = remote('light-fever.satellitesabove.me',5030)

s.recvline()
s.sendline('ticket{india182070mike2:GPqtMURbKXWn8QePo3bXUO1cY2Cp_9wFA1C4FC8qbFRDVRUjwm4rWlDKYNyzZxmy4w}')

for i in range(100):
    equation = s.recvuntil('=')[:-1] 
    print(f'{equation} = {eval(equation)}')
    s.sendline(str(eval(equation)))
    s.interactive()
