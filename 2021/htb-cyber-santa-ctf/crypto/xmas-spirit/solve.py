from math import gcd

mod = 256
possible_a = []
for a in range(1, mod+1):
	if gcd(a, mod) == 1:
		possible_a.append(a)

with open('encrypted.bin', 'rb') as f:
	enc_letter = f.read()

for a in possible_a:
	for b in range(1, mod+1):
		res = b''
		for c in enc_letter[:4]:
			dec = (c-b)*a % mod
			res += bytes([dec])
		if res == b'\x25\x50\x44\x46':
			print(f'a: {a}, b: {b}')
			break

a = 153
b = 160
res = b''
for c in enc_letter:
	dec = (c-b)*a % mod
	res += bytes([dec])

with open('decrypted.pdf', 'wb') as f:
	f.write(res)
