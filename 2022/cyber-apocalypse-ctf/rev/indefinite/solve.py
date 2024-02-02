from pwn import *

p = gdb.debug(['./rev_indefinite/indefinite',
              'fake.txt']).wait()
