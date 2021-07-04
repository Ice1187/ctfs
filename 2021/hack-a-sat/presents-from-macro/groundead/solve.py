from pwn import *

r = remote('unfair-cookie.satellitesabove.me', 5001)
ticket = 'ticket{hotel532690victor2:GFRLqfDN-HsYfO_n9q4NdreqyNkCuVabjeEiJiIKSIOGfRjBqW2HqRlg7ux8GVlLjg}'

r.recv()
r.sendline(ticket)

r.interactive()
