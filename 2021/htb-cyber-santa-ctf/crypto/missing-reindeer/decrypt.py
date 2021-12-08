import gmpy2
from Crypto.Util.number import bytes_to_long

with open('message.enc', 'rb') as f:
	c = f.read()
c = bytes_to_long(c)

n = 0x00e623972884b1f4d722bdd5ee5beb84cb84760c2ed0ffafd93cd6030fb20d7930903bd1731dc74c954a23075303dfd71b885cd66e985bf759ed17a985f7e7d837c857bd31a147d74da261492858fa5fcfb89230878ef4fffcff92fc292989326454afb51bb7ab253fefd5b357bf83a639f153204afc5628f3e02022c6949dc23cb19d2fd639b6d5987ac332a01dd23b437a6777bb967f80e522e941e5f972160aed556db7393919806422ae1a7dc9b19996fdb7b29141472d6803dff42a713db57ac078fca48d1a6861423de3a12ed9cfafb831e5d69b92d71963d023228c2612ea334a652c46121f505d1b5a551224c69fc8239cfe1093de68095f7153159667
e = 3

for k in range(1, 10000000000):
	root, b = gmpy2.iroot(k*n+c, e)
	if (k % 1000) == 0:
		print(k)
	if b == True:
		print(f'Message: {root}')
		break
		
	
