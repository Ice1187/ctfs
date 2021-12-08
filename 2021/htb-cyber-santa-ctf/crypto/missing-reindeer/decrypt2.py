import gmpy2
import base64 as b64
from Crypto.Util.number import bytes_to_long
from Crypto.PublicKey import RSA 

with open('message.enc', 'rb') as f:
	c = f.read()
c = b64.b64decode(c)
c = bytes_to_long(c)

f = '''-----BEGIN PUBLIC KEY-----
MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEA5iOXKISx9NcivdXuW+uE
y4R2DC7Q/6/ZPNYDD7INeTCQO9FzHcdMlUojB1MD39cbiFzWbphb91ntF6mF9+fY
N8hXvTGhR9dNomFJKFj6X8+4kjCHjvT//P+S/CkpiTJkVK+1G7erJT/v1bNXv4Om
OfFTIEr8Vijz4CAixpSdwjyxnS/WObbVmHrDMqAd0jtDemd3u5Z/gOUi6UHl+XIW
Cu1Vbbc5ORmAZCKuGn3JsZmW/beykUFHLWgD3/QqcT21esB4/KSNGmhhQj3joS7Z
z6+4MeXWm5LXGWPQIyKMJhLqM0plLEYSH1BdG1pVEiTGn8gjnP4Qk95oCV9xUxWW
ZwIBAw==
-----END PUBLIC KEY----- '''
key = RSA.importKey(f)
n = key.n
e = key.e

print(n)
print(e)

for k in range(1, 10000000000):
	root, b = gmpy2.iroot(k*n+c, e)
	if (k % 1000) == 0:
		print(k)
	if b == True:
		print(f'Message: {root}')
		break
		
	
