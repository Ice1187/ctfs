from hashlib import sha256

h = sha256((214).to_bytes(8, 'little')).hexdigest()
print(h)
