from Crypto.Util.number import bytes_to_long

n = int(input('n: '))
e = int(input('e: '))

ethan = bytes_to_long(b'Ethan Winters')
for sig in range(2, 10000000000):
   msg = pow(sig, e, n)
   if msg == ethan:
       print('Success')
       break
   elif !(sig % 10000):
       print(sig)

