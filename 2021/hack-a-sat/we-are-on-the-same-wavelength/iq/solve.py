# Ref: https://www.allaboutcircuits.com/textbook/radio-frequency-analysis-design/radio-frequency-demodulation/understanding-i-q-signals-and-quadrature-modulation/
from pwn import *

r = remote('unique-permit.satellitesabove.me', 5006)
ticket = 'ticket{zulu993354bravo2:GAX5odbycFIXlqDNZXbYyXyFV06hjuM4-uuPAhNJZ87LojssrY9Rljq5m8q2ui_ZUQ}'

bits = ''.join('01000011 01110010 01101111 01101101 01110101 01101100 01100101 01101110 01110100 00001010'.split(' '))

iq = ''
for i in range(0, len(bits), 2):
    data = bits[i:i+2]
    if data == '01':
        iq += '-1.0 1.0 '
    elif data == '11':
        iq += '1.0 1.0 '
    elif data == '10':
        iq += '1.0 -1.0 '
    elif data == '00':
        iq += '-1.0 -1.0 '
    else:
        print(f'[-] Error: {data}, iq: {iq}')

r.recv(4096)
r.sendline(ticket)
r.recv(4096)
r.sendline(iq.strip())
print(r.recv(4096).decode('utf-8'))
